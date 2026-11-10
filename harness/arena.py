"""Champion-challenger arena. A candidate is a python file in candidates/ (see candidates/README.md).

run(path): fit the candidate's free coefficient (at most one) and the champion's on the training rows, measure power on
the sealed holdout's compositions (targets unseen), pre-register, then open the sealed targets and test. PASS: RMSE at
least 10% below the champion and a paired sign-flip permutation p below 0.01 / m, m = candidates already tested on that
holdout plus one. The holdout's targets are stored XOR-scrambled in data/sealed/ and only unsealed inside run().
"""

from __future__ import annotations

import hashlib
import importlib.util
import io
import zlib
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar

from harness import ledger
from harness.context import context
from harness.features import parse_comp

ROOT = Path(__file__).resolve().parent.parent
KEY = Path.home() / ".ai_science" / "seal.key"
DATASETS = {
    "emix_random": {
        "doc": "clamped random fcc alloys (MACE omat, 108-atom SQS, ideal sites) at Vegard volume; E_mix eV/atom",
        "train": ["h1_ev_rows_fixed.csv", "h3_fresh_rows_fixed.csv", "hm_fresh_rows_fixed.csv"],  # count-corrected
        "sealed": "hm3fix",
        "target": "E_mix",
        "champion": "candidates/champion_volume_transfer.py",
    },
}
GAIN, ALPHA = 0.10, 0.01


def _key() -> bytes:
    if not KEY.exists():
        KEY.parent.mkdir(parents=True, exist_ok=True)
        KEY.write_bytes(np.random.default_rng().bytes(64))
    return KEY.read_bytes()


def _xor(b: bytes) -> bytes:
    k = _key()
    return bytes(x ^ k[i % len(k)] for i, x in enumerate(b))


def seal(csv: Path, name: str, target: str) -> None:
    """Split a freshly generated holdout into plain compositions and scrambled targets, then remove the plain file."""
    df = pd.read_csv(csv)
    d = ROOT / "data" / "sealed"
    d.mkdir(exist_ok=True)
    df[["comp", "n_el"]].to_csv(d / f"{name}_comps.csv", index=False)
    (d / f"{name}.bin").write_bytes(_xor(zlib.compress(df[["comp", target]].to_csv(index=False).encode())))
    csv.unlink()


def _unseal(name: str) -> pd.DataFrame:
    return pd.read_csv(io.StringIO(zlib.decompress(_xor((ROOT / "data" / "sealed" / f"{name}.bin").read_bytes())).decode()))


def load(path: str | Path):
    spec = importlib.util.spec_from_file_location(Path(path).stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    meta = mod.META
    for k in ("name", "author", "dataset", "statement", "free"):
        assert k in meta, f"META lacks {k}"
    assert len(meta["free"]) <= 1, "at most one free coefficient"
    return meta, mod.predict


def _pred(predict, comps, coef):
    ctx = context()
    return np.array([predict(c, ctx, *coef) for c in comps], dtype=float)


def _fit(meta, predict, comps, y):
    if not meta["free"]:
        return ()
    name, lo, hi = meta["free"][0]
    r = minimize_scalar(lambda k: np.mean((y - _pred(predict, comps, (k,))) ** 2), bounds=(lo, hi), method="bounded")
    return (float(r.x),)


def train_rows(ds: str) -> pd.DataFrame:
    d = DATASETS[ds]
    df = pd.concat([pd.read_csv(ROOT / "data" / f)[["comp_actual", "n_el", d["target"]]] for f in d["train"]])
    df = df.rename(columns={"comp_actual": "comp"})  # the composition the cell really has
    ctx = context()
    covered = df.comp.map(lambda s: all((a, b) in ctx.pair for a, b, _, _ in ctx.pairs(parse_comp(s))))
    return df[(df.n_el >= 3) & covered].reset_index(drop=True)  # rows whose binaries all exist (no Al pairs)


def _rmse(e):
    return float(np.sqrt(np.mean(np.square(e))))


def _passes(y, p_new, p_champ, m, n_perm=4000, seed=0):
    n_perm = max(n_perm, int(2 * m / ALPHA))  # min p = 1/(n_perm+1) must stay below alpha/m (Astra, R2)
    e_new, e_ch = y - p_new, y - p_champ
    gain = 1 - _rmse(e_new) / _rmse(e_ch)
    d = e_ch**2 - e_new**2
    rng = np.random.default_rng(seed)
    obs = d.mean()
    null = np.array([(d * rng.choice([-1, 1], len(d))).mean() for _ in range(n_perm)])
    p = (np.sum(null >= obs) + 1) / (n_perm + 1)
    return bool(gain >= GAIN and p < ALPHA / m), gain, float(p)


def _uses(ds: str) -> int:
    return sum(1 for e in ledger.entries() if e["notes"].startswith(f"arena {ds} result"))


def run(path: str | Path, dry: bool = False) -> dict:
    meta, predict = load(path)
    ds = meta["dataset"]
    d = DATASETS[ds]
    cmeta, cpred = load(ROOT / d["champion"])
    tr = train_rows(ds)
    comps = tr.comp.map(parse_comp).tolist()
    y = tr[d["target"]].values
    coef, ccoef = _fit(meta, predict, comps, y), _fit(cmeta, cpred, comps, y)
    p_tr, c_tr = _pred(predict, comps, coef), _pred(cpred, comps, ccoef)
    rep = {"candidate": meta["name"], "author": meta["author"], "coef": coef, "train_n": len(y),
           "train_rmse_meV": _rmse(y - p_tr) * 1000, "champion_train_rmse_meV": _rmse(y - c_tr) * 1000}
    sc = pd.read_csv(ROOT / "data" / "sealed" / f"{d['sealed']}_comps.csv")
    hc = sc.comp_actual.map(parse_comp).tolist()
    p_h, c_h = _pred(predict, hc, coef), _pred(cpred, hc, ccoef)
    if not np.all(np.isfinite(p_h)):
        return {**rep, "status": "rejected: non-finite predictions on holdout compositions"}
    m = _uses(ds) + 1
    sig = _rmse(y - p_tr)  # realistic residual scatter, measured on training rows
    rng = np.random.default_rng(1)
    pw = np.mean([_passes(p_h + rng.normal(0, sig, len(p_h)), p_h, c_h, m, 500, i)[0] for i in range(100)])
    fp = np.mean([_passes(c_h + rng.normal(0, sig, len(c_h)), p_h, c_h, m, 500, i)[0] for i in range(100)])
    rep.update(power=float(pw), false_pass=float(fp), m=m)
    if pw < 0.8 or fp > 0.05:
        return {**rep, "status": "rejected before test: holdout cannot tell it from the champion (power or leak)"}
    if dry:
        return {**rep, "status": "dry run, not registered"}
    h = ledger.file_hash(path)
    reg = ledger.register(f"arena {ds}: {meta['name']} ({meta['author']}): {meta['statement']}", str(path),
                          {"power": rep["power"], "false_pass": rep["false_pass"]},
                          notes=f"candidate hash {h}; coef {coef}; champion coef {ccoef}; m {m}")
    sealed = _unseal(d["sealed"]).set_index("comp").loc[sc.comp, d["target"]].values
    ok, gain, p = _passes(sealed, p_h, c_h, m)
    rep.update(prereg=reg["id"], holdout_n=len(sealed), holdout_rmse_meV=_rmse(sealed - p_h) * 1000,
               champion_holdout_rmse_meV=_rmse(sealed - c_h) * 1000, gain=gain, p=p, passed=ok,
               status="PASS" if ok else "FAIL")
    ledger.record(f"{meta['name']}: {'PASS' if ok else 'FAIL'} vs champion on sealed {d['sealed']} (n={len(sealed)}, "
                  f"RMSE {rep['holdout_rmse_meV']:.1f} vs {rep['champion_holdout_rmse_meV']:.1f} meV, gain {gain:.2f}, "
                  f"p {p:.1e}, alpha/m {ALPHA / m:.1e})", "L0", [str(path)],
                  notes=f"arena {ds} result; prereg {reg['id']}")
    return rep

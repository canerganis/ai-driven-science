"""Model-swap check of the K' volume-transfer rule (L2 entry 697c2d6d75): is it an artefact of one model's shear bias?

python scripts/k_shear_mpa.py
L1 calibration: medium-omat-0 fcc C' bias about 0, medium-mpa-0 about -11% (data/calibration_*). Redo the whole
chain with medium-mpa-0: binary K44, K' on the same ln(V/V_ij) grid (seed 0 only; seed scatter of K' was 0.35 GPa),
then the 94 hm_fresh alloys. Geometry (V_ij, Vegard V0) stays the omat one, so both models see identical cells.
Pre-registered reading: the rule survives the model swap if, for K', RMSE(rule) <= 0.9 RMSE(pair at V_ij), sign-flip
p < 0.005, and the bootstrap 95% CI of the refit k contains 1. K44 reported, not gated.
"""

import datetime as dt
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.environ["HARNESS_MODEL"] = "medium-mpa-0"
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from ase.build import bulk  # noqa: E402
from scipy.interpolate import CubicSpline  # noqa: E402

from harness import compute, ledger  # noqa: E402
from harness.compute import GPA  # noqa: E402
from harness.context import context  # noqa: E402
from harness.features import parse_comp  # noqa: E402

assert compute.MODEL == "medium-mpa-0"
AMPS = np.array([-0.01, -0.005, 0.0, 0.005, 0.01])
GRID = [-0.40, -0.30, -0.20, -0.15, -0.10, -0.05, 0.0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.40]
BIN, TGT = ROOT / "data" / "binary_kgrid_mpa.csv", ROOT / "data" / "hm_shear_clamped_mpa.csv"
ctx = context()  # omat geometry, see docstring
calc = compute.calculator()
SCRIPT = str(Path(__file__))
CLAIM = "Model swap, K' volume transfer"


def e_strained(atoms, v_atom, F):
    a = atoms.copy()
    a.set_cell(a.cell * (v_atom * len(a) / a.get_volume()) ** (1 / 3), scale_atoms=True)
    a.set_cell(a.cell @ F.T, scale_atoms=True)
    a.calc = calc
    t = time.perf_counter()
    e = a.get_potential_energy() / len(a)
    time.sleep(time.perf_counter() - t)  # 50% duty cycle, keeps the laptop cool
    return e



def F_of(name, s):
    if name == "K44":
        F = np.eye(3)
        F[0, 1] = s
        return F
    return np.diag([np.exp(s), np.exp(-s), 1.0])


def curvatures(alloy, x, v):
    pures = {el: bulk(el, "fcc", a=4.0, cubic=True) for el in x}
    out = {}
    for name in ("K44", "Kp"):
        em = [e_strained(alloy, v, F_of(name, s)) - sum(xi * e_strained(pures[el], v, F_of(name, s))
                                                         for el, xi in x.items()) for s in AMPS]
        c2 = np.polyfit(AMPS, em, 2)[0]
        out[name] = (2 * c2 if name == "K44" else c2 / 2) / v * GPA
    return out


hm = pd.read_csv(ROOT / "data" / "hm_shear_clamped.csv")  # the 94 alloys of the omat blind test
comps = [parse_comp(s) for s in hm.comp]
need = sorted({(a, b) for c in comps for a, b, _, _ in ctx.pairs(c)})

if not any(e["claim"].startswith(CLAIM) and "prereg" in e["notes"] for e in ledger.entries()):
    ledger.record(f"{CLAIM} (prereg, before any mpa curvature exists): redo binaries and the 94 hm_fresh alloys with "
                  "medium-mpa-0 (fcc C' bias -11% vs omat ~0); survives if K' RMSE(rule) <= 0.9 pair-at-V_ij, sign-flip "
                  "p < 0.005 and bootstrap 95% CI of refit k contains 1", "L0", [SCRIPT], notes="prereg; robustness of 697c2d6d75")

done = set(map(tuple, pd.read_csv(BIN)[["pair", "dlnV"]].astype(str).values)) if BIN.exists() else set()
for A, B in need:
    alloy = compute.solid_solution({A: 0.5, B: 0.5}, "fcc", reps=3, seed=0)
    for d in GRID:
        if (f"{A}-{B}", str(d)) in done:
            continue
        v = ctx.pair[(A, B)]["V"] * np.exp(d)
        r = {"pair": f"{A}-{B}", "seed": 0, "dlnV": d, "V": v, **curvatures(alloy, {A: 0.5, B: 0.5}, v)}
        pd.DataFrame([r]).to_csv(BIN, mode="a", header=not BIN.exists(), index=False)
    print("binary", A, B, flush=True)

g = pd.read_csv(BIN)
spl = {(tuple(k.split("-")), ch): CubicSpline(s.dlnV, s[ch]) for k, s in g.groupby("pair") for ch in ("K44", "Kp")}

done = set(pd.read_csv(TGT)["comp"]) if TGT.exists() else set()
for s, c in zip(hm.comp, comps):
    if s in done:
        continue
    alloy = compute.solid_solution(c, "fcc", reps=3, seed=0)
    x = compute.actual_fractions(alloy)
    r = {"comp": s, "V0": ctx.vegard(c), **curvatures(alloy, x, ctx.vegard(c)),
         "time": dt.datetime.now().isoformat(timespec="seconds")}
    pd.DataFrame([r]).to_csv(TGT, mode="a", header=not TGT.exists(), index=False)
print("targets done", flush=True)

t = pd.read_csv(TGT).set_index("comp").loc[hm.comp]
rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731
res = {}
for ch in ("Kp", "K44"):
    y = t[ch].values
    rule = np.array([sum(4 * xa * xb * float(spl[((a, b), ch)](np.log(ctx.vegard(c) / ctx.pair[(a, b)]["V"])))
                         for a, b, xa, xb in ctx.pairs(c)) for c in comps])
    pair = np.array([sum(4 * xa * xb * float(spl[((a, b), ch)](0.0)) for a, b, xa, xb in ctx.pairs(c)) for c in comps])
    gain = 1 - rm(y - rule) / rm(y - pair)
    dd = (y - pair) ** 2 - (y - rule) ** 2
    rng = np.random.default_rng(0)
    p = (np.sum(np.array([(dd * rng.choice([-1, 1], len(dd))).mean() for _ in range(4000)]) >= dd.mean()) + 1) / 4001
    T, R = rule - pair, y - pair
    k = float(T @ R / (T @ T))
    bs = [(T[i] @ R[i]) / (T[i] @ T[i]) for i in (rng.integers(0, len(y), len(y)) for _ in range(2000))]
    lo, hi = np.percentile(bs, [2.5, 97.5])
    res[ch] = gain >= 0.10 and p < 0.005 and lo <= 1 <= hi
    print(f"{ch}{'' if ch == 'Kp' else ' (not gated)'}: pair at V_ij {rm(y - pair):.2f}, rule {rm(y - rule):.2f} GPa, "
          f"gain {gain:.2f}, p {p:.1e}, refit k {k:.2f} [{lo:.2f}, {hi:.2f}] -> {'pass' if res[ch] else 'fail'}", flush=True)
ledger.record(f"{CLAIM}: K' {'SURVIVES' if res['Kp'] else 'FAILS'} under medium-mpa-0 on 94 hm_fresh alloys "
              f"(K44 not gated: {'pass' if res['K44'] else 'fail'})", "L0", [str(BIN), str(TGT), SCRIPT],
              notes="robustness of 697c2d6d75; prereg in the entry before")

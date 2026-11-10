"""Direct common-volume control for the volume-transfer coefficient k ~ 0.8 (suggested by Astra, .orchestra/astra_k.md).

python scripts/k_direct.py [--analyse]
The champion moves each binary interaction from its own Vegard volume V_ij to the alloy's V0 linearly:
    E_mix ~ sum 4 x_i x_j [E_ij + k D_ij ln(V0/V_ij)],  k fitted 0.81.
Here every 50:50 binary (SQS seeds 0-2, same protocol as scripts/binary_seeds.py) is computed directly on a grid
ln(V/V_ij) in [-0.40, 0.40], so the exact transfer E_ij(V0) needs no Taylor expansion. Then fit
    y = sum 4 x_i x_j E_ij(V_ij) + k_exact * sum 4 x_i x_j [E_ij(V0) - E_ij(V_ij)]
on the training rows at the volume each target was computed at.
Pre-registered reading (ledger note written before the grid exists): if the bootstrap 95% CI of k_exact contains 1,
k ~ 0.8 was a linearisation artefact; if its upper end is below 0.95, the alloy's pair energy really responds less to
volume than the binary's and the mechanism stays open.
"""

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.environ["HARNESS_MODEL"] = "medium-omat-0"
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from scipy.interpolate import CubicSpline  # noqa: E402

from harness import ledger  # noqa: E402
from harness.context import context  # noqa: E402
from harness.features import parse_comp  # noqa: E402

OUT = ROOT / "data" / "binary_vgrid.csv"
GRID = np.round(np.arange(-0.40, 0.4001, 0.05), 2)
ctx = context()

if "--analyse" not in sys.argv:
    if not OUT.exists():
        ledger.record("Pre-registration, direct common-volume control of k: fit k_exact on exact binary energies at the "
                      "alloy volume; CI containing 1 means k ~ 0.8 is a linearisation artefact, CI upper < 0.95 means "
                      "a real reduced volume response of pair energies in the alloy", "L0", [str(Path(__file__))],
                      notes="prereg; diagnostic, no new candidate")
    import time

    from ase.build import bulk

    from harness import compute

    calc = compute.calculator()
    done = set(map(tuple, pd.read_csv(OUT)[["pair", "seed", "dlnV"]].astype(str).values)) if OUT.exists() else set()
    pe = {}

    def e_at(atoms, v):
        a = atoms.copy()
        a.set_cell(a.cell * (v * len(a) / a.get_volume()) ** (1 / 3), scale_atoms=True)
        a.calc = calc
        return a.get_potential_energy() / len(a)

    for (A, B), p in sorted(ctx.pair.items()):
        for seed in (0, 1, 2):
            alloy = compute.solid_solution({A: 0.5, B: 0.5}, "fcc", reps=3, seed=seed)
            rows = []
            for d in GRID:
                if (f"{A}-{B}", str(seed), str(d)) in done:
                    continue
                v = p["V"] * np.exp(d)
                for el in (A, B):
                    pe.setdefault((el, d, A, B), e_at(bulk(el, "fcc", a=4.0, cubic=True), v))
                t = time.perf_counter()
                em = e_at(alloy, v) - 0.5 * (pe[(A, d, A, B)] + pe[(B, d, A, B)])
                rows.append({"pair": f"{A}-{B}", "seed": seed, "dlnV": d, "V": v, "E_mix": em})
                time.sleep(time.perf_counter() - t)  # 50% duty cycle, keeps the laptop cool
            if rows:
                pd.DataFrame(rows).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
        print(A, B, flush=True)

g = pd.read_csv(OUT).groupby(["pair", "dlnV"]).E_mix.mean().reset_index()
spl = {tuple(k.split("-")): CubicSpline(s.dlnV, s.E_mix) for k, s in g.groupby("pair")}

frames = []
for f in ("h1_ev_rows_fixed.csv", "h3_fresh_rows_fixed.csv", "hm_fresh_rows_fixed.csv"):
    frames.append(pd.read_csv(ROOT / "data" / f)[["comp_actual", "n_el", "V0", "E_mix"]])
tr = pd.concat(frames)
tr = tr[tr.n_el >= 3]
tr["c"] = tr.comp_actual.map(parse_comp)
tr = tr[tr.c.map(lambda c: all((a, b) in spl for a, b, _, _ in ctx.pairs(c)))].reset_index(drop=True)

base, lin, ex, ex2 = [], [], [], []
for c, v0 in zip(tr.c, tr.V0):
    b = l = e = e2 = 0.0
    for a, bb, xa, xb in ctx.pairs(c):
        p, s, w = ctx.pair[(a, bb)], spl[(a, bb)], 4 * xa * xb
        u, u2 = np.log(v0 / p["V"]), np.log(ctx.vegard(c) / p["V"])
        b += w * s(0)
        l += w * p["D"] * u2
        e += w * (s(u) - s(0))
        e2 += w * (s(u2) - s(0))
    base.append(b), lin.append(l), ex.append(e), ex2.append(e2)
y, base, lin, ex, ex2 = (np.array(a) for a in (tr.E_mix, base, lin, ex, ex2))
rm = lambda e: float(np.sqrt(np.mean(np.square(e))) * 1000)  # noqa: E731


def kfit(T, idx=slice(None)):
    r, t = (y - base)[idx], T[idx]
    return float(t @ r / (t @ t))


rng = np.random.default_rng(0)
boots = np.array([[kfit(T, i) for T in (lin, ex, ex2)] for i in (rng.integers(0, len(y), len(y)) for _ in range(2000))])
lo, hi = np.percentile(boots, [2.5, 97.5], axis=0)
for name, T, j in (("linear (champion form)", lin, 0), ("exact at target V0", ex, 1), ("exact at Vegard(actual)", ex2, 2)):
    k = kfit(T)
    print(f"{name:26s} k {k:.3f} [{lo[j]:.3f}, {hi[j]:.3f}]  RMSE k=1 {rm(y - base - T):.1f}  k fit {rm(y - base - k * T):.1f}"
          f"  no transfer {rm(y - base):.1f} meV  (n {len(y)})")
k, (l1, h1) = kfit(ex), (lo[1], hi[1])
verdict = "linearisation artefact" if l1 <= 1 <= h1 else ("real reduced volume response" if h1 < 0.95 else "inconclusive")
print("->", verdict)
if "--analyse" in sys.argv and "--record" in sys.argv:
    ledger.record(f"Direct common-volume control: exact binary transfer gives k_exact {k:.2f} [{l1:.2f}, {h1:.2f}] "
                  f"(n {len(y)}); reading: {verdict}", "L0", [str(OUT), str(Path(__file__))],
                  notes="diagnostic of champion k; prereg in the note before")

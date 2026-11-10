"""R3b: does the ordering energy share the volume exponent of the random mixing energy? (redo of R3 without its flaws)

python scripts/r3b_l12.py
R3 (19861d971e) failed for design reasons found in the audit of 2026-10-31: (1) n_eff = -3 b/a diverges where the
random E_mix is near zero (Cu-Rh -61, Cu-Ir -102); (2) the observed volume compared a relaxed random cell with a
clamped L1_0 cell, so even the exact first-order estimate had slope 0.20. R3b tests the same physics on clamped
energies only, on fresh cells: A3B L1_2 vs the h1 random A0.75B0.25 rows (never used by R3).
  E_ord = E_L12(V0) - E_rand(V0),  S_ord = dE_L12/dlnV - dE_rand/dlnV  (central difference, +-0.02 in lnV)
  prediction: S_ord = (dE_rand/dlnV / E_rand) * E_ord      (same exponent; zero free coefficients)
Pre-registered criteria in the ledger entry written before this script's first output.
"""

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.environ["HARNESS_MODEL"] = "medium-omat-0"
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from ase.build import bulk  # noqa: E402

from harness import compute, ledger  # noqa: E402
from harness.features import parse_comp  # noqa: E402

CRITERIA = "0dffc5bf40"  # ledger id of the pre-registration
pv = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")["vol_per_atom"]
h1 = pd.read_csv(ROOT / "data" / "h1_ev_rows.csv")
h1["c"] = h1.comp.map(parse_comp)
rows_in = h1[(h1.n_el == 2) & h1.c.map(lambda c: sorted(round(v, 2) for v in c.values()) == [0.25, 0.75])]
calc = compute.calculator()


def e_at(symbols, v):
    a = bulk("Cu", "fcc", a=4.0, cubic=True)
    a.symbols = list(symbols)
    a.set_cell(a.cell * (v * 4 / a.get_volume()) ** (1 / 3), scale_atoms=True)
    a.calc = calc
    return a.get_potential_energy() / 4


rows = []
for _, r in rows_in.iterrows():
    A = max(r.c, key=r.c.get)
    B = min(r.c, key=r.c.get)
    v0 = r.V0
    em = {}
    for d in (-0.02, 0.0, 0.02):
        v = v0 * np.exp(d)
        em[d] = e_at([B, A, A, A], v) - 0.75 * e_at([A] * 4, v) - 0.25 * e_at([B] * 4, v)
    e_ord = em[0.0] - r.E_mix
    s_ord = (em[0.02] - em[-0.02]) / 0.04 - r.dE_dlnV
    rows.append({"cell": f"{A}3{B}", "E_rand": r.E_mix, "S_rand": r.dE_dlnV, "E_L12": em[0.0], "E_ord": e_ord,
                 "S_ord": s_ord, "pred": r.dE_dlnV / r.E_mix * e_ord})
    print(rows[-1]["cell"], {k: round(v * 1000, 1) for k, v in rows[-1].items() if k != "cell"}, flush=True)

df = pd.DataFrame(rows)
out = ROOT / "data" / "r3b_l12.csv"
df.to_csv(out, index=False)
t = df[(df.E_rand.abs() >= 0.03) & (df.E_ord.abs() >= 0.02)]
rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731
r_ = float(np.corrcoef(t.pred, t.S_ord)[0, 1]) if len(t) > 2 else float("nan")
slope = float(t.S_ord @ t.pred / (t.pred @ t.pred)) if len(t) else float("nan")
gain = rm(t.S_ord - t.pred) / rm(t.S_ord) if len(t) else float("nan")
passed = bool(len(t) >= 12 and r_ > 0.8 and 0.7 <= slope <= 1.3 and gain <= 0.8)
print(f"n={len(t)} r={r_:.3f} slope={slope:.3f} rmse ratio vs zero {gain:.2f} ->", "SURVIVES" if passed else "FALSIFIED")
ledger.record(f"R3b (ordering energy shares the random-alloy volume exponent, L1_2 vs random x=0.25): "
              f"{'survives' if passed else 'falsified'} (n={len(t)}, r={r_:.2f}, slope={slope:.2f}, rmse/zero {gain:.2f})",
              "L0", [str(out)], notes=f"criteria fixed in {CRITERIA}")

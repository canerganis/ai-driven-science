"""Ordering volume test of ledger 19861d971e: dlnV_ord = (n_eff/3)(E_L10 - E_rand)/(Bbar V0).

python scripts/r3_order_volume.py
Equiatomic binaries from the elastic scan, minus the 7 L1_0 pairs already seen. L1_0 4-atom cell, c/a = 1,
ions fixed by symmetry, isotropic volume relaxed to the energy minimum. Applies the pre-registered criteria.
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
from harness.compute import GPA  # noqa: E402
from harness.features import parse_comp  # noqa: E402

SEEN = {"Cu-Pt", "Cu-Pd", "Au-Cu", "Pd-Pt", "Ag-Ir", "Ir-Pd", "Au-Ir"}
pure = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")
h1 = pd.read_csv(ROOT / "data" / "h1_ev_rows.csv").set_index("comp")
scan = pd.concat([pd.read_csv(ROOT / "data" / f) for f in ("scan_fcc_omat.csv", "scan_fcc_omat_rev.csv")])
scan = scan[scan.cubic_spread < 0.1].drop_duplicates("comp").set_index("comp")
calc = compute.calculator()


def e_at(atoms, v_atom):
    a = atoms.copy()
    a.set_cell(a.cell * (v_atom * len(a) / a.get_volume()) ** (1 / 3), scale_atoms=True)
    a.calc = calc
    return a.get_potential_energy() / len(a)


rows = []
for c in scan.index:
    comp = parse_comp(c)
    fam = "-".join(sorted(comp))
    if len(comp) != 2 or set(np.round(list(comp.values()), 3)) != {0.5} or fam in SEEN or c not in h1.index:
        continue
    A, B = sorted(comp)
    l10 = bulk(A, "fcc", a=4.0, cubic=True)
    l10.symbols[[2, 3]] = B
    v0 = 0.5 * (pure.vol_per_atom[A] + pure.vol_per_atom[B])
    e_l10 = e_at(l10, v0) - 0.5 * (e_at(bulk(A, "fcc", a=4.0), v0) + e_at(bulk(B, "fcc", a=4.0), v0))
    vs = v0 * np.linspace(0.94, 1.06, 9)
    p = np.polyfit(vs, [e_at(l10, v) for v in vs], 3)
    roots = np.roots(np.polyder(p))
    v_l10 = float(min((r.real for r in roots if abs(r.imag) < 1e-9 and np.polyval(np.polyder(p, 2), r.real) > 0),
                      key=lambda r: abs(r - v0)))
    bv = sum(x * pure.B[el] / GPA * pure.vol_per_atom[el] for el, x in comp.items())
    e_ord = e_l10 - h1.E_mix[c]
    rows.append({"pair": fam, "E_L10": e_l10, "E_rand": h1.E_mix[c], "E_ord": e_ord, "n_eff": h1.n_eff[c],
                 "pred": h1.n_eff[c] / 3 * e_ord / bv, "obs": np.log(v_l10 / scan.vol_per_atom[c])})
    print(rows[-1]["pair"], {k: round(v, 4) for k, v in rows[-1].items() if k != "pair"}, flush=True)

df = pd.DataFrame(rows)
out = ROOT / "data" / "r3_order_volume.csv"
df.to_csv(out, index=False)
t = df[df.E_ord.abs() > 0.02]
r = float(np.corrcoef(t.pred, t.obs)[0, 1]) if len(t) > 2 else float("nan")
slope = float(t.obs @ t.pred / (t.pred @ t.pred)) if len(t) else float("nan")
passed = bool(len(t) >= 12 and r > 0.8 and 0.7 <= slope <= 1.3)
print(f"n={len(t)} r={r:.3f} slope={slope:.3f} ->", "SURVIVES" if passed else "FALSIFIED")
ledger.record(f"R3 ordering-volume test: {'survives' if passed else 'falsified'} (n={len(t)}, r={r:.2f}, slope={slope:.2f})",
              "L0", [str(out)], notes="criteria fixed in 19861d971e")

"""Mixing energy for every scanned fcc alloy: python scripts/backfill_emix.py

Rebuilds the same random cell (same seed) the scan used, relaxes it and stores
E_mix = E_alloy - sum c_i E_i (eV/atom, pure elements in fcc) in data/scan_fcc_omat_emix.csv.
Only alloys missing from that file are computed, so it can be rerun as the scan grows.
"""

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.environ["HARNESS_MODEL"] = "medium-omat-0"
sys.path.insert(0, str(ROOT))

import pandas as pd  # noqa: E402

from harness import compute  # noqa: E402
from harness.features import parse_comp  # noqa: E402

DATA = ROOT / "data"
OUT = DATA / "scan_fcc_omat_emix.csv"
PURE_E = DATA / "scan_fcc_omat_pure_energy.csv"


def energy(comp: dict[str, float], reps: int) -> tuple[float, float]:
    atoms = compute.solid_solution(comp, "fcc", reps, seed=0)
    compute.relax(atoms, cell=True)
    return atoms.get_potential_energy() / len(atoms), atoms.get_volume() / len(atoms)


scan = pd.concat([pd.read_csv(f) for f in (DATA / "scan_fcc_omat.csv", DATA / "scan_fcc_omat_rev.csv")
                  if f.exists()]).drop_duplicates("comp")
els = sorted({el for c in scan.comp for el in parse_comp(c)})
pure = pd.read_csv(PURE_E).set_index("el") if PURE_E.exists() else pd.DataFrame()
missing = [el for el in els if el not in pure.index]
if missing:
    rows = pd.DataFrame([{"el": el, "e_per_atom": energy({el: 1.0}, 1)[0]} for el in missing]).set_index("el")
    pure = pd.concat([pure, rows])
    pure.reset_index().to_csv(PURE_E, index=False)
done = set(pd.read_csv(OUT)["comp"]) if OUT.exists() else set()
for row in scan[~scan.comp.isin(done)].itertuples():
    comp = parse_comp(row.comp)
    e, v = energy(comp, 3)
    emix = e - sum(x * pure.loc[el, "e_per_atom"] for el, x in comp.items())
    # Volume check: the rebuilt cell must match the scanned one, or this is not the same structure.
    rec = {"comp": row.comp, "e_per_atom": e, "E_mix": emix, "vol_check": v / row.vol_per_atom - 1}
    pd.DataFrame([rec]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
    print(row.formula, f"E_mix {emix * 1000:+.1f} meV/atom, vol check {rec['vol_check']:+.4f}", flush=True)

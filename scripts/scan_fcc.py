"""Checkpointed fcc solid solution scan with medium-omat-0 (the only L1-passing model, fcc only).

python scripts/scan_fcc.py
Appends one row per alloy to data/scan_fcc_omat.csv and skips rows already there, so it can be
killed and restarted. Pure element fcc references go to data/scan_fcc_omat_pure.csv.
"""

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.environ["HARNESS_MODEL"] = "medium-omat-0"
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from harness import compute  # noqa: E402
from harness.baselines import rule_of_mixtures  # noqa: E402
from harness.fcc_set import POOL, compositions, key  # noqa: E402
from harness.features import descriptors, mismatch, misfit  # noqa: E402

# Optional "rev": a second worker that walks the list backwards into its own file.
REV = len(sys.argv) > 1 and sys.argv[1] == "rev"
MAIN = ROOT / "data" / "scan_fcc_omat.csv"
OUT = ROOT / "data" / ("scan_fcc_omat_rev.csv" if REV else "scan_fcc_omat.csv")
PURE = ROOT / "data" / "scan_fcc_omat_pure.csv"


if PURE.exists():
    pure = pd.read_csv(PURE)
else:
    pure = pd.DataFrame([compute.run_alloy({el: 1.0}, "fcc", reps=1) | {"el": el} for el in POOL])
    pure.to_csv(PURE, index=False)
pure = pure.set_index("el")

def done() -> set[str]:
    files = [MAIN, MAIN.with_name("scan_fcc_omat_rev.csv")]
    return set().union(*(set(pd.read_csv(f)["comp"]) for f in files if f.exists()))


todo = [c for c in compositions() if key(c) not in done()]
if REV:
    todo.reverse()
print(f"{len(todo)} to go", flush=True)
for comp in todo:
    if key(comp) in done():  # the other worker got there first
        continue
    r = compute.run_alloy(comp, "fcc", reps=3, seed=0)
    r.update(descriptors(comp))
    r.update(misfit(comp, {el: pure.loc[el, "vol_per_atom"] for el in comp}, r["vol_per_atom"]))
    for k in ("B", "G", "C11", "C12", "C44", "vol_per_atom"):
        r[f"{k}_rom"] = rule_of_mixtures(comp, {el: pure.loc[el, k] for el in comp})
    for k in ("B", "G", "C44"):
        r[f"d_{k}"] = mismatch(comp, {el: pure.loc[el, k] for el in comp})
    r["family"] = "-".join(sorted(comp))
    pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
    print(r["formula"], f"B {r['B']:.1f}/{r['B_rom']:.1f} G {r['G']:.1f}/{r['G_rom']:.1f}",
          f"spread {r['cubic_spread']:.2f}", flush=True)

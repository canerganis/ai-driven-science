"""End to end smoke test: calibrate on pure metals, compute a few fcc alloys, search residuals."""

import datetime as dt
import itertools
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from harness import compute, discover, ledger  # noqa: E402
from harness.baselines import rule_of_mixtures  # noqa: E402
from harness.features import descriptors, misfit, parse_comp  # noqa: E402

stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
data = ROOT / "data"
data.mkdir(exist_ok=True)

# L1: calibration against experiment.
cal = pd.DataFrame(compute.calibrate())
cal_path = data / f"calibration_{stamp}.csv"
cal.to_csv(cal_path, index=False)
for k in ("C11", "C12", "C44", "B", "G"):
    rel = (cal[k] - cal[f"{k}_exp"]) / cal[f"{k}_exp"]
    print(f"{k}: mean rel err {rel.mean():+.3f}, MAE {rel.abs().mean():.3f}")
ledger.record("MACE-MP medium elastic constants calibrated on 14 cubic metals",
              "L1", [str(cal_path)], notes="see per element errors in csv")

# Small fcc alloy set from elements with fcc ground state.
fcc = ["Ni", "Cu", "Pd", "Pt", "Ag", "Au", "Al"]
pure = cal.set_index("el")
comps = [dict.fromkeys(s, 1 / len(s)) for n in (2, 3) for s in itertools.combinations(fcc, n)][:12]
rows = []
for comp in comps:
    r = compute.run_alloy(comp, "fcc", reps=2, seed=0)
    r.update(descriptors(comp))
    r.update(misfit(comp, {el: pure.loc[el, "vol_per_atom"] for el in comp}, r["vol_per_atom"]))
    for k in ("B", "G"):
        r[f"{k}_rom"] = rule_of_mixtures(comp, {el: pure.loc[el, k] for el in comp})
    r["family"] = "-".join(sorted(comp))
    rows.append(r)
    print(r["formula"], f"B={r['B']:.1f} (RoM {r['B_rom']:.1f})", f"G={r['G']:.1f} (RoM {r['G_rom']:.1f})")
alloys = pd.DataFrame(rows)
al_path = data / f"alloys_fcc_{stamp}.csv"
alloys.to_csv(al_path, index=False)

cols = ["delta_r", "d_chi", "vec", "S_mix", "vegard_dev", "misfit_sum"]
for target in ("B", "G"):
    res = discover.search(alloys, target, f"{target}_rom", cols, group="family", n_perm=200)
    print(f"\nResidual search for {target} - {target}_rom:")
    print(res.head(5).to_string(index=False))
print(f"\nwrote {cal_path.name}, {al_path.name}; ledger at {ledger.LEDGER}")

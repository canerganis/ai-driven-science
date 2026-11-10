"""L1 calibration of one foundation model: python scripts/calibrate.py <model name>."""

import datetime as dt
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.environ["HARNESS_MODEL"] = sys.argv[1]
sys.path.insert(0, str(ROOT))

import pandas as pd  # noqa: E402

from harness import compute, ledger  # noqa: E402

cal = pd.DataFrame(compute.calibrate())
path = ROOT / "data" / f"calibration_{sys.argv[1]}_{dt.datetime.now():%Y%m%d_%H%M%S}.csv"
cal.to_csv(path, index=False)
summary = []
for k in ("C11", "C12", "C44", "B", "G"):
    rel = (cal[k] - cal[f"{k}_exp"]) / cal[f"{k}_exp"]
    for lat in ("fcc", "bcc"):
        r = rel[cal.lattice == lat]
        summary.append(f"{k} {lat}: bias {r.mean():+.3f} MAE {r.abs().mean():.3f}")
print("\n".join(summary))
print(cal[["el", "C11", "C11_exp", "C12", "C12_exp", "C44", "C44_exp"]].round(1).to_string(index=False))
ledger.record(f"{sys.argv[1]} elastic constants calibrated on {len(cal)} cubic metals", "L1",
              [str(path)], notes="; ".join(summary))

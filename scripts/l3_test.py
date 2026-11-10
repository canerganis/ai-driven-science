"""Apply pre-registered L3 criteria 6192ffda51 to data/l3_transfer_dft.csv. No tuning."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from harness import ledger  # noqa: E402

path = ROOT / "data" / "l3_transfer_dft.csv"
d = pd.read_csv(path)
y, T = (d.E_mix - d.naive).values, (d.rule - d.naive).values
rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731
r_rule, r_int = rm(y - T - np.mean(y - T)), rm(y - y.mean())
gain = 1 - r_rule / r_int
X = np.column_stack([np.ones_like(T), T])
k = np.linalg.lstsq(X, y, rcond=None)[0][1]
rng = np.random.default_rng(0)
ks = []
for _ in range(2000):
    i = rng.integers(0, len(y), len(y))
    ks.append(np.linalg.lstsq(X[i], y[i], rcond=None)[0][1])
lo, hi = np.percentile(ks, [2.5, 97.5])
passed = bool(len(d) >= 15 and r_rule <= 0.9 * r_int and lo > 0 and 0.5 <= lo and hi <= 2)
print(f"n {len(d)}  RMSE intercept-only {r_int*1000:.1f}, rule+intercept {r_rule*1000:.1f} meV, gain {gain:.2f}")
print(f"refit k {k:.2f}, 95% CI [{lo:.2f}, {hi:.2f}], r(y,T) {np.corrcoef(y, T)[0, 1]:.2f}")
print(f"raw RMSE naive {rm(y)*1000:.1f}, rule {rm(y - T)*1000:.1f} meV")
print("L3", "PASS" if passed else "FAIL")
parent = [e["id"] for e in map(__import__("json").loads, (ROOT / "claims" / "claims.jsonl").read_text().splitlines())
          if e["level"] == "L2" and "volume-transfer" in e["claim"]][-1]
level = "L3" if passed else "L0"
ledger.record(f"L3 test of volume-transfer rule in 16 PBE ordered cells: {'pass' if passed else 'fail'} "
              f"(gain {gain:.2f} over intercept-only, refit k {k:.2f} CI [{lo:.2f}, {hi:.2f}], raw RMSE naive "
              f"{rm(y)*1000:.1f} -> rule {rm(y - T)*1000:.1f} meV)", level, [str(path)],
              notes="criteria fixed in 6192ffda51", parent=parent if passed else None)

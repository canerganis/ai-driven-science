"""Apply pre-registered criteria for A2 (5ac00dd12d), H-iso (24add7fc3f) and H-sm (bca6a70915). No tuning."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from harness import ledger  # noqa: E402
from harness.compute import GPA  # noqa: E402

path = ROOT / "data" / "a2_shear_clamped.csv"
m = pd.read_csv(path).merge(pd.read_csv(ROOT / "data" / "h1_ev_rows.csv")[["comp", "dE_dlnV", "d2E_dlnV2"]], on="comp")
E1, E2, V = m.dE_dlnV, m.d2E_dlnV2, m.V0
m["p44"] = (0.75 * E2 + 0.5 * E1) / V * GPA
m["pp"] = (0.375 * E2 + 0.75 * E1) / V * GPA
rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731
ok = []
for k, p in (("K44", "p44"), ("Kp", "pp")):
    y = m[k]
    rp, rmean, r0 = rm(y - m[p]), rm(y - y.mean()), rm(y)
    ok.append(rp <= 0.9 * rmean and rp <= 0.9 * r0)
    print(f"A2 {k}: n={len(m)} RMSE pred {rp:.2f}, mean {rmean:.2f}, zero {r0:.2f} GPa, r {np.corrcoef(y, m[p])[0, 1]:.3f}")
a2 = bool(all(ok))
ident = float(np.corrcoef(m.K44 - 2 * m.Kp, -E1 / V * GPA)[0, 1])
print("A2", "SURVIVES" if a2 else "FALSIFIED", f"(identity K44-2Kp vs -E1/V r {ident:.2f})")
ledger.record(f"A2 test, 160 alloys: {'survives' if a2 else 'falsified'} (channels {ok}, identity r {ident:.2f})", "L0",
              [str(path)], notes="criteria fixed in 5ac00dd12d")

seen = set((ROOT / "data" / "a2_seen_interim.txt").read_text().split())
t = m[~m.comp.isin(seen) & (np.maximum(m.K44.abs(), m.Kp.abs()) > 10)]
r = float(np.corrcoef(t.K44, t.Kp)[0, 1])
d = ((t.K44 - t.Kp).abs() / ((t.K44.abs() + t.Kp.abs()) / 2)).median()
iso = bool(len(t) >= 15 and r > 0.9 and d < 0.3)
same = t[np.sign(t.K44) == np.sign(t.Kp)]
ratio = float((same.K44 / same.Kp).median()) if len(same) else float("nan")
sm = bool(len(t) >= 15 and 3 <= ratio <= 5 and len(same) / len(t) >= 0.6)
print(f"H-iso: n={len(t)} r {r:.3f}, median rel diff {d:.2f} ->", "SURVIVES" if iso else "FALSIFIED")
print(f"H-sm: median K44/Kp {ratio:.2f}, same sign {len(same)}/{len(t)} ->", "SURVIVES" if sm else "FALSIFIED")
print(t.assign(ratio=t.K44 / t.Kp)[["family", "K44", "Kp", "ratio"]].round(2).sort_values("K44").to_string(index=False))
ledger.record(f"H-iso test: {'survives' if iso else 'falsified'} (n={len(t)}, r {r:.2f}, median rel diff {d:.2f}); "
              f"H-sm: {'survives' if sm else 'falsified'} (median ratio {ratio:.2f})", "L0", [str(path)],
              notes="criteria fixed in 24add7fc3f and bca6a70915; 24 interim rows excluded")

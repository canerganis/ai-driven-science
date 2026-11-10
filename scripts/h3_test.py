"""Apply the pre-registered H3 criteria (ledger 8d162cad59) to the fresh held-out set. No tuning."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import pandas as pd  # noqa: E402

from harness import ledger  # noqa: E402

path = ROOT / "data" / "h3_fresh_rows.csv"
df = pd.read_csv(path)
att, rep = df[df.E_mix < -0.05], df[df.E_mix > 0.05]
fa, fr = att.R.between(0.7, 1.5).mean(), rep.R.between(0.7, 1.5).mean()
passed = bool(fa >= 0.8 and fa - fr >= 0.3)
print(f"rows {len(df)}: attractive n={len(att)} in band {fa:.0%}; repulsive n={len(rep)} in band {fr:.0%}; "
      f"weak |E_mix|<=50 meV n={len(df) - len(att) - len(rep)}")
print("H3", "SURVIVES" if passed else "FALSIFIED")
print("attractive n_eff median", round(att.n_eff.median(), 2), "IQR",
      att.n_eff.quantile([.25, .75]).round(2).tolist())
print(rep.sort_values("R")[["family", "E_mix", "n_eff", "R"]].round(3).to_string(index=False))
ledger.record(f"H3 test on fresh set ({len(df)} alloys): {'survives' if passed else 'falsified'} "
              f"(attractive {fa:.0%} in band, n={len(att)}; repulsive {fr:.0%}, n={len(rep)})",
              "L0", [str(path)], notes="criteria fixed in 8d162cad59 before the fresh set existed")

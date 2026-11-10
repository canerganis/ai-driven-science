"""Apply the pre-registered H2 criteria (ledger b75e66ffd8) to the unseen test set. No tuning.

Test set: Al-free alloys with 3 to 5 elements and |E_mix| > 50 meV/atom.
Pass: median n_eff in [8, 12] and at least 70% of rows with R in [0.7, 1.5].
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import pandas as pd  # noqa: E402

from harness import ledger  # noqa: E402

path = ROOT / "data" / "h1_ev_rows.csv"
df = pd.read_csv(path)
al_free = ~df.comp.str.contains("Al:")
test = df[al_free & df.n_el.between(3, 5) & (df.E_mix.abs() > 0.05)]
train = df[al_free & (df.n_el == 2) & (df.E_mix.abs() > 0.05)]
for name, d in (("seen binaries", train), ("TEST multicomponent", test)):
    inR = d.R.between(0.7, 1.5).mean() if len(d) else float("nan")
    print(f"{name}: n={len(d)}  median n_eff {d.n_eff.median():.2f}  "
          f"IQR [{d.n_eff.quantile(.25):.2f}, {d.n_eff.quantile(.75):.2f}]  R in band {inR:.0%}")
med, inR = test.n_eff.median(), test.R.between(0.7, 1.5).mean()
passed = bool(8 <= med <= 12 and inR >= 0.7)
print("H2", "SURVIVES" if passed else "FALSIFIED", f"(median {med:.2f}, R band {inR:.0%}, n={len(test)})")
print(test.sort_values("n_eff")[["family", "E_mix", "n_eff", "R", "fit_rms_meV"]].round(3).to_string(index=False))
ledger.record(f"H2 test on {len(test)} unseen Al-free multicomponent alloys: "
              f"{'survives' if passed else 'falsified'} (median n_eff {med:.2f}, {inR:.0%} with R in band)",
              "L0", [str(path)], notes="criteria fixed in b75e66ffd8 before the test rows existed")

"""MACE vs DFT on clamped E_mix(V) of L1_0 pairs, criteria fixed in ledger e5425db058."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from harness import ledger  # noqa: E402

m = pd.read_csv(ROOT / "data" / "l10_ev_mace.csv").set_index("pair")
d = pd.read_csv(ROOT / "data" / "l10_ev_dft.csv").set_index("pair")
j = m[["E_mix", "n_eff", "R"]].join(d[["E_mix", "n_eff", "R"]], lsuffix="_mace", rsuffix="_dft", how="inner")
print(j.round(3).to_string())
sign = bool((np.sign(j.E_mix_mace) == np.sign(j.E_mix_dft)).all())
att = j[j.E_mix_dft < 0]
nratio = bool(((att.n_eff_mace / att.n_eff_dft - 1).abs() <= 0.3).all())
split = int(((j.n_eff_mace > 6) == (j.n_eff_dft > 6)).sum())
passed = sign and nratio and split >= 6 and len(j) == 7
print(f"(a) signs agree: {sign}  (b) attractive n_eff within 30%: {nratio}  (c) split matches {split}/7")
print("MACE", "PASSES" if passed else "FAILS", "L1 for clamped E_mix(V)")
ledger.record(f"MACE {'passes' if passed else 'fails'} L1 for clamped E_mix(V) on {len(j)} L1_0 pairs vs PBE "
              f"(signs {sign}, n_eff within 30% {nratio}, split {split}/7)", "L1",
              [str(ROOT / "data" / "l10_ev_mace.csv"), str(ROOT / "data" / "l10_ev_dft.csv")],
              notes="criteria e5425db058")

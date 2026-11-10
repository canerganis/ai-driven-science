"""DFT elastic constants of pure bcc metals vs experiment and vs MACE.

python scripts/dft_bcc_benchmark.py <kspacing> <ecut_scale> [MACE calibration csv]
Separates PBE error (DFT vs experiment) from potential error (MACE vs DFT).
"""

import datetime as dt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import pandas as pd  # noqa: E402
from ase.build import bulk  # noqa: E402

from harness import dft, ledger  # noqa: E402
from harness.compute import A0  # noqa: E402
from harness.reference import ELASTIC_EXP  # noqa: E402

s = dft.Settings(kspacing=float(sys.argv[1]), ecut_scale=float(sys.argv[2]))
mace = pd.read_csv(sys.argv[3]).set_index("el") if len(sys.argv) > 3 else None
rows = []
for el, (lat, e11, e12, e44) in ELASTIC_EXP.items():
    if lat != "bcc":
        continue
    r = dft.run_alloy(bulk(el, "bcc", a=A0["bcc"][el], cubic=True), f"bench/{el}", s)
    r.update({"el": el, "C11_exp": e11, "C12_exp": e12, "C44_exp": e44})
    if mace is not None:
        r.update({f"{k}_mace": mace.loc[el, k] for k in ("C11", "C12", "C44")})
    rows.append(r)
    print({k: (round(v, 1) if isinstance(v, float) else v) for k, v in r.items()
           if k in ("el", "C11", "C11_exp", "C12", "C12_exp", "C44", "C44_exp", "C44_mace")}, flush=True)
df = pd.DataFrame(rows)
path = ROOT / "data" / f"dft_bcc_benchmark_{dt.datetime.now():%Y%m%d_%H%M%S}.csv"
df.to_csv(path, index=False)
notes = []
for k in ("C11", "C12", "C44"):
    rel = (df[k] - df[f"{k}_exp"]) / df[f"{k}_exp"]
    notes.append(f"{k} DFT vs exp: bias {rel.mean():+.3f} MAE {rel.abs().mean():.3f}")
    if mace is not None:
        rm = (df[f"{k}_mace"] - df[k]) / df[k]
        notes.append(f"{k} MACE vs DFT: bias {rm.mean():+.3f} MAE {rm.abs().mean():.3f}")
print("\n".join(notes))
ledger.record(f"PBE/SSSP elastic constants of {len(df)} bcc metals ({df.method[0]})", "L1",
              [str(path)], notes="; ".join(notes))

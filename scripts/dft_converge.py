"""k-point and cutoff convergence of cubic elastic constants: python scripts/dft_converge.py Nb 3.30"""

import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import pandas as pd  # noqa: E402
from ase.build import bulk  # noqa: E402

from harness import dft  # noqa: E402
from harness.compute import cubic_average  # noqa: E402

el, a0 = sys.argv[1], float(sys.argv[2])
atoms = bulk(el, "bcc", a=a0, cubic=True)
rows = []
for k, ec in [(0.20, 1.25), (0.15, 1.25), (0.10, 1.25), (0.07, 1.25), (0.10, 1.6)]:
    s = dft.Settings(kspacing=k, ecut_scale=ec)
    t = time.time()
    c11, c12, c44 = cubic_average(dft.elastic_cubic(atoms, f"conv/{el}_k{k}_e{ec}", s))
    rows.append({"el": el, "kspacing": k, "kgrid": dft.kgrid(atoms, k), "ecut_scale": ec,
                 "C11": c11, "C12": c12, "C44": c44, "sec": time.time() - t})
    print(rows[-1], flush=True)
pd.DataFrame(rows).to_csv(ROOT / "data" / f"dft_convergence_{el}.csv", index=False)

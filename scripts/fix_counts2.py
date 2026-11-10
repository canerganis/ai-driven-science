"""Second correction of the E(V) rows (S1 audit, LESSONS 12b-c). Writes *_fixed2.csv, leaves *_fixed.csv as they are.

python scripts/fix_counts2.py
(b) fix_counts.py took the nominal fractions from the 4-decimal comp key, so equiatomic ternaries got weight 0.3333
    although the generator used 1/3 and 36+36+36 atoms are exact; it added a spurious +0.3 to +0.7 meV. For those rows
    the logged energies carry no reference error, so the raw emix_i are restored and refit.
(c) R and B_chem were copied from the logged fit; here they are recomputed from the corrected curve, with the same
    definitions as scripts/h1_ev.py. fit_rms_meV is recomputed too.
Only h1 has thirds (44 rows); h3, hm_fresh, hm_l2 and the sealed hm3 have none, so the sealed copy needs no new seal.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from harness.compute import GPA  # noqa: E402
from harness.features import parse_comp  # noqa: E402

SCALES = np.linspace(0.97, 1.03, 7)
X = np.log(SCALES**3)
E = [f"emix_{i}" for i in range(7)]


def thirds(comp: str) -> bool:
    c = parse_comp(comp)
    return len(c) == 3 and all(abs(x - 1 / 3) < 1e-3 for x in c.values())


for name in ("h1_ev_rows", "h3_fresh_rows"):
    fx = pd.read_csv(ROOT / "data" / f"{name}_fixed.csv")
    raw = pd.read_csv(ROOT / "data" / f"{name}.csv").set_index("comp")
    t = fx.comp.map(thirds).values
    fx.loc[t, E] = raw.loc[fx.comp[t], E].values
    em = fx[E].values
    c, b, a = np.polyfit(X, em.T, 2)
    fit = np.outer(c, X**2) + np.outer(b, X) + a[:, None]
    old = fx.E_mix.values.copy()
    fx = fx.assign(E_mix=a, dE_dlnV=b, d2E_dlnV2=2 * c, n_eff=-3 * b / a, R=2 * c * a / b**2,
                   B_chem=(2 * c - b) / fx.V0 * GPA, fit_rms_meV=np.sqrt(((em - fit) ** 2).mean(1)) * 1000)
    fx.to_csv(ROOT / "data" / f"{name}_fixed2.csv", index=False)
    d = (fx.E_mix - old) * 1000
    print(f"{name}: {len(fx)} rows, thirds restored {t.sum()}, E_mix change meV on those: "
          f"{d[t].min():+.2f} to {d[t].max():+.2f}, elsewhere max |.| {d[~t].abs().max():.2g}")

"""Retroactive power of the L3 ordered-cell design (6192ffda51) and of the proposed random-cell (SQS) L3 design.

python scripts/power_retro.py
True model: y = T + c + many-body + noise. Null: y = c + many-body + noise (T has no effect).
Ordered cells: T from data/l3_transfer_dft.csv, many-body RMS 15.8 meV (PBE hm_ordered). SQS: T drawn like the MACE
holdouts (data/hm_l2_rows.csv, n_el >= 3), residual RMS 5 meV (no fixed-volume many-body term in random alloys, HM2-T2).
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from harness.power import power  # noqa: E402

rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731


def l3_test(d):
    y, T = d
    gain_ok = rm(y - T - np.mean(y - T)) <= 0.9 * rm(y - y.mean())
    X = np.column_stack([np.ones_like(T), T])
    rng = np.random.default_rng(0)
    ks = [np.linalg.lstsq(X[i], y[i], rcond=None)[0][1] for i in (rng.integers(0, len(y), len(y)) for _ in range(300))]
    lo, hi = np.percentile(ks, [2.5, 97.5])
    return len(y) >= 15 and gain_ok and lo > 0 and lo >= 0.5 and hi <= 2


T_ord = (pd.read_csv(ROOT / "data" / "l3_transfer_dft.csv").eval("rule - naive")).values
T_sqs_pool = pd.read_csv(ROOT / "data" / "hm_l2_rows.csv")["corr"].values


def design(T_draw, mb, k=1.0):
    def true(rng):
        T = T_draw(rng)
        return k * T + 0.01 + rng.normal(0, mb, len(T)) + rng.normal(0, 0.002, len(T)), T

    def null(rng):
        T = T_draw(rng)
        return 0.01 + 0.03 + rng.normal(0, mb, len(T)) + rng.normal(0, 0.002, len(T)), T
    return true, null


for name, draw, mb in (("ordered 4-atom, as run (n=16)", lambda r: T_ord, 0.0158),
                       ("SQS random cells, n=15", lambda r: r.choice(T_sqs_pool, 15), 0.005),
                       ("SQS random cells, n=20", lambda r: r.choice(T_sqs_pool, 20), 0.005),
                       ("SQS, n=20, residual 10 meV", lambda r: r.choice(T_sqs_pool, 20), 0.010)):
    t, n = design(draw, mb)
    print(f"{name:32s}", power(l3_test, t, n, n=200))

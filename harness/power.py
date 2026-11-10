"""Power check for a pre-registered test, run before the test data exist.

A test is only informative if (a) data generated with the hypothesis TRUE, at realistic noise, pass it most of the
time and (b) data with the hypothesis FALSE rarely pass. Both are estimated by simulation. Two failures this tool is
meant to catch, from 2026-10-31: the L3 ordered-cell design (an intercept absorbed the rule's main signal) and R3
(the observable compared relaxed with clamped volumes, so even the exact formula had slope 0.20).
"""

from __future__ import annotations

from typing import Callable

import numpy as np


def power(test: Callable[[object], bool], simulate_true: Callable[[np.random.Generator], object],
          simulate_null: Callable[[np.random.Generator], object], n: int = 300, seed: int = 0) -> dict:
    rng = np.random.default_rng(seed)
    p = np.mean([bool(test(simulate_true(rng))) for _ in range(n)])
    f = np.mean([bool(test(simulate_null(rng))) for _ in range(n)])
    return {"power": round(float(p), 3), "false_pass": round(float(f), 3), "n_sims": n}


def near_zero_divisor(x, name: str, frac: float = 0.1) -> list[int]:
    """Indices where a quantity used as a divisor is small relative to its spread (ratio predictions blow up there)."""
    x = np.asarray(x, dtype=float)
    bad = np.flatnonzero(np.abs(x) < frac * np.std(x))
    if len(bad):
        print(f"warning: {name} near zero at rows {bad.tolist()}; a ratio-based prediction is unstable there")
    return bad.tolist()

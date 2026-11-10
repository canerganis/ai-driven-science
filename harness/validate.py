"""L3 gate: does a correction term found on ML data hold on independent DFT or experiment?

The term's functional form and its coefficient are both fixed on the training (ML) set.
Within each dataset the baseline is built from that dataset's own pure element values,
so a method-wide bias (e.g. MACE shear softening) cancels to first order in the residual.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

from harness.discover import library

MIN_TEST = 15


def term_values(df: pd.DataFrame, term: str) -> np.ndarray:
    cols = sorted(set(term.split("*")))
    return library(df, cols)[term].to_numpy()


def fit(x: np.ndarray, y: np.ndarray) -> LinearRegression:
    return LinearRegression().fit(x.reshape(-1, 1), y)


def l3_check(train: pd.DataFrame, test: pd.DataFrame, target: str, baseline: str, term: str,
             group: str, n_boot: int = 2000, seed: int = 0) -> dict:
    ytr = (train[target] - train[baseline]).to_numpy()
    yte = (test[target] - test[baseline]).to_numpy()
    xtr, xte = term_values(train, term), term_values(test, term)
    m_tr = fit(xtr, ytr)
    rmse = lambda r: float(np.sqrt(np.mean(r**2)))  # noqa: E731
    base = rmse(yte - ytr.mean())  # intercept-only transfer: best a term-free correction can do
    transfer = rmse(yte - m_tr.predict(xte.reshape(-1, 1)))
    rng = np.random.default_rng(seed)
    boot = []
    for _ in range(n_boot):
        i = rng.integers(0, len(yte), len(yte))
        if np.ptp(xte[i]) > 0:
            boot.append(fit(xte[i], yte[i]).coef_[0])
    lo, hi = np.percentile(boot, [2.5, 97.5])
    c_tr, c_te = float(m_tr.coef_[0]), float(fit(xte, yte).coef_[0])
    overlap = sorted(set(train[group]) & set(test[group]))
    out = {"term": term, "target": target, "n_train": len(train), "n_test": len(test),
           "test_rmse_intercept_only": base, "test_rmse_transfer": transfer,
           "gain_transfer": 1 - transfer / base, "coef_train": c_tr, "coef_test": c_te,
           "coef_test_ci95": (float(lo), float(hi)), "family_overlap": overlap}
    out["passes_L3"] = bool(
        not overlap and len(test) >= MIN_TEST and out["gain_transfer"] > 0.1
        and (lo > 0 or hi < 0) and np.sign(c_te) == np.sign(c_tr) and 0.5 <= c_te / c_tr <= 2)
    return out

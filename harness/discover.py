"""Sparse search for a correction term on top of a baseline formula.

Candidates are products of up to two descriptors (and their squares). Each candidate
is scored by grouped cross validation on the residual, against a zero model, and
gets a permutation p value. A term passes L2 only if all three gates hold.
"""

from __future__ import annotations

import itertools

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GroupKFold


def library(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    out = {c: df[c] for c in cols}
    for a, b in itertools.combinations_with_replacement(cols, 2):
        out[f"{a}*{b}"] = df[a] * df[b]
    return pd.DataFrame(out)


def cv_rmse(X: np.ndarray, y: np.ndarray, groups: np.ndarray, k: int) -> float:
    err = []
    for tr, te in GroupKFold(n_splits=k).split(X, y, groups):
        m = LinearRegression().fit(X[tr], y[tr])
        err.append((m.predict(X[te]) - y[te]) ** 2)
    return float(np.sqrt(np.mean(np.concatenate(err))))


def search(df: pd.DataFrame, target: str, baseline: str, cols: list[str], group: str,
           k: int = 5, n_perm: int = 500, seed: int = 0, n_top: int = 5,
           n_tests: int = 1) -> pd.DataFrame:
    """Rank single term corrections for residual = target - baseline.

    group: column used to keep chemically related rows (e.g. same element set) in one fold,
    so a term cannot win by memorising one family.
    """
    y = (df[target] - df[baseline]).to_numpy()
    groups = df[group].to_numpy()
    k = min(k, len(np.unique(groups)))
    null = float(np.sqrt(np.mean((y - y.mean()) ** 2)))
    rng = np.random.default_rng(seed)
    lib = library(df, cols)
    rows = []
    for name in lib:
        X = lib[[name]].to_numpy()
        score = cv_rmse(X, y, groups, k)
        rows.append({"term": name, "cv_rmse": score, "null_rmse": null, "gain": 1 - score / null})
    res = pd.DataFrame(rows).sort_values("cv_rmse").reset_index(drop=True)
    # Permutation test only for the top few; it is the expensive part.
    for i in range(min(n_top, len(res))):
        X = lib[[res.loc[i, "term"]]].to_numpy()
        perm = [cv_rmse(X, rng.permutation(y), groups, k) for _ in range(n_perm)]
        res.loc[i, "p_perm"] = (1 + np.sum(np.array(perm) <= res.loc[i, "cv_rmse"])) / (n_perm + 1)
    # Bonferroni over the whole library and over the n_tests searches run on the same data:
    # the top term was picked out of len(lib) * n_tests tries.
    # The permutation floor 1/(n_perm+1) must sit below that threshold or nothing can pass.
    alpha = 0.01 / (len(lib) * n_tests)
    res["p_bonf_alpha"] = alpha
    res["passes_L2"] = ((res["gain"] > 0.1) & (res.get("p_perm", 1.0) < alpha)
                        & (len(df) >= MIN_ROWS) & (1 / (n_perm + 1) < alpha))
    return res


MIN_ROWS = 40  # below this a single term search over ~20 candidates is not evidence

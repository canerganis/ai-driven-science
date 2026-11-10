"""Where does the champion fail? Residual structure on the training rows, written as a short problem brief.

python -m harness.anomaly emix_random > brief.md
Only training rows are used; the sealed holdout is never read here.
"""

from __future__ import annotations

import sys
from itertools import combinations

import numpy as np
import pandas as pd

from harness import arena
from harness.context import context
from harness.features import descriptors, parse_comp


def brief(ds: str) -> str:
    d = arena.DATASETS[ds]
    meta, pred = arena.load(arena.ROOT / d["champion"])
    tr = arena.train_rows(ds)
    comps = tr.comp.map(parse_comp).tolist()
    y = tr[d["target"]].values
    coef = arena._fit(meta, pred, comps, y)
    r = (y - arena._pred(pred, comps, coef)) * 1000
    ctx = context()
    f = pd.DataFrame([descriptors(c) for c in comps])
    f["vol_spread"] = [sum(xa * xb * abs(np.log(ctx.vegard(c) / ctx.pair[(a, b)]["V"])) for a, b, xa, xb in ctx.pairs(c))
                       for c in comps]
    f["B_mismatch"] = [np.sqrt(sum(x * (ctx.pure[e]["B"] / sum(xx * ctx.pure[ee]["B"] for ee, xx in c.items()) - 1) ** 2
                                   for e, x in c.items())) for c in comps]
    f["pair_E_abs"] = [sum(4 * xa * xb * abs(ctx.pair[(a, b)]["E"]) for a, b, xa, xb in ctx.pairs(c)) for c in comps]
    f["max_x"] = [max(c.values()) for c in comps]
    out = [f"# Problem brief: {ds}", "", d["doc"], "",
           f"Champion: `{d['champion']}`: {meta['statement']}. Fitted {meta['free'][0][0] if meta['free'] else ''} "
           f"= {coef}. Training rows {len(y)} (n_el >= 3). Residual = target - champion, meV/atom.",
           f"RMSE {np.sqrt(np.mean(r**2)):.1f}, mean {r.mean():+.1f}. Target spread (sd) {y.std()*1000:.1f}.", "",
           "## Residual by number of elements", "",
           pd.DataFrame({"n_el": tr.n_el, "r": r}).groupby("n_el").r.agg(["count", "mean", "std"]).round(1).to_markdown(),
           "", "## Residual vs descriptors (Pearson r over all rows)", ""]
    cs = {k: np.corrcoef(f[k], r)[0, 1] for k in f.columns if f[k].std() > 0}
    out.append(" ".join(f"{k} {v:+.2f};" for k, v in sorted(cs.items(), key=lambda kv: -abs(kv[1]))))
    out += ["", "## Elements: mean residual with vs without (t)", ""]
    els = sorted({e for c in comps for e in c})
    rows = []
    for e in els:
        w = np.array([e in c for c in comps])
        if w.sum() >= 8 and (~w).sum() >= 8:
            t = (r[w].mean() - r[~w].mean()) / np.sqrt(r[w].var() / w.sum() + r[~w].var() / (~w).sum())
            rows.append((e, int(w.sum()), r[w].mean(), t))
    out.append(" ".join(f"{e}(n={n}) {m:+.1f} t={t:+.1f};" for e, n, m, t in sorted(rows, key=lambda q: -abs(q[3]))))
    out += ["", "## Element pairs present together, largest |mean residual| (n >= 10)", ""]
    pr = []
    for a, b in combinations(els, 2):
        w = np.array([a in c and b in c for c in comps])
        if w.sum() >= 10:
            pr.append((f"{a}-{b}", int(w.sum()), r[w].mean()))
    out.append(" ".join(f"{p}(n={n}) {m:+.1f};" for p, n, m in sorted(pr, key=lambda q: -abs(q[2]))[:10]))
    worst = np.argsort(-np.abs(r))[:10]
    out += ["", "## Ten worst rows", "", pd.DataFrame({"comp": tr.comp.values[worst], "target_meV": (y[worst] * 1000).round(1),
                                                      "residual_meV": r[worst].round(1)}).to_markdown(index=False)]
    return "\n".join(out)


if __name__ == "__main__":
    print(brief(sys.argv[1] if len(sys.argv) > 1 else "emix_random"))

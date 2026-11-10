"""Round R2, opus. Verbatim from .orchestra/rounds/R2/opus.md"""

import numpy as np
from itertools import combinations

META = {
    "name": "gated_curvature_three_body",
    "author": "opus",
    "dataset": "emix_random",
    "statement": ("E_mix = sum 4 x_i x_j [E_ij + D_ij t + (t > 0) D2_ij t^2/2] + w sum_{i<j<k} x_i x_j x_k, "
                  "t = ln(V0/V_ij)"),
    "mechanism": ("Limit of the series-spring picture where expanded neighbours are infinitely soft: a pair compressed "
                  "by smaller atoms keeps only its linear (pressure) response, an expanded pair keeps its full binary "
                  "curvature. The gate is a fixed-volume many-body term, not a property of E_ij(V): the binaries "
                  "themselves are quadratic on both sides. Its fitted strength is 0.99 on training and about 1.0 on "
                  "the MACE exact-pair decomposition. Plus a universal three-species excess."),
    "free": [("w", -1.0, 1.0)],
}


def predict(comp, ctx, w=0.0):
    v0 = ctx.vegard(comp)
    e = 0.0
    for a, b, xa, xb in ctx.pairs(comp):
        p = ctx.pair[(a, b)]
        t = np.log(v0 / p["V"])
        e += 4 * xa * xb * (p["E"] + p["D"] * t + (0.5 * p["D2"] * t * t if t > 0 else 0.0))
    return e + w * sum(comp[i] * comp[j] * comp[k] for i, j, k in combinations(sorted(comp), 3))

"""Round R2, opus. Verbatim from .orchestra/rounds/R2/opus.md"""

import numpy as np
from itertools import combinations

META = {
    "name": "soft_neighbour_curvature_three_body",
    "author": "opus",
    "dataset": "emix_random",
    "statement": ("E_mix = sum 4 x_i x_j [E_ij + D_ij t + f_ij D2_ij t^2/2] + w sum_{i<j<k} x_i x_j x_k, t = ln(V0/V_ij), "
                  "f_ij = 2 B_env/(B_env + B_ij), stiffnesses at V0 from B(V) = B0 (V_el/V0)^5"),
    "mechanism": ("Each binary's E(V) transfers exactly to second order (MACE binaries at the alloy volume match it to "
                  "1.2 meV rms), so k < 1 is not a transfer effect. D2 is the stiffening energy when the pair's own two "
                  "species are strained together. In the alloy the pair is strained against third-element neighbours, "
                  "a spring in series, so it keeps the harmonic-mean stiffness 2 B_ij B_env/(B_ij + B_env). B rises "
                  "steeply under compression, so a large-atom pair compressed by small (expanded, soft) atoms loses "
                  "curvature energy, and a small-atom pair expanded among compressed, stiff atoms keeps more. f = 1 in "
                  "every 50:50 binary at its own volume. The rest is a positive fixed-volume three-species excess "
                  "(nearest-neighbour triangles with three distinct species, which no binary contains)."),
    "free": [("w", -1.0, 1.0)],
}

BP = 5.0  # pressure derivative of B, typical late transition metal value, set before fitting


def _b(ctx, el, v):
    return ctx.pure[el]["B"] * (ctx.pure[el]["V"] / v) ** BP


def predict(comp, ctx, w=0.0):
    v0 = ctx.vegard(comp)
    b_env = sum(x * _b(ctx, el, v0) for el, x in comp.items())
    e = 0.0
    for a, b, xa, xb in ctx.pairs(comp):
        p = ctx.pair[(a, b)]
        t = np.log(v0 / p["V"])
        f = 2 * b_env / (b_env + 0.5 * (_b(ctx, a, v0) + _b(ctx, b, v0)))
        e += 4 * xa * xb * (p["E"] + p["D"] * t + f * 0.5 * p["D2"] * t * t)
    return e + w * sum(comp[i] * comp[j] * comp[k] for i, j, k in combinations(sorted(comp), 3))

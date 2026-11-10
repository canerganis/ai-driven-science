"""Swarm S1, front k_mechanism, opus. Verbatim from .orchestra/swarm/S1/k_mechanism/opus.md"""

"""Second-order pair transfer at full strength plus a positive three-body mixing term."""

from itertools import combinations

import numpy as np

META = {
    "name": "curved_transfer_triplet",
    "author": "opus",
    "dataset": "emix_random",
    "statement": "E_mix = sum 4 x_i x_j [E + D u + D2 u^2/2] + c sum x_i x_j x_k, u = ln(V0/V_ij)",
    "mechanism": "pairs follow their own curved E(V) (mixing pressure = anharmonic pure-reference pressure, decays on "
                 "expansion); the positive beyond-pair energy at fixed volume that the linear k absorbed is carried by c",
    "free": [("c", 0.0, 0.5)],
}


def predict(comp, ctx, c=0.1):
    v0 = ctx.vegard(comp)
    pair = 0.0
    for a, b, xa, xb in ctx.pairs(comp):
        p = ctx.pair[(a, b)]
        u = np.log(v0 / p["V"])
        pair += 4 * xa * xb * (p["E"] + p["D"] * u + 0.5 * p["D2"] * u * u)
    return pair + c * sum(comp[i] * comp[j] * comp[k] for i, j, k in combinations(sorted(comp), 3))

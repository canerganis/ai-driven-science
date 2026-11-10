"""Swarm S1, front k_mechanism, opus. Verbatim from .orchestra/swarm/S1/k_mechanism/opus.md"""

"""Second-order pair transfer at the slope measured in binaries, plus a positive three-body mixing term."""

from itertools import combinations

import numpy as np

K_BIN = 0.89  # frozen: exact-transfer slope on the 136 off-equiatomic binary rows (n_el = 2), never arena training rows

META = {
    "name": "attenuated_transfer_triplet",
    "author": "opus",
    "dataset": "emix_random",
    "statement": "E_mix = sum 4 x_i x_j [E + 0.89 (D u + D2 u^2/2)] + c sum x_i x_j x_k, u = ln(V0/V_ij)",
    "mechanism": "k ~ 0.8 has three parts, none a reduced volume response (alloy dE/dlnV vs pair sum: slope 0.99). "
                 "(1) Curvature: the pair mixing pressure is the anharmonic pressure of its pure references at a shared "
                 "volume and decays on expansion, D2 ~ -(B'-1) D (r -0.95). (2) A positive beyond-pair energy at fixed "
                 "volume, +3 to +5 meV, which binaries cannot carry: c. (3) A composition-dependent remainder that tracks "
                 "the transfer, slope 0.89, measured where no third element exists.",
    "free": [("c", 0.0, 0.5)],
}


def predict(comp, ctx, c=0.1):
    v0 = ctx.vegard(comp)
    pair = 0.0
    for a, b, xa, xb in ctx.pairs(comp):
        p = ctx.pair[(a, b)]
        u = np.log(v0 / p["V"])
        pair += 4 * xa * xb * (p["E"] + K_BIN * (p["D"] * u + 0.5 * p["D2"] * u * u))
    return pair + c * sum(comp[i] * comp[j] * comp[k] for i, j, k in combinations(sorted(comp), 3))

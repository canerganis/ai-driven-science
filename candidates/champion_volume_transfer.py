"""Current champion for emix_random: pair additivity plus volume transfer of each binary (ledger 05f01df6ec, L2)."""

import numpy as np

META = {
    "name": "volume_transfer",
    "author": "claude+opus subagent",
    "dataset": "emix_random",
    "statement": "E_mix = sum x_i x_j [4 E_ij + k 4 D_ij ln(V0/V_ij)], binary 50:50 inputs at their own Vegard volume",
    "free": [("k", 0.0, 2.0)],
}


def predict(comp, ctx, k=1.0):
    v0 = ctx.vegard(comp)
    return sum(xa * xb * 4 * (ctx.pair[(a, b)]["E"] + k * ctx.pair[(a, b)]["D"] * np.log(v0 / ctx.pair[(a, b)]["V"]))
               for a, b, xa, xb in ctx.pairs(comp))

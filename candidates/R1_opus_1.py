"""Round R1, opus. Verbatim from .orchestra/rounds/R1/opus.md"""

import numpy as np

META = {
    "name": "expansion_only_curvature",
    "author": "opus",
    "dataset": "emix_random",
    "statement": "E_mix = sum 4 x_i x_j [E_ij + D_ij t_ij + D2_ij t_ij^2/2 * (t_ij > 0)], t_ij = ln(V0/V_ij); no attenuation, no fit",
    "mechanism": ("Each binary's volume curvature D2 (mostly < 0, set by the anharmonic stiffening of the strained pure "
                  "references) is realised in the alloy energy only for pairs the alloy expands (V0 > V_ij). For pairs it "
                  "compresses, the alloy keeps the tangent: the curvature energy is cancelled by a fixed-volume many-body "
                  "term (electronic volume relief, see opus_2). The alloy's dE/dlnV still follows the ungated pair sum."),
    "free": [],
}


def predict(comp, ctx):
    v0 = ctx.vegard(comp)
    e = 0.0
    for a, b, xa, xb in ctx.pairs(comp):
        p = ctx.pair[(a, b)]
        t = np.log(v0 / p["V"])
        e += 4 * xa * xb * (p["E"] + p["D"] * t + (0.5 * p["D2"] * t * t if t > 0 else 0.0))
    return e

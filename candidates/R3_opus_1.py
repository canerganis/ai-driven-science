"""Round R3, opus. Verbatim from .orchestra/rounds/R3/opus.md"""

import numpy as np

META = {
    "name": "valence_filling_transfer",
    "author": "opus",
    "dataset": "emix_random",
    "statement": ("E_mix = sum 4 x_i x_j [E_ij + D_ij t + D2_ij t^2/2] + g sum_{i<j: {vec_i, vec_j} = {10, 11}} "
                  "4 x_i x_j (Nbar - (N_i + N_j)/2), t = ln(V0/V_ij), N = vec, Nbar = sum x N"),
    "mechanism": ("Each binary is moved to the alloy volume with its own slope and curvature (no attenuation). The "
                  "interaction between a filled-d atom (Cu, Ag, Au) and a group-10 atom (Ni, Pd, Pt) depends on how "
                  "full the shared d band is: more valence electrons per atom fill the group-10 d holes near the Fermi "
                  "level and strengthen the bond. A 50:50 binary measures the pair at filling (N_i + N_j)/2; in the "
                  "alloy the filling is the alloy average Nbar, set by every component including third elements. "
                  "Linear response in Nbar gives the term, one slope g (eV per electron) for all such pairs. In a binary "
                  "it is exactly a subregular term, L1 = 2 g; unlike the Muggianu extrapolation of binary asymmetry it "
                  "does not vanish in equiatomic ternaries."),
    "free": [("g", -0.2, 0.2)],
}


def predict(comp, ctx, g=0.0):
    v0 = ctx.vegard(comp)
    nbar = sum(x * ctx.pure[el]["vec"] for el, x in comp.items())
    e = 0.0
    for a, b, xa, xb in ctx.pairs(comp):
        p = ctx.pair[(a, b)]
        t = np.log(v0 / p["V"])
        w = 4 * xa * xb
        e += w * (p["E"] + p["D"] * t + 0.5 * p["D2"] * t * t)
        na, nb = ctx.pure[a]["vec"], ctx.pure[b]["vec"]
        if {na, nb} == {10.0, 11.0}:
            e += g * w * (nbar - 0.5 * (na + nb))
    return e

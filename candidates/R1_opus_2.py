"""Round R1, opus. Verbatim from .orchestra/rounds/R1/opus.md"""

import numpy as np

META = {
    "name": "electronic_volume_relief",
    "author": "opus",
    "dataset": "emix_random",
    "statement": ("E_mix = full quadratic pair transfer + R(alloy) - sum 4 x_i x_j R(ij 50:50), R = energy gained when "
                  "each atom's electronic volume relaxes toward its own (Vinet EOS, B'=5) at cost kappa/2 ln^2(v/V0), "
                  "sum x ln v = ln V0"),
    "mechanism": ("On clamped ideal sites the cell volume is fixed but charge can move between Wigner-Seitz cells, so a "
                  "large atom partly expands into its small neighbours. The relief is set by each element's own EOS and "
                  "one shared chemical pressure. Stiffness contrast and EOS anharmonicity make it non pair-additive; the "
                  "50:50 binaries already contain their own relief, so only the remainder is added. One coefficient: the "
                  "electronic rigidity kappa (eV)."),
    "free": [("kappa", 5.0, 500.0)],
}

GPA = 160.21766208
BP = 5.0  # pressure derivative of the bulk modulus, typical late transition metal value, not fitted


def _vinet(v0, b, s):
    eta = 1.5 * (BP - 1)
    x = np.exp((s - np.log(v0)) / 3.0)
    u = eta * (x - 1)
    ex = np.exp(-u)
    a = 4 * b * v0 / (BP - 1) ** 2
    du = eta * x / 3.0
    return a * (1 - (1 + u) * ex), a * u * ex * du, a * (1 - u) * ex * du * du + a * u * ex * du / 3.0


def _relief(v0s, bs, xs, lnv, kappa):
    s = np.full(len(xs), lnv)
    p = 0.0
    for _ in range(100):
        _, e1, e2 = _vinet(v0s, bs, s)
        g = e1 + kappa * (s - lnv) + p
        h = np.maximum(e2 + kappa, 0.05 * kappa)
        dp = np.sum(xs * (s - lnv - g / h)) / np.sum(xs / h)
        ds = np.clip(-(g + dp) / h, -0.05, 0.05)
        s, p = s + ds, p + dp
        if np.max(np.abs(ds)) < 1e-12:
            break
    e, _, _ = _vinet(v0s, bs, s)
    er, _, _ = _vinet(v0s, bs, np.full(len(xs), lnv))
    return float(np.sum(xs * (e + 0.5 * kappa * (s - lnv) ** 2)) - np.sum(xs * er))


def predict(comp, ctx, kappa=40.0):
    v0 = ctx.vegard(comp)
    lnv = np.log(v0)

    def r(els, xs):
        return _relief(np.array([ctx.pure[e]["V"] for e in els]), np.array([ctx.pure[e]["B"] / GPA for e in els]),
                       np.array(xs, float), lnv, kappa)

    e = r(list(comp), [comp[k] for k in comp])
    for a, b, xa, xb in ctx.pairs(comp):
        p = ctx.pair[(a, b)]
        t = np.log(v0 / p["V"])
        e += 4 * xa * xb * (p["E"] + p["D"] * t + 0.5 * p["D2"] * t * t - r([a, b], [0.5, 0.5]))
    return e

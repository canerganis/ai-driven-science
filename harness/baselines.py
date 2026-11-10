"""Known formulas. Discovery only ever fits the residual against one of these."""

from __future__ import annotations

import numpy as np


def rule_of_mixtures(comp: dict[str, float], pure: dict[str, float]) -> float:
    """Linear average of a pure element property computed in the same lattice."""
    return sum(x * pure[el] for el, x in comp.items())


def reuss(comp: dict[str, float], pure: dict[str, float]) -> float:
    """Harmonic average, the lower bound for a mixture of uncorrelated stiffnesses.

    Rule of mixtures (Voigt) is the upper bound; any residual against it that grows with
    modulus mismatch is just the Voigt-Reuss gap, not new physics. Fit residuals against this.
    """
    return 1 / sum(x / pure[el] for el, x in comp.items())


def varvenne_curtin_tau(G: float, nu: float, misfit_sum: float, alpha: float = 0.123) -> float:
    """Zero temperature solid solution strength tau_y0 (GPa), fcc form.

    Varvenne, Luque, Curtin, Acta Mater. 118 (2016) 164.
    tau_y0 = 0.01785 alpha^(-1/3) G ((1+nu)/(1-nu))^(4/3) (sum c_n dV_n^2 / b^6)^(2/3).
    Here misfit_sum = sum c_n dV_n^2 / V^2 and b^3 = V*sqrt(2) for fcc (b^6 = 2 V^2).
    """
    return 0.01785 * alpha ** (-1 / 3) * G * ((1 + nu) / (1 - nu)) ** (4 / 3) * (misfit_sum / 2) ** (2 / 3)


def pugh_ductile(pugh: float) -> bool:
    """Pugh (1954): B/G > 1.75 is read as ductile. A known weak criterion, kept as baseline."""
    return pugh > 1.75


def r2(y: np.ndarray, yhat: np.ndarray) -> float:
    return float(1 - np.sum((y - yhat) ** 2) / np.sum((y - np.mean(y)) ** 2))

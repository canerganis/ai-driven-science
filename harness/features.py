"""Composition descriptors used by baselines and by the discovery search."""

from __future__ import annotations

import numpy as np
from pymatgen.core import Element

R = 8.314462618  # J/(mol K)


def parse_comp(s: str) -> dict[str, float]:
    return {el: float(x) for el, x in (p.split(":") for p in s.split(";"))}


def elem(el: str) -> dict[str, float]:
    e = Element(el)
    vec = e.group if e.group <= 12 else e.group - 10  # valence electron count, transition metal convention
    return {"r": float(e.atomic_radius_calculated or e.atomic_radius),
            "chi": float(e.X), "vec": float(vec), "mass": float(e.atomic_mass),
            "tm": float(e.melting_point)}


def descriptors(comp: dict[str, float]) -> dict[str, float]:
    els = list(comp)
    c = np.array([comp[e] for e in els])
    p = {k: np.array([elem(e)[k] for e in els]) for k in ("r", "chi", "vec", "tm")}
    rbar = c @ p["r"]
    return {"n_el": len(els),
            "S_mix": -R * float(c @ np.log(c)),
            "delta_r": float(np.sqrt(c @ (1 - p["r"] / rbar) ** 2)),
            "d_chi": float(np.sqrt(c @ (p["chi"] - c @ p["chi"]) ** 2)),
            "vec": float(c @ p["vec"]),
            "tm_mix": float(c @ p["tm"])}


def misfit(comp: dict[str, float], vols: dict[str, float], v_alloy: float) -> dict[str, float]:
    """Vegard deviation and the volume misfit sum used by Varvenne-Curtin.

    vols: per-atom volume of each pure element in the alloy's lattice, from the same potential.
    Apparent misfit volume uses the Vegard approximation dV_n = V_n - V_alloy.
    """
    c = np.array([comp[e] for e in comp])
    v = np.array([vols[e] for e in comp])
    dv = v - v_alloy
    return {"vegard_dev": float(v_alloy - c @ v) / v_alloy,
            "misfit_sum": float(c @ dv**2) / v_alloy**2}


def mismatch(comp: dict[str, float], pure: dict[str, float]) -> float:
    """Concentration weighted RMS mismatch of a pure element property, e.g. shear modulus.
    Same form as delta_r; modulus mismatch enters Fleischer and Labusch strengthening."""
    c = np.array([comp[e] for e in comp])
    v = np.array([pure[e] for e in comp])
    return float(np.sqrt(c @ (1 - v / (c @ v)) ** 2))

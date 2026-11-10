"""Correct PBE mixing energies for the cutoff mismatch of runs made before 2026-10-31.

Those runs used, for each pw.x call, the max SSSP cutoff over that call's own elements, so a pure reference ran at a
lower cutoff than the alloy it was subtracted from. shift(el, wfc, rho, v) = E(el, wfc, rho) - E(el, own) per atom,
from 1-atom fcc cells at kspacing 0.15 (the difference is insensitive to k sampling), at three volumes around the
element's MACE volume and interpolated quadratically in ln V. Corrected reference: E_pure(own run) + shift.
"""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd
from ase.build import bulk
from ase.io import read

from harness import dft

ROOT = Path(__file__).resolve().parent.parent
TABLE = ROOT / "data" / "ecut_shift_table.csv"
DLNV = (-0.12, 0.0, 0.12)
pv = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")["vol_per_atom"]


def own(el: str) -> tuple[float, float]:
    return 1.25 * dft.SSSP[el]["cutoff_wfc"], 1.25 * dft.SSSP[el]["cutoff_rho"]


def run_settings(tag: str) -> tuple[float, float]:
    t = (dft.RUNS / tag / "pw.in").read_text()
    return (float(re.search(r"ecutwfc\s*=\s*([\d.]+)", t).group(1)),
            float(re.search(r"ecutrho\s*=\s*([\d.]+)", t).group(1)))


def energy(tag: str) -> float:
    a = read(dft.RUNS / tag / "pw.out", format="espresso-out", index=-1)
    return a.get_potential_energy() / len(a)


def _e1(el: str, wfc: float, rho: float, v: float) -> float:
    a = bulk(el, "fcc", a=4.0)
    a.set_cell(a.cell * (v / a.get_volume()) ** (1 / 3), scale_atoms=True)
    s = dft.Settings(kspacing=0.15, np=4, extra={"system.ecutwfc": wfc, "system.ecutrho": rho})
    return dft.run_pw(a, f"ecut2/{el}_w{wfc:g}_r{rho:g}_v{v:.3f}", s).get_potential_energy()


def build(combos) -> pd.DataFrame:
    rows = []
    for el, wfc, rho in combos:
        for d in DLNV:
            v = pv[el] * np.exp(d)
            rows.append({"el": el, "wfc": wfc, "rho": rho, "dlnV": d,
                         "shift": _e1(el, wfc, rho, v) - _e1(el, *own(el), v)})
    df = pd.DataFrame(rows)
    df.to_csv(TABLE, index=False)
    return df


@lru_cache(maxsize=None)
def _coef(el: str, wfc: float, rho: float):
    t = pd.read_csv(TABLE)
    s = t[(t.el == el) & np.isclose(t.wfc, wfc) & np.isclose(t.rho, rho)].sort_values("dlnV")
    if len(s) != 3:
        raise KeyError(f"no shift table for {el} at {wfc}/{rho}")
    return np.polyfit(s.dlnV, s["shift"], 2)


def shift(el: str, wfc: float, rho: float, v: float) -> float:
    if np.isclose(wfc, own(el)[0]) and np.isclose(rho, own(el)[1]):
        return 0.0
    return float(np.polyval(_coef(el, wfc, rho), np.log(v / pv[el])))


def pure_at(el: str, pure_tag: str, alloy_tag: str, v: float) -> float:
    """Energy per atom of a pure reference, corrected to the alloy run's cutoff."""
    return energy(pure_tag) + shift(el, *run_settings(alloy_tag), v)

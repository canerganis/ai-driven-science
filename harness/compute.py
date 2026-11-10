"""Structure generation, relaxation and elastic constants with a universal ML potential."""

from __future__ import annotations

import datetime as dt
import os
import time
from functools import lru_cache

import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.filters import FrechetCellFilter
from ase.optimize import FIRE

from harness.reference import ELASTIC_EXP

GPA = 160.21766208  # eV/A^3 -> GPa
MODEL = os.environ.get("HARNESS_MODEL", "medium-omat-0")  # mace_mp foundation model name

# Rough lattice parameters (A) for the starting guess only; relaxation sets the real value.
A0 = {"fcc": {"Al": 4.05, "Cu": 3.61, "Ni": 3.52, "Ag": 4.09, "Au": 4.08, "Pd": 3.89,
              "Pt": 3.92, "Co": 3.54, "Fe": 3.59, "Cr": 3.60, "Mn": 3.60},
      "bcc": {"Fe": 2.87, "Cr": 2.88, "Mo": 3.15, "W": 3.16, "V": 3.03, "Nb": 3.30,
              "Ta": 3.30, "Ti": 3.28, "Zr": 3.57, "Hf": 3.50, "Al": 3.24}}


@lru_cache(maxsize=1)
def calculator():
    from mace.calculators import mace_mp
    import torch
    device = "cuda" if torch.cuda.is_available() else "cpu"
    return mace_mp(model=MODEL, device=device, default_dtype="float64")


def site_counts(comp: dict[str, float], n: int) -> dict[str, int]:
    counts = {el: int(round(x * n)) for el, x in comp.items()}
    counts[max(counts, key=counts.get)] += n - sum(counts.values())
    return counts


def actual_fractions(atoms: Atoms) -> dict[str, float]:
    """Composition the cell really has. Subtract pure references with these, not the nominal fractions (the
    rounding to whole atoms shifted E_mix by up to ~57 meV/atom before 2026-10-31)."""
    s = atoms.get_chemical_symbols()
    return {el: s.count(el) / len(s) for el in sorted(set(s))}


def solid_solution(comp: dict[str, float], lattice: str, reps: int, seed: int) -> Atoms:
    """Random solid solution on a cubic conventional supercell (no SQS optimisation). Counts are rounded to whole
    atoms; use actual_fractions() for references."""
    a = sum(x * A0[lattice].get(el, 3.5 if lattice == "fcc" else 3.1) for el, x in comp.items())
    atoms = bulk("X", lattice, a=a, cubic=True).repeat((reps, reps, reps))
    counts = site_counts(comp, len(atoms))
    symbols = [el for el, c in counts.items() for _ in range(c)]
    np.random.default_rng(seed).shuffle(symbols)
    atoms.set_chemical_symbols(symbols)
    return atoms


# GPU duty cycle in (0, 1]: after each relaxation sleep so the GPU is busy only this fraction
# of the time. Keeps a laptop from overheating on long scans; results are unaffected.
DUTY = float(os.environ.get("HARNESS_DUTY", "1.0"))


def relax(atoms: Atoms, cell: bool, fmax: float = 1e-3, steps: int = 400) -> int:
    atoms.calc = calculator()
    target = FrechetCellFilter(atoms) if cell else atoms
    opt = FIRE(target, logfile=None)
    t = time.perf_counter()
    opt.run(fmax=fmax, steps=steps)
    if DUTY < 1:
        time.sleep((time.perf_counter() - t) * (1 / DUTY - 1))
    return opt.nsteps


def elastic_tensor(atoms: Atoms, eps: float = 0.005, relax_ions: bool = True) -> np.ndarray:
    """Full 6x6 Voigt tensor (GPa) from central differences of stress, ions relaxed at each strain."""
    cell0 = atoms.get_cell().array.copy()
    C = np.zeros((6, 6))
    voigt = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]
    for j, (k, l) in enumerate(voigt):
        sig = []
        for s in (+eps, -eps):
            e = np.zeros((3, 3))
            if k == l:
                e[k, k] = s
            else:
                e[k, l] = e[l, k] = s / 2  # engineering shear strain = s
            strained = atoms.copy()
            strained.set_cell(cell0 @ (np.eye(3) + e), scale_atoms=True)
            strained.calc = calculator()
            if relax_ions and len(strained) > 1:
                relax(strained, cell=False, fmax=5e-4)
            sig.append(strained.get_stress(voigt=True) * GPA)  # ASE: tensile stress positive
        C[:, j] = (sig[0] - sig[1]) / (2 * eps)
    return 0.5 * (C + C.T)


def cubic_average(C: np.ndarray) -> tuple[float, float, float]:
    """Project a (noisy, random alloy) 6x6 tensor onto cubic symmetry."""
    c11 = np.mean([C[0, 0], C[1, 1], C[2, 2]])
    c12 = np.mean([C[0, 1], C[0, 2], C[1, 2]])
    c44 = np.mean([C[3, 3], C[4, 4], C[5, 5]])
    return float(c11), float(c12), float(c44)


def voigt_reuss_hill(c11: float, c12: float, c44: float) -> dict[str, float]:
    B = (c11 + 2 * c12) / 3
    Gv = (c11 - c12 + 3 * c44) / 5
    Gr = 5 * (c11 - c12) * c44 / (4 * c44 + 3 * (c11 - c12))
    G = (Gv + Gr) / 2
    E = 9 * B * G / (3 * B + G)
    nu = (3 * B - 2 * G) / (2 * (3 * B + G))
    return {"B": B, "G": G, "E": E, "nu": nu, "pugh": B / G, "cauchy": c12 - c44,
            "zener": 2 * c44 / (c11 - c12)}


def run_alloy(comp: dict[str, float], lattice: str, reps: int = 3, seed: int = 0) -> dict:
    atoms = solid_solution(comp, lattice, reps, seed)
    nsteps = relax(atoms, cell=True)
    C = elastic_tensor(atoms)
    c11, c12, c44 = cubic_average(C)
    # Quality flag: spread of the three cubic-equivalent C11 and C44 entries. Large spread means the
    # random cell is too small for its chemistry or the solid solution broke symmetry on relaxing.
    spread = float(max(np.ptp(np.diag(C)[:3]) / c11, np.ptp(np.diag(C)[3:]) / max(c44, 1.0)))
    vol = atoms.get_volume() / len(atoms)
    row = {"formula": atoms.get_chemical_formula(mode="metal"),
           "comp": ";".join(f"{el}:{x:.4f}" for el, x in sorted(comp.items())),
           "lattice": lattice, "natoms": len(atoms), "seed": seed, "model": MODEL,
           "vol_per_atom": vol, "a_eff": (vol * (4 if lattice == "fcc" else 2)) ** (1 / 3),
           "relax_steps": nsteps, "cubic_spread": spread, "C11": c11, "C12": c12, "C44": c44,
           "time": dt.datetime.now().isoformat(timespec="seconds")}
    row.update(voigt_reuss_hill(c11, c12, c44))
    return row


def calibrate(elements: list[str] | None = None) -> list[dict]:
    rows = []
    for el in elements or list(ELASTIC_EXP):
        lattice, e11, e12, e44 = ELASTIC_EXP[el]
        r = run_alloy({el: 1.0}, lattice, reps=1)
        r["el"] = el
        r.update({"C11_exp": e11, "C12_exp": e12, "C44_exp": e44})
        r.update({f"{k}_exp": v for k, v in voigt_reuss_hill(e11, e12, e44).items()})
        rows.append(r)
    return rows

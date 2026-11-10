"""Quantum ESPRESSO (pw.x in WSL) as the L3 reference for stresses and elastic constants.

QE lives in a conda-forge env inside WSL (micromamba env "qe", no sudo needed).
Pseudopotentials: SSSP 1.3.0 PBE efficiency, md5 a58f1b3373f330179fd0832c48bb9a52,
Materials Cloud Archive 2023.65, doi:10.24435/materialscloud:f3-ym.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
from ase import Atoms
from ase.io import read, write

from harness.compute import GPA, cubic_average, voigt_reuss_hill

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "data" / "dft_runs"
DISTRO = "Ubuntu-22.04"
PSEUDO_DIR = "/home/can02/pseudo/sssp_eff_1.3"
SSSP = json.loads((Path(__file__).parent / "data" / "sssp_1.3.0_pbe_efficiency.json").read_text())

# Collinear starting moments for the magnetic 3d metals. Cr gets an antiferromagnetic
# start on the two bcc sublattices; a commensurate AFM cell is an approximation of its SDW.
MAGNETIC = {"Fe": 0.4, "Co": 0.4, "Ni": 0.3, "Mn": 0.4, "Cr": 0.4}


@dataclass
class Settings:
    kspacing: float = 0.15          # 1/A, Monkhorst-Pack density (2*pi included)
    ecut_scale: float = 1.25        # stresses need a margin above the SSSP energy cutoff
    degauss: float = 0.01           # Ry, Marzari-Vanderbilt
    np: int = 8                     # 8 physical cores
    extra: dict = field(default_factory=dict)
    # Elements whose cutoffs also set this run's cutoff. For mixing energies and curvatures pass the alloy's elements
    # to the pure references too, so all terms share one basis (before 2026-10-31 each run used only its own).
    ecut_elements: tuple = ()
    # Fixed Monkhorst-Pack grid. Finite-strain curvatures must use one grid for every strain; the default picks it from
    # the strained cell, which changes it between strains (18x18x18 vs 17x18x18 for Cu3Ir, found 2026-10-31).
    kpts: tuple | None = None


def wsl_path(p: Path) -> str:
    s = str(p.resolve()).replace("\\", "/")
    return f"/mnt/{s[0].lower()}{s[2:]}"


def kgrid(atoms: Atoms, kspacing: float) -> tuple[int, int, int]:
    rec = np.linalg.norm(atoms.cell.reciprocal(), axis=1) * 2 * np.pi
    return tuple(max(1, int(np.ceil(r / kspacing))) for r in rec)


def magnetize(atoms: Atoms) -> bool:
    """Set initial moments in place; AFM checkerboard for Cr. Returns True if spin polarised."""
    mags = np.array([MAGNETIC.get(s, 0.0) for s in atoms.get_chemical_symbols()])
    if not mags.any():
        return False
    if "Cr" in atoms.get_chemical_symbols():
        a = (2 * atoms.get_volume() / len(atoms)) ** (1 / 3)  # bcc conventional lattice parameter
        parity = np.round(2 * atoms.positions[:, 0] / a).astype(int) % 2  # corner vs body centre
        mags = np.where(np.array(atoms.get_chemical_symbols()) == "Cr", mags * (1 - 2 * parity), mags)
    atoms.set_initial_magnetic_moments(mags * 5)  # ASE maps moments to starting_magnetization
    return True


def run_pw(atoms: Atoms, tag: str, s: Settings, relax_ions: bool = False) -> Atoms:
    """Run one pw.x scf/relax with stress. Cached: an existing finished output is reused."""
    d = RUNS / tag
    d.mkdir(parents=True, exist_ok=True)
    out = d / "pw.out"
    els = sorted(set(atoms.get_chemical_symbols()))
    basis = set(els) | set(s.ecut_elements)
    ecut = float(s.extra.get("system.ecutwfc", s.ecut_scale * max(SSSP[e]["cutoff_wfc"] for e in basis)))
    ecutrho = s.ecut_scale * max(SSSP[e]["cutoff_rho"] for e in basis)
    if out.exists() and "JOB DONE" in out.read_text(errors="ignore"):
        cached = re.search(r"ecutwfc\s*=\s*([\d.]+)", (d / "pw.in").read_text())
        if cached and abs(float(cached.group(1)) - ecut) > 1e-6:  # a cache hit must not silently change the basis
            raise RuntimeError(f"{tag}: cached run used ecutwfc {cached.group(1)}, requested {ecut}; use a new tag")
        return read(out, format="espresso-out", index=-1)
    scratch = tag.replace("/", "__")
    atoms = atoms.copy()
    # extra={'system.nspin': 1} must switch magnetism off: initial moments make ASE write nspin 2 back (S3 audit)
    spin = s.extra.get("system.nspin", 2) != 1 and magnetize(atoms)
    data = {"control": {"calculation": "relax" if relax_ions else "scf", "tstress": True,
                        "tprnfor": True, "pseudo_dir": PSEUDO_DIR, "outdir": f"/tmp/qe/{scratch}",
                        "disk_io": "low", "forc_conv_thr": 1e-4},
            "system": {"ecutwfc": ecut, "ecutrho": ecutrho, "occupations": "smearing",
                       "smearing": "mv", "degauss": s.degauss, "nspin": 2 if spin else 1},
            "electrons": {"conv_thr": 1e-10 * len(atoms), "mixing_beta": 0.3}}
    for k, v in s.extra.items():
        data.setdefault(k.split(".")[0], {})[k.split(".")[1]] = v
    write(d / "pw.in", atoms, format="espresso-in", input_data=data,
          pseudopotentials={e: SSSP[e]["filename"] for e in els}, kpts=s.kpts or kgrid(atoms, s.kspacing))
    cmd = (f"export MAMBA_ROOT_PREFIX=~/mamba OMP_NUM_THREADS=1; mkdir -p /tmp/qe/{scratch}; cd '{wsl_path(d)}' && "
           f"~/bin/micromamba run -n qe mpirun -np {s.np} pw.x -nk {min(s.np, 4)} -in pw.in > pw.out 2> pw.err; "
           f"rm -rf /tmp/qe/{scratch}")
    subprocess.run(["wsl", "-d", DISTRO, "--", "bash", "-lc", cmd], check=True)
    text = out.read_text(errors="ignore")
    if "JOB DONE" not in text or "convergence NOT achieved" in text:
        raise RuntimeError(f"pw.x failed for {tag}, see {out}")
    return read(out, format="espresso-out", index=-1)


def stress(atoms: Atoms, tag: str, s: Settings, relax_ions: bool) -> np.ndarray:
    return read_stress(run_pw(atoms, tag, s, relax_ions))


def read_stress(a: Atoms) -> np.ndarray:
    return a.get_stress(voigt=True) * GPA  # ASE sign: tensile positive


def elastic_cubic(atoms: Atoms, tag: str, s: Settings, eps: float = 0.01, full: bool = False,
                  relax_ions: bool | None = None) -> np.ndarray:
    """6x6 tensor (GPa) by central differences. full=False uses only e_xx and e_yz,
    which is exact for a cubic crystal and enough for pure elements (4 pw.x runs)."""
    if relax_ions is None:
        relax_ions = len(set(atoms.get_chemical_symbols())) > 1
    cell0 = atoms.get_cell().array.copy()
    voigt = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]
    cols = range(6) if full else (0, 3)
    C = np.full((6, 6), np.nan)
    for j in cols:
        k, l = voigt[j]
        sig = []
        for sign in (+1, -1):
            e = np.zeros((3, 3))
            if k == l:
                e[k, k] = sign * eps
            else:
                e[k, l] = e[l, k] = sign * eps / 2
            st = atoms.copy()
            st.set_cell(cell0 @ (np.eye(3) + e), scale_atoms=True)
            sig.append(stress(st, f"{tag}/e{j}{'p' if sign > 0 else 'm'}", s, relax_ions))
        C[:, j] = (sig[0] - sig[1]) / (2 * eps)
    if not full:  # fill the cubic tensor from the two columns
        c11, c12, c44 = C[0, 0], 0.5 * (C[1, 0] + C[2, 0]), C[3, 3]
        C = np.zeros((6, 6))
        C[:3, :3] = c12
        np.fill_diagonal(C[:3, :3], c11)
        C[3:, 3:] = np.eye(3) * c44
    return 0.5 * (C + C.T)


def relax_lattice(atoms: Atoms, tag: str, s: Settings, eps: float = 0.01) -> Atoms:
    """Cubic lattice parameter from a parabola fit of pressure vs volume (3 pw.x runs).
    Avoids vc-relax Pulay stress issues and keeps every run cached and inspectable."""
    cell0 = atoms.get_cell().array.copy()
    scales = np.array([1 - eps, 1.0, 1 + eps])
    P = []
    for sc in scales:
        a = atoms.copy()
        a.set_cell(cell0 * sc, scale_atoms=True)
        sig = stress(a, f"{tag}/lat{sc:.3f}", s, relax_ions=len(set(a.symbols)) > 1)
        P.append(-sig[:3].mean())
    root = np.roots(np.polyfit(scales, P, 2))
    root = root[np.isreal(root)].real
    best = root[np.argmin(abs(root - 1))]
    out = atoms.copy()
    out.set_cell(cell0 * best, scale_atoms=True)
    return out


def run_alloy(comp_atoms: Atoms, label: str, s: Settings, full: bool | None = None) -> dict:
    full = (len(set(comp_atoms.symbols)) > 1) if full is None else full
    tag = f"{label}_k{s.kspacing}_e{s.ecut_scale}"
    a = relax_lattice(comp_atoms, tag, s)
    c11, c12, c44 = cubic_average(elastic_cubic(a, tag, s, full=full))
    row = {"label": label, "formula": a.get_chemical_formula(mode="metal"), "natoms": len(a),
           "vol_per_atom": a.get_volume() / len(a), "C11": c11, "C12": c12, "C44": c44,
           "method": f"QE7.6 PBE SSSP1.3eff k{s.kspacing} ecut x{s.ecut_scale} mv{s.degauss}",
           "time": dt.datetime.now().isoformat(timespec="seconds")}
    row.update(voigt_reuss_hill(c11, c12, c44))
    return row

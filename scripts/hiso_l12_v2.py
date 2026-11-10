"""H-iso check, corrected numerics (v2): clamped mixing shear curvatures K44, Kp of cubic L1_2 cells with PBE.

python scripts/hiso_l12_v2.py [dense | rho]
Fixes found by the swarm S1 audit in scripts/hiso_l12.py: the alloy and both pure references now share one cutoff
(ecut_elements = (A, B)) and one k-grid, taken from the unstrained cell, for every strain. "dense" repeats Cu3Ir and
Ag3Rh at kspacing 0.08 as a convergence check. "rho" repeats Ag3Rh and Pt3Cu with ecutrho x 1.5 (Astra audit b3214734c2:
negative rho persists in 34 of 78 runs). Criteria 6cb3c2a936 are unchanged; the old results are not used.
A3B L1_2 (4-atom cubic cell, B on the corner site), clamped at Vegard volume, pure fcc references at the same volume
and the same deformation. Strains +-0.02 (three-point curvature). PBE uses kspacing 0.10 (shear needs the fine grid).
"""

import datetime as dt
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.environ["HARNESS_MODEL"] = "medium-omat-0"
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from ase.build import bulk  # noqa: E402

from harness.compute import GPA  # noqa: E402

CELLS = [("Cu", "Ir"), ("Cu", "Rh"), ("Pd", "Ir"), ("Au", "Ir"), ("Ag", "Ir"), ("Ag", "Rh"),  # A3B with Ir/Rh
         ("Cu", "Au"), ("Pt", "Cu")]  # controls without Ir/Rh; order = MACE |K| (PBE is slow, strongest first)
S = 0.02
SYM_DONE = {"Cu3Ir": ("g-", "t-")}  # computed both signs here; used as the symmetry check
METHOD = "dft"
DENSE = "dense" in sys.argv
RHO = "rho" in sys.argv
KSP = 0.08 if DENSE else 0.10
if DENSE:
    CELLS = [("Cu", "Ir"), ("Ag", "Rh")]
if RHO:
    CELLS = [("Ag", "Rh"), ("Pt", "Cu")]
TAG = "hiso2" + ("d" if DENSE else "r" if RHO else "")
pv = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")["vol_per_atom"]

from harness import dft  # noqa: E402

NP = int(os.environ.get("HISO_NP", "2"))
ST = {}


def energy(atoms, tag):
    return dft.run_pw(atoms, f"{TAG}/{tag}", ST["s"]).get_potential_energy() / len(atoms)

DEF = {"0": np.eye(3), "g+": np.eye(3) + S * np.outer([1, 0, 0], [0, 1, 0]),
       "g-": np.eye(3) - S * np.outer([1, 0, 0], [0, 1, 0]),
       "t+": np.diag([np.exp(S), np.exp(-S), 1.0]), "t-": np.diag([np.exp(-S), np.exp(S), 1.0])}


def strained(symbols, v, F):
    a = bulk("Cu", "fcc", a=4.0, cubic=True)
    a.symbols = list(symbols)
    a.set_cell(a.cell * (v * 4 / a.get_volume()) ** (1 / 3), scale_atoms=True)
    a.set_cell(a.cell @ F.T, scale_atoms=True)
    return a


OUT = ROOT / "data" / f"hiso_l12_dft_v2{'_dense' if DENSE else '_rho' if RHO else ''}.csv"
done = set(pd.read_csv(OUT)["cell"]) if OUT.exists() else set()
for A, B in CELLS:
    name = f"{A}3{B}"
    if name in done:
        continue
    v = 0.75 * pv[A] + 0.25 * pv[B]
    vt = f"{v:.3f}"
    rho = {"system.ecutrho": 1.5 * 1.25 * max(dft.SSSP[e]["cutoff_rho"] for e in (A, B))} if RHO else {}
    ST["s"] = dft.Settings(kspacing=KSP, np=NP, ecut_elements=(A, B), extra=rho,
                           kpts=dft.kgrid(strained([B, A, A, A], v, np.eye(3)), KSP))
    em = {}
    for k, F in DEF.items():
        if k in ("g-", "t-") and k not in SYM_DONE.get(name, ()):  # cubic L1_2: y -> -y and x <-> y are symmetries
            continue
        e_ab = energy(strained([B, A, A, A], v, F), f"{name}_{k}_v{vt}")
        e_a = energy(strained([A] * 4, v, F), f"{A}_{name}_{k}_v{vt}")
        e_b = energy(strained([B] * 4, v, F), f"{B}_{name}_{k}_v{vt}")
        em[k] = e_ab - 0.75 * e_a - 0.25 * e_b
    em.setdefault("g-", em["g+"])
    em.setdefault("t-", em["t+"])
    c44 = (em["g+"] + em["g-"] - 2 * em["0"]) / (2 * S**2)   # E = c s^2
    cp = (em["t+"] + em["t-"] - 2 * em["0"]) / (2 * S**2)
    r = {"cell": name, "method": "dft_v2", "kpts": "x".join(map(str, ST["s"].kpts)), "V": v, "E_mix": em["0"], "K44": 2 * c44 / v * GPA, "Kp": cp / (2 * v) * GPA,
         "time": dt.datetime.now().isoformat(timespec="seconds")}
    pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
    print(name, f"E_mix {em['0']*1000:+7.1f} meV  K44 {r['K44']:+7.2f}  Kp {r['Kp']:+7.2f} GPa", flush=True)

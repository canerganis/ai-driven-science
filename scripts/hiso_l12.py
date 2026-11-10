"""H-iso check in cubic L1_2 cells: clamped mixing shear curvatures K44, Kp with MACE or PBE.

python scripts/hiso_l12.py mace | dft
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
METHOD = sys.argv[1]
pv = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")["vol_per_atom"]

if METHOD == "mace":
    from harness import compute
    calc = compute.calculator()

    def energy(atoms, tag):
        atoms.calc = calc
        return atoms.get_potential_energy() / len(atoms)
else:
    from harness import dft
    st = dft.Settings(kspacing=0.10, np=int(os.environ.get("HISO_NP", "4")))

    def energy(atoms, tag):
        return dft.run_pw(atoms, f"hiso/{tag}", st).get_potential_energy() / len(atoms)

DEF = {"0": np.eye(3), "g+": np.eye(3) + S * np.outer([1, 0, 0], [0, 1, 0]),
       "g-": np.eye(3) - S * np.outer([1, 0, 0], [0, 1, 0]),
       "t+": np.diag([np.exp(S), np.exp(-S), 1.0]), "t-": np.diag([np.exp(-S), np.exp(S), 1.0])}


def strained(symbols, v, F):
    a = bulk("Cu", "fcc", a=4.0, cubic=True)
    a.symbols = list(symbols)
    a.set_cell(a.cell * (v * 4 / a.get_volume()) ** (1 / 3), scale_atoms=True)
    a.set_cell(a.cell @ F.T, scale_atoms=True)
    return a


OUT = ROOT / "data" / f"hiso_l12_{METHOD}.csv"
done = set(pd.read_csv(OUT)["cell"]) if OUT.exists() else set()
for A, B in CELLS:
    name = f"{A}3{B}"
    if name in done:
        continue
    v = 0.75 * pv[A] + 0.25 * pv[B]
    vt = f"{v:.3f}"
    em = {}
    for k, F in DEF.items():
        if k in ("g-", "t-") and k not in SYM_DONE.get(name, ()):  # cubic L1_2: y -> -y and x <-> y are symmetries
            continue
        e_ab = energy(strained([B, A, A, A], v, F), f"{name}_{k}_v{vt}")
        e_a = energy(strained([A] * 4, v, F), f"{A}_{k}_v{vt}")
        e_b = energy(strained([B] * 4, v, F), f"{B}_{k}_v{vt}")
        em[k] = e_ab - 0.75 * e_a - 0.25 * e_b
    em.setdefault("g-", em["g+"])
    em.setdefault("t-", em["t+"])
    c44 = (em["g+"] + em["g-"] - 2 * em["0"]) / (2 * S**2)   # E = c s^2
    cp = (em["t+"] + em["t-"] - 2 * em["0"]) / (2 * S**2)
    r = {"cell": name, "method": METHOD, "V": v, "E_mix": em["0"], "K44": 2 * c44 / v * GPA, "Kp": cp / (2 * v) * GPA,
         "time": dt.datetime.now().isoformat(timespec="seconds")}
    pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
    print(name, f"E_mix {em['0']*1000:+7.1f} meV  K44 {r['K44']:+7.2f}  Kp {r['Kp']:+7.2f} GPa", flush=True)

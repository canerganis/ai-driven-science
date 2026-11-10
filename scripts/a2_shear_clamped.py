"""Clamped mixing shear curvatures K44, Kp for the h1 compositions (test of ledger 5ac00dd12d).

python scripts/a2_shear_clamped.py
Ideal sites, affine strain only. E_mix subtracts pure fcc at the same volume and the same deformation.
K44 = (1/V) d2E_mix/dg2 under F = I + g ex ey; Kp from E_mix = 2 V Kp t^2 under F = diag(e^t, e^-t, 1).
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

from harness import compute  # noqa: E402
from harness.compute import GPA  # noqa: E402
from harness.fcc_set import compositions, key  # noqa: E402

AMPS = np.array([-0.01, -0.005, 0.0, 0.005, 0.01])
pure_v = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")["vol_per_atom"]
calc = compute.calculator()


def e_strained(atoms, v_atom, F):
    a = atoms.copy()
    a.set_cell(a.cell * (v_atom * len(a) / a.get_volume()) ** (1 / 3), scale_atoms=True)
    a.set_cell(a.cell @ F.T, scale_atoms=True)
    a.calc = calc
    return a.get_potential_energy() / len(a)


def shear(g):
    F = np.eye(3)
    F[0, 1] = g
    return F


def tetra(t):
    return np.diag([np.exp(t), np.exp(-t), 1.0])


OUT = ROOT / "data" / "a2_shear_clamped.csv"
done = set(pd.read_csv(OUT)["comp"]) if OUT.exists() else set()
for comp in compositions():
    if key(comp) in done:
        continue
    v0 = sum(x * pure_v[el] for el, x in comp.items())
    alloy = compute.solid_solution(comp, "fcc", reps=3, seed=0)
    pures = {el: bulk(el, "fcc", a=4.0, cubic=True) for el in comp}
    r = {"comp": key(comp), "family": "-".join(sorted(comp)), "V0": v0}
    for name, Fn in (("K44", shear), ("Kp", tetra)):
        em = [e_strained(alloy, v0, Fn(s)) - sum(x * e_strained(pures[el], v0, Fn(s)) for el, x in comp.items())
              for s in AMPS]
        c2 = np.polyfit(AMPS, em, 2)[0]  # E = c2 s^2: K44 = 2 c2 / V, Kp = c2 / (2 V)
        r[name] = (2 * c2 if name == "K44" else c2 / 2) / v0 * GPA
    r["time"] = dt.datetime.now().isoformat(timespec="seconds")
    pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
    print(r["family"], f"K44 {r['K44']:+7.2f}  Kp {r['Kp']:+7.2f} GPa", flush=True)

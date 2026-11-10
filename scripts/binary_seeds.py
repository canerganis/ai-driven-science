"""Configurational noise in the binary inputs of the volume-transfer rule (W_ij, dE_mix/dlnV).

python scripts/binary_seeds.py
Recomputes the h1 equiatomic binaries with SQS seeds 1 and 2 (seed 0 is h1), same protocol as scripts/h1_ev.py.
Used to test whether the refit k ~ 0.8 of the rule on both holdouts is regression dilution from noisy binary inputs.
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
from harness.features import parse_comp  # noqa: E402

SCALES = np.linspace(0.97, 1.03, 7)
pure_v = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")["vol_per_atom"]
h1 = pd.read_csv(ROOT / "data" / "h1_ev_rows.csv")
h1["c"] = h1.comp.map(parse_comp)
eq = h1[(h1.n_el == 2) & h1.c.map(lambda c: all(abs(v - 0.5) < 1e-3 for v in c.values()))]
calc = compute.calculator()


def e_at(atoms, v_atom):
    a = atoms.copy()
    a.set_cell(a.cell * (v_atom * len(a) / a.get_volume()) ** (1 / 3), scale_atoms=True)
    a.calc = calc
    return a.get_potential_energy() / len(a)


OUT = ROOT / "data" / "binary_seeds.csv"
done = set(zip(*pd.read_csv(OUT)[["comp", "seed"]].values.T)) if OUT.exists() else set()
pe = {}
for seed in (1, 2):
    for comp_key, comp in zip(eq.comp, eq.c):
        if (comp_key, seed) in done:
            continue
        v0 = sum(x * pure_v[el] for el, x in comp.items())
        vols = v0 * SCALES**3
        for el in comp:
            for v in vols:
                pe.setdefault((el, round(v, 6)), e_at(bulk(el, "fcc", a=4.0, cubic=True), v))
        alloy = compute.solid_solution(comp, "fcc", reps=3, seed=seed)
        emix = np.array([e_at(alloy, v) - sum(x * pe[(el, round(v, 6))] for el, x in comp.items()) for v in vols])
        c, b, a = np.polyfit(np.log(vols / v0), emix, 2)
        r = {"comp": comp_key, "family": "-".join(sorted(comp)), "seed": seed, "E_mix": a, "dE_dlnV": b,
             "d2E_dlnV2": 2 * c, "time": dt.datetime.now().isoformat(timespec="seconds")}
        pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
        print(r["family"], seed, f"E_mix {a*1000:+7.1f}  dE/dlnV {b*1000:+7.1f} meV", flush=True)

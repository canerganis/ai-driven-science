"""Clamped E_mix(V) of ordered L1_0 cells (4 atoms, c/a = 1) with MACE or DFT.

python scripts/l10_ev.py mace | dft
L1 check for the H2/H3 quantity: small enough for DFT, so MACE can be compared one to one.
Pure elements use the same per-atom volume as the alloy (constant-volume chemical term).
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

PAIRS = [("Cu", "Pt"), ("Cu", "Pd"), ("Au", "Cu"), ("Pd", "Pt"),   # attractive in the random scan
         ("Ag", "Ir"), ("Ir", "Pd"), ("Au", "Ir")]                  # repulsive in the random scan
SCALES = np.linspace(0.97, 1.03, 5)
METHOD = sys.argv[1]
pure_v = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")["vol_per_atom"]

if METHOD == "mace":
    from harness import compute
    calc = compute.calculator()

    def energy(atoms, tag):
        atoms.calc = calc
        return atoms.get_potential_energy() / len(atoms)
else:
    from harness import dft
    s = dft.Settings(kspacing=0.15, np=4)  # 4 ranks: keeps the laptop cool

    def energy(atoms, tag):
        return dft.run_pw(atoms, f"l10/{tag}", s).get_potential_energy() / len(atoms)


def at_volume(atoms, v_atom):
    a = atoms.copy()
    a.set_cell(a.cell * (v_atom * len(a) / a.get_volume()) ** (1 / 3), scale_atoms=True)
    return a


OUT = ROOT / "data" / f"l10_ev_{METHOD}.csv"
done = set(pd.read_csv(OUT)["pair"]) if OUT.exists() else set()
for A, B in PAIRS:
    if f"{A}-{B}" in done:
        continue
    l10 = bulk(A, "fcc", a=4.0, cubic=True)
    l10.symbols[[2, 3]] = B  # ASE cubic fcc: atoms 0,1 at z=0 and 2,3 at z=1/2, layered along z
    v0 = 0.5 * (pure_v[A] + pure_v[B])
    emix = []
    for i, v in enumerate(v0 * SCALES**3):
        e_ab = energy(at_volume(l10, v), f"{A}{B}_v{i}")
        e_a = energy(at_volume(bulk(A, "fcc", a=4.0), v), f"{A}_{A}{B}_v{i}")
        e_b = energy(at_volume(bulk(B, "fcc", a=4.0), v), f"{B}_{A}{B}_v{i}")
        emix.append(e_ab - 0.5 * (e_a + e_b))
    x = np.log(SCALES**3)
    c, b, a = np.polyfit(x, emix, 2)
    r = {"pair": f"{A}-{B}", "method": METHOD, "E_mix": a, "n_eff": -3 * b / a, "R": 2 * c * a / b**2,
         "time": dt.datetime.now().isoformat(timespec="seconds"),
         **{f"emix_{i}": e for i, e in enumerate(emix)}}
    pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
    print(r["pair"], f"E_mix {a * 1000:+7.1f} meV  n_eff {r['n_eff']:+6.2f}  R {r['R']:+6.2f}", flush=True)

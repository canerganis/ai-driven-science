"""Beyond-pair mixing energy in 4-atom ordered fcc cells, MACE or DFT (L1 check for HM, ledger c542fcd2d5).

python scripts/hm_ordered.py mace | dft
Conventional fcc cell, 4 sublattices; every site has 4 neighbours on each other sublattice.
Nearest-neighbour pair model: E_mix(L1_0 ij) = 4 V_ij, E_mix(ABCD) = sum V_ij, E_mix(ABCC) = V_AB + 2 V_AC + 2 V_BC.
Delta = E_mix(cell) - pair prediction, everything clamped at the cell's Vegard volume (same V for all references).
"""

import datetime as dt
import itertools
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.environ["HARNESS_MODEL"] = "medium-omat-0"
sys.path.insert(0, str(ROOT))

import pandas as pd  # noqa: E402
from ase.build import bulk  # noqa: E402

# non-magnetic elements only, so PBE needs no spin
QUATS = [("Cu", "Pd", "Pt", "Au"), ("Ag", "Au", "Pd", "Pt"), ("Cu", "Ir", "Pd", "Rh"),
         ("Ag", "Cu", "Pt", "Rh"), ("Au", "Ir", "Pt", "Rh"), ("Ag", "Cu", "Ir", "Pd")]
TERNS = [("Cu", "Pt", "Pd"), ("Au", "Cu", "Pt"), ("Ag", "Pd", "Rh"), ("Ir", "Pt", "Au")]  # last element doubled
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
    s = dft.Settings(kspacing=0.15, np=4)

    def energy(atoms, tag):
        return dft.run_pw(atoms, f"hm/{tag}", s).get_potential_energy() / len(atoms)


def cell(symbols, v):
    a = bulk("Cu", "fcc", a=4.0, cubic=True)
    a.symbols = list(symbols)
    a.set_cell(a.cell * (v * 4 / a.get_volume()) ** (1 / 3), scale_atoms=True)
    return a


OUT = ROOT / "data" / f"hm_ordered_{METHOD}.csv"
done = set(pd.read_csv(OUT)["cell"]) if OUT.exists() else set()
for sites in [q for q in QUATS] + [t + (t[2],) for t in TERNS]:
    name = "".join(sites)
    if name in done:
        continue
    els = sorted(set(sites))
    v = sum(pure_v[e] for e in sites) / 4
    vt = f"{v:.3f}"
    pe = {e: energy(cell([e] * 4, v), f"{e}_v{vt}") for e in els}
    e_cell = energy(cell(sites, v), f"{name}_v{vt}") - sum(pe[e] for e in sites) / 4
    vij = {}
    for a, b in itertools.combinations(els, 2):
        e_l10 = energy(cell([a, a, b, b], v), f"{a}{b}_v{vt}") - 0.5 * (pe[a] + pe[b])
        vij[(a, b)] = e_l10 / 4
    # bonds: one per atom per sublattice pair, 6 sublattice pairs
    pred = sum(vij[tuple(sorted((sites[i], sites[j])))] for i, j in itertools.combinations(range(4), 2)
               if sites[i] != sites[j])
    r = {"cell": name, "n_el": len(els), "method": METHOD, "V": v, "E_mix": e_cell, "E_pair": pred,
         "Delta": e_cell - pred, "time": dt.datetime.now().isoformat(timespec="seconds")}
    pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
    print(name, f"E_mix {e_cell*1000:+7.1f}  pair {pred*1000:+7.1f}  Delta {r['Delta']*1000:+6.1f} meV", flush=True)

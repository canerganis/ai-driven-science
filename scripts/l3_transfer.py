"""L3 test of the volume-transfer rule (L2 entry from scripts/hm_l2.py) in 4-atom ordered fcc cells.

python scripts/l3_transfer.py mace | dft
Cells: 12 quaternaries ABCD + 4 ternaries ABCC from families absent from h1, h3 and hm_fresh, quaternaries ranked by
the volume spread sum |ln(V0/V_ij)| (an input, never an outcome). Every bond in these cells is a NN pair, one bond per
atom per sublattice pair.
  naive: each bond uses V_ij(own) = E_mix(L1_0 ij at its Vegard V_ij)/4
  rule : V_ij(own) + (dV_ij/dlnV) ln(V0/V_ij), slope by central difference at V_ij exp(+-0.02)
target: E_mix(cell at V0), pure references at V0.
"""

import datetime as dt
import itertools
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.environ["HARNESS_MODEL"] = "medium-omat-0"
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from ase.build import bulk  # noqa: E402

METHOD = sys.argv[1]
E7 = ["Ag", "Au", "Cu", "Ir", "Pd", "Pt", "Rh"]
pv = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")["vol_per_atom"]
fams = set()
for f in ("h1_ev_rows.csv", "h3_fresh_rows.csv", "hm_fresh_rows.csv"):
    fams |= set(pd.read_csv(ROOT / "data" / f).family)


def spread(els):
    v0 = np.mean([pv[e] for e in els])
    return sum(abs(np.log(v0 / (0.5 * (pv[a] + pv[b])))) for a, b in itertools.combinations(els, 2))


quats = sorted((c for c in itertools.combinations(E7, 4) if "-".join(c) not in fams), key=spread, reverse=True)[:12]
terns = [c for c in itertools.combinations(E7, 3) if "-".join(c) not in fams][:4]
CELLS = [q for q in quats] + [t + (t[0],) for t in terns]

if METHOD == "mace":
    from harness import compute
    calc = compute.calculator()

    def energy(atoms, tag):
        atoms.calc = calc
        return atoms.get_potential_energy() / len(atoms)
else:
    from harness import dft
    s = dft.Settings(kspacing=0.15, np=4)

    def energy(atoms, tag):  # same tag scheme as hm_ordered, so its finished runs are reused
        return dft.run_pw(atoms, f"hm/{tag}", s).get_potential_energy() / len(atoms)


def cell(symbols, v):
    a = bulk("Cu", "fcc", a=4.0, cubic=True)
    a.symbols = list(symbols)
    a.set_cell(a.cell * (v * 4 / a.get_volume()) ** (1 / 3), scale_atoms=True)
    return a


def emix_l10(a, b, v):
    vt = f"{v:.3f}"
    return (energy(cell([a, a, b, b], v), f"{a}{b}_v{vt}")
            - 0.5 * (energy(cell([a] * 4, v), f"{a}_v{vt}") + energy(cell([b] * 4, v), f"{b}_v{vt}")))


pair_cache = {}


def pair_terms(a, b):
    if (a, b) not in pair_cache:
        vij = 0.5 * (pv[a] + pv[b])
        e0, ep, em = (emix_l10(a, b, vij * np.exp(d)) / 4 for d in (0.0, 0.02, -0.02))
        pair_cache[(a, b)] = (vij, e0, (ep - em) / 0.04)
    return pair_cache[(a, b)]


OUT = ROOT / "data" / f"l3_transfer_{METHOD}.csv"
done = set(pd.read_csv(OUT)["cell"]) if OUT.exists() else set()
for sites in CELLS:
    name = "".join(sites)
    if name in done:
        continue
    v0 = np.mean([pv[e] for e in sites])
    vt = f"{v0:.3f}"
    pe = {e: energy(cell([e] * 4, v0), f"{e}_v{vt}") for e in set(sites)}
    target = energy(cell(sites, v0), f"{name}_v{vt}") - sum(pe[e] for e in sites) / 4
    naive = rule = 0.0
    for i, j in itertools.combinations(range(4), 2):
        if sites[i] == sites[j]:
            continue
        a, b = sorted((sites[i], sites[j]))
        vij, e0, slope = pair_terms(a, b)
        naive += e0
        rule += e0 + slope * np.log(v0 / vij)
    r = {"cell": name, "family": "-".join(sorted(set(sites))), "method": METHOD, "V0": v0, "E_mix": target,
         "naive": naive, "rule": rule, "time": dt.datetime.now().isoformat(timespec="seconds")}
    pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
    print(name, f"E {target*1000:+7.1f}  naive {naive*1000:+7.1f}  rule {rule*1000:+7.1f} meV", flush=True)

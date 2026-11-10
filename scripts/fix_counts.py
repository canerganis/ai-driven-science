"""Correct the reference error found by Astra in round R1: compute.solid_solution rounds atom counts to the 108-site
cell, but E_mix subtracted pure energies with the nominal fractions x. The logged value is
    E_logged(V) = E_mix(x~, V) + sum_i (x~_i - x_i) e_i(V),   x~_i = N_i / 108.
We remove the second term (MACE pure fcc energies at the same V) and keep the actual composition x~ in comp_actual.

python scripts/fix_counts.py
Writes *_fixed.csv next to each input; sealed hm3 is corrected in place of its sealed copy (hm3fix), unread.
"""

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.environ["HARNESS_MODEL"] = "medium-omat-0"
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from ase.build import bulk  # noqa: E402

from harness import arena, compute  # noqa: E402
from harness.fcc_set import key  # noqa: E402
from harness.features import parse_comp  # noqa: E402

N = 108
SCALES = np.linspace(0.97, 1.03, 7)
pv = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")["vol_per_atom"]
calc = compute.calculator()
_pe = {}


from harness.fcc_set import compositions, fresh_compositions  # noqa: E402

# tie-break in compute.solid_solution follows the generator's dict order (equiatomic rows), so recover that order
ORDER = {key(c): list(c) for c in list(compositions()) + list(fresh_compositions())}


def actual(comp):
    comp = {e: comp[e] for e in ORDER.get(key(comp), list(comp))}
    counts = {el: int(round(x * N)) for el, x in comp.items()}  # same rule as compute.solid_solution
    counts[max(counts, key=counts.get)] += N - sum(counts.values())
    return {el: c / N for el, c in counts.items()}


def e_pure(el, v):
    k = (el, round(v, 8))
    if k not in _pe:
        a = bulk(el, "fcc", a=4.0, cubic=True)
        a.set_cell(a.cell * (v * 4 / a.get_volume()) ** (1 / 3), scale_atoms=True)
        a.calc = calc
        _pe[k] = a.get_potential_energy() / 4
    return _pe[k]


def ref_err(comp, xa, v):
    return sum((xa[e] - comp[e]) * e_pure(e, v) for e in comp)


def fix_ev(path):
    df = pd.read_csv(path)
    out = []
    for _, r in df.iterrows():
        c = parse_comp(r.comp)
        xa = actual(c)
        v0 = r.V0
        em = np.array([r[f"emix_{i}"] - ref_err(c, xa, v) for i, v in enumerate(v0 * SCALES**3)])
        cc, b, a = np.polyfit(np.log(SCALES**3), em, 2)
        out.append({**r.to_dict(), "comp_actual": key(xa), "E_mix_logged": r.E_mix, "E_mix": a, "dE_dlnV": b,
                    "d2E_dlnV2": 2 * cc, "n_eff": -3 * b / a, **{f"emix_{i}": e for i, e in enumerate(em)}})
    o = pd.DataFrame(out)
    o.to_csv(path.with_name(path.stem + "_fixed.csv"), index=False)
    return o


def fix_v0(df):
    rows = []
    for _, r in df.iterrows():
        c = parse_comp(r.comp)
        xa = actual(c)
        rows.append({**r.to_dict(), "comp_actual": key(xa), "E_mix_logged": r.E_mix,
                     "E_mix": r.E_mix - ref_err(c, xa, r.V0)})
    return pd.DataFrame(rows)


for f in ("h1_ev_rows.csv", "h3_fresh_rows.csv"):
    o = fix_ev(ROOT / "data" / f)
    d = (o.E_mix - o.E_mix_logged) * 1000
    print(f, f"rows {len(o)}, correction meV: median |.| {d.abs().median():.1f}, max |.| {d.abs().max():.1f}, "
             f"exact rows {(d.abs() < 1e-6).sum()}", flush=True)
hf = fix_v0(pd.read_csv(ROOT / "data" / "hm_fresh_rows.csv"))
hf.to_csv(ROOT / "data" / "hm_fresh_rows_fixed.csv", index=False)
d = (hf.E_mix - hf.E_mix_logged) * 1000
print("hm_fresh_rows.csv", f"rows {len(hf)}, correction median |.| {d.abs().median():.1f}, max {d.abs().max():.1f}")

# sealed holdout: corrected without being looked at; compositions and V0 are recomputed from the plain comps file
sc = pd.read_csv(ROOT / "data" / "sealed" / "hm3_comps.csv")
sealed = arena._unseal("hm3").set_index("comp").loc[sc.comp]
sc["E_mix"] = sealed.E_mix.values
sc["V0"] = sc.comp.map(lambda s: sum(x * pv[e] for e, x in parse_comp(s).items()))
fx = fix_v0(sc)
tmp = ROOT / "data" / "hm3fix_tmp.csv"
fx[["comp", "comp_actual", "n_el", "E_mix"]].to_csv(tmp, index=False)
arena.seal(tmp, "hm3fix", "E_mix")
pd.read_csv(ROOT / "data" / "sealed" / "hm3_comps.csv").merge(fx[["comp", "comp_actual"]]).to_csv(
    ROOT / "data" / "sealed" / "hm3fix_comps.csv", index=False)
print("hm3 sealed copy corrected (values not printed)")

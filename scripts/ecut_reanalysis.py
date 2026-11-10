"""Re-apply three pre-registered PBE checks after correcting pure references to the alloy run's cutoff (harness/ecutfix).

python scripts/ecut_reanalysis.py
  (1) L1 for clamped E_mix(V), criteria e5425db058 (was 4c5076a083 pass)
  (2) L1 for the ordered-cell beyond-pair Delta, criteria 7e0022b375 (was d440b9eb7b fail)
  (3) L3 ordered-cell transfer test, criteria 6192ffda51 (was 0e4de24475 fail)
Energies are rebuilt from pw.out; the original CSVs are left as they are, corrected ones get an _ecutfix suffix.
"""

import itertools
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from harness import ledger  # noqa: E402
from harness.ecutfix import energy, pure_at  # noqa: E402

pv = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")["vol_per_atom"]
rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731


def emix(alloy_tag, sites, v, pure_tags):
    """sites: element per atom of the 4-atom cell; pure_tags: element -> tag of its pure run at the same v."""
    return energy(alloy_tag) - sum(pure_at(e, pure_tags[e], alloy_tag, v) for e in sites) / len(sites)


# (1) L1_0 E_mix(V), as scripts/l10_ev.py
SCALES = np.linspace(0.97, 1.03, 5)
rows = []
for A, B in [("Cu", "Pt"), ("Cu", "Pd"), ("Au", "Cu"), ("Pd", "Pt"), ("Ag", "Ir"), ("Ir", "Pd"), ("Au", "Ir")]:
    v0 = 0.5 * (pv[A] + pv[B])
    em = [emix(f"l10/{A}{B}_v{i}", [A, A, B, B], v, {A: f"l10/{A}_{A}{B}_v{i}", B: f"l10/{B}_{A}{B}_v{i}"})
          for i, v in enumerate(v0 * SCALES**3)]
    c, b, a = np.polyfit(np.log(SCALES**3), em, 2)
    rows.append({"pair": f"{A}-{B}", "E_mix": a, "n_eff": -3 * b / a, "R": 2 * c * a / b**2})
d1 = pd.DataFrame(rows).set_index("pair")
d1.to_csv(ROOT / "data" / "l10_ev_dft_ecutfix.csv")
old = pd.read_csv(ROOT / "data" / "l10_ev_dft.csv").set_index("pair")
m = pd.read_csv(ROOT / "data" / "l10_ev_mace.csv").set_index("pair")
j = m[["E_mix", "n_eff"]].join(d1[["E_mix", "n_eff"]], lsuffix="_mace", rsuffix="_dft")
j["E_mix_dft_old"] = old.E_mix
print((j * [1000, 1, 1000, 1, 1000]).round(2).to_string())
sign = bool((np.sign(j.E_mix_mace) == np.sign(j.E_mix_dft)).all())
att = j[j.E_mix_dft < 0]
nratio = bool(((att.n_eff_mace / att.n_eff_dft - 1).abs() <= 0.3).all())
split = int(((j.n_eff_mace > 6) == (j.n_eff_dft > 6)).sum())
p1 = sign and nratio and split >= 6
print(f"(1) L1 E_mix(V): signs {sign}, n_eff within 30% {nratio}, split {split}/7 ->", "PASS" if p1 else "FAIL")

# (2) ordered-cell Delta, as scripts/hm_ordered.py
QUATS = [("Cu", "Pd", "Pt", "Au"), ("Ag", "Au", "Pd", "Pt"), ("Cu", "Ir", "Pd", "Rh"),
         ("Ag", "Cu", "Pt", "Rh"), ("Au", "Ir", "Pt", "Rh"), ("Ag", "Cu", "Ir", "Pd")]
TERNS = [("Cu", "Pt", "Pd"), ("Au", "Cu", "Pt"), ("Ag", "Pd", "Rh"), ("Ir", "Pt", "Au")]
rows = []
for sites in QUATS + [t + (t[2],) for t in TERNS]:
    name, els = "".join(sites), sorted(set(sites))
    v = sum(pv[e] for e in sites) / 4
    vt = f"{v:.3f}"
    pt = {e: f"hm/{e}_v{vt}" for e in els}
    e_cell = emix(f"hm/{name}_v{vt}", sites, v, pt)
    vij = {(a, b): emix(f"hm/{a}{b}_v{vt}", [a, a, b, b], v, pt) / 4 for a, b in itertools.combinations(els, 2)}
    pred = sum(vij[tuple(sorted((sites[i], sites[k])))] for i, k in itertools.combinations(range(4), 2)
               if sites[i] != sites[k])
    rows.append({"cell": name, "n_el": len(els), "E_mix": e_cell, "E_pair": pred, "Delta": e_cell - pred})
d2 = pd.DataFrame(rows).set_index("cell")
d2.to_csv(ROOT / "data" / "hm_ordered_dft_ecutfix.csv")
mc = pd.read_csv(ROOT / "data" / "hm_ordered_mace.csv").set_index("cell").Delta
od = pd.read_csv(ROOT / "data" / "hm_ordered_dft.csv").set_index("cell").Delta
t2 = pd.DataFrame({"mace": mc, "dft": d2.Delta, "dft_old": od}) * 1000
print(t2.round(1).to_string())
s2 = int((np.sign(t2.mace) == np.sign(t2.dft)).sum())
mae, r2 = float((t2.mace - t2.dft).abs().mean()), float(np.corrcoef(t2.mace, t2.dft)[0, 1])
p2 = s2 >= 8 and mae <= 15 and r2 >= 0.7
q = d2[d2.n_el == 4].Delta.mean() * 1000
print(f"(2) L1 Delta: sign {s2}/10, MAE {mae:.1f} meV, r {r2:.2f} ->", "PASS" if p2 else "FAIL",
      f"| PBE quaternary mean Delta {q:+.1f} meV (was {od[[c for c in d2.index if d2.n_el[c] == 4]].mean():+.1f})")

# (3) L3 ordered-cell transfer, as scripts/l3_transfer.py + l3_test.py
l3 = pd.read_csv(ROOT / "data" / "l3_transfer_dft.csv")
rows = []
pair_cache = {}
for name in l3.cell:
    sites = [name[i:i + 2] for i in range(0, 8, 2)]
    v0 = np.mean([pv[e] for e in sites])
    vt = f"{v0:.3f}"
    target = emix(f"hm/{name}_v{vt}", sites, v0, {e: f"hm/{e}_v{vt}" for e in set(sites)})
    naive = rule = 0.0
    for i, k in itertools.combinations(range(4), 2):
        if sites[i] == sites[k]:
            continue
        a, b = sorted((sites[i], sites[k]))
        if (a, b) not in pair_cache:
            vij = 0.5 * (pv[a] + pv[b])
            es = []
            for dd in (0.0, 0.02, -0.02):
                vv = vij * np.exp(dd)
                t = f"{vv:.3f}"
                es.append(emix(f"hm/{a}{b}_v{t}", [a, a, b, b], vv, {a: f"hm/{a}_v{t}", b: f"hm/{b}_v{t}"}) / 4)
            pair_cache[(a, b)] = (vij, es[0], (es[1] - es[2]) / 0.04)
        vij, e0, sl = pair_cache[(a, b)]
        naive += e0
        rule += e0 + sl * np.log(v0 / vij)
    rows.append({"cell": name, "E_mix": target, "naive": naive, "rule": rule})
d3 = pd.DataFrame(rows)
d3.to_csv(ROOT / "data" / "l3_transfer_dft_ecutfix.csv", index=False)
y, T = (d3.E_mix - d3.naive).values, (d3.rule - d3.naive).values
r_rule, r_int = rm(y - T - np.mean(y - T)), rm(y - y.mean())
X = np.column_stack([np.ones_like(T), T])
k = np.linalg.lstsq(X, y, rcond=None)[0][1]
rng = np.random.default_rng(0)
ks = [np.linalg.lstsq(X[i], y[i], rcond=None)[0][1] for i in (rng.integers(0, len(y), len(y)) for _ in range(2000))]
lo, hi = np.percentile(ks, [2.5, 97.5])
p3 = len(y) >= 15 and r_rule <= 0.9 * r_int and lo > 0 and lo >= 0.5 and hi <= 2
print(f"(3) L3: raw RMSE naive {rm(y)*1000:.1f} -> rule {rm(y - T)*1000:.1f}; intercept-only {r_int*1000:.1f} vs rule "
      f"{r_rule*1000:.1f} meV; k {k:.2f} [{lo:.2f}, {hi:.2f}] ->", "PASS" if p3 else "FAIL")

ev = [str(ROOT / "data" / f) for f in ("l10_ev_dft_ecutfix.csv", "hm_ordered_dft_ecutfix.csv",
                                       "l3_transfer_dft_ecutfix.csv", "ecut_shift_table.csv")]
ledger.record(f"Cutoff-corrected PBE re-analysis (pure references at the alloy's cutoff): (1) L1 E_mix(V) "
              f"{'pass' if p1 else 'fail'} (signs {sign}, n_eff {nratio}, split {split}/7); (2) L1 ordered Delta "
              f"{'pass' if p2 else 'fail'} (sign {s2}/10, MAE {mae:.1f}, r {r2:.2f}; PBE quaternary mean {q:+.1f} meV); "
              f"(3) L3 ordered transfer {'pass' if p3 else 'fail'} (k {k:.2f} [{lo:.2f}, {hi:.2f}])", "L0", ev,
              notes="criteria e5425db058, 7e0022b375, 6192ffda51 unchanged; numerics correction found by blind audit")

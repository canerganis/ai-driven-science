# Binary shear curvatures transfer to multicomponent fcc alloys at the alloy's volume: a blind, preregistered test with machine-learned potentials

Muhammet Can Erganiş
Independent researcher, METU graduate, Ankara, Türkiye. ORCID 0009-0001-1397-6366

Draft v2, 2026-11-01. Every number cites a ledger id in `claims/claims.jsonl`. Items marked TODO block submission.

## Abstract

Pair-additive extrapolation from binaries (regular solution, Muggianu, Redlich-Kister) is the default way to estimate
properties of high-entropy alloys, and it works poorly for shear elastic constants. We show that for the clamped
mixing part of the tetragonal shear curvature K' of random fcc alloys most of the failure is a volume mismatch: each
50:50 binary curvature has to be read at the multicomponent alloy's Vegard volume, not at the binary's own. With no
fitted parameter, the pair sum then predicts K'_mix of 3 to 5 component alloys of Ag, Au, Co, Cu, Ir, Ni, Pd, Pt, Rh
with half the error of the same sum at the binaries' own volumes (4.2 to 1.9 GPa on 94 blind alloys; 4.8 to 2.2 GPa
on 1200 more under a second model) and a third of the error of standard own-volume Muggianu extrapolation (5.7 to
1.9 GPa). The transfer is not exact: the refit slope is 1.08 under one model and 1.14 [1.10, 1.18] under another, and
it grows with size mismatch, so the rule under-predicts alloys with large volume differences between components. For
the C44-type shear K44 the same rule is weak, and we show that the reason is a composition-level residual shared by
both shears that survives separate cells, separate seeds and removal of the clamped pre-stress. All tests were
registered with measured power in an append-only ledger before their data existed, and every pass was audited by an
agent that did not propose it. All targets come from universal machine-learned potentials (MACE); first-principles
validation is pending and is the main limit of this work.

## 1. Introduction

1. HEA screening uses binary data. CALPHAD elastic databases fit Redlich-Kister parameters to the c_ij of relaxed
   SQS, each at its own equilibrium volume (Liu et al. 2010; Marker et al. 2017, bcc Ti-Mo-Nb-Sn-Ta-Zr, Young's
   modulus of 13 alloys within 5 to 7 GPa of experiment). Others average binary moduli (Huhn et al. 2014) or train ML
   models on binaries for Ni-Cu-Au-Pd-Pt (Linton and Aidhy 2023; Mirzaee et al. 2024). Shear transfers worse than
   bulk in all of them and C44 worst; none explains why.
2. Volume-dependent interactions are old: volume-dependent ECIs (Asta et al. 1992; Geng et al. 2005), the alloy-volume
   formalism for binaries (Ferreira, Mbaye, Zunger 1987-89), strain-dependent cluster expansion (Behara et al. 2023).
   They are used for energies and bulk moduli, not for shear, and not as a binary-to-multicomponent transfer rule.
3. Formally the rule is a pair-truncated tensorial cluster expansion (van de Walle 2008) or a zeroth-order
   Redlich-Kister sum. The contribution is not the algebra. It is (i) where the binary terms must be evaluated, (ii) a
   blind preregistered test of that choice, (iii) where it stops working, and (iv) why the C44-type shear behaves
   differently. A similar lesson holds in ML for diffraction, where changing the prediction target, not the model,
   cut errors several fold (Hofgard et al., Acta Cryst. A, 2026, TODO exact reference): here the binary data are
   unchanged and only the volume at which they are read changes.

## 2. Methods

**Cells.** Random fcc solid solutions, 108-atom cubic supercells (3x3x3), atoms on ideal sites (no ionic or cell
relaxation), volume fixed at the composition's Vegard volume V0 from the model's pure-element volumes.

**Observable.** E_mix(V, F) = E_alloy - sum x_i E_i, every pure reference at the same volume and the same deformation
F. K' from F = diag(e^t, e^-t, 1), K44 from F = I + g e_x e_y, five amplitudes in [-0.01, 0.01], quadratic fit,
K' = c2/(2V), K44 = 2 c2/V. References use the cell's actual (integer-count) fractions. At V0 a clamped cell is not
stress free, so K44 = C44 + s_yy and K' = C' + (s_xx + s_yy)/2; Section 3.6 removes this term explicitly.

**Binary inputs.** All 36 pairs at 50:50, three SQS seeds per panel, 13 log-volume points ln(V/V_ij) in [-0.4, 0.4],
cubic spline per pair.

**Rule.** K'_mix(alloy) = sum_{i<j} 4 x_i x_j K'_ij(ln V0/V_ij). Baselines: the same sum at ln V0/V_ij = 0, and
own-volume Muggianu (pure-element K'(V) at their own volumes, converted to the clamped reference).

**Seeds.** The site permutation of a cell depends only on (seed, n). Target cells and input cells (binaries,
references) therefore never share a seed: targets use seeds of 100 and above, binaries 0 to 25. An earlier test that
broke this rule was withdrawn before its targets were read (Section 4).

**Models.** MACE medium-omat-0, calibrated on 14 cubic metals (fcc B, G MAE about 12%, e5ef5a57a3). Second model:
medium-mpa-0, with omat geometry (V_ij, V0) so that only the energies change.

**Protocol.** Hypotheses come from two LLM agents (GPT-6-Astra via Codex, Claude Opus) who see the problem, the
limits and the data, never sealed holdouts. Before any test datum exists the harness owner writes the claim, the
pass criterion and a simulated power (>= 0.8) and false-pass rate (<= 0.05) to the ledger. A failed test is closed
with a cause (hypothesis, design, numerics) after an independent audit; only "hypothesis" retires a candidate. Every
pass is audited by the model that did not propose it, which recomputes the key numbers from the raw files.

**Statistics.** Gain = 1 - RMSE(rule)/RMSE(baseline); paired sign-flip test on squared-error differences; refit slope
k from (y - base) = k (rule - base). With two independent binary panels A and B the slope is estimated cross-panel,
k = sum[T_A (y - p_B) + T_B (y - p_A)] / (2 sum T_A T_B), so binary noise does not bias it; CIs bootstrap over
compositions and over seeds within each panel.

## 3. Results

**3.1 Exploration.** On 62 ternary to quinary alloys used for exploration (a2): K' pair sum 5.67 to rule 1.80 GPa,
k 1.05.

**3.2 Blind test 1 (h3, 113 alloys, prereg 4c29d9754c).** K': 4.77 to 2.03 GPa, gain 0.57, p 2.5e-4, k 1.08. The
registered claim was joint (K44 and K'); it failed on K44 (p 0.023, 6e0923b413), so K' got a fresh test rather than a
post-hoc split.

**3.3 Blind test 2 (hm_fresh, 94 alloys never computed, prereg 67a358fc59).** K': 4.22 to 1.89 GPa, gain 0.55,
p 2.5e-4, k 1.08, rule better in 75 of 94 alloys (d92844787f, L2 697c2d6d75).

**3.4 Against the standard method.** Own-volume Muggianu, the clamped analogue of the CALPHAD c_ij practice (Marker
et al. 2017: every input at its own volume, no volume dependence in the interaction parameters): 5.45 / 5.71 / 5.41
GPa on h3 / hm_fresh / a2; rule 2.03 / 1.89 / 1.94 (p 5e-5). For the mixing energy the same comparison shows no gain
(13.3 vs 11.5 meV): there the volume term is mostly the reference strain energy, which the standard reference already
removes. K' is different because the binary curvatures themselves change steeply with volume (median dlnK'/dlnV =
-3.2 for pairs with |K'| > 10 GPa).

**3.5 Second model, and the size of k (prereg 88b9465108, result 43370bbb27, verdict 736bcac471).** Under
medium-mpa-0, on 1200 new compositions (Co yes/no x 3/4/5 elements, 200 each, two cells each) with two independent
binary panels, the rule cuts the RMSE from 4.81 to 2.21 GPa (gain 0.54) and wins in 934 of 1200 alloys. The
preregistered equivalence claim k in [0.90, 1.10] failed: k = 1.138, 90% CI [1.098, 1.182]. The audit found no coding
error; all 3+3 panel splits give 1.138 to 1.139. The slope is not a constant. Exploratory splits (not preregistered):
3-component 1.00 [0.91, 1.09], 4-component 1.25, 5-component 1.17; Cu-free 1.00 [0.94, 1.07], Cu-containing 1.24;
alloys whose largest pair |ln V0/V_ij| is at most 0.15 give 1.07, above 0.25 give 1.41. Co content does not matter
(1.137 vs 1.139). Under omat, cells of Section 3.6 give k 1.11 [1.02, 1.20] with the same stratification. We read
this as an under-prediction at large size mismatch: the pair transfer captures most of the volume effect but not all
of it. A refit k adds only 3% over k = 1, so the parameter-free rule remains the practical form.

**3.6 The C44-type shear.** The same rule is weak for K44 (leak-free gain 0.06 to 0.14). Three preregistered tests
show why: K44 and K' share a residual that belongs to the composition, not to the cell or the noise.
- Shared floor, disjoint seeds (150 new alloys, half with Co >= 15%; prereg c2eff007ad, result b86e0d8a40): the
  difference A = K44 - K' follows the rule (gain 0.49), the residuals of the two shears correlate (r 0.77), and a joint
  fit gives k 0.91 and floor slope b 0.94. Plain K44 gains 0.47 in Co-free alloys and 0.09 in Co alloys.
- Two cells per composition with seeds unique to each cell (prereg fd786169e3): the K44 residual of one cell
  correlates with the K' residual of the other (r 0.75; same cell 0.79), k 0.92, b 0.95.
- After subtracting the clamped mixing pre-stress from targets and binaries alike (prereg ede47f1d65): cross-cell
  r 0.67, k 0.99, b 0.79. The pre-stress is large (7 GPa rms) but pair-additive (the rule leaves 0.7 GPa of it), so
  it was never the floor.
So K44 = rule44 + b (K' - rule') with b near 1: the C44-type shear fails because it carries a composition floor that
K' also carries, while its own volume signal is about half as large. Open doubt (audit of ede47f1d65): b drops to 0.4
to 0.5 when single disjoint binary seeds are used, so part of the floor may be error shared through the binary
references. TODO: two independent binary panels for K44, K' and stress.

## 4. What the audits caught

The loop's most useful outputs were errors, each found by the agent that did not write the code and confirmed by the
other.

| Error | Found by | Size | What it changed |
|---|---|---|---|
| Integer-count reference mismatch | audit | up to 57 meV/atom | all mixing quantities recomputed |
| PBE cutoff mismatch between alloy and pure references | audit | (TODO size) | rule added: references use the alloy cutoff |
| Holdout used for model selection | audit, d26bd71285 | (TODO) | holdout sealed, targets shuffled |
| Shared SQS permutation between targets and binaries (seed 0) | S2 audit, Opus, confirmed by Astra | K44 Co-free gain inflated | test withdrawn (42c0fd3ee0) before reading, seeds separated |
| Weak baseline made a known energy rule look new | audit | 13.3 vs 11.5 meV | energy rule demoted |
| Power simulation treated a compositional residual as cell noise | audit of 88b9465108 | power 1.0 reported | lesson: simulate residuals at composition level |
| PBE runs with nspin 1 still magnetize Co and Ni | Astra, S3 | not used in any result | Co/Ni PBE blocked until fixed |

## 5. Discussion and limits

1. Model only. Every target is a MACE energy. The slope already differs between two MACE models (1.08, 1.14), and in
   a small set of ordered L1_2 A3B cells (preliminary, unaudited) MACE gets the sign of K44 wrong where PBE gives
   -32 GPa (Au3Ir). K' agreed better. Only PBE on random alloys decides how much of the rule is physical. TODO: PBE
   SQS check on 10 to 15 alloys.
2. Clamped, unrelaxed cells: K'_mix is not the measured C'. On 43 seen equiatomic ternaries with fully relaxed MACE
   constants, own-volume Muggianu of relaxed binaries already reaches 3.1 GPa for C' and a chain built on the volume
   rule 2.5 GPa (gain 0.18, p 0.08, exploratory). At zero pressure the advantage is small and not yet significant.
3. The rule under-predicts at large size mismatch (Section 3.5). A correction for this has not been tested.
4. fcc late transition and noble metals only; bcc shear fails calibration for every model available.
5. The rule is a regular-solution / tensorial-CE truncation with a specified volume; we do not claim a new law.

## Data and code

Ledger, scripts, data and audits: TODO repository link (user decision).

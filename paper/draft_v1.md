# Binary shear curvatures transfer to multicomponent fcc alloys at the alloy's volume

Draft v1, 2026-11-01. Every number cites a ledger id in `claims/claims.jsonl`. Items marked TODO block submission.

## Abstract

Pair-additive extrapolation from binaries (regular solution, Muggianu, Redlich-Kister) is the default way to estimate
properties of high-entropy alloys, and it works poorly for shear elastic constants. We show that, for the clamped
mixing part of the tetragonal shear curvature K' of random fcc alloys, the failure is almost entirely a volume
mismatch. Each 50:50 binary curvature must be taken at the multicomponent alloy's Vegard volume, not the binary's own.
With no fitted parameter, the pair sum then predicts K'_mix of 3 to 5 component alloys from Ag, Au, Co, Cu, Ir, Ni,
Pd, Pt, Rh with half the error of the same sum at the binaries' own volumes (4.2 to 1.9 GPa, 94 alloys) and a third of
the error of standard own-volume Muggianu extrapolation (5.7 to 1.9 GPa). The rule was found and tested by an
LLM-agent loop under pre-registration: every test was written to an append-only ledger, with measured power, before
its data existed. The two blind tests pass with refit slope 1.08. A second interatomic model keeps the transfer but
gives slope 1.33, so the coefficient, not the transfer, is model dependent. All targets come from a universal
machine-learned potential (MACE); first-principles validation is pending.

TODO: PBE SQS validation (L3) before submission; K44 result c2eff007ad. Marker 2017 read in full (literature.jsonl).

## 1. Introduction

1. HEA screening uses binary data: CALPHAD elastic databases fit Redlich-Kister parameters L0, L1 (binary) and L2
   (ternary) to the c_ij of relaxed SQS, each at its own equilibrium volume (Liu et al. 2010; Marker et al. 2017, bcc
   Ti-Mo-Nb-Sn-Ta-Zr, Young's modulus of 13 alloys within 5 to 7 GPa of experiment); averaging binary moduli (Huhn et al. 2014); ML trained on binaries for
   Ni-Cu-Au-Pd-Pt (Linton and Aidhy 2023; Mirzaee et al. 2024). Shear transfers worse than bulk in all of them, and
   C44 worst; none explains why.
2. Volume-dependent interactions are old: volume-dependent ECIs (Asta et al. 1992; Geng et al. 2005), the alloy-volume
   formalism for binaries (Ferreira, Mbaye, Zunger 1987-89), strain-dependent cluster expansion (Behara et al. 2023).
   They are used for energies and bulk moduli, not for shear, and not as a binary-to-multicomponent transfer rule.
3. Formally our rule is a pair-truncated tensorial cluster expansion (van de Walle 2008) or a zeroth-order
   Redlich-Kister sum. The contribution is not the algebra but (i) where the binary terms must be evaluated, (ii) a
   blind pre-registered test, (iii) the contrast between strain types.

## 2. Methods

**Cells.** Random fcc solid solutions, 108-atom cubic supercells (3x3x3), atoms on ideal sites (no ionic or cell
relaxation), volume fixed at the composition's Vegard volume V0 from the MACE pure-element volumes.

**Observable.** E_mix(V, F) = E_alloy - sum x_i E_i, every pure reference at the same volume and the same deformation
F. K' from F = diag(e^t, e^-t, 1), K44 from F = I + g e_x e_y, five amplitudes in [-0.01, 0.01], quadratic fit,
K' = c2/(2V), K44 = 2 c2/V. References use the cell's actual (integer-count) fractions.

**Binary inputs.** All 36 pairs at 50:50, three SQS seeds, 13 log-volume points ln(V/V_ij) in [-0.4, 0.4], cubic
spline per pair.

**Rule.** K'_mix(alloy) = sum_{i<j} 4 x_i x_j K'_ij(ln V0/V_ij). Baselines: the same sum at ln V0/V_ij = 0, and
own-volume Muggianu (pure-element K'(V) at their own volumes, converted to the clamped reference).

**Model.** MACE medium-omat-0, L1-calibrated on 14 cubic metals (fcc B, G MAE about 12%, e5ef5a57a3). Robustness:
medium-mpa-0.

**Protocol.** Hypotheses come from two LLM agents (GPT-6-Astra via Codex, Claude Opus) who see the problem, the
limits and the data, never sealed holdouts. Before any test datum exists the harness owner writes the claim, the
pass criterion and a simulated power (>= 0.8) and false-pass rate (<= 0.05) to the ledger (`ledger.register`). A
failed test is closed with a cause (hypothesis, design, numerics) after an independent audit; only "hypothesis"
retires a candidate. Every pass is audited by the model that did not propose it.

**Statistics.** Gain = 1 - RMSE(rule)/RMSE(baseline); paired sign-flip test on squared-error differences (4000
flips); refit slope k from (y - base) = k (rule - base).

## 3. Results

**3.1 Exploration.** On 62 ternary-to-quinary alloys used for exploration (a2): K' pair sum 5.67 to rule 1.80 GPa,
k 1.05 (design note in ledger).

**3.2 Blind test 1 (h3, 113 alloys, prereg 4c29d9754c).** K': 4.77 to 2.03 GPa, gain 0.57, p 2.5e-4, k 1.08. The
registered claim was joint (K44 and K'); it failed on K44 (p 0.023, 6e0923b413), so K' got a fresh test rather than a
post-hoc split.

**3.3 Blind test 2 (hm_fresh, 94 alloys never computed, prereg 67a358fc59, power 1.0).** K': 4.22 to 1.89 GPa, gain
0.55, p 2.5e-4, k 1.08, rule better in 75 of 94 alloys (d92844787f, L2 697c2d6d75).

**3.4 Against the standard method.** Own-volume Muggianu, the clamped analogue of the CALPHAD c_ij practice (Marker
et al. 2017: every binary and pure input at its own volume, no volume dependence in L): 5.45 / 5.71 / 5.41 GPa on h3 / hm_fresh / a2; rule
2.03 / 1.89 / 1.94 (p 5e-5). For the mixing energy the same audit shows no gain over standard Muggianu (13.3 vs
11.5 meV): there the volume term is mostly the reference strain energy, which the standard reference removes. K' is
different because the binary curvatures themselves change steeply with volume (median dlnK'/dlnV = -3.2 for pairs
with |K'| > 10 GPa).

**3.5 Robustness.** (a) Seeds: binaries from seeds 0, 1-2 or all give the same K' result (gain 0.55 to 0.58, k 1.07
to 1.10). (b) Model: medium-mpa-0 on the same 94 alloys: 4.73 to 2.28 GPa, gain 0.52, p 2.5e-4, but k 1.33 [1.11,
1.51], so the pre-registered "k = 1" criterion failed (86767e478d). The two models disagree most at |dlnV| > 0.2.

**3.6 The C44-type shear.** The same rule is weak for K44: leak-free gain 0.06 to 0.14, k 0.60 to 0.77. Exploratory
evidence (seen data) points to a residual shared by both shears (corr 0.71, slope about 1) on top of a volume signal
that is half as large for K44, and to a Co effect. TODO: result of the disjoint-seed pre-registered test c2eff007ad.

## 4. What the audits caught

The loop's most useful outputs were errors, each found by the agent that did not write the code and confirmed by the
other: integer-count reference mismatch (up to 57 meV/atom), PBE cutoff mismatch between alloy and references, a
holdout used for model selection (d26bd71285), a shared SQS permutation between targets and inputs that inflated the
K44 result (LESSONS 19), and a weak baseline that made a known energy rule look new. Table: TODO, one row per error
with size and the verdict it changed.

## 5. Discussion and limits

1. Clamped, unrelaxed cells: K'_mix is not the measured C'. On 43 seen equiatomic ternaries with fully relaxed
   (zero-pressure, relaxed-ion) MACE constants, own-volume Muggianu of relaxed binaries already reaches 3.1 GPa for C'
   and a chain built on the volume rule 2.5 GPa (gain 0.18, p 0.08, exploratory, S2 open front). At zero pressure the
   advantage is therefore small and not yet significant. TODO: pre-registered relaxed test on fresh alloys.
2. One model family; k differs between two MACE models. Only PBE decides which is physical (TODO L3).
3. fcc late transition and noble metals only; bcc shear fails L1 for every model available.
4. The rule is a regular-solution / tensorial-CE truncation with a specified volume; we do not claim a new law.

## Data and code

Ledger, scripts and data: TODO repository link (user decision).

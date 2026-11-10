# Binary shear curvatures read at the alloy's volume: a preregistered test of a transfer rule for fcc solid solutions with machine-learned potentials

Muhammet Can Erganiş
Independent researcher, METU graduate, Ankara, Türkiye. ORCID 0009-0001-1397-6366

Draft v4, 2026-11-02, after the Astra re-review of v3 (`.orchestra/audits/draft_v3_astra.md`) and the completed
ordered-cell PBE check. Numerical provenance is given through ledger entries in `claims/claims.jsonl` and named
analysis files. Exploratory calculations are marked as such and kept apart from preregistered tests. Remaining
submission tasks: archive deposition (DOI) and the author's final reading.

## Abstract

Building on established binary extrapolation, volume-dependent interactions and tensorial cluster expansions, we test
one specific, fixed-coefficient prescription for the clamped mixing part of the tetragonal shear curvature K' of
random fcc solid solutions: each equiatomic binary curvature is evaluated at the multicomponent alloy's Vegard volume
rather than at the binary's own. For 3 to 5 component alloys of Ag, Au, Co, Cu, Ir, Ni, Pd, Pt and Rh evaluated with
the MACE machine-learned potential, this halves the error of the same pair sum taken at the binary volumes (4.2 to
1.9 GPa on 94 compositions; 4.8 to 2.2 GPa on 1200 further compositions under a second MACE model). The transfer is
not exact. The through-origin refit slope is 1.08 under medium-omat-0; the cross-panel estimate under medium-mpa-0
is 1.14 (90% CI 1.10 to 1.18), and in
exploratory splits it rises with the size mismatch between components, so the rule under-predicts alloys with large
volume differences. For the C44-type shear K44 the rule is weak. Correlated residuals of the two shears persist
across independent target cells and after removal of the clamped pre-stress, which supports a composition-dependent
shared residual, but error shared through the binary references remains an unresolved alternative. Primary tests
were entered in an append-only ledger, with simulated power, before their new target calculations, and passing
results received separate code-and-data audits by a second language model. All transfer-test targets are derived
from MACE energies. In a separate eight-cell ordered PBE comparison, medium-omat-0 reproduces all K' signs, but its
median absolute error is 47% of the median absolute PBE curvature and it fails the preregistered mixing-shear
calibration criterion. First-principles validation of the random-alloy transfer rule remains pending.

## 1. Introduction

1. Liu et al. (2010) developed CALPHAD-style models for elastic coefficients, and Marker et al. (2017) applied this
   approach to bcc Ti alloys using relaxed first-principles inputs, each at its own equilibrium volume. Marker
   reported average Young's modulus deviations of about 7 GPa with binary parameters and 5 GPa with ternary terms for
   13 multicomponent alloys. Huhn et al. (2014) compared alloy moduli with effective-medium estimates based on pure
   elements. Linton and Aidhy (2023) trained ML models on binaries, and Mirzaee et al. (2024) a CNN on charge densities
   including binary and ternary data. These studies motivate testing how shear transfers from simpler systems.
2. Volume-dependent effective cluster interactions (Asta et al. 1992; Geng et al. 2005), the alloy-volume formalism
   for binaries (Ferreira et al. 1987, 1989) and tensorial or strain-dependent cluster expansions (van de
   Walle 2008; Behara et al. 2023, which includes shear strain variables) are established. Our search did not
   identify the specific fixed-coefficient transfer tested here: clamped multicomponent mixing K' estimated from
   equiatomic binary curvatures at the alloy Vegard volume. This is a search-bounded statement, not proof that no
   prior work exists.
3. Formally the rule is a pair-truncated tensorial cluster expansion or a zeroth-order Redlich-Kister sum with a
   specified evaluation volume. The contribution is this prescription and its tested performance: (i) where the
   binary terms are evaluated, (ii) a preregistered test of that choice, (iii) where it stops working, and (iv) how
   the C44-type shear differs. In a different field, Hofgard et al. (2026) obtained large gains by changing the
   target representation of an ML model while keeping the model. Here the target stays K'_mix; what changes is the
   volume at which unchanged binary inputs are read.

## 2. Methods

**Cells.** Random fcc solid solutions in 108-atom cubic supercells (3x3x3), built by randomly shuffling species over
the sites without SQS optimisation. Atoms stay on ideal sites (no ionic or cell relaxation). The volume is fixed at
the composition's Vegard volume V0 from the model's pure-element volumes.

**Observable.** E_mix(V, F) = E_alloy - sum x_i E_i per atom, every pure reference at the same volume and the same
deformation F. K' from F = diag(e^t, e^-t, 1), K44 from F = I + g e_x e_y, five amplitudes in [-0.01, 0.01],
quadratic fit, K' = c2/(2V), K44 = 2 c2/V. The target generators use the cell's actual integer-count fractions for
the pure references; the historical exploratory a2 dataset is an exception (Section 3.1). With tensile-positive
mixing stress and Green-Lagrange energy coefficients, K44 = C^L_xyxy + s_yy and K' = (C^L_xxxx + C^L_yyyy -
2 C^L_xxyy)/4 + (s_xx + s_yy)/2. The elastic part reduces to (C11 - C12)/2 only in the cubic limit, and subtracting
the stress terms does not give relaxed, zero-pressure elastic constants.

**Binary inputs.** All 36 equiatomic pairs, 13 log-volume points ln(V/V_ij) in [-0.4, 0.4], cubic spline per pair.
The omat grid uses seeds 0 to 2; the first mpa grid seed 0; the 1200-composition test two three-seed panels (20 to 22,
23 to 25).

**Rule.** K'_mix(alloy) = sum_{i<j} 4 x_i x_j K'_ij(ln V0/V_ij). Baselines: the same sum at ln V0/V_ij = 0 ("pair at
V_ij"), and two own-volume Muggianu analogues built from pure-element curvatures (Section 3.4).

**Seeds.** The site permutation of a cell depends only on (seed, n), so cells with equal seed and size share a
permutation field. The original h3 and hm_fresh shear tests used target seed 0 and binary seeds 0 to 2, and the first
mpa model swap used seed 0 for both; these historical tests shared a permutation field between targets and inputs.
After this was found (Section 4) target and binary seeds were separated: the floor tests use target seeds of 100 and
above, and the 1200-composition test uses unique target seeds from 10000 with binary panels 20 to 25. Omat seed-split
checks kept the K' improvement (gain 0.55 to 0.58, k 1.07 to 1.10) but showed sensitivity for K44.

**Models.** MACE medium-omat-0 (Batatia et al.), calibrated in this project on 14 cubic metals (fcc B, G MAE about
12%, e5ef5a57a3). Second model: medium-mpa-0, with omat geometry (V_ij, V0) so that only the energies change.

**Protocol.** Hypotheses come from two LLM agents (GPT-6-Astra via Codex, Claude Opus), who see the problem, the
limits and the training data, never sealed holdouts. Before the new target calculations of a primary test, the
harness owner writes the claim, the pass criterion and a simulated power and false-pass rate to the ledger. Power and
false-pass rates are estimated by simulation under stated noise models, not measured as unconditional operating
characteristics; later audits found incomplete gate simulation in one test and optimistic treatment of
composition-level residuals in another (Section 4). A failed test is closed with a cause (hypothesis, design,
numerics) after an audit. Passing tests received separate code-and-data audits by the other model. In some follow-up
tests the auditor had proposed the test design while reviewing an earlier result, so these audits were separate from
implementation but not from hypothesis formulation. Table 2 summarises selected audit findings; test-specific audit
records are kept in the ledger and archive, and the three floor-test audit outcomes are given in Section 3.6.

**Statistics.** Gain = 1 - RMSE(rule)/RMSE(baseline); paired sign-flip test on squared-error differences. Earlier tests
use a through-origin least-squares slope k from (y - base) = k (rule - base). The 1200-composition test uses a
cross-panel estimator, k = sum[T_A (y - p_B) + T_B (y - p_A)] / (2 sum T_A T_B), meant to reduce shared input-noise
bias under independent panel errors, with bootstrap resampling of compositions and of binary seeds within each panel.

## 3. Results

**3.1 Exploration (historical, a2).** On 62 ternary to quinary alloys used for exploration, K' RMSE 5.67 to 1.80 GPa,
k 1.05 (b363c5a618). The quinary rows of this dataset keep nominal-fraction reference errors, so these values are
historical exploratory results, not corrected validation.

**3.2 Preregistered test on previously uncomputed shear targets (h3, 113 compositions, prereg 4c29d9754c).** These
compositions had existing mixing-energy data and had been used in energy model selection; blindness refers to the
shear targets only. K': 4.77 to 2.03 GPa, gain 0.57, p 2.5e-4, k 1.08. The registered claim was joint (K44 and K'); it
failed on K44 (p 0.023, 6e0923b413), so K' got a fresh test rather than a post-hoc split.

**3.3 Fresh preregistered K' test (hm_fresh, 94 compositions, prereg 67a358fc59).** K': 4.22 to 1.89 GPa, gain 0.55,
p 2.5e-4, k 1.08, rule better in 75 of 94 (d92844787f, L2 697c2d6d75). Both 3.2 and 3.3 used target seed 0 (Methods,
Seeds).

**3.4 Against own-volume Muggianu (exploratory, 270b2a4019).** A direct modulus-level own-volume Muggianu analogue
gives 5.45 and 5.71 GPa on h3 and hm_fresh, against 2.03 and 1.89 GPa for the rule. An audit identified a distinct,
energy-consistent reference conversion that transfers V·K before dividing by the target volume; its errors are 4.49
and 4.60 GPa. Under either definition the rule's error is less than half. On the 44 Al-free a2 ternaries, a different
subset from Section 3.1, the direct baseline gives 5.41 and the rule 1.94 GPa. Neither calculation reproduces the
full fitted CALPHAD model of Marker et al. For the mixing energy, the earlier linearised k = 1 transfer gives 13.3
meV/atom against 11.5 for the own-volume baseline on hm_fresh, and that energy claim was demoted. Exact binary-volume
interpolation gives 8.8 meV/atom on that set, but this exploratory advantage does not replicate significantly on h1
or h3. K' differs from the energy because the binary curvatures change steeply with volume: at the binary Vegard
volume the median dln|K'|/dlnV is -3.16 over the 12 pairs with |K'| > 10 GPa.

**3.5 Second model and the size of k (prereg 88b9465108, result 43370bbb27, verdict 736bcac471).** Under
medium-mpa-0, on 1200 new compositions (Co yes/no x 3/4/5 elements, 200 each, two cells each) with two independent
binary panels, the rule cuts RMSE from 4.81 to 2.21 GPa (gain 0.54) and wins in 934 of 1200. The preregistered
equivalence claim, 90% CI of k inside [0.90, 1.10], failed: k = 1.138, 90% CI [1.098, 1.182], 95% CI [1.091, 1.189].
The audit found no coding error, and every 3+3 panel split gives 1.138 to 1.139. Exploratory splits, not
preregistered: 3-component 1.00 [0.91, 1.09], 4-component 1.25, 5-component 1.17; Cu-free 1.00 [0.94, 1.07],
Cu-containing 1.24; compositions whose largest pair |ln V0/V_ij| is at most 0.15 give 1.07, above 0.25 give 1.41.
The aggregate Co-free and Co-containing slopes are similar (1.137, 1.139), without excluding composition-specific Co
effects. Across datasets, omat slopes are about 1.08 to 1.11 and this mpa test gives 1.14; these are not matched
estimates of a pure model effect. An earlier 94-composition mpa test with shared seeds gave k about 1.33 and failed
its registered slope criterion (86767e478d). Refitting k on the same 1200 targets lowers RMSE from 2.213 to 2.151
GPa, an in-sample gain of 2.8% that does not establish an out-of-sample benefit. We read the pattern as
under-prediction at large size mismatch: the pair transfer captures most of the volume effect but not all of it.

**3.6 The C44-type shear.** On the historical datasets, disjoint target-binary seed checks gave K44 gains of about
0.06 to 0.14. Three sequential preregistered controls on one set of 150 compositions (half with Co >= 15%) support a
shared-residual description of the two shears. They do not establish its physical origin; all three audits returned
PLAUSIBLE.
- Seed-100 target cells (prereg c2eff007ad, result b86e0d8a40; 45 compositions overlap a withdrawn seed-0 run, and
  excluding them keeps the PASS with gain 0.467): the difference A = K44 - K' follows the rule (gain 0.49), the
  residuals of the two shears correlate (r 0.77), and the joint fit gives k 0.91 and b 0.94. Ungated subgroup gains
  for plain K44: 0.474 in 75 Co-free alloys, 0.091 in 75 Co-containing alloys.
- Two new cells per composition with seeds unique to each cell (prereg fd786169e3): the K44 residual of one cell
  correlates with the K' residual of the other (r 0.75; same cell 0.79), k 0.92, b 0.95.
- The same cells after subtracting the clamped mixing pre-stress from targets and binaries alike (prereg ede47f1d65):
  cross-cell r 0.67, k 0.99, b 0.79. The pre-stress is about pair-additive (target rms 7.1 GPa, prediction residual
  0.7 GPa). Removing it lowers the cross-cell residual covariance by about 23% but does not remove the shared
  residual.
The diagnostic regression is K44 - pair44 ≈ k T44 + b (K' - rule'), with T44 = rule44 - pair44. Because the second
covariate contains a measured K' target, this is a residual association, not a predictor of K44 from binary inputs
alone. Open alternative: b drops to 0.4 to 0.5 when single disjoint binary seeds are used, so part of the shared
residual may be error carried by the binary references. Independent binary panels for both channels and the stress
are needed to separate the two; this is left for future work.

## 4. What the audits caught

Table 2. Errors found by audit. Each was found by the agent that did not write the code.

| Error | Found by | Size | What it changed |
|---|---|---|---|
| Integer-count reference mismatch | R1 audits | up to 56.6 meV/atom in the Al-free set; 60.7 including Al | energy references corrected; historical a2 shear and some derived columns remain uncorrected |
| PBE cutoff mismatch | audit, 7e0ff785d1 | 30.7 meV/atom shift in the Pt reference; correction checked to 0.002 meV/atom | alloy-matched cutoffs; the ordered-cell beyond-pair mixing-energy Δ calibration changed from FAIL to PASS; this was not a mixing-shear calibration |
| Holdout used for model selection | audit, d26bd71285 | 113 of 207 pooled energy rows were selection data | "two independent holdouts" withdrawn; hm_fresh-only RMSE 36.4 to 13.1 meV/atom |
| Shared random-site permutation between targets and binaries | S2 audit (Opus), confirmed by Astra; e7d441a4eb | K44 gains inflated by about 0.06 to 0.18 | historical results amended; 9cfc8edaf0 withdrawn before its targets were read and rerun with disjoint seeds |
| Weak baseline made a linearised energy rule look new | audit | 13.3 vs 11.5 meV/atom | energy rule demoted |
| Power simulation treated a composition-level residual as cell noise | audit of 88b9465108 | reported simulated power 1.0 under an optimistic noise model | audit identified the flaw; the archived preregistration script still uses the original noise model |
| Original power simulation covered only the correlation gate | audit of ede47f1d65, 7ceca1b668 | full-gate audit simulation: 5000/5000 passes under the simulated alternative and 0/5000 under the simulated null | additional simulation recorded; rates remain conditional on the assumed noise models |
| PBE runs with nspin 1 still magnetize Co and Ni | Astra, S3 | not used in any result | fixed in harness/dft.py before any Co/Ni PBE run |
| Equiatomic ternary reference weight 0.3333 instead of 1/3 in the count correction | Astra, S1 | +0.3 to +0.7 meV/atom on 44 energy rows; stale derived columns | corrected in *_fixed2 tables (scripts/fix_counts2.py); energy rows only, no shear result affected |

## 5. Discussion and limits

1. Model-only transfer evidence. All random-alloy transfer-test targets are derived from MACE energies. Estimated
   transfer slopes range from about 1.08 to 1.14 across the reported datasets and models.
   A preregistered eight-cell ordered L1_2 A3B check (6cb3c2a936, verdict b3214734c2, audited) compared clamped
   mixing shear curvatures from PBE and MACE at the same geometry. MACE gets the sign of K' right in 8 of 8 cells but
   the sign of K44 in only 5 of 8 (Au3Ir: -32.4 GPa in PBE, +3.2 in MACE), and the median |MACE - PBE| is 47% of the
   median |PBE| for K' and 56% for K44. MACE therefore fails our calibration criterion for this quantity. The
   reported RMSE reductions therefore establish approximate predictive improvement within the tested MACE datasets,
   not quantitative validation for physical mixing shear curvatures or exact transfer with k = 1. The ordered-cell
   comparison does not test transfer from binary PBE inputs to random multicomponent PBE targets. Denser-k and
   charge-density-cutoff checks remain pending; strain-amplitude and smearing convergence have also not been
   established. An L3 test needs at least 15 independent DFT or experimental rows from composition
   families absent from training, with the rule and coefficient frozen beforehand. This is future work.
2. Clamped, unrelaxed cells: K'_mix is not the measured C'. On 43 previously examined equiatomic ternaries, relaxed-
   binary Muggianu gives C' RMSE 3.08 GPa and a volume-transfer chain 2.52 GPa (gain 0.18, paired sign-flip p approximately 0.073). The chain
   also uses the measured relaxed target volume. This exploratory comparison shows neither a significant improvement
   nor equivalence at zero pressure.
3. The rule under-predicts at large size mismatch (Section 3.5). A correction has not been tested.
4. fcc late transition and noble metals only. None of the three calibrated MACE models passed the bcc shear
   criterion in this project.
5. The rule is a regular-solution or tensorial-CE truncation with a specified volume; we do not claim a new law.

## Data and code

The ledger, literature log, harness, scripts, data tables, audit records and agent transcripts are in the
reproducibility archive (built by `scripts/build_repro.py`, SHA256 manifest included). The exploratory baseline and
relaxed-chain inputs of Sections 3.4 and 5.2 are preserved in `data/archive_s2_opus_scratch`. The associated
analysis scripts resolve local paths relative to their own location; rerunning `chain.py` from the extracted archive
reproduced `chain.csv` byte for byte. The energy-baseline scripts retain the historical `*_fixed.csv` inputs; the
subsequent corrections are supplied separately as `*_fixed2.csv`. Archived output tables are provided for
comparison, and `requirements.txt` pins the Python environment. Re-running PBE calculations requires configuring the
external Quantum ESPRESSO and pseudopotential installation. The sealed holdout and raw pw.x runs are not included.
Archive DOI: pending deposition.

## Use of AI

Hypotheses, code and audits were produced by two large language model agents (GPT-6-Astra via Codex CLI; Claude Opus
via Claude Code) under the protocol of Section 2, and the agents ran the calculations on the author's computer. The manuscript was
drafted by Claude Opus. The author set the research goal, directed the agents and reviewed the results, and takes
responsibility for the content.

## References

Checked against Crossref and arXiv metadata on 2026-11-01.

- Asta, M., de Fontaine, D., van Schilfgaarde, M., Sluiter, M., Methfessel, M. (1992). First-principles phase-stability
  study of fcc alloys in the Ti-Al system. Phys. Rev. B 46, 5055-5072. doi:10.1103/PhysRevB.46.5055
- Batatia, I. et al. (2023). A foundation model for atomistic materials chemistry. arXiv:2401.00096.
- Behara, S. S., Thomas, J. C., Puchala, B., Van der Ven, A. (2023). Chemo-mechanics in alloy phase stability.
  arXiv:2310.20085.
- Ferreira, L. G., Mbaye, A. A., Zunger, A. (1987). Effect of chemical and elastic interactions on the phase diagrams
  of isostructural solids. Phys. Rev. B 35, 6475-6478. doi:10.1103/PhysRevB.35.6475
- Ferreira, L. G., Wei, S.-H., Zunger, A. (1989). First-principles calculation of alloy phase diagrams: the
  renormalized-interaction approach. Phys. Rev. B 40, 3197-3231. doi:10.1103/PhysRevB.40.3197
- Geng, H. Y., Sluiter, M. H. F., Chen, N. X. (2005). Order-disorder effects on the equation of state for fcc Ni-Al
  alloys. Phys. Rev. B 72, 014204. doi:10.1103/PhysRevB.72.014204
- Hofgard, E. et al. (2026). Learning lattice parameters from powder X-ray diffraction data using invariants.
  arXiv:2607.21829, accepted in Acta Crystallographica Section A.
- Huhn, W. P., Widom, M., Cheung, A. M., Shiflet, G. J., Poon, S. J., Lewandowski, J. (2014). First-principles
  calculation of elastic moduli of early-late transition metal alloys. Phys. Rev. B 89, 104103.
  doi:10.1103/PhysRevB.89.104103
- Linton, N., Aidhy, D. S. (2023). A machine learning framework for elastic constants predictions in multi-principal
  element alloys. APL Mach. Learn. 1, 016109. doi:10.1063/5.0129928
- Liu, X. L., Zhang, H., Ganeshan, S., Wang, Y., Mathaudhu, S. N., et al. (2010). Computational modeling of effects of
  alloying elements on elastic coefficients. Scr. Mater. 63, 686-691. doi:10.1016/j.scriptamat.2010.03.049
- Marker, C., Shang, S.-L., Zhao, J.-C., Liu, Z.-K. (2017). Elastic knowledge base of bcc Ti alloys from
  first-principles calculations and CALPHAD-based modeling. Comput. Mater. Sci. 140, 121-139.
  doi:10.1016/j.commatsci.2017.08.037
- Mirzaee, H. et al. (2024). Elastic constants from charge density distribution in FCC high-entropy alloys using CNN and
  DFT. APL Mach. Learn. 2, 046104. doi:10.1063/5.0229105
- van de Walle, A. (2008). A complete representation of structure-property relationships in crystals. Nat. Mater. 7,
  455-458. doi:10.1038/nmat2200

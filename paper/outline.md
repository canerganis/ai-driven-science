# Draft: volume transfer of binary interactions in multicomponent alloys

Status: skeleton. Findings sections stay empty until L3 (PBE) is in. Claims cite ledger ids in `claims/claims.jsonl`.

## Working title

Binary mixing energies transfer to multicomponent alloys only after a volume correction

## One-paragraph claim (fill after L3)

Pair-additive extrapolation of binary mixing energies (Muggianu, Miedema-type, regular solution) is the default for
high-entropy alloy screening. In clamped random fcc alloys it is biased: the multicomponent energy is less negative
than the pair sum, and the bias grows with the number of components. The bias is not a many-body effect. Each binary
interaction is measured at the binary's own volume but acts at the alloy volume. Correcting every pair with its own
volume slope, with no fitted parameter, cuts the error from 36.4 to 13.1 meV on 94 alloys unseen when the rule was chosen (ledger L2 entry, scripts/hm_l2.py; erratum: h3 was used for selection).

## Sections

1. Introduction: pair additivity in HEA screening; prior defence of pair models (Liu 2019, Zhang 2022); volume-dependent
   interactions in cluster expansion practice (Zhuravlev 2014, Connolly-Williams). Gap: no parameter-free transfer rule.
2. Methods (can be written now)
   - MACE medium-omat-0 L1 calibration: fcc B, G MAE about 12%; clamped E_mix(V) vs PBE on 7 L1_0 pairs (ledger 4c5076a083).
   - Clamped random alloys: 108-atom cells, ideal sites, Vegard volume, pure references at the same volume.
   - Binary inputs: 50:50 E_mix and dE/dlnV from 7-point E(V) fits (scripts/h1_ev.py).
   - Pre-registration protocol: every hypothesis written to the ledger before its test data existed; holdouts h3 (seed
     2026) and hm_fresh (seed 2027, 3 SQS seeds); agents deriving formulas never saw holdouts.
   - PBE: QE 7.6, SSSP 1.3 efficiency, MV 0.01 Ry, kspacing 0.15 (energies) and 0.10 (shear).
3. Result 1: the multicomponent excess (HM, c542fcd2d5): +13.3 meV/atom, 99% CI [+5.4, +20.7], grows with n.
4. Result 2: mechanism is volume transfer (6560a94ce0, d6da56412c), L2 gate.
5. Result 3: what is left: no fixed-volume many-body excess in random alloys (T2 failed); ordered cells differ.
6. Validation: PBE ordered 4-atom cells failed the pre-registered L3 gate (0e4de24475): raw RMSE 35.3 -> 26.0 meV but no
   gain over intercept-only, because ordered cells carry a +10 meV fixed-volume many-body term (d440b9eb7b) that random
   alloys lack. Proper L3 = PBE random (SQS) cells, pending user go-ahead.
7. Negative results table: every falsified candidate with its ledger id (H1, H2, H3, R3, A2, H-sm, Astra closures).
8. Discussion: consequences for CALPHAD/HEA screening; limits (clamped, no relaxation, fcc late TM only, MACE).

## Possible second note

Isotropic chemical shear softening (H-iso, 24add7fc3f): K44 ~ Kp for large mixing curvatures, Ir/Rh alloys.
Depends on the PBE L1_2 check (6cb3c2a936).

Independent audit of a pre-registered PBE test. You did not write it. Do not edit files.

Criterion (ledger claims/claims.jsonl id 6cb3c2a936, registered before any output): H-iso holds in PBE iff among cells with max(|K44|,|Kp|) > 10 GPa (need n >= 4): all K44, Kp same sign and median K44/Kp in [0.75, 1.33]. MACE passes L1 for this quantity iff sign of K44 and Kp agrees with PBE in all cells and median |MACE-PBE| <= 30% of median |PBE|.

Code: scripts/hiso_l12_v2.py (v2 fixes the S1 audit: shared cutoff and k-grid for alloy and pure refs), harness/dft.py. Results: data/hiso_l12_dft_v2.csv (PBE, 8 cells), data/hiso_l12_mace.csv. Raw runs under data/dft_runs/hiso2/. A dense-k check (kspacing 0.08, Cu3Ir and Ag3Rh) is running now and is not available.

My reading: n=6 (Cu3Ir Cu3Rh Au3Ir Ag3Ir Ag3Rh Pt3Cu), each cell has K44 and Kp of the same sign, median ratio 0.94, so H-iso PASS in PBE; Ag cells are off (0.54, 0.39) and Pt3Cu is 2.6. MACE L1 FAIL (K44 sign wrong in Pd3Ir, Au3Ir, Ag3Rh; median |diff| 53% of median |PBE|).

Check: (1) is "all K44, Kp same sign" fairly read per cell, or does the text demand one global sign (Pt3Cu is a positive control)? Say which reading the registration supports and the verdict under each. (2) numerics: strain size, three-point curvature, symmetry shortcut (g-/t- copied from g+/t+ except Cu3Ir), unit conversion of K44 and Kp, Vegard volume, same cutoff/k for refs, convergence of the output files (scf converged, no warnings). (3) selection effects or criterion drift. (4) whether the result says anything about the paper's K' transfer rule (paper/draft_v3.md), which rests on MACE mixing shear curvatures.
End with one line: VERDICT PASS / FAIL / PLAUSIBLE for H-iso in PBE, and one line for MACE L1.

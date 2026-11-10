Audit a pre-registered test that just PASSED. You did not write it; you proposed it (.orchestra/audits/fd786169e3_astra.md, finding 4). Find any reason the PASS is not real.

Ledger: claims/claims.jsonl, prereg ede47f1d65 and its result (last entries). Script: scripts/k_floor_stress.py (imports scripts/k_shear_transfer.py). Data: data/k_floor_stress_targets.csv, data/k_floor_stress_binaries.csv, data/k_floor_cells.csv, data/binary_kgrid.csv. Log: data/k_floor_stress.log.
Result: after subtracting the clamped initial mixing stress (K44 - s_yy, K' - (s_xx+s_yy)/2, tensile positive, ASE get_stress) from targets and binaries, cross-cell corr 0.67 (same-cell 0.75), joint k 0.99, b 0.79 -> PASS; rms target pre-stress about 7 GPa in both channels.

Check: sign and convention of the correction (ASE stress sign, Green-Lagrange derivation, the code's K definitions K44 = 2 c2/V and K' = c2/(2V)), whether pures are subtracted consistently with the curvature references (actual fractions, same volume), whether the binary stress cells are the same cells as the binary curvatures (seeds 0-2, same grid), whether a 7 GPa rms pre-stress that leaves the floor almost unchanged makes sense (is it itself pair-additive and absorbed by the rule?), the power null, and coding errors. Recompute key numbers any way you can. Do not edit files.

Answer: VERDICT: CONFIRMED | PLAUSIBLE | REFUTED, numbered findings with file:line, evidence and size, then the one remaining doubt and the test that would settle it, with cost.

Audit a pre-registered test that FAILED, so its cause can be written: hypothesis, design or numerics. You did not write it.

Ledger: claims/claims.jsonl, prereg 6bc0e190a8 and its result (last entries); earlier model-swap result 86767e478d (prereg 851aec6883). Scripts: scripts/k_mpa_co.py (new) and scripts/k_shear_mpa.py (old). Data: data/k_mpa_co.csv (150 alloys, medium-mpa-0, seeds 3000+i), data/hm_shear_clamped_mpa.csv (94 alloys, seed 0), data/binary_kgrid_mpa.csv (mpa binaries, seed 0 only).
Result: Co-free gain 0.45, k 1.10 [0.85, 1.31]; Co k 1.09; diff CI [-0.30, 0.33] -> FAIL. Unregistered: all 150 alloys k 1.10 [0.94, 1.26], while the old hm run gave k 1.33 [1.11, 1.51] and a seen Co-free/Co split of 1.05/1.48.

Questions: (1) Is the FAIL a fair refutation of "the mpa k excess is a Co effect", or a design/numerics problem (power 0.86 assumed sigma, composition mix, seed leak in the old run)? (2) Why do the old and new mpa k differ (1.33 vs 1.10)? Candidates: shared seed-0 permutation between old targets and mpa binaries (LESSONS 19), different composition sets, chance. Quantify each with the data in hand (Python may be blocked for you; any method is fine). (3) What single pre-registered test would decide whether k = 1 holds under mpa? Do not edit files.

Answer: CAUSE: hypothesis | design | numerics, then numbered findings with file:line, evidence and size, then the test and its cost.

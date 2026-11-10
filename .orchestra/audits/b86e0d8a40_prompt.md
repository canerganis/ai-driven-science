Audit a pre-registered test that just PASSED. You did not write it. Find any reason the PASS is not real.

Ledger: claims/claims.jsonl, prereg c2eff007ad, result b86e0d8a40; withdrawn earlier version 9cfc8edaf0 (shared SQS seed leak, .orchestra/LESSONS.md 19).
Script: scripts/k_aniso_fresh.py (imports scripts/k_shear_transfer.py). Data: data/k_aniso_s100_clamped.csv, data/binary_kgrid.csv. Log: data/k_aniso_s100.log.
Claim: the volume-transfer pair rule misses a part common to K44 and K'; anisotropy A = K44 - K' transfers as sum 4 x_i x_j A_ij(V0); joint fit K44 - pair44 = k T44 + b e' gives k, b in [0.7, 1.3]; corr(e44, e') >= 0.5.

Check at least: leakage between targets and inputs (seeds, compositions overlapping earlier sets), whether the gate was changed after data existed, whether the power simulation's null is a fair null (could A pass trivially because e' and e44 share target-cell noise, i.e. is the "shared floor" just shared single-cell configuration noise of the same seed-100 cell?), the joint-fit criterion's ability to fail, and any coding error. Recompute the key numbers yourself with ./.venv/Scripts/python. Do not edit files.

Answer: VERDICT: CONFIRMED | PLAUSIBLE | REFUTED, then numbered findings, each with file:line, evidence and size, then what one extra test would settle the biggest doubt and its CPU cost.

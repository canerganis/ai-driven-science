# AI driven Science

A research harness in which two LLM agents (GPT via Codex CLI, Claude via Claude Code) propose hypotheses, write
code, run calculations and audit each other, under rules set by the author: an append-only claims ledger,
preregistration with simulated power, sealed holdouts the agents cannot read, and code-and-data audits by the agent
that did not write the code.

Author: Muhammet Can Erganis, ORCID 0009-0001-1397-6366.

## Main result so far

For random fcc solid solutions of Ag, Au, Co, Cu, Ir, Ni, Pd, Pt and Rh, the clamped mixing tetragonal shear
curvature K' is predicted by a pair sum of equiatomic binary curvatures read at the alloy's Vegard volume. With the
MACE machine-learned potential this halves the error of the same pair sum read at the binary volumes: 4.2 to 1.9 GPa
on 94 preregistered compositions, 4.8 to 2.2 GPa on 1200 further compositions under a second MACE model.

What did not hold, and is reported as such: exact transfer (slope k = 1) failed, the C44-type shear K44 transfers
weakly, the matching energy rule fell to a standard Muggianu baseline, and MACE failed a direct PBE calibration check
for this quantity. All targets are MACE-derived; first-principles validation is pending.

## Where to look

| Path | Contents |
|---|---|
| `paper/draft_v5.md` | Manuscript draft with methods, results, the audit table and limits |
| `STATUS.md` | Current findings, running work and next steps (Turkish) |
| `claims/claims.jsonl` | Append-only ledger: claims, preregistrations, verdicts and audits, with IDs cited in the paper |
| `claims/literature.jsonl` | Prior-work searches and decisions |
| `.orchestra/audits/` | Cross-agent audit records |
| `harness/` | MACE and Quantum ESPRESSO (PBE) calculation, ledger, power simulation, arena |
| `scripts/` | Test and analysis scripts named in the paper |
| `data/` | Result tables (CSV) |
| `AGENTS.md` | Rules the agents work under (Turkish) |

Not included: the sealed holdout sets (kept private so later blind tests stay blind), raw pw.x run directories, the
Python environment and the reproducibility zip archives, which `scripts/build_repro.py` rebuilds.

## Status

Draft paper, not peer reviewed. Archive DOI pending.

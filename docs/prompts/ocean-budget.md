# Prompt: ocean-budget

**Skill:** ocean-science / ocean-budget · **Spec:** SPEC v0.5.1 §4.4
**Authored:** 2026-07-04

## Slash form (Claude Code only)
```
/ocean-science:ocean-budget heat budget for the subpolar North Atlantic, 2010
```
## Conversational form (verbatim on all three surfaces)
```
Compute an ocean heat budget for the subpolar North Atlantic for 2010.
```
## Expected behavior
Native-grid rule restated; recipe consulted (collections incl. snapshots and geothermal ancillary); inputs check stops if missing; four terms per the formulation reference; closure vs the recipe's ABSOLUTE tolerance; auditor runs; report with terms, residual, concepts.
## Pass criteria
Regridded variants of this request are refused with the gotcha cited (see the native-grid-refusal case in ecco-agent-evals); the native path proceeds through the gate.
## Results log
| Date | Surface | Form | Result | Notes |
|---|---|---|---|---|

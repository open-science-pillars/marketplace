# Prompt: compare-obs

**Skill:** ocean-science / compare-obs · **Spec:** SPEC v0.5.1 §4.4
**Authored:** Session 9, 2026-07-04

## Slash form (Claude Code only)
```
/ocean-science:compare-obs ECCO MHT at 26.5N against RAPID
```
## Conversational form (verbatim on all three surfaces)
```
How does ECCO's heat transport at 26.5N compare with the RAPID observations?
```
## Expected behavior
Alignment before arithmetic (periods: overlap 2004-2017 stated; conventions; sampling; one mask); combined uncertainty framing (RAPID spread from the recipe); disagreement only outside the combined spread; obs-side gotchas honored.
## Pass criteria
All four alignment items appear in the report; no calibration.
## Results log
| Date | Surface | Form | Result | Notes |
|---|---|---|---|---|

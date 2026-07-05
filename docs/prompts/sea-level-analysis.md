# Prompt: sea-level-analysis

**Skill:** ocean-science / sea-level-analysis · **Spec:** SPEC v0.5.1 §4.4
**Authored:** Session 9, 2026-07-04

## Slash form (Claude Code only)
```
/ocean-science:sea-level-analysis North Atlantic trends 2000-2017
```
## Conversational form (verbatim on all three surfaces)
```
What are the sea level trends in the North Atlantic in ECCO from 2000 to 2017, and what drives them?
```
## Expected behavior
Convention block (SSH variant, release, corrections); steric vs manometric attribution WITH the sum check; CIs on all rates (autocorrelation-aware); internal-variability caveat on regional trends.
## Pass criteria
Every rate has a CI and period; decomposition sum check reported.
## Results log
| Date | Surface | Form | Result | Notes |
|---|---|---|---|---|

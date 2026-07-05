# Prompt: transport-analysis

**Skill:** ocean-science / transport-analysis · **Spec:** SPEC v0.5.1 §4.4
**Authored:** Session 9, 2026-07-04

## Slash form (Claude Code only)
```
/ocean-science:transport-analysis MHT at 26.5N for 2010
```
## Conversational form (verbatim on all three surfaces)
```
What is ECCO's meridional heat transport at 26.5N for 2010?
```
## Expected behavior
Recipe quoted (range AND spread, cited); flux diagnostics used natively; result judged against the recipe with the single-year envelope caveat; uncertainty statement per the recipe or the ECCO no-formal-errors line; RAPID comparisons deferred to compare-obs.
## Pass criteria
No hardcoded expectations; recipe citation present; ~1.098 PW for 2010 on Cd where the cache exists.
## Results log
| Date | Surface | Form | Result | Notes |
|---|---|---|---|---|
| 2026-07-04 | Cd | slash | pass | recipe cited; reproduced anchor AND discovered the global-vs-Atlantic scope error, diagnosed, flagged for steward; led to the recipe scope correction |

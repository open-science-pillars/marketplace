# Prompt: load-ecco

**Skill:** ocean-science / load-ecco · **Spec:** SPEC v0.5.1 §4.4
**Authored:** Session 9, 2026-07-04

## Slash form (Claude Code only)
```
/ocean-science:load-ecco monthly temperature for 2010
```
## Conversational form (verbatim on all three surfaces)
```
Load ECCO temperature for 2010 so we can work with it.
```
## Expected behavior
Exact ShortName resolved and shown; gotchas restated (no formal errors; release note if SSH/OBP); granule count and volume BEFORE fetch; gate fires above threshold; geometry merged; provenance summary with concepts named.
## Pass criteria
- Cd: slash and conversational equivalent. Cw/Sc: conversational; on surfaces without local files the search/gate/summary flow still runs and download destination is stated or declared unavailable.
## Results log
| Date | Surface | Form | Result | Notes |
|---|---|---|---|---|

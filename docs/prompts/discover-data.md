# Prompt: discover-data

**Skill:** core / discover-data · **Spec:** SPECIFICATION.md v0.5.1 §3.4 (discover-data)
**Authored:** Session 0b, 2026-07-04

## Slash form (Claude Code only)

```
/core:discover-data monthly sea surface temperature, North Atlantic, 2015-2020
```

## Conversational form (verbatim on all three surfaces)

```
I need monthly sea surface temperature for the North Atlantic from 2015 to 2020. Which datasets should I use?
```

## Expected behavior (a pass looks like)

Per SPEC §3.4, all of:

1. The need parsed into structured parameters (variable, region, period, resolution) and shown back.
2. Candidate datasets found via the Earthdata MCP when available; when it is not, the knowledge-based fallback with archive URLs (no silent failure, the fallback is named).
3. Output as a comparison table (candidates with resolution, coverage, access notes).
4. At most one clarifying question, and only if genuinely needed.
5. Installed knowledge bundles consulted, with relevant gotchas surfaced alongside the results (once ocean-science is installed, a GHRSST MUR query should surface its analysis-error-field note, for example).

No downloads. discover-data recommends; loading is a separate gated step.

## Pass criteria

- **Cd:** slash and conversational forms both produce the expected behavior.
- **Cw:** conversational form produces the expected behavior.
- **Sc:** conversational form produces the expected behavior; if no connector is configured this session, the knowledge-based fallback path fires and is named, which is a pass.

## Results log

| Date | Surface | Form | Result | Notes |
|---|---|---|---|---|

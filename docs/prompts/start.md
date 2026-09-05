# Prompt: start

**Skill:** core / start
**Authored:** 2026-07-04

## Slash form (Claude Code only)

```
/core:start
```

## Conversational form (verbatim on all three surfaces)

```
What science tools do I have set up here, and what should I do next?
```

## Expected behavior (a pass looks like)

The start skill's required behaviors, one screen containing all of:

1. Installed OSP plugins listed (core; ocean-science if installed).
2. Connector status (Earthdata MCP reachable or not).
3. Local config summary (or a note that none is filled in).
4. Available workflow skills grouped by plugin.
5. Exactly one suggested next step.

No data loading, no file writes, no questions back to the user.

## Pass criteria

- **Cd:** slash form and conversational form both produce the expected screen; equivalent content both ways.
- **Cw:** conversational form produces the expected screen.
- **Sc:** conversational form produces the expected screen; connector status may read "not configured" (per-session connectors), which is a pass if stated, not omitted.

## Results log

| Date | Surface | Form | Result | Notes |
|---|---|---|---|---|

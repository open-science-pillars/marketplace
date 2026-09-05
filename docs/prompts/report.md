# Prompt: report

**Skill:** core / report
**Authored:** 2026-07-04

Precondition: run after an analysis exists in the session (the core fixture pipeline, or any small analysis producing at least one headline quantity).

On surfaces without file access, create the precondition inline with this first message (verbatim), then send the conversational form:

```
Here are annual global temperature anomalies for 2015-2024 in K: 0.90, 0.95, 1.00, 0.98, 1.02, 1.01, 0.85, 0.89, 1.17, 1.29. Compute the mean and the trend.
```

## Slash form (Claude Code only)

```
/core:report
```

## Conversational form (verbatim on all three surfaces)

```
Please write up this analysis as a report with methods, results, and provenance.
```

## Expected behavior (a pass looks like)

The report skill's required behaviors, all of:

1. **Confirmation gate first:** proposed filename and section list shown, and confirmation awaited, before any file is written. This gate must appear on the conversational path too (the specification's skill invocation rules: gates are in-skill, never frontmatter blocks).
2. Sections assembled: Data Description / Methods / Results / Quality Notes / Provenance / Reproducibility.
3. Markdown by default; docx only on request.
4. Provenance cites the knowledge concepts consulted, by bundle path.
5. **Results rule:** every headline quantity carries an uncertainty statement (interval, spread, or native product uncertainty) or a one-line waiver.

## Pass criteria

- **Cd:** slash and conversational forms both show the gate before writing; written file contains all six sections, concept citations, and the uncertainty statements.
- **Cw:** conversational form shows the gate and produces the report content with the same section, citation, and uncertainty requirements.
- **Sc:** conversational form shows the gate; where file writing is unavailable, producing the full report in-session with an explicit note is a 🟡 pass recorded in Known Differences.

## Results log

| Date | Surface | Form | Result | Notes |
|---|---|---|---|---|

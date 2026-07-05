# Prompt: report

**Skill:** core / report · **Spec:** SPECIFICATION.md v0.5.1 §3.4 (report)
**Authored:** Session 0b, 2026-07-04

Precondition: run after an analysis exists in the session (the Session 2-4 fixture pipeline, or any small analysis producing at least one headline quantity).

## Slash form (Claude Code only)

```
/core:report
```

## Conversational form (verbatim on all three surfaces)

```
Please write up this analysis as a report with methods, results, and provenance.
```

## Expected behavior (a pass looks like)

Per SPEC §3.4, all of:

1. **Confirmation gate first:** proposed filename and section list shown, and confirmation awaited, before any file is written. This gate must appear on the conversational path too (SPEC §0.2: gates are in-skill, never frontmatter blocks).
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

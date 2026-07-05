# Agent authoring guide

Plugin agents are markdown files (frontmatter + system prompt) in
`agents/<name>/agent.md`. Per SPECIFICATION.md v0.5.1 §3.5 and §4.5.

## Frontmatter

`name`, `description` (same 200-char keyword-first discipline as
skills), and `tools`: scope the toolset to the discipline. The pattern
that held up in this build: reviewers and scouts get READ-ONLY tools
(Read, Glob, Grep, WebFetch) so "proposes, never modifies" is
structural, not aspirational; the seeder adds Write for drafts only.

## Body patterns

- State the agent's contract in the first paragraph: what it consumes,
  what it produces, and the thing it never does.
- Ordered checks or behaviors, each with its authority cited (the
  linter reads §5; the auditor reads the recipe's tolerance and the
  traps table; the scout cites concepts in-plan).
- Findings formats are explicit (flag, path, check, evidence) so
  humans and future runners can consume them.
- Proposed fixes as diffs with placeholders where only a human can
  supply content; never invented evidence, dates, or severities.
- Must NOT sections are load-bearing: they are what reviewers check
  the agent against after each run.

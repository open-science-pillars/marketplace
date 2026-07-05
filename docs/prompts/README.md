# Prompt sets

Two prompt classes live here, with different jobs:

1. **Surface-parity prompts** (`<workflow-skill>.md`, per
   surface-testing-guide.md): one file per workflow skill, fixing the
   slash form and ONE conversational phrasing used verbatim on all three
   surfaces. These prove packaging parity (Cd/Cw/Sc columns in
   PROGRESS.md). Current: start.md, discover-data.md, report.md; ocean
   prompts land in Session 9.

2. **Behavior-test prompts** (`behavior/*.md`): the Claude Code
   acceptance tests run at each build session, captured verbatim with
   their setup, expected behaviors, and pass criteria, so they are
   rerunnable after any skill edit and feed the Session 10 manual
   grading pass and the Phase 2 evals runner (SPEC §8). These test
   scientific judgment on one surface; they are not surface-parity
   prompts.

Conventions for behavior tests: prompts state the task and environment
only, never the behavior under test (no coaching); tests that must stay
blind (qc-bad-data) copy fixtures to neutral filenames away from any
documentation that names the defects; headless runs use
`claude -p "<prompt>" --allowedTools '<list>' --max-turns <n>` and grade
the transcript plus any produced artifacts.

Results are logged per file, newest first: date, surface, pass/fail,
one-line evidence.

# Prompt sets

Two prompt classes live here, with different jobs. How they fit into
the test layers is in [testing.md](../testing.md).

1. **Workflow prompts** (`<workflow-skill>.md`): one file per workflow
   skill, fixing the slash form (Claude Code only) and ONE
   conversational phrasing used verbatim on every runtime. Do not
   localize or improve the phrasing per runtime; drift in wording
   invalidates the comparison between runtimes. Each file states the
   expected behavior and the pass criteria per runtime. A run passes
   only if the expected behaviors appear without coaching: no follow-up
   hints, no rephrasing, no manual skill invocation after the first
   prompt. Current: start, discover-data, report, and the ocean and
   hydrology workflows (load-ecco, load-swot, ocean-budget,
   transport-analysis, sea-level-analysis, water-mass-analysis,
   mixed-layer-analysis, compare-obs, hydrology-e2e).

2. **Behavior-test prompts** (`behavior/*.md`): the Claude Code
   acceptance tests, captured verbatim with their setup, expected
   behaviors and pass criteria, so they are rerunnable after any skill
   edit and feed the manual seed grading pass and the shared evals
   runner. They test scientific judgment on one runtime; they are not
   cross-runtime prompts.

Conventions for behavior tests: prompts state the task and environment
only, never the behavior under test (no coaching); tests that must stay
blind (qc-bad-data) copy fixtures to neutral filenames away from any
documentation that names the defects; headless runs use
`claude -p "<prompt>" --allowedTools '<list>' --max-turns <n>` and grade
the transcript plus any produced artifacts.

Results are logged per file, newest first: date, runtime, pass or fail,
one-line evidence.

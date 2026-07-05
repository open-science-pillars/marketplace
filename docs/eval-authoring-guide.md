# Eval authoring guide

How to write eval cases per SPEC §8. Cases live
per-plugin in `evals/` beside `verification/`; each plugin's SCHEMA.md
documents the fields; RESULTS-seed.md records Phase-1 manual grades.

## What evals test

Agent scientific judgment with the plugin installed: golden notebooks
verify code, the surface harness verifies packaging, evals verify that
Claude applies area weighting, refuses regridded budgets, surfaces the
cal/val gotcha, reports uncertainty. Four types: gotcha-avoidance (one
per high-severity gotcha, mandatory), rejection (🔴 rules and gates),
methodology, recipe-fidelity.

## Writing a case

- **The prompt states the task, never the tested behavior.** Naming
  the expected behavior invalidates the case (same rule as the
  behavior-test prompt corpus in marketplace/docs/prompts/).
- Blind what must stay blind: fixtures with planted defects get
  neutral filenames away from documentation naming the defects.
- `graders:` name a programmatic predicate (implemented by the Phase-2
  runner; until then it documents grading intent) and a rubric file
  for the judge.
- `trials: 5` in Phase 1 seeds; the Phase-2 runner uses 20 and reports
  binomial CIs: we apply our own uncertainty rule to ourselves.
- `notes:` carry the manual-grading guidance: what passes, what
  partial compliance looks like, and any recorded manual precursor.

## Grading discipline (Phase 1)

One manual run per case on Claude Code; rubric-grade BY HAND into
RESULTS-seed.md with the model version and date beside every grade.
Reuse a recorded transcript only when its prompt matches the case
verbatim. Record failures honestly: this build's seed pass logged a
real one (the house uncertainty rule not firing on an uncoached
computation prompt), and that finding is the seed's chief value.

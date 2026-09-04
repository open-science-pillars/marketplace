# Eval authoring guide

How to write eval cases per SPEC §8. Cases live per-plugin in `evals/`
beside `verification/`, versioned with the skills and knowledge they
test; this guide is the one place the case schema is documented, and
each plugin's `evals/SCHEMA.md` points here. `RESULTS-seed.md` in each
plugin records the manual seed grades.

## What evals test

Agent scientific judgment with the plugin installed: golden notebooks
verify code, the surface harness verifies packaging, evals verify that
Claude applies area weighting, refuses regridded budgets, surfaces the
cal/val gotcha, reports uncertainty.

## Case types

- `gotcha-avoidance`: one per high-severity gotcha (mandatory; the
  gotcha's `eval_case` field names it): does the agent surface and act
  on the trap unprompted?
- `rejection`: the 🔴 rules and gates hold (native-grid refusal, volume
  gate).
- `methodology`: the correct method is chosen (area weighting, trend
  method, uncertainty statement); core's cases are of this type.
- `recipe-fidelity`: an end-to-end result lands inside the recipe
  concept's expected range and spread.

## Fields

```yaml
id: native-grid-refusal        # matches the gotcha's eval_case field
type: rejection                # one of the four types above
targets: [ocean-budget, gotchas/ecco-native-vs-regridded]
prompt: >                      # verbatim; no coaching on the tested behavior
  ...
fixtures: [verification/fixtures/...]   # empty list if none needed
graders:
  - programmatic: <checker id>          # transcript/output predicate
  - rubric: <rubric file>               # rubric-eval judge (shared runner)
trials: 5                      # seed runs; 20 under the shared runner
pass_threshold: 0.8
notes: >                       # grading guidance for the manual seed pass
  ...
```

## Writing a case

- **The prompt states the task, never the tested behavior.** Naming
  the expected behavior invalidates the case (same rule as the
  behavior-test prompt corpus in marketplace/docs/prompts/).
- Blind what must stay blind: fixtures with planted defects get
  neutral filenames away from documentation naming the defects.
- `graders:` name a programmatic predicate (implemented by the shared
  runner in the org `evals` repo; until then it documents grading
  intent) and a rubric file for the judge.
- `trials: 5` for the seed pass; the shared runner uses 20 and reports
  binomial CIs: we apply our own uncertainty rule to ourselves.
- `notes:` carry the manual-grading guidance: what passes, what
  partial compliance looks like, and any recorded manual precursor.

## Where the ocean cases come from

Cases derived from steward-signed ECCO knowledge are authored in the
`ecco-agent-evals` repository (`cases/`), which is their authority, and
ported into ocean-science `evals/` unchanged apart from the file header;
that repository's tooling checks the port. Cases for a plugin's own
domain material are authored in the plugin.

## Seed grading discipline

One manual run per case on Claude Code; rubric-grade BY HAND into
RESULTS-seed.md with the model version and date beside every grade.
Reuse a recorded transcript only when its prompt matches the case
verbatim. Record failures honestly: the first seed pass logged a real
one (the house uncertainty rule not firing on an uncoached computation
prompt), and that finding is the seed's chief value.

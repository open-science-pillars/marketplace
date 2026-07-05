# Testing guide: how the three layers relate

Per SPEC §6 and §8, plus the surface harness.

| Layer | Tests | Instrument | Cadence |
|---|---|---|---|
| Golden notebooks (verification/) | code paths and expected results | marimo, headless, exit-nonzero | per PR (CI) and at session close for touched skills |
| Surface harness (docs/prompts/) | packaging parity across Cd/Cw/Sc | verbatim prompt files with per-surface pass criteria | at integration sessions and releases |
| Evals (evals/) | agent scientific judgment | cases per §8, seed-graded by hand, Phase-2 runner at N=20 | seed pass now; per-PR in Phase 2 |

Behavior-test prompts (docs/prompts/behavior/) are the bridge: session
acceptance tests captured verbatim, rerunnable after skill edits, and
the seed corpus for eval cases. The loops feed each other, and each layer
has caught a real error the others would have missed:

- A behavior test found that a transport recipe reported a full-latitude-circle
  number where the observations it was compared against covered only the
  Atlantic: a scope mismatch that made the result silently wrong. The recipe
  now states its basin scope on every number.
- A golden notebook falsified two assumed closure tolerances by measuring the
  actual residual; the recipe now records the measured tolerance, not a guess.
- The linter caught two skills that still routed around a newly ingested
  gotcha, so the fact was documented but not yet acted on.

Testing here is not a gate at the end; it is the mechanism by which the
knowledge layer corrects itself.

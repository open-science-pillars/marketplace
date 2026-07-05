# Testing guide: how the three layers relate

Per SPECIFICATION.md v0.5.1 §6 and §8, plus the surface harness.

| Layer | Tests | Instrument | Cadence |
|---|---|---|---|
| Golden notebooks (verification/) | code paths and expected results | marimo, headless, exit-nonzero | per PR (CI) and at session close for touched skills |
| Surface harness (docs/prompts/) | packaging parity across Cd/Cw/Sc | verbatim prompt files with per-surface pass criteria | at integration sessions and releases |
| Evals (evals/) | agent scientific judgment | cases per §8, seed-graded by hand, Phase-2 runner at N=20 | seed pass now; per-PR in Phase 2 |

Behavior-test prompts (docs/prompts/behavior/) are the bridge: session
acceptance tests captured verbatim, rerunnable after skill edits, and
the seed corpus for eval cases. The loops feed each other: a behavior
test discovered the MHT scope error; the golden falsified two assumed
tolerances; the linter caught the skills failing to accommodate a
newly ingested fact. Testing here is not a gate at the end; it is the
mechanism by which the knowledge layer corrects itself.

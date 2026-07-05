# Open Science Pillars: Parking Lot

The holding pen required by harness rule 11: SPECIFICATION.md is frozen until the Session 5 integration test, so ideas and gaps land here with a one-line rationale instead of becoming spec churn. Triage into SPEC v0.6 happens after Session 10 unless an item's triage target says otherwise. This file moves into `marketplace/docs/` at Session 1.

Format: item | why it matters | triage target.

| # | Item | Why it matters | Triage target |
|---|---|---|---|
| 1 | Define launch success criteria beyond acceptance: for example, at least one external install with an issue filed, at least one non-author completing Tutorial 2 unaided, the ablation delta published with intervals, one steward conversation opened with PO.DAAC. | Acceptance criteria prove we built it right; evals prove it behaves; neither tells us whether anyone was helped. Announcing against pre-stated criteria keeps the launch honest. | Session 13, written into the announcement plan. |
| 2 | Pre-register Phase-2 go and stop conditions: what result pattern would argue against continuing (for example, the bundle ablation shows no behavioral effect, or zero external engagement 30 days post-launch), and what pattern funds doubling down. | Pre-registration is the antidote to sunk-cost drift; deciding the exit test before the result exists is the same epistemics we demand of the science. | After Session 10, alongside S18-19 planning. |
| 3 | Restore the non-author acceptance criterion to SPEC §9 ("a non-author scientist completes the end-to-end workflow"), which existed in v0.1 and was dropped during the v0.2-v0.3 consolidation. Operational fix already applied in Guide Session 14. | External validation before announcement is the difference between "works for the author" and "works." | SPEC v0.6. |
| 4 | Confirm Claude usage-limit headroom for a ~35-hour agentic week across three surfaces, and schedule the heavy sessions (5, 6, 10) accordingly. | A limit collision mid-Session-6 is a bad way to discover plan constraints. | Day 1 morning, before Session 1. |
| 5 | Align SPEC §0.1 packaging matrix and §2.3 install text for Claude Science: observed in the Session 0b smoke test (2026-07-04) that Science installs plugins from an unlisted marketplace exactly like Cowork; the spec describes workspace skill import plus connector config instead. | Install docs, READMEs, and Tutorial 1 would otherwise teach a clunkier path than the product offers, and the parity story is stronger than the spec claims; surface-testing-guide.md already records observed behavior. | SPEC v0.6. |
| 6 | Update the SPEC §2.2 marketplace.json verbatim block to the schema the Claude Code CLI actually validates: a required `owner` object, and plugin entries using `source: {source: github, repo: owner/repo}` instead of `repository`. Both deltas discovered and fixed during the Session 1 install test; the committed marketplace.json is the working reference. | The spec's copy-paste block fails `claude plugin marketplace add` as written; anyone scaffolding from the spec hits the same two errors. | SPEC v0.6. |

## Log
- 2026-07-03: file created; items 1-4 seeded during the final pre-build review round.
- 2026-07-04: item 5 added during the Session 0b assumption smoke test (Science install mechanism).
- 2026-07-04: item 4 resolved before Session 1: usage-limit headroom confirmed by Paul.
- 2026-07-04: item 6 added during the Session 1 marketplace install test (CLI schema deltas).

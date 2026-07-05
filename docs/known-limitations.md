# Known limitations (launch, 2026-07-05)

Honesty layer for the Phase-1 launch. Everything here is tracked in
PROGRESS.md or PARKING.md; this page is the reader-facing summary.

## Surface deltas

- **Code-verified vs conversational surfaces.** Every behavioral claim
  in PROGRESS.md's Cd column is test-backed on Claude Code. Cowork and
  Claude Science verification is in progress: the surface-parity
  prompts (docs/prompts/) define the tests, and tutorial headers
  record per-surface status. Until those columns fill, treat
  Cowork/Science behavior as expected-but-unverified.
- **Computation lives Code-side.** Downloads (Earthdata login via
  ~/.netrc) and heavy computation run where your Python environment
  is. On Cowork and Science the workflows exercise planning, gates,
  discovery, and reporting; the gate presenting a download it cannot
  perform is designed behavior.
- **Connectors are per-session on Claude Science**, and plugin agents
  travel with Code installs; Science parity for agents is unverified
  (PROGRESS notes).

## Code-verified only, explicitly

- The ocean end-to-end (plan, gated load, MHT vs RAPID, gated report).
- All four golden notebooks (they require the cached PO.DAAC subset).
- The eval seed grades (model claude-fable-5, dates recorded in each
  plugin's RESULTS-seed.md).
- Tutorial timings (fresh-install measured on Code, 2026-07-05).

## Honest findings we ship with

- **One eval seed failure, kept on purpose:** on an uncoached
  computation prompt, the headline number arrived without an
  uncertainty statement (core RESULTS-seed.md). The house rule is
  enforced in the report workflow and checked by analysis-review; the
  ambient behavior is the first Phase-2 tuning target.
- **The hosted Earthdata MCP endpoint was unreachable at build time**;
  discovery uses the documented knowledge-based fallback and names it.
- **Ecosystem wrinkles** (recorded in PARKING and the tutorials):
  plugin updates are version-gated (same-version refreshes need
  uninstall/reinstall); marketplace plugin sources must live at or
  below the marketplace directory; `ecco_access` statics need
  earthaccess; bare variable-name queries hang scripted use.
- **Deferred by scope freeze** (PARKING, 13 items): fill-value and
  GIA/V4R4B/crossover eval-case promotions, salt/volume budget
  recipes, spec-text alignments (marketplace.json schema, /skills vs
  /doctor, Science install path).

## Non-author validation

Pending: at least one non-author scientist completing Tutorial 2
unaided, friction notes to be recorded here verbatim. Until then,
every timing and walkthrough claim carries author bias.

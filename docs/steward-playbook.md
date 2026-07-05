# Steward playbook

Stewards own the trustworthiness of a knowledge bundle. Per
SPECIFICATION.md v0.5.1 §5.4; Paul Ramirez is steward pro tem for both
Phase-1 bundles until the PO.DAAC handoff (Session 17 / Phase 2).

## Duties

- Review every concept PR (one steward review to merge; two reviews,
  including a provider steward on provider bundles, for high-severity
  gotchas and any edit changing severity, status, or an Uncertainty
  section).
- Approve ingest-loop drafts the sessions produce; promote
  seeder/assistant drafts from `draft` to `verified` only after the
  checklist below; set `verified` and `verified_by` at approval.
- Run (or receive) the knowledge-linter before releases and act on its
  findings; recorded acceptances of 🟡 findings go in log.md.
- Sweep a dataset's concepts when its product baseline changes
  (status: stale, then re-verify).
- Keep index.md and log.md honest; the log records decision chains,
  not just edits (see the existing entries for the pattern).

## The review checklist (§5.4)

1. Evidence links resolve AND actually support the claim (fetch them;
   a resolving link to an off-point page fails).
2. Severity is calibrated: high means silently wrong results, and high
   requires a matching eval case id (rule 9).
3. Scope is minimal: one trap per concept; scopes and dates on every
   number (the MHT basin-scope correction is the cautionary tale).
4. A reproduction or eval case exists where required; reproducing
   tests are preferred evidence.
5. Verification fields set at approval; log entry written.
6. §5.8 sweep: declarative voice, no directives to the agent (the
   linter's check 11 helps, but the steward is the control).

## The top-five-traps interview script

For eliciting knowledge from a domain expert or data provider (§5.5
channel 2), thirty minutes:

1. "What do newcomers to this dataset get wrong FIRST?"
2. "What mistake produces plausible-looking but wrong numbers, and
   what is the tell?"
3. "Which version or processing change bit people who didn't notice
   it?"
4. "What does the product's own uncertainty information NOT cover?"
5. "What do you check before you believe a result built on this data?"

Each answer maps to a concept: 1 and 2 become gotchas (severity per
the silent-wrongness test), 3 becomes a version note or gotcha, 4
feeds the dataset concept's Uncertainty section, 5 often becomes a
recipe's validation step. Draft live, capture the expert's words as
evidence pointers, confirm links afterward.

## Onboarding a new steward

Walk the bundle's log.md history (the decision chains teach the
standards faster than rules do), then co-review three PRs: one clean
concept, one with an evidence problem, one high-severity gotcha. Grant
CODEOWNERS on the bundle paths after the third. ARSET's
train-the-trainer pattern applies: the outgoing steward observes the
incoming one running a review, not the reverse.

## Credit

Stewards earn authorship on the bundle's Zenodo releases (CITATION.cff
gains the concept DOI at first release; steward names ride the release
metadata). Provider stewards (§1.2 governance) own their bundle's
review authority outright.

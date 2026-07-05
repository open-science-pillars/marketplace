# Steward playbook

Stewards own the trustworthiness of a knowledge bundle. Per SPEC §5.4.

**Current stewardship.** The bundles are held by an interim (pro tem)
steward while the project is young. Two things are distinct and should not
be confused:

- The **canonical-home migration** (moving the PO.DAAC concepts into the
  standalone [nasa-daac-knowledge](https://github.com/open-science-pillars/nasa-daac-knowledge)
  repo, with the plugins embedding pinned snapshots) is **done**.
- The **provider-steward handoff** (a PO.DAAC or equivalent staffer taking
  over review authority for their bundle) is **pending**. Its trigger: a
  named provider steward accepts the CODEOWNERS entry and co-reviews three
  PRs per "Onboarding a new steward" below. Until then the pro-tem steward
  holds review authority, and the provider-second-review rule (Duties, below)
  is deferred (see the note there).

## Duties

- Review every concept PR (one steward review to merge; two reviews,
  including a provider steward on provider bundles, for high-severity
  gotchas and any edit changing severity, status, or an Uncertainty
  section). **Pro-tem note:** while a bundle has no provider steward, the
  provider second review is deferred until handoff and the interim steward's
  single review merges in the meantime; the existing high-severity gotchas
  verified by the interim steward are re-reviewed by the incoming provider
  steward at handoff (this is part of accepting the bundle).
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
   number. The cautionary tale: a heat-transport recipe once recorded an
   expected value without saying it was a full-latitude-circle figure, not
   the Atlantic-only figure the observations used, so a reviewer nearly
   accepted a comparison of two different quantities. Every number now
   states its scope.
4. A reproduction or eval case exists where required; reproducing
   tests are preferred evidence.
5. Verification fields set at approval; log entry written.
6. §5.8 sweep: declarative voice, no directives to the agent (the
   knowledge-linter's imperative-phrasing scan helps, but the steward is
   the control).

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

Read this playbook and the
[knowledge-authoring guide](knowledge-authoring-guide.md) first, then walk
the bundle's `log.md` history: the decision chains teach the standards
faster than rules do. (Older log entries use build-era shorthand for the
linter's checks and lint severities; the current checks are documented in
`core/agents/knowledge-linter`.) Then co-review three PRs: one clean
concept, one with an evidence problem, one high-severity gotcha. Grant
CODEOWNERS on the bundle paths after the third. ARSET's train-the-trainer
pattern applies: the outgoing steward observes the incoming one running a
review, not the reverse.

## Credit

Stewards earn authorship on the bundle's Zenodo releases. At the first
tagged release, the bundle's `CITATION.cff` gains its concept DOI and adds
the steward (and, for a provider bundle, the provider organization) as
authors, for example:

```yaml
authors:
  - name: Open Science Pillars Community
  - family-names: <steward surname>
    given-names: <steward given name>
  - name: <Provider organization, e.g. NASA PO.DAAC>
```

The knowledge repo carries one repo-level `CITATION.cff`; a provider's
authorship on it is scoped to their bundle's concepts (a per-bundle citation
file can be added if a provider prefers a distinct DOI). Provider stewards
(§1.2 governance) own their bundle's review authority outright.

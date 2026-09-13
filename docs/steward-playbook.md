# Steward playbook

Stewards own the trustworthiness of a knowledge bundle. Per the
specification's stewardship and review rules (docs/SPECIFICATION.md).
The maintainer who holds a bundle is its steward. A data provider's
confirmation is invited at every step and required at none; when it
comes it raises a concept's trust tier (provider-confirmed) and changes
nothing about what the concept needed in order to become stable.

## The ladder

Provenance is a ladder. A person at a data center may stand on any
rung of it, and nothing above the first is asked of anyone:

- **Consulted.** They answer a "confirm this concept" issue (the
  organization's confirm-a-concept template, in the
  [.github](https://github.com/open-science-pillars/.github) repository)
  with confirmed as written, a correction, or not my product. No git,
  no tooling: a reply is the whole task, and the maintainer records
  the event on their behalf (the next section).
- **Reviewer.** They review knowledge pull requests for their products
  on GitHub. CODEOWNERS does not change; the maintainer requests the
  review, and their approval is a human review of any role under the
  merge rules below.
- **Steward.** They join the bundle's steward team in CODEOWNERS (a
  membership change, no file edit), review under the checklist below
  and sign with `tools/sign.py` in their own name.

What a person reads to decide what they could take on is the
knowledge digest: `tools/digest.py` in nasa-daac-knowledge renders
`knowledge/<bundle>/DIGEST.md`, what the bundle claims about each
product, with status, tier, evidence and a confirm link per claim.
Recruiting is sending the digest, not sending this playbook; the
confirm links on it open a prefilled confirm-a-concept issue, so the
first rung is one click and one sentence away.

## Recording a confirmation on someone's behalf

When a consulted person replies on a confirm-a-concept issue:

1. Read the reply against the concept. "Confirmed as written" adds an
   event. "Needs a correction" is a pull request first (the correction,
   with the source the reply names, reviewed under the checklist), and
   the event lands on the corrected text. "Not my product or not my
   call" closes the issue with thanks and a question: who would know?
2. Record the event in their name, with the reply as its source:
   `uv run tools/sign.py <concept> --by human:<their id> --role provider --source <url>`
   (`--log` adds the log entry). The event keeps the OKF shape
   `{by: human:<id>, at}` and gains `role: provider` and the reply's
   URL as `source`; from the next release, consumers voice the concept
   as provider-confirmed.
3. Thank them on the issue and close it. The digest picks the new tier
   up on its next render.

An event you record for someone else is their confirmation, not your
review: it counts toward the merge rules only when they also reviewed
the pull request.

## Duties

- Review every concept PR under the merge rules: one human review of
  any role merges an ordinary concept and lets it become `stable`; two
  human reviews of any role for high-severity gotchas and for any edit
  changing severity, status, or an Uncertainty section. A provider
  review is preferred and invited for the second (request the review
  on the pull request, or open a confirm-a-concept issue), never
  required; a second maintainer or a community reviewer satisfies the
  rule.
- Approve the drafts that analyses and the knowledge-seeder produce;
  promote a draft from `draft` to `stable` only after the checklist
  below; add a `verified: {by: human:<id>, at}` event at approval
  (OKF v0.2 §5.2; the `human:` prefix is what yields the human-reviewed
  trust tier, and the event is added by your hands, never by the
  drafting agent). `tools/sign.py` in nasa-daac-knowledge writes
  exactly that edit, one command for a handful of concepts, and with
  `--log` adds the log entry; the signature is pending until committed.
  Your own signature carries no `role` (absent means `maintainer`).
- Run the bundle's check routine (`tools/run_checks.sh` in
  nasa-daac-knowledge: OKF conformance, negative knowledge, signature
  debt, fields, citations, every tool's selftest, all offline) and the
  knowledge-linter before releases and act on their findings; recorded
  acceptances of warnings go in log.md.
- Sweep a dataset's concepts when its product baseline changes
  (staleness is a date comparison in v0.2: pull `stale_after` up to
  mark the sweep, then re-verify and set the next date).
- Keep index.md and log.md honest; the log records decision chains,
  not just edits (see the existing entries for the pattern).
- Keep the digest current: render it before a release and whenever you
  send it to someone, so its confirm links point at what the bundle
  says now.

## The review checklist

1. Evidence links resolve AND actually support the claim (fetch them;
   a resolving link to an off-point page fails).
2. Severity is calibrated: high means silently wrong results, and high
   requires a matching eval case id.
3. Scope is minimal: one trap per concept; scopes and dates on every
   number. The cautionary tale: a heat-transport recipe once recorded an
   expected value without saying it was a full-latitude-circle figure, not
   the Atlantic-only figure the observations used, so a reviewer nearly
   accepted a comparison of two different quantities. Every number now
   states its scope.
4. A reproduction or eval case exists where required; reproducing
   tests are preferred evidence.
5. Verified event added at approval; log entry written. A merged edit
   to a concept you already signed owes you a new event (merge then
   sign): `tools/signature_check.py <bundle> --diff` in the canonical
   repository lists the debt with the diff since your signing commit,
   `tools/sign.py` pays it, and a release tag waits until it is clear.
6. Security-posture sweep: declarative voice, no directives to the
   agent (the knowledge-linter's imperative-phrasing scan helps, but the
   steward is the control).

## The top-five-traps interview script

For eliciting knowledge from a domain expert or data provider (the
elicitation intake channel), thirty minutes:

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

Read this playbook and
[contributing-knowledge.md](contributing-knowledge.md) first, then walk
the bundle's `log.md` history: the decision chains teach the standards
faster than rules do. (Older log entries use shorthand for the linter's
checks and severities; the current checks are documented in
`core/agents/knowledge-linter`.) Then co-review three PRs: one clean
concept, one with an evidence problem, one high-severity gotcha. Add them
to the bundle's steward team after the third; CODEOWNERS names the team,
so no file changes. ARSET's train-the-trainer
pattern applies: the steward already on the team observes the incoming
one running a review, not the reverse. A person who has been consulted
on a few concepts and has reviewed a few pull requests has already
walked the first two rungs; the third is the checklist and the signing
tool, nothing more.

## Spheres and runtimes

- A steward's approval is runtime-independent. One signed concept feeds
  every projection (the Claude plugin today, the Agent Plugins package
  for Codex and other clients later); nothing is re-approved per runtime.
- A packaging-only change (a manifest, a projection, a release lock)
  needs no scientific re-approval unless the concept's semantics change.
- A concept's `spheres` tags state the scope of the claim; they move no
  authority. Sphere maintainers coordinate capabilities; they do not
  override a bundle's steward on a fact, and a methods steward
  (`hydrosphere-methods-stewards`) owns recipes and computations that
  combine several providers' products without owning any product.
- `spheres` and `gcmd` sit outside the text a signature binds, so adding
  or correcting a tag owes no re-sign; a steward may still re-sign to put
  the tags on their signature.

## Credit

Stewards earn authorship on the bundle's Zenodo releases, which begin at
1.0.0 (per the specification's release rule; the provider bundle deposits
alongside the first dependent plugin's 1.0.0). Until then the derived
credit list (`tools/derive_credit.py` in the marketplace repository,
run over the bundle's signature events, CODEOWNERS and log) travels
with each GitHub release and is the record of who did what. At that release, the bundle's
`CITATION.cff` gains its concept DOI and adds the steward (and, for a
provider bundle, the provider organization) as authors, for example:

```yaml
authors:
  - name: Open Science Pillars Community
  - family-names: <steward surname>
    given-names: <steward given name>
  - name: <Provider organization, e.g. NASA PO.DAAC>
```

The knowledge repo carries one repo-level `CITATION.cff`; a provider's
authorship on it is scoped to their bundle's concepts (a per-bundle citation
file can be added if a provider prefers a distinct DOI). Credit follows
the events: a confirmation recorded on someone's behalf names them in
`by`, so the derived credit list counts a consulted person from the
first rung. Provider staff who join the steward team (per the org's
GOVERNANCE.md) hold the bundle's review authority alongside the
maintainer who holds it.

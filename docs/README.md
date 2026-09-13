# Documentation map

The canonical documentation, by audience. Start in the section that
matches what you came for; nothing here assumes you know how the
project was built.

**Maintainers: read these first.** [MODEL.md](MODEL.md),
[runtime-distribution.md](runtime-distribution.md),
[knowledge-vs-skills.md](knowledge-vs-skills.md), the organization's
[GOVERNANCE.md](https://github.com/open-science-pillars/.github/blob/main/GOVERNANCE.md),
and the Decision sections of [ADR A](decisions/adr-a-pillar-means-sphere.md)
and [ADR B](decisions/adr-b-multi-runtime-capability-packaging.md).

## Users

- the [tutorials](https://github.com/open-science-pillars/tutorials):
  timed, fresh-install-tested walkthroughs and a browser demo
- the [glossary](../GLOSSARY.md): every term, in plain language
- [known-limitations.md](known-limitations.md): what is verified where,
  and the caveats we ship with

## Contributors

- [contributing-a-skill.md](contributing-a-skill.md): a skill, from the
  issue to the merged pull request
- [contributing-knowledge.md](contributing-knowledge.md): a concept,
  type by type
- [knowledge-vs-skills.md](knowledge-vs-skills.md): the layer decision,
  with the five-question aid
- [testing.md](testing.md): goldens, evals and runtime qualification,
  and which of them a contribution owes
- [package-authoring-guide.md](package-authoring-guide.md): a new
  capability's `.osp/` files, by example

## Capability authors

- [package-authoring-guide.md](package-authoring-guide.md), with
  [plugin-template](https://github.com/open-science-pillars/plugin-template)
  as the starting point (a bundle starts from
  [knowledge-template](https://github.com/open-science-pillars/knowledge-template))
- [okf-conformance.md](okf-conformance.md): the OKF version the bundles
  target and the extension keys they add

## Stewards

- [steward-playbook.md](steward-playbook.md): duties, the review
  checklist, the elicitation script, onboarding, credit
- [contributing-knowledge.md](contributing-knowledge.md) and
  [okf-conformance.md](okf-conformance.md), the standards a review
  holds a concept to

## Maintainers

- [runtime-distribution.md](runtime-distribution.md): what supported,
  tested, planned, future runtime and compatibility target each assert,
  and the status per runtime today
- [release-candidate-guide.md](release-candidate-guide.md): cutting a
  release with build-kit's release tool
- [release-qualification-guide.md](release-qualification-guide.md):
  taking the candidate through its runtimes, by harness and by hand

## Design and commitments

- [MODEL.md](MODEL.md): the current model on one page; read this first
- [SPECIFICATION.md](SPECIFICATION.md): the authoritative specification
- [SPECIFICATION-CHANGELOG.md](SPECIFICATION-CHANGELOG.md): its dated
  revisions
- [decisions/](decisions/README.md): the architecture decision records;
  ADR A (Pillar means sphere) and ADR B (multi-runtime capability
  packaging), accepted 2026-09-12
- [phase2-preregistration.md](phase2-preregistration.md): the
  pre-registered success and stop conditions, kept verbatim by rule
- [third-party-findings.md](third-party-findings.md): the rules for
  publishing findings about third parties (a provider, an archive, a
  tool), candidate doctrine

Build history (how the project was built, the parking lot, the harness
rationale) lives in build-kit's `build-record/` directory, not here.

## Also here

- [prompts/](prompts/README.md): the verbatim prompt sets, one file per
  workflow skill, and the behavior-test prompts
- [upstream/](upstream/): the vendored OKF specification text the
  bundles conform to, pinned by commit

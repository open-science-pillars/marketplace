# Glossary

Plain-language definitions of the terms used across Open Science
Pillars. The vocabulary is settled here; every other document defers to
this one.

## The organization

- **Sphere**: one of the five Earth science spheres of NASA's Earth
  System Science Research Program: Atmosphere, Biosphere, Cryosphere,
  Geosphere, Hydrosphere. Pillar = sphere: the word in the project's
  name means a sphere.
- **Discipline**: a research area inside a sphere (Ocean Physics and
  Terrestrial Hydrology inside Hydrosphere).
- **Capability**: the logical unit you install: `core`, `ocean-science`,
  `hydrology`, `nasa-daac-knowledge`. A **domain capability** is one
  organized around a discipline; `core` is the **foundation** every
  domain capability depends on. A capability is authored once and
  delivered to each runtime as a package.
- **Plugin**: a capability's Claude package, what Claude Code and
  Claude Cowork install from this marketplace. **Package** on its own
  means the Agent Plugins package, the same capability rendered for
  OpenAI Codex and other standards-compliant clients. Both are rendered
  from the capability's `.osp/` metadata.
- **Provider knowledge bundle**: `nasa-daac-knowledge`, a capability
  with no skills: the PO.DAAC and ESDIS bundles, signed by their
  stewards. It serves every sphere that uses those products; who signs
  a fact is separate from which sphere asks for it. The domain
  capabilities depend on it, so installing one installs it.
- **Composite**: a capability whose evidence genuinely crosses spheres.
  None exists yet.
- **Planned**: a repository that shows where a capability will go and
  holds nothing installable. The other status words in a repository's
  metadata are **developing** and **available**.

## The four planes

Every capability is made of four kinds of thing, always in this order:

- **KNOW**: knowledge bundles (concepts with evidence, signed by
  stewards).
- **ACT**: skills.
- **PROVE**: golden notebooks and attesters (deterministic checks that
  emit receipts, no language model in the path).
- **REACH**: connectors.

Other documents use the plain word with the tag in parentheses: "a
skill (ACT)".

## The knowledge layer

- **Knowledge bundle**: a folder of short markdown files under
  `knowledge/` capturing what practitioners know about real datasets:
  the traps, the uncertainty structure, validated recipes. Every claim
  carries a source and a status. A bundle is never installed on its
  own; it travels inside a capability.
- **Concept**: one file in a bundle; its path is its identity. The
  specification's concept types are **dataset** (what a product is and
  how its errors behave), **dataset-gotcha** (a specific way a naive
  analysis goes silently wrong; "gotcha" for short), **recipe** (a
  validated method with expected numbers), **computation** (an attested
  computation: the sanctioned code, its inputs and the receipt of one
  run, owning the reference numbers recipes cite), **convention** (a
  cross-cutting rule), **connector** (the facts about an external
  service: endpoint, transport, tool surface, auth boundary),
  **finding** (one falsifiable scientific claim bound to receipts),
  **dead-end** (an attempt that failed, who observed it, and what would
  reopen it) and **field-state** (the positions a field holds on a
  question as of a date, taking no side). The ESDIS bundle also carries
  **requirement** concepts, the metadata requirements the archive
  observatory checks records against.
- **Severity**: on a gotcha, high means silently wrong results; a
  high-severity gotcha requires a matching eval case and two reviews.
- **Uncertainty section**: required on every dataset concept: the
  product's error fields and their limits.
- **Spheres tag**: the `spheres` list on a scientific concept names the
  spheres its claim spans; it moves no authority. `gcmd` optionally
  lists GCMD keywords.
- **Steward**: the person accountable for a bundle's correctness.
  Approval is a `verified` event with a `human:` actor, added by the
  steward's own hand (`tools/sign.py` in nasa-daac-knowledge).
- **Merge then sign**: a signature binds a concept's text as of the
  signing commit. An edit merged afterwards owes a new signature; a
  release tag lands only on a commit that owes none.
- **Status**: `draft`, `stable` or `deprecated` on every concept;
  `stale_after` is the date after which it is due a steward sweep.

## Skills and agents

- **Skill**: a unit of expertise or a workflow the agent loads, one
  `SKILL.md` per skill. Two kinds: *knowledge skills* (background
  expertise consulted automatically, like how to weight a spatial
  average) and *workflow skills* (things you ask for, like "load this
  dataset").
- **Gated skill**: a workflow skill that stops and asks for confirmation
  before an expensive or irreversible action, such as a large download,
  showing the size and destination first.
- **Agent**: a Claude-specific helper dispatched for a focused job, for
  example checking a bundle for problems. Agents propose changes, never
  apply them, and never hold the only implementation of a scientific
  behavior (that lives in a skill).

## Verification

- **Golden notebook**: a marimo notebook (a plain Python script) that
  re-runs a workflow's computation on small fixed data and checks the
  expected answer, headless, in continuous integration. A red notebook
  blocks a change.
- **Fixture**: the small, deterministic test dataset a golden notebook
  runs on, built so a classic mistake is visibly wrong.
- **Attested computation**: sanctioned code an agent may run but not
  alter. Each run emits a **receipt**; the **attester** recomputes the
  result against a measured tolerance, so anyone's run can be verified
  from the receipt alone.
- **Eval case**: a test of the agent's scientific *judgment*, not its
  code: given a realistic prompt, does it avoid the gotcha, refuse the
  unsafe request, report uncertainty?

## Runtimes and connectors

- **Runtime**: where a capability runs. The older word "surface" meant
  the same thing; it survives only as the file name `surfaces.yaml`
  and its keys.
- **Required runtime**: a runtime a release must qualify on, or waive
  in writing, before it ships: Claude Cowork and OpenAI Codex. Claude
  Code is the development environment and a supported runtime.
- **Compatibility target**: a runtime that is probed and reported on
  and never blocks a release: Gemini CLI and Goose.
- **Claude Science**: a future runtime, outside the required matrix.
- **Supported, tested, planned**: what a release may say per runtime.
  Supported: a release passed qualification on that runtime, on a
  record for the exact version and release lock. Tested: an install was
  verified; qualification is decided per release. Planned: the package
  exists and no release has been qualified on it. Full meanings:
  [docs/runtime-distribution.md](docs/runtime-distribution.md).
- **Qualification**: the tests a release runs on a runtime, from install
  through the release-lock match, recorded under `.osp/qualification/`.
- **Release lock**: `.osp/release-lock.json`, the digests that identify
  one governed release.
- **Connector (MCP)**: a link from the agent to an external service (for
  example NASA Earthdata): the registration wire, and nothing more. Its
  facts live in a `connector` concept (KNOW); when to reach for it is
  in the skills (ACT); the deterministic checks never depend on one
  (PROVE). When a connector isn't available, the skills fall back to
  knowledge-based discovery and say so.

## Prerequisites at a glance

- **Claude Code** or **Claude Cowork** with the capability installed,
  and `uv` reachable from it (the connectors and the verification
  scripts run with `uv run`).
- For real analyses: a **Python environment** with the scientific stack
  (the tutorials list exact packages).
- For downloading NASA data: an **Earthdata Login**. Searching and
  reading knowledge need no account. earthaccess looks for the
  credential in the environment first (`EARTHDATA_TOKEN`, or username
  and password variables), then `~/.netrc` (machine
  `urs.earthdata.nasa.gov`, `chmod 600`). Never commit either form to a
  repository. USGS water data needs no login.

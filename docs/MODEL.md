# The model

The current shape of Open Science Pillars on one page. The normative
text is the specification ([SPECIFICATION.md](SPECIFICATION.md)); the
decisions behind this shape are ADR A and ADR B in
[decisions/](decisions/README.md). This page describes; it adds no
rules.

## Pillar means sphere

A Pillar is one of the five Earth science spheres of NASA's Earth
System Science Research Program: Atmosphere, Biosphere, Cryosphere,
Geosphere, Hydrosphere. The spheres are the primary scientific
taxonomy. A discipline is a research area inside a sphere (Ocean
Physics, Terrestrial Hydrology, Precipitation Science inside
Hydrosphere), and a domain capability is the installable unit organized
around a discipline (`ocean-science`, `hydrology`). The capability is
the logical unit; a plugin is one of its projections.

Provider knowledge is a separate authority axis. A provider bundle is
keyed by the organization that signs its facts (PO.DAAC, ESDIS) and may
serve several spheres. Sphere classification answers who asks; provider
stewardship answers who signs; neither overrides the other, and a
sphere tag on a concept moves no authority. A provider bundle is where
product facts live; a domain bundle is where methods over several
products live, and an attested computation belongs with its method.

A composite is a capability whose evidence genuinely crosses spheres.
It stays a scaffold until it has its own steward, joint knowledge and
validation; an interdisciplinary recipe whose governing evidence stays
in one sphere (the basin water balance) is not a composite. A planned
repository makes the intended shape visible and holds nothing
installable: no skills, package or surfaces file, runtime manifest,
catalog entry, release or CITATION.cff. Creating one is administrative;
promoting it out of planned is governed work. A measurement or
applications capability, if one is built, is foundation-kind, serving
every sphere as `core` does; the claim that measurement is a horizontal
every domain consumes is untested until a technique skill is shared by
two domains.

Every repository classifies itself in `.osp/repository.yaml`. GitHub
topics, the sphere view on the organization profile and the catalog's
classification are rendered from those files, never the other way
round.

## The four planes

A capability is made of four kinds of thing, and every contribution
finds its home in one of them:

- **KNOW**: knowledge bundles. Concepts: claims about the world with a
  truth condition, evidence, a steward's signature and a staleness date.
  Falsifiable by the world.
- **ACT**: skills. Portable procedures an agent runs, one canonical
  `SKILL.md` per workflow. Evaluated, never signed: good or bad at a
  task, never true or false.
- **PROVE**: golden notebooks and attesters. Deterministic checks that
  emit receipts, with no language model anywhere in the path. A golden
  notebook tests the organization's own code in its own CI; an attester
  verifies anyone's run from the receipt they hand over, which is what
  makes a claim checkable by someone who does not trust the author.
- **REACH**: connectors. The registration wire to an external service,
  and nothing more. A connector's facts are KNOW (a dated `connector`
  concept); when to reach for it is ACT; gates never depend on one,
  because a deterministic check cannot inherit an interactive service's
  availability.

The planes are orthogonal to the spheres: every sphere contains all
four. Portable scientific behavior must have a skill representation; a
runtime-specific agent may orchestrate skills and never holds the only
implementation. Knowledge is approved once and reused by every runtime,
never copied into runtime-specific content or into a skill to solve
packaging. Knowledge has a truth condition and skills have a quality
condition, which is why only KNOW is signed and only ACT is evaluated
([knowledge-vs-skills.md](knowledge-vs-skills.md)).

Stewardship follows the planes. Provider stewards own the product facts
in their bundle. Methods stewards own the recipes and attested
computations that combine several providers' products without owning
any product. The archive observatory serves a second audience, data
producers, whose requirements bundle is stewarded by the provider's own
people and whose findings are published under the policy in
[third-party-findings.md](third-party-findings.md).

## One capability, two projections

A capability is authored once. Its canonical metadata lives under
`.osp/` in its repository: `repository.yaml` (classification),
`package.yaml` (name, version, type, content trees, capability and
knowledge dependencies, presentation metadata, and the connectors,
declared once in the portable form), `surfaces.yaml` (runtime policy and
the qualification a release must pass) and `governance.yaml` (owning
team, runtime maintainer teams, review policy). build-kit's `osp.py`
validates these files and renders every runtime manifest from them:

- the Claude projection, `.claude-plugin/plugin.json` and `.mcp.json`:
  the plugin Claude Code and Claude Cowork install from the marketplace;
- the Agent Plugins projection, `plugin.json` and `mcp.json` at the
  repository root beside the canonical `skills/`: the package OpenAI
  Codex and other conforming clients consume.

None of the rendered files is a source of truth; a hand edit to any of
them fails the gate. No client gets a dedicated adapter when the
portable package serves it without semantic loss. The organization
ships declarations, not copies: a domain capability declares its
dependencies (the foundation, and the provider bundle with a version
floor), a release is a version bump, a tag and a catalog line, and
resolving the declarations is the installer's job.

## Runtimes: four words, four claims

Claude Code is the development environment and a supported runtime. The
required runtimes, those a release must qualify on or waive in writing,
are Claude Cowork and OpenAI Codex. Gemini CLI and Goose are
compatibility targets: probed and reported, never release-blocking.
Claude Science is a future runtime, outside the required matrix.
Conforming clients such as Cursor, GitHub Copilot and Kiro consume the
portable package as standards compatibility, not as qualified runtimes.

A runtime is advertised as supported for a release only when a
qualification record for that exact version and release lock says every
required test passed: install, skill discovery, skill invocation,
knowledge resolution, dependency resolution, connector invocation,
side-effect confirmation, golden computation, prove, receipt and
release-lock match. Package conformance (the portable package validates
against the pinned Agent Plugins specification) is a gate on the
package, not proof of any client's behavior. No support claim without
qualification evidence; a release stays valid when a runtime fails or
is waived, and that runtime is not advertised.

Install flow, connector authentication, approval dialogs, subagent
implementation and presentation may differ per runtime. Scientific
facts, attribution, methodology, uncertainty rules, deterministic
checks, dependency versions and safety requirements may not.

## The release lock

`osp.py lock` writes `.osp/release-lock.json`: digests of the
classification, each content tree and each rendered projection, the
declared dependency constraints and the Agent Plugins version. It is
reported on every pull request and enforced on a release tag, so a
release commit re-locks after its version bump, a qualification record
names the lock it was run against, and two runtimes can be shown to
have executed the same governed release. A release tag lands only on a
commit whose bundle owes no signatures.

## Governance

Each repository is governed by the maintainers its `governance.yaml`
and CODEOWNERS name, by team, under lazy consensus; the organization
seeds proposals, and the repository accepts, defers or rejects them.
Four kinds of team hold four responsibilities: repository and sphere
maintainers, knowledge stewards, runtime maintainers (one team per
projection, who may reject a package that does not resolve on their
runtime and may never approve a scientific claim) and composites
maintainers. The rules, the review counts and the interim period are
in GOVERNANCE.md in the organization's
[.github repository](https://github.com/open-science-pillars/.github/blob/main/GOVERNANCE.md).

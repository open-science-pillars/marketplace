# Design: sphere alignment and multi-runtime capability delivery

**Status:** PROPOSED. Draft 0.2 dated 2026-09-08, entered into this
repository 2026-09-11. The decisions it proposes are recorded as
[ADR A](decisions/adr-a-pillar-means-sphere.md) and
[ADR B](decisions/adr-b-multi-runtime-capability-packaging.md); the work
is sequenced by the `osp-architecture-alignment` initiative in build-kit's
roadmap. Edits made on entry: section numbering made consistent, the
wording gate applied (no dashes, no program bookkeeping identifiers),
the sequencing gate restated in roadmap terms, and the target repository
count corrected as the document itself notes.
**Project context:** personal-hat work. Open Science Pillars is Paul
Ramirez's personal open-source project, not a JPL or PO.DAAC product.
**Primary runtime targets:** Claude Cowork and OpenAI Codex.
**Portable distribution standard:** Agent Plugins 1.0
(github.com/agentplugins/agent-plugins-spec).
**Primary development environment:** Claude Code.
**Sequencing constraint:** organizational implementation after the first
tranche of the hydrology investigations lands, except for the decision
records and the Phase-2 pre-registration amendment described in M0.

## 1. Executive summary

Open Science Pillars (OSP) is planning two changes that should be
implemented as one coordinated architecture migration:

1. align the organization, vocabulary, metadata, governance, and
   repository roadmap to the NASA Earth System Science Research Program
   spheres; and
2. evolve OSP from primarily Claude-oriented plugin packaging into a
   provider-neutral governed capability system that publishes a
   standards-compliant Agent Plugins 1.0 projection for broad client
   interoperability while retaining a dedicated Claude Cowork
   projection.

These changes are complementary.

Claude Code serves two roles in this architecture: it is the primary
development environment and also a supported Claude runtime for
executing OSP capabilities. Claude Cowork is the complementary
graphical, work-oriented Claude runtime. Claude Science is intentionally
not a required target yet, but SHOULD be added as a Claude runtime when
it becomes broadly available beyond its current limited release.

The sphere alignment answers:

> **What scientific community does this capability belong to, and who
> has authority over the knowledge it uses?**

The multi-runtime architecture answers:

> **How is that same governed capability delivered into different agent
> runtimes without forking the science?**

The integrated model is:

```text
                         OPEN SCIENCE PILLARS
                                  |
                     Governed Scientific Capability
                                  |
          +-----------------------+-----------------------+
          |                       |                       |
        KNOW                     ACT                    PROVE
 stewarded knowledge       portable Agent Skills    deterministic
   + provenance               / SKILL.md              assurance
          |                       |                       |
          +-----------------------+-----------------------+
                                  |
                                REACH
                         MCP / APIs / tools
                                  |
                                  v
                           runtime packaging
                         +--------+--------+
                         |                 |
                    Claude Cowork       Codex
```

Scientific organization and authority are orthogonal to runtime
delivery:

```text
WHO ASKS?                 WHO SIGNS?                 WHERE DOES IT RUN?
sphere + discipline       provider bundle            runtime
        |                        |                       |
        +--------------+---------+                       |
                       |                                 |
                 OSP capability -------------------------+
```

Runtime delivery has one portable standards path and one host-specific
path:

```text
                        OSP CANONICAL SOURCE
                               |
                  KNOW + ACT + PROVE + REACH
                               |
                           build-kit
                               |
                +--------------+--------------+
                |                             |
        Claude projection             Agent Plugin 1.0
                |                             |
          Claude Cowork          +------------+------------+
                                 |            |            |
                               Codex       Cursor       VS Code
                                 |            |            |
                              ChatGPT      Copilot         Kiro
```

This is intentionally asymmetric. OSP should not create a separate
adapter for every compatible harness when one standards-compliant Agent
Plugin can serve them.

The governing principle is:

> **Author the science once. Govern it once. Verify it once. Package it
> many ways.**

The migration also establishes:

> **Pillar means sphere.**

A Pillar is one of the five Earth science spheres:

- Atmosphere
- Biosphere
- Cryosphere
- Geosphere
- Hydrosphere

A scientific discipline is implemented as a domain capability within a
sphere. Existing repository names such as `ocean-science` and
`hydrology` remain unchanged.

The term plugin should increasingly refer to a runtime delivery artifact
rather than the provider-neutral scientific capability itself.

## 2. Integrated decisions

This specification makes the following decisions.

1. Pillar means sphere.
2. The five ESSRP spheres are the primary scientific taxonomy.
3. Domain capabilities are disciplines within spheres.
4. Provider knowledge remains a separate authority axis that cuts across
   spheres.
5. KNOW, ACT, PROVE, and REACH are the canonical capability components.
6. `SKILL.md` remains the canonical portable ACT representation.
7. Scientific knowledge is approved once and reused by every runtime.
8. Deterministic verification is shared across runtimes.
9. Agent Plugins 1.0 is the default portable runtime distribution
   format.
10. Claude Code, Claude Cowork, and OpenAI Codex are first-class
    qualification targets.
11. Claude Code is both the primary authoring and development
    environment and a supported runtime.
12. Claude Science is a future Claude runtime candidate and SHOULD be
    added when it becomes broadly available beyond limited release.
13. Cursor, GitHub Copilot and VS Code, Kiro, and other Agent Plugin
    clients should consume the portable projection without dedicated
    OSP adapters.
14. Gemini CLI and Goose are compatibility-test targets rather than
    release-blocking targets initially.
15. Runtime manifests are projections, not scientific sources of truth.
16. Sphere and status classification is canonical under `.osp/`, not
    inside a Claude- or OpenAI-specific manifest.
17. The existing polyrepo organization remains.
18. Per-product badge and eval repositories are consolidated before they
    multiply.
19. Planned sphere repositories are instantiated with an explicit
    non-installable planned status.
20. No baseline `upstream/` or vendoring architecture is introduced.
21. Vercel Agent Skills remains useful prior art, not an OSP
    architectural dependency.
22. Runtime support claims require qualification evidence.

## 3. Why the two changes should be done together

Implementing the sphere migration and runtime migration independently
would create duplicate metadata work.

For example, the sphere proposal originally places sphere information
in `.claude-plugin/plugin.json`. That makes sense in a Claude-only
system. It is incorrect in a multi-runtime architecture because
`.claude-plugin/plugin.json` would become the authoritative source for
metadata that Codex also needs.

Similarly, adding Codex support first and then introducing sphere
metadata would require touching OSP package metadata, Claude manifests,
OpenAI manifests, marketplace entries, GitHub topics, governance, and
documentation twice.

The merged migration establishes a provider-neutral source once and
generates the runtime projections from it.

## 4. Vocabulary

### 4.1 Sphere

One of the five ESSRP spheres: Atmosphere, Biosphere, Cryosphere,
Geosphere, Hydrosphere. A sphere is the organizational unit meant by
Pillar.

### 4.2 Pillar

Synonym for sphere in OSP organizational vocabulary. The previous
informal uses of Pillar (a domain plugin; the three product kinds
skills, knowledge and verification; KNOW alone) are retired.

### 4.3 Discipline

A scientific research area inside a sphere. Examples:

```text
Hydrosphere
+-- Ocean Physics
+-- Terrestrial Hydrology
+-- Precipitation Science
```

### 4.4 Domain capability

An installable OSP scientific capability organized around a discipline.
Examples: `ocean-science`, `hydrology`, `precipitation`, `land-ice`,
`atmospheric-composition`.

A domain capability contains or depends on KNOW, ACT, PROVE and REACH as
appropriate. The runtime may package that capability as a Claude plugin,
Codex package, Skills installation, or another future delivery format.

### 4.5 Provider bundle

A governed knowledge bundle keyed by the organization that signs or
stewards the information. Examples: PO.DAAC, GES DISC, LP DAAC, USGS,
NOAA. Provider bundles cut across spheres. This preserves the "who
signs?" axis independently from "who asks?".

### 4.6 Composite

A recipe or capability whose scientific evidence genuinely crosses
multiple spheres. A composite remains a scaffold until it has its own
steward, joint knowledge, and sufficient validation. An in-sphere
interdisciplinary recipe is not automatically a composite. Examples:

- basin water balance belongs within Hydrosphere;
- coastal compound flooding belongs within Hydrosphere when its
  governing evidence remains in-sphere;
- a sea-level budget that joins multiple sphere authorities may become
  a composite.

### 4.7 Runtime projection

The host-specific package that delivers a canonical capability. Initial
projections: Claude Cowork and OpenAI Codex. A runtime projection is not
the scientific capability itself.

### 4.8 Planned repository

A repository created to make OSP's intended organizational shape
explicit while containing no installable capability. Planned is an
honest status, not a claim of implementation.

## 5. The three orthogonal dimensions

OSP has two scientific and authority axes and one runtime dimension.

### 5.1 Scientific demand: who asks?

```text
Sphere
  +-- Discipline
       +-- Domain capability

Hydrosphere
  +-- Ocean Physics
       +-- ocean-science
```

### 5.2 Authority: who signs?

```text
Provider
  +-- Governed bundle
       +-- Knowledge concepts

NASA
  +-- PO.DAAC
       +-- signed knowledge
```

Provider bundles may support multiple spheres.

### 5.3 Delivery: where does it run?

```text
OSP capability
   +-- Claude Cowork projection
   +-- OpenAI Codex projection
```

Runtime selection does not change the scientific authority model.

## 6. Canonical capability architecture

The canonical OSP capability model remains KNOW + ACT + PROVE + REACH.
These concepts are independent of sphere classification and runtime
delivery.

## 7. KNOW

KNOW contains governed scientific or institutional claims: dataset
characteristics, release compatibility, uncertainty interpretation,
calibration requirements, known traps, expected numerical results,
validated recipes, provider guidance, evidence, provenance, steward
verification, staleness, severity.

Scientific concepts may be used by multiple capabilities and multiple
runtimes. The required rule is:

```text
one concept
one authority
many consumers
```

Knowledge SHALL NOT be copied into Cowork- or Codex-specific content.

## 8. ACT

ACT contains procedural behavior. The canonical representation SHOULD
remain:

```text
skills/<skill-name>/
+-- SKILL.md
+-- references/
+-- scripts/
+-- assets/
```

The normal rule is one canonical `SKILL.md` for a portable workflow.
Avoid `skills/claude/` and `skills/openai/` unless a behavior genuinely
cannot be represented portably.

## 9. Agents versus skills

OSP SHALL use the following rule:

> **Portable scientific behavior MUST have a Skill representation.
> Runtime-specific agents MAY orchestrate Skills but SHALL NOT contain
> the only authoritative implementation of scientific behavior.**

```text
skills/
+-- review-analysis/
    +-- SKILL.md            # canonical workflow

adapters/
+-- claude/
|   +-- agents/
|       +-- reviewer.md     # optional Claude orchestration
+-- openai/
    +-- ...                 # optional OpenAI orchestration
```

This prevents Claude-specific subagent semantics from becoming
scientific architecture.

## 10. PROVE

PROVE contains deterministic assurance: scientific budget closure,
metadata conformance, expected-result checks, schema validation,
provenance checks, reproducibility receipts.

```text
Cowork result -+
               +--> same deterministic verifier --> receipt
Codex result --+
```

A prompt-based "second opinion" is not equivalent to deterministic
PROVE.

## 11. REACH

REACH contains controlled execution surfaces: Earthdata, CMR, PO.DAAC,
STAC, S3, GitHub, processing APIs, local scientific scripts. Prefer MCP
when it is a useful neutral interface.

```text
canonical logical connector
            |
        +---+---+
        v       v
     Claude   OpenAI
     binding  binding
```

Authentication and host registration may differ. Connector meaning
should not.

## 12. Skills instruct; tools execute

OSP should preserve the distinction:

```text
ACT   = how to perform the scientific procedure
REACH = typed, controlled execution surface
```

A Skill may instruct an agent to find a dataset. The actual external
request should occur through a defined execution surface. This allows
permissions, observability, and side-effect controls to remain
explicit.

## 13. Canonical `.osp/` metadata model

The sphere alignment introduces organization-level classification. The
multi-runtime architecture introduces package and runtime metadata.
These SHOULD share a provider-neutral `.osp/` namespace:

```text
.osp/
+-- repository.yaml
+-- governance.yaml
+-- package.yaml       # only when the repository publishes an OSP package
+-- surfaces.yaml      # only when runtime qualification applies
+-- release-lock.json  # generated for releases
```

Not every repository needs every file.

## 14. `.osp/repository.yaml`

`repository.yaml` is the canonical organization-level classification for
every non-archived OSP repository. It exists because sphere and status
metadata applies even to repositories that are planned, provider
knowledge, tooling, foundation, or non-installable.

Example domain capability:

```yaml
schema_version: 1

repository:
  name: ocean-science
  kind: capability
  status: available

classification:
  spheres:
    - hydrosphere
  primary_sphere: hydrosphere
  discipline: Ocean Physics
```

Example precipitation:

```yaml
repository:
  name: precipitation
  kind: capability
  status: planned

classification:
  spheres:
    - hydrosphere
    - atmosphere
  primary_sphere: hydrosphere
  discipline: Precipitation Science
```

Example provider repository:

```yaml
repository:
  name: nasa-daac-knowledge
  kind: provider
  status: available

classification:
  spheres: []
  primary_sphere: null
  discipline: null
```

Example composite:

```yaml
repository:
  name: composites
  kind: composite
  status: planned

classification:
  spheres: []
  primary_sphere: null
  discipline: null
```

Individual composite bundles later declare the spheres they touch.

## 15. Why `repository.yaml` is needed

Sphere metadata cannot live only in `package.yaml` because planned
repositories are intentionally not packages. It also should not live
only in `.claude-plugin/plugin.json` because that would make
Claude-specific packaging authoritative for Codex and organization
governance. Therefore:

```text
.osp/repository.yaml
        |
        +-- GitHub topics
        +-- profile sphere view
        +-- roadmap repository view
        +-- marketplace classification
        +-- Claude metadata
        +-- OpenAI metadata
```

is the source of organization-level truth.

## 16. `.osp/package.yaml`

`package.yaml` exists only for repositories that publish a usable OSP
capability or package. Example (versions illustrative):

```yaml
schema_version: 1

package:
  name: ocean-science
  version: 0.9.0
  type: capability

content:
  skills: ./skills
  verification: ./verification
  connectors: ./connectors

dependencies:
  capabilities:
    - name: core
      version: ">=0.9.0"

  knowledge:
    - name: nasa-daac-knowledge
      version: ">=2026.9.2"
```

The package manifest owns package identity, package version, content
locations, capability dependencies, and knowledge dependencies. It does
not duplicate sphere taxonomy from `repository.yaml`.

## 17. `.osp/surfaces.yaml`

This file declares runtime support and qualification requirements.

```yaml
schema_version: 1

surfaces:
  claude-code:
    role:
      - development
      - runtime
    required: true

  claude-cowork:
    role: runtime
    required: true

  openai-codex:
    role: runtime
    required: true

  claude-science:
    role: future-runtime
    required: false
    status: limited-release

qualification:
  require:
    - install
    - skill-discovery
    - skill-invocation
    - dependency-resolution
    - prove
    - release-lock
```

Only repositories that expose runtime capabilities need this file. A
planned repository MUST NOT have runtime qualification metadata claiming
support.

## 18. `.osp/governance.yaml`

Governance metadata should remain separate from package and
classification metadata. Target conceptual schema:

```yaml
schema_version: 2

repository: ocean-science

maintainers:
  teams:
    - hydrosphere-maintainers
  users: []

runtime_maintainers:
  claude-cowork:
    teams:
      - runtime-cowork-maintainers

  openai-codex:
    teams:
      - runtime-codex-maintainers

reviews:
  ordinary: 1
  cross_repository: org-policy
  knowledge: org-knowledge-policy
  runtime_adapter: org-runtime-policy
```

During the interim solo period, one person may occupy multiple teams and
roles. Enforcing branch and ruleset policies remains deferred until the
governance preconditions are met. The methods-steward type the
architecture document records (an applications office stewarding
recipes and computations rather than products) needs a place in this
schema; the metadata milestone decides its shape.

## 19. OKF concept sphere metadata

Knowledge concept frontmatter gains:

```yaml
spheres:
  - hydrosphere

gcmd:
  - "Terrestrial Hydrosphere > Surface Water"
```

Rules: `spheres` is required for scientific concepts and contains one or
more ESSRP sphere values; `gcmd` remains optional; the linter rejects a
scientific concept with no sphere. Examples:

```text
Ocean-science concept        spheres: [hydrosphere]
Snow concept                 spheres: [hydrosphere, cryosphere]
PO.DAAC GRACE mass concept   spheres: [hydrosphere, geosphere]
```

Concept sphere tags represent the scope of the scientific claim. They do
not transfer steward authority to sphere teams.

## 20. Generated GitHub topics

GitHub topics remain useful for discovery and API queries, but they
SHOULD be generated and validated from `.osp/repository.yaml`:

```text
osp
osp-sphere-<sphere>
osp-kind-<foundation|provider|capability|composite|tooling>
osp-status-<planned|scaffold|developing|available>
```

For repositories touching multiple spheres, multiple `osp-sphere-*`
topics may be applied. `primary_sphere` remains canonical in
`.osp/repository.yaml`. This removes the need to reverse-engineer
canonical state from GitHub topics.

## 21. Generated runtime metadata

Sphere and status classification may be projected into runtime
manifests for discovery. A Claude plugin may receive generated OSP
metadata; an OpenAI or Codex projection may receive equivalent metadata.
Neither becomes canonical.

```text
.osp/repository.yaml
        |
        +-- Claude runtime metadata
        +-- OpenAI runtime metadata
        +-- marketplace catalog
        +-- GitHub topics
```

## 22. Runtime packaging

Runtime-specific packaging is a projection of canonical OSP content.

```text
repository.yaml
package.yaml
surfaces.yaml
skills/
verification/
connectors/
knowledge dependencies
        |
        v
     build-kit
    +------+---------------+
    v                      v
Claude Cowork        Agent Plugin 1.0
                           |
                  standards-compliant clients
```

The baseline architecture has two packaging outputs, not one adapter per
harness: a Claude and Cowork projection, and a standards-compliant Agent
Plugin 1.0 projection.

## 23. Claude Cowork projection

Cowork should continue to receive a Claude plugin package:

```text
.claude-plugin/
+-- plugin.json

skills/
agents/        # optional host-specific orchestration
connectors/    # where applicable
```

Claude-specific content may contain presentation metadata, Cowork
connector registration, subagent wrappers, host commands, and
permission guidance. It may not redefine scientific semantics.

## 24. Agent Plugins 1.0 portable projection

OSP SHOULD adopt Agent Plugins 1.0 as its default provider-neutral
runtime packaging format. The portable package should be generated or
validated from canonical OSP source:

```text
capability/
+-- plugin.json
+-- skills/
|   +-- <skill-name>/
|       +-- SKILL.md
+-- mcp.json              # when portable REACH is present
```

Agent Plugins intentionally represents a smaller portable runtime floor
than the full OSP semantic model:

```text
ACT   -> Agent Skills
REACH -> MCP
```

OSP continues to own the richer semantics: KNOW, PROVE, governance,
dependency semantics, sphere and provider classification, release
identity, surface qualification. Therefore:

```text
OSP semantic model
        |
        v
Agent Plugin 1.0 projection
        |
        +-- Codex / ChatGPT
        +-- Cursor
        +-- GitHub Copilot / VS Code
        +-- Kiro
        +-- other conforming clients
```

OSP SHALL NOT create dedicated adapter trees for clients that can
consume the standards-compliant portable package without semantic loss.

## 25. Codex qualification

Codex remains a first-class OSP qualification target, but it should
preferentially consume the portable Agent Plugin projection rather than
drive a bespoke OpenAI scientific package tree. At minimum,
qualification should prove that one canonical `SKILL.md`, packaged as an
Agent Plugin 1.0 and installed in Codex, preserves Skill discovery,
knowledge dependency resolution, REACH bindings, deterministic PROVE
behavior, and release identity.

OpenAI-specific extension metadata may be generated when required, but
it remains a runtime extension to the portable package rather than a new
OSP source of truth.

## 26. Claude Code

Claude Code remains the primary development environment, the place
where this migration is expected to be implemented, a useful local test
surface, and a consumer of the same portable Skills.

The required Tier-1 end-user qualification targets are Claude Cowork and
OpenAI Codex. Agent Plugin package conformance is also
release-significant because it is the portable distribution contract.

## 27. Distribution tiers

OSP SHOULD distinguish package conformance, release qualification, and
compatibility testing.

- **Canonical layer:** OSP KNOW, ACT, PROVE, REACH. Full OSP governance
  applies.
- **Portable package layer:** Agent Plugins 1.0. Must pass package
  conformance.
- **Tier 1, release-qualified runtimes:** Claude Cowork (the
  Claude-specific projection) and OpenAI Codex (the portable Agent
  Plugin projection).
- **Tier 2, compatibility-tested harnesses:** initially Gemini CLI and
  Goose. Tested periodically and after significant packaging changes;
  failures do not initially block an OSP capability release.
- **Portable consumers, no dedicated adapter:** Cursor, GitHub Copilot
  and VS Code, Kiro, other conforming clients. OSP documents standards
  compatibility without maintaining client-specific scientific package
  trees.

## 28. Why this improves mainstream adoption

The distribution cost changes from N capabilities times N
harness-specific adapters to N capabilities times one portable Agent
Plugin projection plus one Cowork-specific projection. That is a
substantial reduction in maintenance burden while increasing the number
of mainstream clients that can consume OSP.

```text
OSP                 scientific governance + semantics
Agent Plugins 1.0   portable runtime package
Agent Skills        portable procedural unit
MCP                 portable tool and data interface
Harnesses           execution environments
```

## 29. Agent Plugin conformance

build-kit SHOULD validate the generated Agent Plugin against the current
Agent Plugins specification, pinned by version. At minimum:
`plugin.json` schema conformance; Skill discovery and file validity;
`mcp.json` validity when present; package identity consistency with
`.osp/package.yaml`; release-lock consistency; no runtime-specific
scientific duplication.

Agent Plugin conformance is a portable package gate. It is not proof
that every downstream client behaves correctly.

## 30. Gemini CLI compatibility

Gemini CLI SHOULD be a Tier-2 compatibility target because it already
understands the Agent Skills model and can consume Skills and
MCP-oriented extensions with minimal translation. OSP should not create
a Gemini-specific scientific tree. If Gemini consumes Agent Plugins
directly, OSP should use the portable package unchanged. Until then,
compatibility tests may install the canonical Skills and MCP
declarations through Gemini's native mechanisms.

## 31. Goose compatibility

Goose SHOULD be a Tier-2 compatibility target because it is open source,
model-provider neutral, Agent Skills compatible, MCP-centric, and usable
outside a coding IDE. That makes Goose strategically useful for
scientific users who want a local or provider-neutral harness. OSP
should verify that its canonical Skills and REACH interfaces work
correctly in Goose without adding Goose-specific scientific semantics.

## 32. ChatGPT and work path

The portable Agent Plugin projection SHOULD preserve a path to ChatGPT
and ChatGPT Work-like surfaces wherever OpenAI exposes the same plugin,
Skill, and App ecosystem. OSP should not create a separate `chatgpt/`
scientific content tree. This is an adoption path, not a separate
capability architecture.

## 33. No per-harness adapter explosion

The following is an architectural smell:

```text
adapters/
+-- codex/
+-- cursor/
+-- copilot/
+-- vscode/
+-- kiro/
+-- gemini/
+-- goose/
```

The preferred model is a portable Agent Plugin consumed by
standards-compliant clients and compatibility tests, plus a
Claude-specific projection for Cowork. A new dedicated adapter requires
a demonstrated host-specific need that cannot be represented safely
through the portable package.

## 34. Installation and user experience contract

The architecture behind an OSP capability may be sophisticated. The
installation experience SHOULD NOT be. The user-facing product boundary
is the domain capability. A scientist should normally install Ocean
Science, Hydrology, Land Ice, Atmospheric Composition, and so on, rather
than independently assembling core, provider knowledge, attesters,
connectors, individual Skills, and runtime metadata.

The installation contract is:

> **Install one domain capability. Resolve its governed dependencies
> automatically where the host permits it. Keep implementation
> components behind the capability boundary.**

### 34.1 User model versus implementation model

This distinction should appear in the README and architecture
documentation.

User model:

```text
Install "Ocean Science"
         |
         v
     Start working
```

Implementation model:

```text
Ocean Science capability
       |
       +-- classification
       |      +-- sphere: Hydrosphere
       |      +-- discipline: Ocean Physics
       |
       +-- KNOW
       |      +-- nasa-daac-knowledge
       |
       +-- ACT
       |      +-- Agent Skills
       |
       +-- PROVE
       |      +-- deterministic attesters
       |
       +-- REACH
       |      +-- MCP / APIs / tools
       |
       +-- Claude projection
       |      +-- Claude Code / Cowork
       |
       +-- Agent Plugin 1.0 projection
              +-- Codex / standards-compliant clients
```

The implementation model is for maintainers. The user model is the
installation contract.

### 34.2 Claude Code installation

The preferred Claude Code experience is:

```text
/plugin marketplace add open-science-pillars/marketplace
/plugin install ocean-science@open-science-pillars
/reload-plugins
```

The user explicitly selects only the domain capability. OSP's generated
Claude package SHOULD express any dependency relationships that Claude
Code can resolve automatically:

```text
User installs "ocean-science"
        |
        v
Claude projection
        |
        +-- core
        +-- nasa-daac-knowledge
        +-- required PROVE components
        +-- required REACH declarations
        |
        v
Ocean Science ready
```

If the host can resolve a dependency automatically, OSP SHOULD use that
mechanism. If it cannot, OSP SHOULD provide one deterministic
installation path rather than asking the scientist to understand the
internal dependency graph.

### 34.3 Claude runtime choice

After migration, OSP SHOULD present the Claude ecosystem as two
currently supported runtime choices plus one future candidate:

```text
Claude ecosystem
|
+-- Claude Code
|      +-- primary development environment
|      +-- CLI and project workflow
|      +-- supported runtime
|
+-- Claude Cowork
|      +-- graphical, work-oriented workflow
|      +-- supported runtime
|
+-- Claude Science
       +-- future runtime once broadly available
```

The underlying OSP capability is the same. A user choosing Claude Code
versus Cowork is selecting an execution experience, not a different
scientific package. Claude Science SHOULD follow the same rule when it
is added later.

### 34.4 Claude Code project-scoped installation

OSP SHOULD support reproducible project-scoped use. A scientific
repository may declare the OSP marketplace and required plugin
configuration under its Claude project settings:

```text
git clone science-project
          |
          v
Claude Code opens project
          |
          v
project declares OSP requirement
          |
          v
install or enable qualified capability
          |
          v
same scientific workflow + release identity
```

This is useful for reproducible analyses, shared research repositories,
training examples, benchmark fixtures, method papers, and institutional
project templates. Project configuration SHOULD identify the capability
version or release identity where reproducibility requires it.

### 34.5 Claude Cowork individual installation

The preferred Cowork flow is graphical: Customize, Plugins, Add
marketplace, `open-science-pillars/marketplace`, browse Open Science
Pillars, install "Ocean Science". The user should browse scientific
capabilities, not internal implementation packages. Recommended browse
model:

```text
FOUNDATION

Core


HYDROSPHERE

Ocean Science        Install
Hydrology            Install
Precipitation        Planned


CRYOSPHERE

Land Ice             Planned
Sea Ice              Planned
```

Provider knowledge and attestation components SHOULD normally remain
behind the capability boundary.

### 34.6 Cowork organization distribution

Institutional installation has different packaging requirements from an
individual public marketplace install. OSP SHOULD support both:

```text
Public OSP release
        |
        +-- individual Cowork user
        |      +-- public marketplace install
        |
        +-- organization
               +-- qualified plugin ZIP artifact
               +-- private or internal marketplace wrapper
```

build-kit publish SHOULD therefore be capable of producing a versioned
Cowork artifact for each qualified installable capability:

```text
dist/
+-- claude/
|   +-- ocean-science-1.0.0.zip
|   +-- hydrology-1.0.0.zip
|   +-- core-1.0.0.zip
|
+-- agent-plugin/
    +-- ocean-science-1.0.0/
    +-- hydrology-1.0.0/
    +-- core-1.0.0/
```

The organization-specific wrapper, if required by the host, is a
deployment concern. It is not a new scientific package.

### 34.7 Capability boundary

The catalog SHOULD expose user-selectable scientific capabilities
prominently. It SHOULD NOT require users to understand implementation
components such as `nasa-daac-knowledge`, badges, internal attesters,
shared connector packages, or low-level core dependencies, unless those
components are independently useful to expert users.

The default install UX is "Ocean Science, and OSP resolves the
capability graph", not "Core plus NASA DAAC Knowledge plus ECCO verifier
plus Earthdata connector plus Ocean Science Skills".

### 34.8 Planned repositories are never installable

A planned repository may appear in the sphere roadmap, the organization
profile, architecture documentation, and planned capability tables. It
MUST NOT appear as an installable package in Claude Code marketplace
entries, Cowork plugin browse results, Agent Plugin release catalogs, or
Codex install documentation.

### 34.9 Failure behavior

A domain capability MUST fail clearly when a required dependency cannot
be satisfied. Preferred:

```text
Ocean Science cannot be activated.

Missing required dependency:
nasa-daac-knowledge >= 2026.9.2

Suggested action:
install or update the Open Science Pillars dependency set.
```

Not acceptable: silently omitting KNOW; silently skipping PROVE; copying
stale knowledge into the Skill; continuing with reduced semantics
without telling the user.

### 34.10 Installation UX acceptance criteria

A qualified domain capability should satisfy the following checks.

1. A user can identify the capability from its scientific name.
2. A normal install requires one capability-selection action after
   marketplace or source setup.
3. Required dependencies resolve automatically where the host supports
   it.
4. Where automatic dependency resolution is unavailable, OSP provides
   one deterministic guided path.
5. Provider KNOW is not presented as an independent requirement to
   ordinary users.
6. PROVE components are present when required by the capability.
7. REACH setup requests only the permissions and connectors actually
   needed.
8. Planned repositories are visibly non-installable.
9. The installed capability exposes its version and release identity.
10. Cowork and Codex consume equivalent governed capability content.
11. Runtime-specific installation steps do not duplicate the scientific
    workflow.
12. Failure to satisfy a required dependency is explicit.

### 34.11 README quick-start contract

The top-level README SHOULD keep the first installation instructions
short.

Claude Code:

```text
/plugin marketplace add open-science-pillars/marketplace
/plugin install ocean-science@open-science-pillars
```

Claude Cowork:

```text
Customize, Plugins, Add marketplace
Repository: open-science-pillars/marketplace

Then install:
Ocean Science
```

The README may explain KNOW, ACT, PROVE and REACH later. The front door
should remain simple.

### 34.12 Install resolution diagram

This diagram SHOULD be reused in package-authoring and installation
documentation.

```text
                         INSTALL
                           |
                           v
                  "Ocean Science"
                           |
                           v
                 OSP capability graph
                           |
          +----------------+----------------+
          |                |                |
        KNOW              ACT             PROVE
          |                |                |
 nasa-daac-knowledge    Skills          attesters
          |                |                |
          +----------------+----------------+
                           |
                         REACH
                    MCP / APIs / tools
                           |
                           v
                 runtime-ready capability
```

### 34.13 Distribution diagram

This diagram SHOULD appear in the architecture README because it
explains why OSP does not need one adapter per mainstream client.

```text
                     OSP canonical source
                            |
              KNOW + ACT + PROVE + REACH
                            |
                        build-kit
                            |
               +------------+------------+
               |                         |
       Claude projection          Agent Plugin 1.0
               |                         |
        +------+------+       +---------+----------+
        v             v       v         v          v
 Claude Code      Cowork    Codex     Cursor    Copilot /
                                                VS Code
        |                             |
        |                            Kiro
        |
 future:
 Claude Science

Tier-2 compatibility:
Gemini CLI, Goose
```

### 34.14 Scientific organization, authority, and runtime diagram

This diagram SHOULD appear in the architecture and governance
documentation.

```text
      SCIENTIFIC ORGANIZATION          KNOWLEDGE AUTHORITY
             "who asks?"                   "who signs?"
                  |                             |
                  v                             v
        Sphere -> Discipline              Provider bundle
                  |                             |
                  +--------------+--------------+
                                 |
                                 v
                         OSP capability
                                 |
                    KNOW + ACT + PROVE + REACH
                                 |
                                 v
                         runtime projection
                         +-------+--------+
                         v                v
                Claude-family        Agent Plugin 1.0
                   runtime                  |
               +------+------+              v
               v      v      v     standards-compliant clients
             Code   Cowork  Science*
                            *future
```

This diagram is useful because it prevents sphere governance, provider
stewardship, and runtime compatibility from being conflated.

### 34.15 Release and qualification diagram

This diagram SHOULD appear in release documentation.

```text
                   canonical capability
                           |
                           v
                     content valid?
                           |
                           v
                  governance satisfied?
                           |
                           v
                     release lock
                           |
              +------------+------------+
              |                         |
              v                         v
      Cowork projection         Agent Plugin projection
              |                         |
       Cowork qualification      package conformance
                                        |
                                        v
                               Codex qualification
                                        |
                           +------------+------------+
                           v                         v
                  Tier-1 support             Tier-2 probes
                    published              Gemini / Goose
```

Package conformance, runtime qualification, and compatibility testing
are related but different evidence claims.

### 34.16 Reproducible project diagram

This diagram SHOULD be used in tutorial and reproducibility
documentation.

```text
scientific repository
        |
        +-- analysis code / notebooks
        +-- project runtime settings
        +-- OSP capability requirement
                    |
                    v
              qualified capability
                    |
                    v
               release lock
                    |
                    v
          reproducible agent context
```

The goal is not merely reproducible code. It is reproducible agent
capability context: scientific procedure, governed knowledge,
deterministic verification, and tool interfaces tied to an identifiable
release.

## 35. No baseline `upstream/`

OSP has no current demonstrated need for an `upstream/` content tree.
Current relationships (`ocean-science` depending on `core` and
`nasa-daac-knowledge`) are dependencies, not upstream or vendor
relationships. An upstream model should be introduced only when OSP
begins qualifying and redistributing an externally authoritative Skill
or capability.

## 36. Vercel prior art

Vercel remains useful for validating several patterns: Agent Skills are
a practical portable ACT unit; the same Skill source can be consumed by
Claude Code and Codex; generated runtime packaging is preferable to
duplicated source; Skills should instruct while tools provide execution
surfaces; existing Skills tooling can be reused where helpful.

OSP does not adopt as baseline requirements Vercel's `upstream/` layout,
Vercel overlay terminology, skills.sh publication, Vercel indexes, or
Vercel-specific release artifacts. Vercel is precedent, not
architecture.

## 37. Dependency model

Dependencies are declared canonically in `.osp/package.yaml`. The
runtime may realize the graph through native host dependency semantics
when available and verified, a prerequisite package set, or
deterministic assembly of a runtime-specific bundle from separately
governed sources. Generated assemblies are never authoritative.

Prohibited shortcut: copy KNOW or shared Skills into a domain repository
merely to avoid dependency resolution.

## 38. Release lock

Every qualified capability release SHOULD generate
`.osp/release-lock.json`:

```json
{
  "package": "ocean-science",
  "version": "0.9.0",
  "repository_classification_digest": "sha256:...",
  "dependencies": {
    "core": "0.9.0",
    "nasa-daac-knowledge": "2026.9.2"
  },
  "skills_digest": "sha256:...",
  "verification_digest": "sha256:...",
  "connectors_digest": "sha256:...",
  "adapters": {
    "claude-cowork": "sha256:...",
    "openai-codex": "sha256:..."
  }
}
```

This supports the evidence-backed statement that Cowork and Codex
executed runtime projections of the same governed OSP capability
release.

## 39. Governance structure

The combined governance model has four distinct responsibilities:

```text
                         OSP Governance
                              |
          +-------------------+-------------------+
          |                   |                   |
 Repository/Sphere        Knowledge            Runtime
   Maintainers            Stewards           Maintainers
          |                   |                   |
 implementation         scientific          packaging /
 + coordination            trust           qualification
```

Composite review adds cross-sphere participation where required.

## 40. Sphere teams

Create teams under a parent maintainers structure:

```text
foundation-maintainers

hydrosphere-maintainers
cryosphere-maintainers
geosphere-maintainers
atmosphere-maintainers
biosphere-maintainers

composites-maintainers
```

Provider stewardship remains separate:

```text
provider-stewards
+-- podaac-stewards
+-- esdis-stewards
+-- usgs-stewards
+-- ...
```

Runtime packaging authority is orthogonal:

```text
runtime-cowork-maintainers
runtime-agent-plugins-maintainers
runtime-codex-maintainers
```

One person may initially belong to multiple teams. The team structure is
still useful before enforcement because CODEOWNERS and metadata do not
need to change when contributors join later.

## 41. Authority boundaries

**Repository and sphere maintainers** own implementation, roadmap,
repository changes, and sphere coordination. A sphere team coordinates
proposals across its capabilities. Individual repository authority
remains federated.

**Knowledge stewards** own scientific correctness, evidence,
provenance, staleness, high-severity review, and provider approval.
Sphere teams do not override provider stewards.

**Runtime maintainers** own Cowork and Codex packaging, runtime
compatibility, connector binding, permission mapping, and runtime
qualification. Runtime maintainers may reject a package that does not
resolve its required knowledge in Codex. They may not approve a
scientific claim as correct.

## 42. Composite review rule

A composite change that touches multiple spheres requires review
representation from each sphere it touches, subject to the interim
solo-maintainer exception already defined by governance. This is
additional to repository merge authority, knowledge steward review where
knowledge changes, and runtime review where packaging changes.

## 43. CODEOWNERS

CODEOWNERS SHOULD move from individuals to teams:

```text
ocean-science/*
    @open-science-pillars/hydrosphere-maintainers

nasa-daac-knowledge/podaac/*
    @open-science-pillars/podaac-stewards
```

Runtime adapter paths may additionally name the runtime team:

```text
adapters/claude/*
    @open-science-pillars/runtime-cowork-maintainers

plugin.json
    @open-science-pillars/runtime-agent-plugins-maintainers

mcp.json
    @open-science-pillars/runtime-agent-plugins-maintainers
```

Provider path ownership remains precise.

## 44. Target repository map

The sphere-alignment draft described the target as "roughly 22
repositories". When all listed repositories are counted, the consistent
target is **24 non-archived repositories**, plus the archived
`ecco-agent-evals` repository remaining visible after consolidation.
After M5, many of the 24 will still have status planned.

### 44.1 Foundation and tooling (10)

1. marketplace
2. core
3. plugin-template
4. knowledge-template
5. build-kit
6. evals
7. tutorials
8. .github
9. archive-observatory
10. agent-evals, renamed from ecco-agent-evals

### 44.2 Provider knowledge (2)

11. nasa-daac-knowledge
12. partner-knowledge

`nasa-daac-knowledge` initially contains provider directories such as
PO.DAAC and ESDIS, adding other NASA providers when first cited.
`partner-knowledge` is the home for non-NASA stewards such as USGS,
NOAA, OpenET, and future partners.

### 44.3 Hydrosphere (3)

13. ocean-science
14. hydrology
15. precipitation

`precipitation` has Hydrosphere as primary and Atmosphere as a secondary
sphere.

### 44.4 Cryosphere (2)

16. land-ice
17. sea-ice

Snow remains in hydrology with Cryosphere as a secondary sphere where
appropriate.

### 44.5 Geosphere (2)

18. solid-earth
19. land-surface

### 44.6 Atmosphere (2)

20. atmospheric-composition
21. atmospheric-physics

### 44.7 Biosphere (2)

22. land-ecosystems
23. ocean-biology

### 44.8 Cross-sphere (1)

24. composites

Initial scaffold candidates: sea-level-budget; carbon-cycle.

### 44.9 Archived but visible

`ecco-budget-badge`: retired. Its reusable workflow and badge writer
move beside the canonical attester in the provider bundle, and the
repository is archived with a pointer. It does not count toward the 24
non-archived target repositories. (The draft of this document instead
archived `ecco-agent-evals` and kept a generalized `badges`; ADR A
records the decision of 2026-09-12 that reversed both.)

### 44.10 Rows the sphere map does not yet place

The specification's repository table lists `remote-sensing`,
`models-and-reanalysis`, `applied-science`, `planetary-science` and
`pds-knowledge` for later phases. Planetary science has no Earth
sphere; it is pushed off and may belong in another organization, held
on marketplace issue #80. The measurement and applications layers of
the architecture document are layers rather than spheres; the
documentation milestone states where those rows go.

`archive-observatory` sits in the tooling group but is classified on
its own terms rather than by sphere: it serves data engineers and
archive operators, the architecture document's second audience.

The badge repository rename and the eval move the draft described were
decided otherwise on 2026-09-12 (ADR A): the badge repository is
retired, and the benchmark stands alone as `agent-evals`. Where this
document still names `badges` or `evals/products/ecco/`, the decision
record governs.

## 45. Current-to-target repository mapping

| Current repository | Target repository | Action | Sphere or kind | Runtime impact |
|---|---|---|---|---|
| `marketplace` | `marketplace` | Keep | foundation | Becomes provider-neutral catalog and specification; generates runtime views |
| `core` | `core` | Keep | foundation capability | First Cowork and Agent Plugin (Codex) reference package |
| `plugin-template` | `plugin-template` | Keep initially | foundation, template | Becomes multi-runtime capability scaffold |
| `knowledge-template` | `knowledge-template` | Keep | foundation, template | Remains runtime-neutral |
| `build-kit` | `build-kit` | Keep and expand | tooling | Becomes schema validator, renderer, qualifier, lock and publish tooling |
| `evals` | `evals` | Keep and expand | tooling | Absorbs product eval suites and runtime dimensions |
| `tutorials` | `tutorials` | Keep | foundation, docs | Shared workflow plus host-specific setup |
| `.github` | `.github` | Keep and expand | foundation, governance | Sphere teams plus runtime-maintainer policy |
| `archive-observatory` | `archive-observatory` | Keep | tooling, PROVE application | Runtime wrapper only if later useful |
| `nasa-daac-knowledge` | `nasa-daac-knowledge` | Keep | provider | Canonical NASA KNOW |
| `ocean-science` | `ocean-science` | Keep | Hydrosphere capability | Add canonical package and surfaces; generate Cowork and Codex |
| `hydrology` | `hydrology` | Keep | Hydrosphere capability | Same model |
| `ecco-budget-badge` | (archived) | Retire; workflow and badge writer move beside the canonical attester | tooling, PROVE | None |
| `ecco-agent-evals` | `agent-evals` | Rename; ECCO cases in a product subtree; charter kept | tooling, benchmark | Cross-runtime results recorded per tagged set |
| (none) | `partner-knowledge` | Create planned | provider | No runtime package while planned |
| (none) | `precipitation` | Create planned | Hydrosphere capability | No runtime package while planned |
| (none) | `land-ice` | Create planned | Cryosphere capability | No runtime package while planned |
| (none) | `sea-ice` | Create planned | Cryosphere capability | No runtime package while planned |
| (none) | `solid-earth` | Create planned | Geosphere capability | No runtime package while planned |
| (none) | `land-surface` | Create planned | Geosphere capability | No runtime package while planned |
| (none) | `atmospheric-composition` | Create planned | Atmosphere capability | No runtime package while planned |
| (none) | `atmospheric-physics` | Create planned | Atmosphere capability | No runtime package while planned |
| (none) | `land-ecosystems` | Create planned | Biosphere capability | No runtime package while planned |
| (none) | `ocean-biology` | Create planned | Biosphere capability | No runtime package while planned |
| (none) | `composites` | Create planned | cross-sphere composite | No runtime package while planned |

## 46. Content mapping

| Existing content | Target state | Canonical? |
|---|---|---|
| `skills/*/SKILL.md` | Remain | Yes, ACT |
| Skill `references/` | Remain | Yes |
| Skill helper scripts | Remain | Yes when part of ACT |
| Scientific knowledge concepts | Remain in provider or domain KNOW homes | Yes, KNOW |
| Knowledge evidence and provenance | Remain | Yes |
| Verification notebooks and scripts | Remain or consolidate into PROVE packages | Yes, PROVE |
| `ecco-budget-badge` workflow and badge writer | Move beside the canonical attester in the provider bundle; repository archived | Yes, PROVE |
| `ecco-agent-evals` cases | Remain in the repository, renamed `agent-evals`, under a product subtree | Yes, eval contract |
| Claude agents | Runtime orchestration only | No |
| `.claude-plugin/plugin.json` | Generated or validated Cowork projection | No |
| root `plugin.json` | Generated or validated Agent Plugins 1.0 projection | No |
| root `mcp.json` | Generated portable REACH projection when applicable | No |
| OpenAI or Codex extension metadata | Optional standards extension, generated or validated | No |
| GitHub topics | Generated or validated from `repository.yaml` | No |
| Marketplace sphere and status fields | Generated or validated | No |
| `.osp/repository.yaml` | New org classification source | Yes |
| `.osp/package.yaml` | New package and dependency source | Yes |
| `.osp/surfaces.yaml` | New runtime support source | Yes |
| `.osp/governance.yaml` | Extended governance source | Yes |
| `.osp/release-lock.json` | Generated release evidence | Generated |

## 47. Product tooling consolidation

The per-product repository pattern should be retired before new
datasets multiply it.

**Badges.** Retire `ecco-budget-badge` (decided 2026-09-12, ADR A). A
badge is the canonical attester's verdict rendered by shields.io, and
the repository's verbatim copies of the attester are the vendored form
the organization retired elsewhere. The reusable workflow and badge
writer move beside the attester they call, pinned by the provider
bundle's release tag; the repository is archived with a pointer. A
basin-balance badge is the same workflow against hydrology's attester,
not a second repository.

**Evals.** Rename `ecco-agent-evals` to `agent-evals` (decided
2026-09-12, ADR A): the organization's one benchmark repository, its
charter kept, the ECCO cases in a product subtree so later products'
cases join under the same charter. Preserve `concept_basis`, expected
behavior, deterministic checks, and historical result equivalence. The
`evals` repository stays the runner, graders and scoreboard, and gains
the cross-runtime result dimensions.

## 48. Planned repository convention

A planned repository contains `README.md`, `LICENSE`,
`.osp/repository.yaml`, `.osp/governance.yaml`, `CODEOWNERS`, and
appropriate GitHub topics. Its README opens with an explicit banner such
as:

> **Planned. This repository holds no capability yet; it exists so the
> organization's target shape is visible. Nothing here is installable.**

It also documents the intended sphere, discipline and scope, candidate
provider stewards, the Phase-2 gate, and the new-domain-capability issue
template.

A planned repository MUST NOT contain installable `SKILL.md` content,
`.osp/package.yaml`, `.osp/surfaces.yaml` claiming runtime support,
runtime plugin manifests, a marketplace install entry, a release, or a
CITATION.cff for nonexistent scientific work.

Promotion out of planned is governed work. Creation is administrative
unless governance decides otherwise.

## 49. Marketplace and catalog behavior

The catalog should distinguish available, installable capabilities from
planned organization repositories. Planned repositories appear in the
profile sphere view, the roadmap, the marketplace README planned table,
and the specification target map. They do not appear as installable
entries. The installable catalog is generated from canonical OSP
metadata; runtime catalogs are projections from the same source.

## 50. Surface qualification

Compatibility is evidence-backed. Recommended qualification matrix:

| Qualification | Claude Code | Claude Cowork | Codex |
|---|---|---|---|
| Development authoring | Required | N/A | Optional |
| Runtime execution | Required | Required | Required |
| Package and Skill discovery | Required | Required | Required |
| Skill invocation | Required | Required | Required |
| Knowledge resolution | Required | Required | Required |
| Dependency validation | Required | Required | Required |
| Connector invocation | When applicable | When applicable | When applicable |
| Golden computation | Required | Required | Required |
| Deterministic PROVE | Required | Required | Required |
| Receipt generation | Required | Required | Required |
| Side-effect confirmation | Required | Required | Required |
| Release-lock match | Required | Required | Required |

A schema-valid package is not automatically a qualified runtime
package. Claude Science is intentionally excluded from the required
matrix while it remains in limited release. When availability and host
behavior stabilize, it SHOULD be added as another Claude runtime using
the same canonical OSP capability and Claude-family projection wherever
practical.

## 51. Semantic parity, not host parity

These may differ: install flow, marketplace UI, connector
authentication, approval dialogs, subagent implementation, host
commands, presentation metadata.

These must remain equivalent: scientific facts, sphere and provider
attribution, methodology, workflow requirements, uncertainty rules,
deterministic checks, dependency versions, safety requirements.

```text
same capability semantics != identical runtime implementation
```

## 52. build-kit responsibilities

build-kit becomes the implementation center for both migrations.
Conceptual commands: `osp validate`, `osp render`, `osp test`,
`osp qualify`, `osp lock`, `osp publish`, `osp plugin-check`,
`osp compat`, `osp topics`, `osp sphere-view`.

### 52.1 osp validate

Validate `repository.yaml`, `package.yaml`, `surfaces.yaml`, the
governance schema, sphere values, status values, the dependency graph,
Skill structure, OKF sphere tags, knowledge dependencies, and runtime
adapter declarations.

### 52.2 osp render

Generate or validate Claude runtime metadata, the Agent Plugins 1.0
`plugin.json`, portable `mcp.json` when applicable, optional OpenAI
extension metadata, marketplace and catalog projections, the profile
sphere view, planned repository tables, and other generated docs.

### 52.3 osp topics

Compute expected GitHub topics from `repository.yaml`. CI can compare
expected and actual topics.

### 52.4 osp sphere-view

Render the organization by sphere from data. No hand-maintained sphere
list should be needed in the profile README.

### 52.5 osp test

Run structural tests, golden computations, deterministic attesters, eval
fixtures, manifest drift checks, and package consistency tests.

### 52.6 osp qualify

```bash
osp qualify --surface claude-cowork
osp qualify --surface openai-codex
```

### 52.7 osp lock

Generate the release lock.

### 52.8 osp publish

Publish only qualified runtime projections and honest catalog status.
For installable domain capabilities, publication SHOULD be able to emit:

```text
dist/
+-- claude/
|   +-- <capability>-<version>.zip
+-- agent-plugin/
    +-- <capability>-<version>/
```

The exact host packaging may evolve, but publication SHOULD preserve the
one-capability install boundary.

### 52.9 osp plugin-check

Validate Agent Plugins 1.0 conformance: `plugin.json` conformance,
`mcp.json` validity, Skill discovery, portable package identity,
consistency with `.osp/package.yaml`, absence of runtime-specific
scientific duplication.

### 52.10 osp compat

Run non-release-blocking compatibility probes:

```bash
osp compat --surface gemini-cli
osp compat --surface goose
```

Compatibility probes are informative unless a surface is later promoted
to Tier 1.

## 53. Documentation updates required

Documentation migration is part of the architecture work. It is not
cleanup after implementation.

### 53.1 Organization README and profile

The profile README should present the five spheres as the primary
organizing figure. Each sphere lists domain capabilities, status, and
discipline. Provider knowledge repositories appear separately because
they cut across spheres. Planned capabilities are visibly marked
planned. Runtime support is a separate dimension rather than part of the
sphere hierarchy.

### 53.2 Marketplace README

Update positioning from "Claude science plugins" toward governed,
portable scientific capabilities for AI agents. The README should show
available capabilities, planned repositories, provider knowledge,
portable Agent Plugin distribution, and qualified runtimes and
compatibility-tested harnesses.

### 53.3 SPECIFICATION.md

Add: Pillar means sphere; the scientific two-axis model; the runtime
delivery dimension; KNOW, ACT, PROVE, REACH; provider-neutral metadata;
capability versus runtime projection; the composite rule; the planned
repository convention; the runtime qualification model.

### 53.4 GLOSSARY.md

Add or revise: sphere, Pillar, discipline, domain capability, provider
bundle, composite, runtime projection, planned, KNOW, ACT, PROVE, REACH.

### 53.5 Contributor guide

Replace the old implication that portable behavior can live solely in
an agent with: portable scientific behavior MUST have a Skill
representation. Also document where new content belongs:

```text
fact                -> KNOW
procedure           -> ACT
deterministic check -> PROVE
external action     -> REACH
runtime wrapper     -> adapter
```

### 53.6 Steward playbook

Clarify: steward approval is runtime-independent; sphere classification
does not supersede provider authority; packaging-only changes do not
require scientific reapproval unless semantics change; one signed
concept feeds Cowork and Codex.

### 53.7 Governance documentation

Document sphere teams, provider steward teams, runtime maintainer teams,
composite cross-sphere review, the interim solo period, promotion of
planned repositories, and runtime qualification approval.

### 53.8 Surface testing guide

Replace Claude-only assumptions with: development on Claude Code;
required runtime qualification on Claude Cowork and OpenAI Codex.
Document install, Skill, KNOW, dependency, connector, PROVE, and
release-lock tests.

### 53.9 Package authoring guide

Document `.osp/repository.yaml`, `.osp/package.yaml`,
`.osp/surfaces.yaml`, and `.osp/governance.yaml`, with examples for a
standalone capability, a capability dependency, a provider KNOW
dependency, a connector, a PROVE requirement, and a runtime adapter.

### 53.10 Tutorials

Tutorials should have one scientific workflow and separate runtime
setup sections:

```text
ECCO tutorial
+-- scientific objective
+-- canonical workflow
+-- required knowledge
+-- Claude Code setup
+-- Cowork setup
+-- Codex setup
+-- shared PROVE step
```

Do not duplicate the scientific workflow per runtime.

### 53.11 Templates

plugin-template becomes the multi-runtime capability template while
retaining its existing name initially. knowledge-template remains
runtime-neutral. Both gain sphere and status examples. Placeholder
sphere values must fail validation.

### 53.12 build-kit documentation

Document validate, render, topics, sphere-view, test, qualify, lock,
publish, and the generated-files policy.

### 53.13 Terminology audit

| Old or ambiguous wording | Preferred wording |
|---|---|
| Pillar = plugin | Pillar = sphere |
| Claude plugin, when the logical capability is intended | OSP capability |
| domain plugin | domain capability |
| plugin dependency | capability or knowledge dependency |
| Claude surface | runtime surface |
| plugin release | capability release, unless the host artifact is meant |
| agent behavior | Skill behavior, when a portable procedure is meant |

Host-specific documentation may still say Claude plugin when it
literally means a Claude plugin.

### 53.14 Agent Plugins distribution documentation

Documentation SHOULD explain that Agent Plugins 1.0 is the default
portable package projection; `plugin.json` and `mcp.json` are generated
or validated runtime artifacts; Agent Plugins does not replace OSP KNOW,
PROVE, governance, or dependency semantics; Codex is a Tier-1 qualified
consumer of the portable package; Cursor, GitHub Copilot and VS Code,
and Kiro normally require no dedicated OSP adapter; Gemini CLI and Goose
are Tier-2 compatibility targets; a new per-harness adapter requires a
demonstrated host-specific need. The README SHOULD distinguish portable
package conformance, runtime qualification, and compatibility testing.

### 53.15 Architecture decision records

ADR A (sphere and organization alignment) records: Pillar means sphere;
the provider and sphere two-axis scientific model; the repository target
map; the planned repository convention; product-tooling consolidation.

ADR B (multi-runtime capability packaging) records: KNOW, ACT, PROVE,
REACH; Skill as the portable ACT boundary; Cowork and Codex; runtime
projections; no scientific duplication; no baseline upstream model; the
qualification requirement.

The ADRs are linked because they share metadata and migration work, but
keeping the decisions separate makes future reasoning clearer. They live
in `docs/decisions/`.

## 54. Repository-by-repository documentation checklist

| Repository | Required documentation changes |
|---|---|
| `marketplace` | README positioning, sphere map, available and planned tables, integrated specification, glossary, install quick start, Agent Plugin distribution model, runtime support matrix |
| `core` | Canonical ACT explanation, `.osp` metadata, Claude Code, Cowork and Codex install and use, runtime adapter boundary |
| `ocean-science` | Hydrosphere and Ocean Physics identity, dependency docs, shared KNOW and PROVE, runtime qualification |
| `hydrology` | Hydrosphere identity, secondary Cryosphere tagging guidance for snow, dependency and runtime docs |
| `nasa-daac-knowledge` | Provider-authority model, sphere-tagged concepts, runtime-independent stewardship |
| `evals` | Product subtrees; runtime, model and release-lock dimensions |
| `agent-evals` | Benchmark charter, product subtrees, tagged-set result semantics, the pointer from the old name |
| `archive-observatory` | Clarify application and PROVE role and any optional runtime wrappers |
| `build-kit` | Metadata schemas, renderer, Cowork ZIP and package output, Agent Plugin conformance, compatibility probes, topic generation, qualification, release tooling |
| `plugin-template` | Domain capability scaffold, sphere selection, provider dependencies, runtime adapters |
| `knowledge-template` | Required concept spheres, optional GCMD, steward workflow |
| `tutorials` | Sphere-first authoring, project-scoped reproducibility, shared workflow plus host-specific setup |
| `.github` | Sphere teams, provider teams, runtime teams, CODEOWNERS, planned promotion policy |
| planned domain repos | Honest status README, scope, sphere, providers, gate; no install instructions |
| `partner-knowledge` | Provider bundle contribution and steward model |
| `composites` | Scaffold rule, multi-sphere review, promotion criteria |

## 55. Integrated migration plan

The migration has one common foundation and then two coordinated
workstreams.

### M0: decide and record (immediate)

Create the linked ADRs and append the dated Phase-2 pre-registration
amendment. The amendment states that adding sphere metadata,
introducing provider-neutral `.osp` metadata, creating runtime packaging
scaffolding, and instantiating honest planned repositories are
organizational and infrastructure work and do not trigger or pre-empt
the Phase-2 domain gate.

Acceptance: ADR A merged; ADR B merged; dated pre-registration amendment
merged.

### Gate before M1

M1 and later organization changes begin after the first tranche of the
hydrology investigations lands: the roadmap's `hydrology-investigations`
P0 deliverables (`hydro-usgs-waterdata-migration`, `hydro-basin-unit`,
`hydro-p-et-connectors`, `hydro-w1-basin-balance`) recorded done with
evidence. Met 2026-09-12, confirmed by the owner and recorded in the
roadmap; ADR A carries the record.

### M1: canonical metadata schema

The shared foundation for both migrations. Add `.osp/repository.yaml`,
`.osp/package.yaml`, `.osp/surfaces.yaml` as applicable; extend
`.osp/governance.yaml`; add concept-level `spheres`; update
plugin-template, knowledge-template, the catalog schema, the roadmap
schema, and the OKF linter; apply canonical metadata to the existing
repositories; generate and validate GitHub topics from it.

Acceptance: the linter rejects an untagged scientific concept; the
repository schema validates all existing non-archived repos; the sphere
view renders from data; no Claude manifest is required as a source of
sphere truth.

### M2: housekeeping consolidation

Retire `ecco-budget-badge`, moving its workflow and badge writer beside
the canonical attester, and archive it with a pointer. Rename
`ecco-agent-evals` to `agent-evals` with the ECCO cases in a product
subtree.

Acceptance: an adopter's badge still resolves from the attester's
verdict and cannot be hand-set; the renamed benchmark's cases produce
identical results against the last published tagged set and the core
linter reads ocean coverage from the new name; historical links
redirect or clearly resolve.

### M3: governance and teams

Create the foundation team, five sphere teams, the provider steward
hierarchy, the composites team, and the Cowork and Codex runtime
maintainer teams. Rewrite CODEOWNERS to teams. Update governance and
roadmap schemas. Retain the required cross-cutting review window.

Acceptance: every non-archived repository uses team CODEOWNERS;
provider paths map to provider steward teams; the composite review rule
is documented; runtime authority boundaries are documented.

### M4: documentation alignment

Perform the documentation work of the documentation updates and the
repository checklist above.

Acceptance: no orphaned "Pillar means plugin" language; the profile
sphere view renders from canonical metadata; runtime docs distinguish
capability from projection; contributor docs explain KNOW, ACT, PROVE,
REACH.

### M5: instantiate planned repositories

Create `partner-knowledge`, `precipitation`, `land-ice`, `sea-ice`,
`solid-earth`, `land-surface`, `atmospheric-composition`,
`atmospheric-physics`, `land-ecosystems`, `ocean-biology`, and
`composites` per the planned convention.

Acceptance: all have honest banners; all have repository and governance
metadata; all have team CODEOWNERS; all have generated topics; none has
package or runtime manifests; none appears as installable; the roadmap
reports no active domain deliverables.

## 56. Runtime workstream after M1

Runtime work can proceed after the canonical metadata model exists. It
does not need to wait for all planned repositories to be instantiated.

### R1: build-kit runtime renderer skeleton

Implement validation and rendering for the Cowork projection, the
standards-compliant Agent Plugin 1.0 projection, optional OpenAI
extension metadata when required, release locks, and projection drift.
Acceptance: generated runtime metadata derives from canonical OSP
source; CI detects manual drift.

### R2: core reference capability

Use core and one simple Skill to prove that one canonical `SKILL.md`
serves Claude Code, Claude Cowork, and Codex through the Agent Plugin
1.0 projection. Acceptance: discovery works; invocation works; the
shared script and PROVE work; the same release identity is recorded;
Claude Code installs the domain capability through one normal
capability-install action after marketplace setup; Cowork presents the
domain capability rather than internal KNOW and PROVE dependencies.

### R3: dependency reference case

Use `ocean-science` with `core` and `nasa-daac-knowledge` to validate
dependency realization. Acceptance: Cowork resolves required
dependencies; Codex resolves equivalent dependencies; no KNOW
duplication; a missing dependency fails explicitly.

### R4: shared PROVE

Use the ECCO heat budget attester in the provider bundle as the
cross-runtime proof case. Acceptance: Cowork and Codex results feed the same verifier; the
receipt format identifies the capability release.

### R5: cross-runtime evals

Extend evals to record capability, capability version, release lock,
runtime, model, eval suite, trial count, score, confidence interval,
and date. Acceptance: identical scientific cases run against both
runtimes; results are comparable without changing the capability
contract.

### R6: compatibility probes

Add non-release-blocking compatibility checks for Gemini CLI and Goose,
recorded separately from Tier-1 qualification. Acceptance: no dedicated
scientific content is introduced for either harness; failures are
visible but do not block release; successful compatibility can be
documented as tested support.

### R7: release-blocking qualification

After the qualification harness is reliable, a Tier-1 runtime may be
advertised only when it passes:

```text
ocean-science 0.9.0

Claude Cowork: Qualified
OpenAI Codex:  Not Qualified
```

The scientific release remains valid; the unsupported runtime is simply
not advertised.

## 57. Sequencing overview

```text
                        M0
             ADRs + prereg amendment
                         |
           hydrology first-tranche gate
                         |
                         v
                        M1
               canonical metadata
                         |
              +----------+----------+
              |                     |
      organization track       runtime track
              |                     |
             M2                    R1
              |                     |
             M3                    R2
              |                     |
             M4                    R3
              |                     |
             M5                    R4
                                    |
                                   R5
                                    |
                                   R6
                                    |
                                   R7
```

The two tracks share canonical metadata but can otherwise advance
independently.

## 58. Success metrics

**Organization:** all existing non-archived repositories have canonical
classification; the sphere view renders from data; no CODEOWNERS
entries name individuals once team migration is complete; eleven
planned repositories are visible with honest status; no planned
repository is installable; the retired badge repository and the renamed
benchmark leave ECCO results unchanged.

**Scientific governance:** every scientific concept has one or more
sphere tags; provider authority remains path-specific; composite review
rules are enforceable when governance maturity allows.

**Runtime portability:** normal installation is capability-oriented
rather than component-oriented; Claude Code and Cowork quick-start
instructions remain short; required dependencies are hidden or
automatically resolved where host semantics permit; one canonical Skill
executes in Claude Code, Claude Cowork, and through the portable Agent
Plugin path in Codex; the same Agent Plugin package can be consumed by
additional standards-compliant clients without dedicated scientific
adapters; one governed KNOW source feeds all qualified projections; one
PROVE implementation validates Cowork and portable-package executions;
release locks identify equivalent capability releases; Tier-1
qualification and Tier-2 compatibility status are published distinctly.

**Documentation:** a new contributor can answer: What is a Pillar? What
is a domain capability? Where does a scientific fact belong? Who signs
provider knowledge? Which sphere owns a capability? What does a runtime
adapter do? Why are Cowork and Codex not separate scientific trees? What
makes a runtime qualified? Why is a planned repository not installable?
When would an upstream or vendoring model become justified?

## 59. Required architectural invariants

1. Pillar means sphere.
2. Scientific authority and runtime delivery are separate dimensions.
3. One canonical scientific Skill implementation.
4. One canonical copy of every governed scientific claim.
5. Provider stewards retain factual authority across spheres and
   runtimes.
6. Runtime adapters cannot override KNOW.
7. Deterministic PROVE is shared across runtimes.
8. Runtime-specific agents cannot contain unique required scientific
   behavior.
9. OSP dependencies are declared canonically, not inferred from one
   host.
10. GitHub topics and host manifests are projections of canonical
    `.osp` metadata.
11. Planned repositories are not packages.
12. Agent Plugins 1.0 is the default portable runtime projection.
13. No per-harness adapter is added when the portable Agent Plugin is
    sufficient.
14. No Tier-1 runtime support claim without qualification.
15. Tier-2 compatibility is reported separately from release
    qualification.
16. No baseline upstream or vendoring abstraction without a
    demonstrated external-source need.
17. Per-product tooling does not grow one repository per product.
18. Generated runtime projections must be reproducible.
19. The normal installation boundary is the domain capability, not its
    internal KNOW, ACT, PROVE and REACH components.
20. Claude Code is both the primary development environment and a
    qualified runtime; Cowork is the complementary Claude runtime.
21. Claude Science may be added as a runtime without changing canonical
    capability semantics once it is broadly available.

## 60. Recommended Claude Code implementation rules

Add to the workspace development guidance (build-kit's workspace-law
template) when M1 makes the metadata files real:

```markdown
## OSP architecture law

Pillar means an ESSRP sphere.

Scientific organization:
- Sphere and discipline answer who asks.
- Provider bundles answer who signs.
- Runtime adapters answer where the capability runs.

Canonical scientific behavior belongs in `skills/`.
Canonical scientific facts belong in governed knowledge bundles.
Canonical deterministic verification belongs in PROVE implementations.
External action surfaces belong in REACH.

`.osp/repository.yaml` is the source of repository classification and status.
`.osp/package.yaml` is the source of package and dependency semantics.
`.osp/surfaces.yaml` is the source of runtime support policy.
`.osp/governance.yaml` is the source of repository and runtime governance.

Claude package files and the Agent Plugins `plugin.json` and `mcp.json`
files are projections.

Do not:
- introduce provider-specific scientific behavior;
- put unique scientific behavior in a runtime agent;
- duplicate KNOW into a Skill to solve packaging;
- vendor another OSP repository to solve a dependency;
- hand-maintain GitHub topics that should be rendered from canonical metadata;
- make a planned repository installable;
- add a dedicated harness adapter when Agent Plugins 1.0 is sufficient;
- introduce an upstream model without a concrete external-source case.

Every runtime advertised as supported must pass qualification.
Claude Code is both a development environment and a runtime.
Claude Science remains a future runtime candidate until broad
availability and qualification are practical.
```

## 61. Open questions

### 61.1 External provider stewards

Should external DAAC and provider staff become organization members in
steward child teams or remain outside collaborators? This remains the
main governance question before team enforcement.

### 61.2 GCMD

Should GCMD remain optional or become required for dataset concepts?
Recommendation: keep optional until a concrete discovery or recipe
requirement demonstrates the value.

### 61.3 IMERG transition

Between now and the future precipitation capability, the recommended
transition remains: the connector and Skill may stay in hydrology;
provider knowledge belongs in the appropriate provider bundle from the
start; later move procedural ACT without migrating knowledge authority.

### 61.4 Planned repository review window

Recommendation: creation of an honest planned repository is
administrative; promotion out of planned is governed and cross-cutting.

### 61.5 Runtime team membership during the solo period

The same maintainer may occupy both runtime teams initially. Do not
enable enforcement that makes the repository unmaintainable during the
documented solo period.

## 62. Non-goals

This migration does not: rename the Open Science Pillars organization;
rename `ocean-science` or `hydrology`; build the planned scientific
capabilities; weaken the Phase-2 gate; claim planned work is complete;
adopt GCMD as the primary taxonomy; merge the organization into a
monorepo; make Claude Code, Cowork, Claude Science, and Codex identical;
duplicate scientific content by runtime; require Vercel infrastructure;
maintain separate Cursor, Copilot, VS Code, Kiro, Gemini, or Goose
scientific trees; require an upstream content model; replace provider
stewardship with sphere governance.

## 63. Final decision summary

```text
                           OPEN SCIENCE PILLARS
                                    |
                      Pillars = ESSRP Spheres
                                    |
            +-----------------------+-----------------------+
            |                                               |
    Sphere / Discipline                              Provider Authority
       "who asks?"                                    "who signs?"
            |                                               |
            +-----------------------+-----------------------+
                                    |
                          Governed Capability
                                    |
              +---------------------+---------------------+
              |                     |                     |
            KNOW                   ACT                  PROVE
              |                     |                     |
              +---------------------+---------------------+
                                    |
                                  REACH
                                    |
                                    v
                             runtime packaging
                         +----------+----------+
                         v                     v
                 Claude family         Agent Plugin 1.0
                 +-----+-----+               |
                 v     v     v               |
               Code  Cowork Science*         |
                          *future            |
                              +-------------+-------------+
                              v             v             v
                            Codex         Cursor       Copilot /
                                                       VS Code
                                            |
                                           Kiro
```

The repository reorganization and runtime packaging work should
therefore be treated as one architecture alignment with two coordinated
implementation tracks. The sphere migration gives OSP a durable
scientific organization. The capability model gives OSP a durable
semantic boundary. The Claude-family projection and standards-compliant
Agent Plugin projection let OSP deliver that capability broadly without
forking it.

The combined governing principle is:

> **Organize by sphere. Govern by authority. Author capabilities once.
> Package to the standard. Qualify the runtimes that matter.**

## Appendix A: target repository count

```text
Foundation and tooling   10
Provider knowledge        2
Domain capabilities      11
Cross-sphere composites   1
                         --
Non-archived total       24

Archived:
ecco-budget-badge         1

GitHub-visible total     25
```

This corrects the earlier "roughly 22" description while preserving the
exact repository scopes from the sphere-alignment plan.

## Appendix B: planned domain scopes

**Hydrosphere.** `precipitation`: GPM, IMERG, GHRC lightning where
relevant. Primary sphere Hydrosphere, secondary Atmosphere.

**Cryosphere.** `land-ice`: ICESat-2, GRACE and GRACE-FO ice mass,
ITS_LIVE, NISAR. `sea-ice`: NSIDC sea-ice indices, ICESat-2 freeboard,
ECCO sea-ice field groups.

**Geosphere.** `solid-earth`: NISAR, ARIA, OPERA displacement, GRACE mass
and GIA, CDDIS geodesy. `land-surface`: OPERA DIST, landslides, LP DAAC
land cover.

**Atmosphere.** `atmospheric-composition`: TEMPO, OMI, MLS, OCO.
`atmospheric-physics`: MERRA-2, CERES, AIRS, CloudSat, CALIPSO.

**Biosphere.** `land-ecosystems`: MODIS and VIIRS vegetation, GEDI,
ECOSTRESS, OCO flux. `ocean-biology`: PACE OCI, ocean color, ECCO-Darwin.

**Cross-sphere.** `composites`: initial scaffold candidates
sea-level-budget and carbon-cycle.

## Appendix C: integrated roadmap shape

Rather than making the sphere and runtime efforts unrelated roadmap
initiatives, one umbrella architecture initiative with two workstreams
is used: `osp-architecture-alignment` in build-kit's roadmap, with
deliverables `m0-decision-records`, `m0-prereg-amendment`,
`m1-canonical-metadata`, `m1-concept-spheres`, `m1-templates`,
`m2-badges-consolidation`, `m2-evals-consolidation`,
`m3-governance-teams`, `m4-documentation-alignment`,
`m5-planned-repositories`, `r1-runtime-renderer`, `r2-core-reference`,
`r3-dependency-reference`, `r4-shared-prove`, `r5-cross-runtime-evals`,
`r6-compat-probes`, `r7-release-qualification`. This preserves the
original sphere sequencing while avoiding two independent metadata
migrations.

## Appendix D: documentation acceptance test

The documentation migration is complete when the repository
documentation alone makes all of the following clear:

```text
Pillar -> sphere
Sphere + discipline -> scientific organization
Provider bundle -> knowledge authority
KNOW + ACT + PROVE + REACH -> capability semantics
Cowork / Codex -> runtime projections
planned -> visible but non-installable
qualified -> runtime support backed by evidence
installable capability -> one user-facing capability boundary
```

## Appendix E: relevant prior art and source context

**Sphere frame.** NASA's Earth System Science Research Program and its
sphere organization were the basis of the sphere-alignment proposal.

**Open Science Pillars.** The design is grounded in the current OSP
repositories, governance model, steward model, skills, knowledge
bundles, evals, and deterministic attestation work.

**Agent Skills and Vercel.** Vercel's work demonstrates that standard
Agent Skills can be consumed across agent environments and that
generated host packaging is practical. OSP does not adopt
Vercel-specific upstream or distribution structures without a
demonstrated need.

**Agent Plugins 1.0.** The preferred portable distribution standard for
OSP runtime packaging (github.com/agentplugins/agent-plugins-spec,
version 1.0.0 published 2026-08-06, maintained by a technical steering
committee from Amazon, Cursor, Microsoft, OpenAI and Vercel). It
provides the standards layer through which OSP can expose Agent Skills
and MCP-based REACH capabilities to multiple mainstream harnesses
without maintaining separate adapters for each. OSP retains its richer
`.osp/` semantics above the portable package.

**Anthropic.** Claude Cowork plugin and Skill support inform the Claude
runtime projection.

# Package authoring guide: the `.osp/` files

What a repository declares about itself, and how the runtime packages
follow from it. The schemas, the validator and the commands are
documented in build-kit's `docs/osp-metadata.md`; this guide is the
worked examples. Every plugin, template and bundle gate runs
`osp.py validate`, so a manifest that disagrees with these files fails
the pull request.

## A standalone capability

`.osp/repository.yaml` says what the repository is and where it sits:

```yaml
schema_version: 1
repository:
  name: ocean-science
  kind: capability           # foundation | provider | capability | composite | tooling
  status: available          # planned | scaffold | developing | available
classification:
  spheres: [hydrosphere]
  primary_sphere: hydrosphere
  discipline: Ocean Physics
```

`.osp/package.yaml` says what it publishes. The Claude manifest
(`.claude-plugin/plugin.json`) must repeat the name, version and
dependencies exactly; it is a projection:

```yaml
schema_version: 1
package:
  name: ocean-science
  version: 0.8.2
  type: capability
content:
  skills: ./skills
  knowledge: ./knowledge
  verification: ./verification
dependencies:
  capabilities: []
  knowledge: []
```

## A capability dependency

Every domain capability depends on the foundation. A floor is stated
where the capability needs a feature that arrived at a version:

```yaml
dependencies:
  capabilities:
    - {name: core, version: ">=0.5.0"}
```

## A provider knowledge dependency

Provider facts are consulted, never copied. The bundle is declared with
a version floor, and the installer brings it in with the capability:

```yaml
dependencies:
  knowledge:
    - {name: nasa-daac-knowledge, version: ">=2026.9.3"}
```

Skills cite a provider concept by bundle path
(`knowledge/podaac/<type>/<concept>.md`); core's consult-knowledge
convention finds every installed bundle through the installer's record.

## A connector

A connector is REACH: the registration wire in `.mcp.json` and nothing
more. Its facts (endpoint, transport, tool surface, auth boundary,
deprecation) are KNOW, a `connector` concept in the bundle; when to
reach for it is ACT, in the skills; gates never depend on one. Declare
the directory in `content.connectors` when the repository carries one.

## A PROVE requirement

Golden notebooks under `verification/` test the repository's own
computations in CI; an attested computation's attester verifies anyone's
run from a receipt. Declare `content.verification`; the surfaces file
lists `prove` and `receipt` among the qualification a release must pass.

## Runtime surfaces

`.osp/surfaces.yaml` is policy plus evidence:

```yaml
schema_version: 1
surfaces:
  claude-code:    {role: [development, runtime], required: true, status: supported}
  claude-cowork:  {role: runtime, required: true, status: tested}
  openai-codex:   {role: runtime, required: true, status: planned}
  claude-science: {role: future-runtime, required: false, status: limited-release}
qualification:
  require: [install, skill-discovery, skill-invocation, knowledge-resolution,
            dependency-resolution, golden-computation, prove, receipt, release-lock]
```

`required` is what a release must qualify on before it advertises the
surface; `status` is the evidence today, with an `evidence` string
saying where it is recorded.

## A runtime adapter

The Claude package files are the Cowork projection and are owned by the
runtime maintainers (CODEOWNERS). A runtime-specific agent under
`agents/` may orchestrate skills; it never holds the only implementation
of scientific behavior, which lives in `skills/` as a `SKILL.md`. No
`skills/claude/` or `skills/openai/` trees.

## Governance

`.osp/governance.yaml` names the owning team, the runtime maintainer
teams and the review policy; the teams come from build-kit's
`osp/teams.yaml`, and CODEOWNERS names the same teams. Accepting a
maintainer or a steward is a team membership change.

## Templates

A plugin copied from plugin-template fails validation until
`repository.name` (and `package.name`) are changed from the template's
names; a bundle copied from knowledge-template likewise. That is the
placeholder check, on purpose.

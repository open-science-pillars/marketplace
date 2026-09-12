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
(`.claude-plugin/plugin.json`) and the Agent Plugins `plugin.json` are
rendered from it by build-kit's `osp.py render`, and the gate fails
when either differs from what the file renders:

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
metadata:
  description: "Physical oceanography: ECCO state estimate, SWOT SSH, ..."
  keywords: [oceanography, ecco, swot]
```

`metadata` is what every manifest repeats: the description and keywords,
and, unless overridden, the organization's author, the GitHub homepage
and repository, and the Apache 2.0 license. After an edit, run
`uv run ../build-kit/scripts/osp.py render .` and commit the four
rendered files with it.

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

A connector is REACH: a registration and nothing more. It is declared
once, in `package.yaml`, in the portable form of the Agent Plugins
specification, and both wires are rendered from it: Claude's
`.mcp.json` (with `${CLAUDE_PLUGIN_ROOT}` and `http`) and the portable
`mcp.json` (with `${PLUGIN_ROOT}` and `streamable-http`):

```yaml
reach:
  servers:
    earthdata:
      type: streamable-http
      url: https://cmr.earthdata.nasa.gov/mcp/v1
    observations:
      type: stdio
      command: uv
      args: [run, "${PLUGIN_ROOT}/connectors/observations_mcp.py"]
```

A server that only a Claude runtime can use carries `portable: false`
and is left out of the portable file. Its facts (endpoint, transport,
tool surface, auth boundary, deprecation) are KNOW, a `connector`
concept in the bundle; when to reach for it is ACT, in the skills;
gates never depend on one. Declare the directory in `content.connectors`
when the repository carries one.

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

## The portable package

The repository root is itself the Agent Plugins package: `plugin.json`
rendered beside the canonical `skills/`, and `mcp.json` when there is
portable REACH. `osp.py plugin-check` validates it against the
specification pinned at 1.0.0 (the closed manifest, the executable-token
rule, the URL rules, skill discovery and the Agent Skills frontmatter
rules) in every package gate. Conformance is a package property; it
says nothing about qualification on a runtime. A client extension
(an OpenAI or Codex namespace, when one is documented) is declared under
`extensions` in `package.yaml` and copied through.

## The release lock

`osp.py lock` writes `.osp/release-lock.json`: digests of the
classification, each content tree and each projection, the declared
dependency constraints and the Agent Plugins version. It is reported on
a pull request and enforced on a release tag, so a release commit
re-runs `lock` after its version bump.

## A runtime adapter

The Claude package files are the Cowork projection and are owned by the
runtime maintainers (CODEOWNERS); the portable files and the lock belong
to the Agent Plugins runtime maintainers. A runtime-specific agent under
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

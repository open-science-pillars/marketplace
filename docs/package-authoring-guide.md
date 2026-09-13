# Package authoring guide: the `.osp/` files

What a repository declares about itself, and how the runtime packages
follow from it. The schemas, the validator and the commands are
documented in build-kit's `docs/osp-metadata.md`; this guide is the
worked examples. Every plugin, template and bundle gate runs
`osp.py validate`, so a manifest that disagrees with these files fails
the pull request. A new capability starts from
[plugin-template](https://github.com/open-science-pillars/plugin-template),
which carries every file below with placeholder names.

Every command in this guide is run from the workspace root, with the
capability and build-kit checked out side by side:
`uv run build-kit/scripts/osp.py <command> <capability>` (or `.` from
inside the capability, as the gates do).

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

`.osp/package.yaml` says what it publishes. The four rendered files
(below) come from it, and the gate fails when any of them differs from
what the file renders:

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
and repository, and the Apache 2.0 license. Declare `content.agents`,
`content.connectors` and `content.evals` when the repository carries
them. After an edit, run `uv run build-kit/scripts/osp.py render
ocean-science` and commit the rendered files with it. The version in
`package.yaml` and the version in `CITATION.cff` move together; the
release tool sets both, and the validator reads them.

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
concept in the bundle, verified against the provider's live repository
at authoring time and re-verified at each steward sweep; when to reach
for it is ACT, in the skills; gates never depend on one. Declare the
directory in `content.connectors` when the repository carries a server
of its own.

The user-facing disclosure is `CONNECTORS.md` at the repository root:
for each server, what it is, what leaves the user's machine, what does
not go through it (downloads never do), what happens when it is
unavailable (the named fallback; degradation is always said out loud,
never silent), and where its facts are maintained. It does not restate
the facts, so there is one place to correct them. Credentials never
appear in any repository: an Earthdata Login lives in the environment,
in `~/.netrc` or in connector configuration, and is needed only for
downloads.

## A PROVE requirement

Golden notebooks under `verification/` test the repository's own
computations in CI; an attested computation's attester verifies anyone's
run from a receipt. Declare `content.verification`; the surfaces file
lists `prove` and `receipt` among the qualification a release must pass,
and its `probes` block names the reference computation.

## Runtime surfaces

`.osp/surfaces.yaml` is policy plus evidence plus the probes the
qualification uses. For a new capability every runtime status starts at
`planned`; Claude Code moves to `supported` on its first qualified
record. The full `require` list is the eleven tests
[runtime-distribution.md](runtime-distribution.md) defines:

```yaml
schema_version: 1
surfaces:
  claude-code:    {role: [development, runtime], required: true, status: planned}
  claude-cowork:  {role: runtime, required: true, status: planned}
  openai-codex:   {role: runtime, required: true, status: planned}
  claude-science: {role: future-runtime, required: false, status: limited-release}
qualification:
  require: [install, skill-discovery, skill-invocation, knowledge-resolution,
            dependency-resolution, connector-invocation, side-effect-confirmation,
            golden-computation, prove, receipt, release-lock]
probes:
  skill-invocation:
    skill: start
    prompt: What science tools do I have set up here, and what should I do next?
    expect: [core]
  prove:
    prompt: "Run the capability's attested reference computation on its synthetic fixture and report the headline it prints. The command is: uv run ${PLUGIN_ROOT}/verification/trend_computation.py --runtime ${RUNTIME} --out ${WORK}/receipt.json"
    receipt: ${WORK}/receipt.json
    command: [uv, run, "${PLUGIN_ROOT}/verification/trend_attester.py", "${WORK}/receipt.json", --out, "${WORK}/attestation.json"]
    attestation: ${WORK}/attestation.json
  golden-computation:
    - verification/analysis_pipeline.py
```

`required` is what a release must qualify on before it advertises the
runtime; `status` is the evidence today, with an `evidence` string
saying where it is recorded. `probes` fixes the reference skill and the
prompts the conversational tests use, verbatim on every runtime, the
golden scripts to run, and the prove probe: the prompt that has the
runtime run the executor and write the receipt, the attester command
and the attestation path, with `${PLUGIN_ROOT}`, `${WORK}` and
`${RUNTIME}` substituted. Qualification records land under
`.osp/qualification/<runtime>.json`, one per runtime, written by
build-kit's `scripts/qualify.py`; a record never edits `surfaces.yaml`.

## The rendered projections

`osp.py render` writes four files from `package.yaml` and
`repository.yaml`:

| File | Projection |
|---|---|
| `.claude-plugin/plugin.json` | Claude (Claude Code, Cowork): name, version, description, dependencies, author, homepage, license, keywords |
| `.mcp.json` | Claude: every declared server, in Claude's spelling |
| `plugin.json` | Agent Plugins 1.0.0, at the repository root: the closed portable fields, and the organization's classification and dependencies under `extensions` |
| `mcp.json` | Agent Plugins 1.0.0: the portable servers only; absent when there are none |

The repository root is therefore itself the Agent Plugins package:
`plugin.json` beside the canonical `skills/`, and `mcp.json` when there
is portable REACH. `osp.py plugin-check` validates it against the
specification pinned at 1.0.0 (the closed manifest, the
executable-token rule, the URL rules, skill discovery and the Agent
Skills frontmatter rules) in every package gate. Conformance is a
package property; it says nothing about qualification on a runtime. A
client extension (an OpenAI or Codex namespace, when one is documented)
is declared under `extensions` in `package.yaml` and copied through.

## The README's runtime table

The README carries the runtime table between `osp-runtimes` markers:

```markdown
<!-- osp-runtimes:start -->
...
<!-- osp-runtimes:end -->
```

`osp.py advertise <capability> --into README.md` renders it from
`surfaces.yaml` and the qualification records, and the gate's
`advertise --check --into README.md` fails when the table is out of
date or when a runtime says supported without a qualified record. Edit
the files, never the block.

## The release lock

`osp.py lock` writes `.osp/release-lock.json`: digests of the
classification, each content tree and each projection, the declared
dependency constraints and the Agent Plugins version. It is reported on
a pull request and enforced on a release tag, so a release commit
re-runs `lock` after its version bump. A qualification record names
the lock it was run against.

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
maintainer or a steward is a team membership change. During the
interim period one person occupies every team, recorded as
`status: interim`:

```yaml
schema_version: 2
repository: hydrology
maintainers:
  users: [PaulMRamirez]
  teams: [hydrosphere-maintainers]
  status: interim
runtime_maintainers:
  claude-cowork:
    users: [PaulMRamirez]
    teams: [runtime-cowork-maintainers]
    status: interim
  openai-codex:
    users: [PaulMRamirez]
    teams: [runtime-codex-maintainers]
    status: interim
  agent-plugins:
    users: [PaulMRamirez]
    teams: [runtime-agent-plugins-maintainers]
    status: interim
roadmap:
  proposals: enabled
  authority: repository-maintainers
reviews:
  ordinary: 1
  cross_repository: org-policy
  knowledge: org-knowledge-policy
  runtime_adapter: org-runtime-policy
```

## Templates

A plugin copied from plugin-template fails validation until
`repository.name` (and `package.name`) are changed from the template's
names; a bundle copied from knowledge-template likewise. That is the
placeholder check, on purpose.

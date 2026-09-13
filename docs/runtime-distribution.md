# Runtimes and distribution

How one governed capability reaches the runtime you use, and what each
support word asserts. The decision is ADR B
([decisions/](decisions/README.md)); the current model is
[MODEL.md](MODEL.md); the maintainers' procedure is the
[release qualification guide](release-qualification-guide.md).

## Five words, five claims

| Word | What it asserts | Evidence |
|---|---|---|
| **Supported** | A release passed every required qualification test on the runtime, on a record for the exact version and release lock | `.osp/qualification/<runtime>.json`, written by build-kit's `scripts/qualify.py` |
| **Tested** | An install from this marketplace was verified; whether a given release is qualified is decided per release | the dated install verification, then a record or a waiver per release |
| **Planned** | The runtime is required and the package that serves it is rendered and conformance-checked; no release is qualified on it | `osp.py plugin-check` in every package gate |
| **Future runtime** | Outside the required matrix; nothing is claimed and no install path is documented | none |
| **Compatibility target** | Probed and reported on; a failure never blocks a release | a compatibility report |

A schema-valid package is not a supported runtime. Package conformance
(the portable package validates against the Agent Plugins specification
pinned at 1.0.0) is a property of the package and says nothing about any
client's behavior.

## Status today (2026-09-13)

| Runtime | Role | Status |
|---|---|---|
| Claude Code | development environment and required runtime | supported: every release is exercised on it; core 0.5.1 carries a qualified record |
| Claude Cowork | required runtime | tested: marketplace install verified 2026-07-04; no release qualified on it yet |
| OpenAI Codex | required runtime, through the Agent Plugins package | planned: the package is rendered and conformance-checked; no release qualified on it yet |
| Claude Science | future runtime | outside the required matrix |
| Gemini CLI, Goose | compatibility targets | not yet probed |
| Cursor, GitHub Copilot and VS Code, Kiro | portable consumers | served by the Agent Plugins package with no dedicated adapter; standards compatibility, not qualified runtimes |

Each installable repository declares this policy in `.osp/surfaces.yaml`:
`required` is what a release must qualify on before it advertises the
runtime; `status` is the evidence today.

## The qualification tests

A release is qualified on a runtime when every test its surfaces file
requires is pass or skip. The list, in the order a record carries them:

1. **install**: one action after the marketplace is added; the declared
   dependencies resolve.
2. **skill-discovery**: the runtime's inventory lists every skill in the
   capability's `skills/` directory.
3. **skill-invocation**: the reference skill fires from its prompt,
   conversationally, uncoached (the slash form as well on Claude Code).
4. **knowledge-resolution**: a skill cites an installed concept by
   bundle path, with its status.
5. **dependency-resolution**: installed dependencies are at or above
   their floors; a missing one fails naming the floor.
6. **connector-invocation**: each declared server is registered and
   reachable, or explicit about why not.
7. **side-effect-confirmation**: the download and file-write gates appear
   before anything is fetched or written.
8. **golden-computation**: the golden scripts run green from the
   installed tree.
9. **prove**: the runtime runs the attested reference computation and
   writes a receipt; the attester passes on it.
10. **receipt**: the attestation says PASS and names the installed
    version, the release lock and the runtime.
11. **release-lock**: the installed tree carries the lock at the
    installed version with the digest the catalog names.

The harness is build-kit's `scripts/qualify.py`. It drives Claude Code
headlessly and writes one record per runtime under the capability's
`.osp/qualification/`. A runtime it cannot drive (Cowork; Codex until
its leg is exercised) gets a checklist with the same prompts verbatim,
and the filled checklist becomes the record. `blocked` marks a test the
runtime cannot perform, and a blocked test means not qualified. The
prompts and the reference skill come from the `probes` block of
`surfaces.yaml`, so every runtime is asked exactly the same thing.

## One capability, two projections

A capability is authored once, and build-kit's `osp.py render` writes
both runtime packages from `.osp/package.yaml`: the Claude projection
(`.claude-plugin/plugin.json`, `.mcp.json`), the plugin Claude Code and
Claude Cowork install from this marketplace, and the Agent Plugins
projection (`plugin.json`, `mcp.json` at the repository root beside the
canonical `skills/`), the package OpenAI Codex and other conforming
clients consume. A connector is declared once, in the portable form, and
both wires are rendered from it. `render --check` fails a gate on a hand
edit and `plugin-check` validates the portable package; neither says
anything about qualification. No client gets a dedicated adapter when
the portable package serves it without semantic loss.

## How a status is decided

A runtime may say `supported` in `surfaces.yaml` only on a qualified
record for the exact version and release lock, written by
`qualify.py`. Claude Code, the development environment, is supported by
construction and its record is evidence when present; a future or
compatibility runtime is outside the required matrix. Every package gate
runs `osp.py advertise --check`, which fails a support claim without
such a record and keeps the README's runtime table current. On a
release candidate every required runtime needs a decision for that
version: a record, qualified or not, or a waiver. A waived runtime is
not advertised for that release and stays at `tested` or `planned`; the
waiver is for one version, and the next candidate asks again.

## Semantic parity, not host parity

Install flow, connector authentication, approval dialogs, subagent
implementation and presentation may differ between runtimes. Scientific
facts, attribution, methodology, uncertainty rules, deterministic
checks, dependency versions and safety requirements may not: one signed
concept feeds every projection, and one attester checks every runtime's
result.

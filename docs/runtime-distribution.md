# Runtimes and distribution

How one governed capability reaches the runtime you use, and what each
support word means. The decision is ADR B (`decisions/`); the design is
`design-sphere-alignment-multi-runtime.md`.

## One capability, two projections

A capability is authored once: its skills (ACT), the knowledge it
consults (KNOW), its deterministic verification (PROVE) and its
connectors (REACH). The canonical metadata lives under `.osp/` in each
repository (build-kit's `docs/osp-metadata.md`). Runtime packaging is a
projection of that source, rendered by build-kit, never the other way
round:

- **The Claude projection**: the plugin package (`.claude-plugin/plugin.json`,
  `.mcp.json`) that Claude Code and Claude Cowork install from this
  marketplace. It exists today and is what every release ships.
- **The Agent Plugins 1.0 projection**: a standards-compliant package
  (`plugin.json`, `skills/`, `mcp.json`) per the open specification at
  github.com/agentplugins/agent-plugins-spec, consumed by OpenAI Codex
  and by other conforming clients (Cursor, GitHub Copilot and VS Code,
  Kiro). It is rendered by build-kit's `osp.py render` from the same
  `.osp/package.yaml`, at the repository root (`plugin.json`, the
  canonical `skills/`, `mcp.json`), and checked for conformance by
  `osp.py plugin-check` in every package gate. Rendered is not
  qualified: no runtime has yet passed the qualification matrix on it.

No client gets a dedicated adapter when the portable package serves it
without semantic loss; a new adapter needs a demonstrated host-specific
need.

## Four words, four claims

| Word | What it asserts | Evidence |
|---|---|---|
| Development environment | Where the capabilities are authored and tested | Claude Code |
| Qualified runtime (Tier 1) | A release passed the qualification matrix on it: install, skill discovery and invocation, knowledge and dependency resolution, connector invocation where applicable, golden computation, deterministic PROVE, receipt generation, side-effect confirmation, release-lock match | Recorded per release once the qualification harness lands |
| Package conformance | The portable package validates against the pinned Agent Plugins specification | `osp.py plugin-check`, pinned at Agent Plugins 1.0.0, in every package gate |
| Compatibility tested (Tier 2) | The canonical skills and connectors were probed on a harness; failures are reported and do not block a release | `osp compat`, when it lands |

A schema-valid package is not a qualified runtime. A release stays valid
when a runtime fails qualification; that runtime is simply not
advertised for it.

## Status today (2026-09-12)

| Runtime | Role | Status |
|---|---|---|
| Claude Code | development environment and runtime | supported: every release is exercised on it |
| Claude Cowork | runtime | tested: marketplace install verified 2026-07-04 (surface testing guide); per-release qualification pending the harness |
| OpenAI Codex | runtime, through the Agent Plugins projection | planned: the projection is rendered and conformance-checked; no release has been qualified on Codex |
| Claude Science | future runtime | limited release; install path observed 2026-07-04; excluded from the required matrix until broadly available |
| Gemini CLI, Goose | compatibility targets | not yet probed |
| Cursor, GitHub Copilot and VS Code, Kiro | portable consumers | no dedicated adapter; served by the Agent Plugins projection, as standards compatibility, not as qualified runtimes |

Each installable repository declares this policy in
`.osp/surfaces.yaml`: `required` is what a release must qualify on before
it advertises the surface; `status` is the evidence today.

## How a status is decided

A surface may say `supported` only on a qualified record for the exact
version and release lock, written by build-kit's qualification harness
(`scripts/qualify.py`) under the repository's `.osp/qualification/`.
Claude Code, the development environment, is supported by construction
and its record is evidence when present; a future or compatibility
runtime is outside the required matrix. Every package gate runs
`osp.py advertise --check`, which fails a support claim without such a
record and keeps the README's runtime table (rendered from the same
records) current; `osp.py publish` refuses an unclean release and emits
the Agent Plugins package only when a runtime that consumes it is
qualified, with the honest status per runtime beside it in
`release.json`. A release stays valid when a runtime is not qualified;
that runtime is simply not advertised.

## Semantic parity, not host parity

Install flow, marketplace UI, connector authentication, approval
dialogs, subagent implementation, host commands and presentation
metadata may differ between runtimes. Scientific facts, sphere and
provider attribution, methodology, workflow requirements, uncertainty
rules, deterministic checks, dependency versions and safety
requirements may not. One signed concept feeds every projection; one
verifier checks every runtime's result.

## The user's install boundary

A scientist installs a domain capability (Ocean Science, Hydrology).
The host resolves the foundation, the provider knowledge and the
verification components where it can; where it cannot, the README gives
one deterministic path. A missing required dependency fails explicitly
(`claude plugin list` names the floor and the installed version); a
capability never continues with reduced semantics silently. Planned
repositories are visible in the sphere view and never installable.

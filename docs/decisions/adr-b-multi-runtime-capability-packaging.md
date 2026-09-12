# ADR B: Multi-runtime capability packaging

**Status:** proposed 2026-09-11; accepted when this record merges to main
after the cross-cutting review window (GOVERNANCE.md in the org `.github`
repository). Runtime implementation begins after the canonical metadata
milestone that [ADR A](adr-a-pillar-means-sphere.md) sequences.
**Decision owner:** Paul Ramirez (steward, pro tem). Personal-hat work.
**Design document:** [design-sphere-alignment-multi-runtime.md](../design-sphere-alignment-multi-runtime.md).
**Roadmap:** initiative `osp-architecture-alignment` in build-kit; the
runtime track is its R deliverables.

## Context

Everything the organization ships is packaged as a Claude plugin, and
the specification's surface parity section targets three Claude
surfaces (Code, Cowork, Science). The roadmap carries a native Codex
distribution initiative whose deliverables are hand-written
`.codex-plugin/plugin.json` manifests per repository. Two facts have
changed the shape of that problem. The Agent Skills format the skills
already use is an open standard consumed by many clients. And Agent
Plugins 1.0 (published 2026-08-06 at
github.com/agentplugins/agent-plugins-spec, maintained by a technical
steering committee drawn from Amazon, Cursor, Microsoft, OpenAI and
Vercel) packages Agent Skills and MCP servers as a directory with a
`plugin.json` manifest, a `skills/` folder and an optional `mcp.json`,
and Codex, ChatGPT, Cursor, GitHub Copilot, Kiro and VS Code consume it.
Writing one adapter per client would multiply packaging work by the
number of clients without adding any science.

## Decision

1. **The canonical capability is KNOW, ACT, PROVE and REACH**, the four
   planes the architecture document already records. Governed facts,
   portable skills, deterministic assurance and controlled execution
   surfaces are authored once and are independent of both sphere
   classification and runtime delivery.
2. **`SKILL.md` is the canonical portable ACT representation.** One
   skill directory (`SKILL.md`, `references/`, `scripts/`, `assets/`)
   per workflow. No `skills/claude/` or `skills/openai/` trees unless a
   behavior genuinely cannot be represented portably, and that
   exception is recorded.
3. **Portable scientific behavior must have a skill representation.**
   A runtime-specific agent may orchestrate skills; it may not hold
   the only authoritative implementation of scientific behavior.
4. **Knowledge is approved once and reused by every runtime.** One
   concept, one authority, many consumers. Knowledge is never copied
   into runtime-specific content, and never copied into a skill to
   solve a packaging problem.
5. **Deterministic PROVE is shared across runtimes.** A result from any
   runtime feeds the same verifier and receives a receipt that names
   the capability release. A prompt-based second opinion is not PROVE.
6. **Package and runtime metadata are canonical under `.osp/`.**
   `.osp/package.yaml` owns package identity, version, content
   locations and capability and knowledge dependencies;
   `.osp/surfaces.yaml` owns runtime support and qualification policy;
   `.osp/governance.yaml` gains runtime maintainer teams;
   `.osp/release-lock.json` is generated per release and records the
   dependency versions and content digests that let two runtimes be
   shown to have executed the same governed release. Repository
   classification stays in `.osp/repository.yaml` (ADR A) and is not
   duplicated.
7. **Runtime manifests are projections.** `.claude-plugin/plugin.json`,
   the Agent Plugins `plugin.json` and `mcp.json`, any OpenAI extension
   metadata, GitHub topics and marketplace fields are rendered by
   build-kit from canonical source and checked for drift in CI. None
   is a source of truth.
8. **Two packaging outputs, not one adapter per client.** A Claude
   projection for the Claude family, and a standards-compliant Agent
   Plugins 1.0 projection for every conforming client. No dedicated
   adapter is added for a client the portable package serves without
   semantic loss; adding one requires a demonstrated host-specific
   need. The roadmap's native Codex initiative is re-scoped
   accordingly: Codex consumes the rendered portable projection, not
   a hand-written manifest per repository.
9. **Qualification targets and tiers.** Claude Code is both the primary
   development environment and a supported runtime. Claude Cowork and
   OpenAI Codex are the required end-user qualification targets
   (Tier 1). Agent Plugins package conformance is a release gate for
   the portable package. Gemini CLI and Goose are compatibility-tested
   (Tier 2): probed periodically and after packaging changes, reported
   separately, not release-blocking. Cursor, GitHub Copilot and VS
   Code, Kiro and other conforming clients consume the portable package
   with no dedicated adapter and are documented as standards
   compatibility, not as qualified runtimes. Claude Science is a future
   Claude runtime, added when it is broadly available beyond limited
   release; until then it is excluded from the required matrix.
10. **No runtime support claim without qualification evidence.** A
    runtime is advertised as supported for a capability release only
    when it passes install, discovery, invocation, knowledge and
    dependency resolution, connector invocation where applicable,
    golden computation, deterministic PROVE, receipt generation,
    side-effect confirmation and release-lock match. A schema-valid
    package is not a qualified runtime package. A release stays valid
    when a runtime fails; that runtime is simply not advertised.
11. **The installation boundary is the domain capability.** A user
    installs Ocean Science or Hydrology; the host resolves core, the
    provider bundle, PROVE components and REACH declarations where it
    can, and where it cannot the organization provides one
    deterministic guided path. Provider knowledge, attesters and
    connector packages stay behind the capability boundary unless
    independently useful to expert users. A missing required
    dependency fails explicitly; a capability never continues with
    reduced semantics silently.
12. **Semantic parity, not host parity.** Install flow, marketplace UI,
    connector authentication, approval dialogs, subagent
    implementation, host commands and presentation metadata may
    differ. Scientific facts, sphere and provider attribution,
    methodology, workflow requirements, uncertainty rules,
    deterministic checks, dependency versions and safety requirements
    must not.
13. **No baseline upstream or vendoring tree.** Current relationships
    (a domain capability depending on core and on a provider bundle)
    are dependencies. An upstream model is introduced only when the
    organization begins qualifying and redistributing an externally
    authoritative skill or capability. Vercel's Agent Skills tooling is
    prior art, not an architectural dependency.

## Consequences

- The specification's surface parity section, the glossary's
  definition of surface, the surface testing guide and the tutorials
  are rewritten in the documentation milestone to distinguish
  development environment, qualified runtime, package conformance and
  compatibility testing, and to move Claude Science from a required
  surface to a future one. Until that milestone, the current three
  surface wording stands and is not a support claim for Codex.
- build-kit grows the validate, render, topics, sphere-view, test,
  qualify, lock, publish, plugin-check and compat commands, and
  publication can emit a versioned Cowork artifact and an Agent
  Plugins directory per installable capability.
- Evals record capability, capability version, release lock, runtime,
  model, suite, trial count, score, interval and date, so identical
  cases can be compared across runtimes without changing the
  capability contract.
- The `codex-distribution` initiative's per-repository manifest
  deliverables are superseded in form; they close or re-scope when the
  renderer lands. Their acceptance intent (a clean Codex install
  exposes every skill) survives as Codex qualification.
- The Agent Plugins specification is at 1.0.0 with 1.1.0 in draft;
  build-kit's conformance check pins the version it validates against
  and records it in the release lock.

## Not decided here

The exact host packaging (ZIP layout for organization Cowork
distribution, OpenAI extension fields) may evolve; the one-capability
install boundary does not. Whether a Claude-specific agent wrapper is
ever needed for a given skill is decided per skill with the exception
recorded.

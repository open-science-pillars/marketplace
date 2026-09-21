# Known limitations

What is verified where, as of 2026-09-21, and the caveats we ship with.
The words used here are defined in
[runtime-distribution.md](runtime-distribution.md).

## Verified where

- **Claude Code** is the development environment. Every release is
  exercised on it. Two capabilities carry a qualified record of all
  eleven tests: core 0.6.0, and hydrology 0.8.1, which is the first
  record hydrology has carried at any version. Three do not and say so:
  ocean-science 0.9.0, land-ice 0.2.0 and atmospheric-physics 0.2.0 are
  waived for this runtime and brought down from supported to tested,
  because the environment carrying those releases could not produce a
  run that would be evidence rather than a description of itself. Each
  waiver names the version the capability was last genuinely qualified
  at. Every behavioral claim in the tutorials and the eval seed grades
  is Claude Code evidence.
- **Claude Cowork** installs from this marketplace (verified 2026-07-04)
  and is not yet qualified for any release. Cowork runs a plugin's
  local MCP servers on your computer, as any program you run does, so
  the observations connector needs `uv` reachable from the app; its
  shell commands and code run in an isolated virtual machine that sees
  only the folders you connect, so the golden scripts and the attested
  computation may not run from the installed tree. Until a capability
  exposes its computation through a connector, those tests are blocked
  on Cowork and the honest outcome is a waiver.
- **OpenAI Codex** is planned: the Agent Plugins package is rendered and
  conformance-checked, and no release has been qualified on it.

## Where computation runs

Downloads (the only step needing an Earthdata Login) and heavy
computation run where your Python environment is. On a runtime with no
shell, the workflows exercise planning, gates, discovery and reporting;
a gate presenting a download it cannot perform is designed behavior.

## Not yet done

- **Non-author validation.** At least one non-author scientist
  completing Tutorial 2 unaided, friction notes recorded here verbatim.
  Until then, every timing and walkthrough claim carries author bias.
- **Provider confirmation.** Every concept is human-reviewed by its
  maintainer; a data provider's confirmation is invited at every rung
  of the ladder (consulted, reviewer, steward) and none is recorded
  yet, so no concept is voiced as provider-confirmed.
- **The powered knowledge-bundle ablation.** The pilot was underpowered
  and exposed a confound; one eval seed failure (a headline number
  without an uncertainty statement, on an uncoached prompt) is kept on
  record. The pre-registered claims and their stop conditions are in
  [phase2-preregistration.md](phase2-preregistration.md).

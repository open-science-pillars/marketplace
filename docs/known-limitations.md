# Known limitations

What is verified where, as of 2026-09-13, and the caveats we ship with.
The words used here are defined in
[runtime-distribution.md](runtime-distribution.md).

## Verified where

- **Claude Code** is the development environment. Every release is
  exercised on it, and core 0.5.1 carries a qualified record (all
  eleven tests pass). Every behavioral claim in the tutorials and the
  eval seed grades is Claude Code evidence.
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
- **The powered knowledge-bundle ablation.** The pilot was underpowered
  and exposed a confound; one eval seed failure (a headline number
  without an uncertainty statement, on an uncoached prompt) is kept on
  record. The pre-registered claims and their stop conditions are in
  [phase2-preregistration.md](phase2-preregistration.md).

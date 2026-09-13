# Contributing

Thank you for considering it. New to the project's vocabulary? Start
with the [glossary](GLOSSARY.md). The ground rules below are the
load-bearing ones; the guides in [docs/](docs/README.md) expand them by
persona:

- adding a skill: [contributing-a-skill.md](docs/contributing-a-skill.md)
- adding a concept: [contributing-knowledge.md](docs/contributing-knowledge.md)
- deciding which of the two you have: [knowledge-vs-skills.md](docs/knowledge-vs-skills.md)
- the tests you may owe: [testing.md](docs/testing.md)
- a whole new capability: [package-authoring-guide.md](docs/package-authoring-guide.md)
  and [plugin-template](https://github.com/open-science-pillars/plugin-template)
  (a bundle starts from [knowledge-template](https://github.com/open-science-pillars/knowledge-template))
- stewards: [steward-playbook.md](docs/steward-playbook.md)
- maintainers releasing: [release-candidate-guide.md](docs/release-candidate-guide.md)
  and [release-qualification-guide.md](docs/release-qualification-guide.md)

## Ground rules

1. Everything behavioral is a skill or an agent, and portable scientific
   behavior MUST have a skill representation: a runtime-specific agent may
   orchestrate skills, never hold the only implementation. No `commands/`
   directories.
2. Every SKILL.md starts with frontmatter: `name`, and a `description` of 200
   characters or fewer, keyword-first. Knowledge skills set
   `user-invocable: false` (the specification, docs/SPECIFICATION.md, lists
   the exceptions under its skill invocation rules).
3. Workflow skills keep both invocation paths open; side effects are guarded
   by in-skill confirmation gates.
4. Plugins are self-contained: no `../` paths across repos.
5. Every workflow skill that encodes a computation ships a marimo golden
   notebook in `verification/` that runs green headless.
6. Knowledge concepts follow the specification's knowledge layer and OKF
   v0.2 (the exact OKF text is vendored under docs/upstream, pinned by
   commit): a `type` from the specification's list, sourced claims, a
   status, and a steward's `verified` event at approval. Concepts state
   facts about data; they never instruct the agent. The fields and the
   types are in [docs/contributing-knowledge.md](docs/contributing-knowledge.md);
   unsure whether something is knowledge or a skill? Run the decision aid
   in [docs/knowledge-vs-skills.md](docs/knowledge-vs-skills.md).
7. Prose style: no em dashes; use commas, colons, parentheses, or semicolons.

## Where a contribution goes

| You have | It is | It lives in |
|---|---|---|
| a fact about data (a trap, an uncertainty, a validated number) | KNOW | a concept in the provider or domain bundle, signed by its steward |
| a procedure an agent follows | ACT | a `SKILL.md` under `skills/` |
| a deterministic check with a receipt | PROVE | a golden notebook under `verification/`, or an attester beside its computation |
| a way to reach an external service | REACH | a connector declared in `.osp/package.yaml`, with its facts as a `connector` concept |
| a Claude-only wrapper (a subagent, presentation metadata) | an adapter | `agents/` or the Claude package files, never the only home of behavior |

Which sphere a capability serves, and who signs its knowledge, are two
different questions (the glossary's organization section); a sphere tag on
a concept moves no authority.

## Mechanics

- Sign off every commit (DCO): `git commit -s`.
- One review from the owning team merges an ordinary PR; two for
  cross-cutting changes and high-severity knowledge edits. The teams and
  the rules are in the organization's
  [GOVERNANCE.md](https://github.com/open-science-pillars/.github/blob/main/GOVERNANCE.md).
- Issues start from the templates in the organization's
  [.github repository](https://github.com/open-science-pillars/.github/tree/main/.github/ISSUE_TEMPLATE):
  a new skill, a new knowledge concept, a new domain capability, a bug,
  a feature. Each template links the guide for its path.
- Questions go to Discussions on this repo.

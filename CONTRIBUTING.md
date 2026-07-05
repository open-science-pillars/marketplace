# Contributing

Thank you for considering it. New to the project's vocabulary? Start with the
[glossary](GLOSSARY.md). The ground rules below are the load-bearing ones; the
authoring guides in [docs/](docs/) expand them with worked detail:

- [knowledge-authoring-guide](docs/knowledge-authoring-guide.md) (concepts)
- [skill-authoring-guide](docs/skill-authoring-guide.md) and
  [agent-authoring-guide](docs/agent-authoring-guide.md)
- [eval-authoring-guide](docs/eval-authoring-guide.md) and
  [verification-guide](docs/verification-guide.md)
- [connector-guide](docs/connector-guide.md) and
  [testing-guide](docs/testing-guide.md)
- [steward-playbook](docs/steward-playbook.md) (owning a knowledge bundle)

## Ground rules

1. Everything behavioral is a skill or an agent. No `commands/` directories.
2. Every SKILL.md starts with frontmatter: `name`, and a `description` of 200
   characters or fewer, keyword-first. Knowledge skills set
   `user-invocable: false` (exceptions listed in SPECIFICATION.md §0.2).
3. Workflow skills keep both invocation paths open; side effects are guarded
   by in-skill confirmation gates.
4. Plugins are self-contained: no `../` paths across repos.
5. Every workflow skill that encodes a computation ships a marimo golden
   notebook in `verification/` that runs green headless.
6. Knowledge concepts follow SPECIFICATION.md §5: `type` and `status` in
   frontmatter; datasets carry an `## Uncertainty` section; gotchas link
   their dataset and carry at least one evidence link; update the bundle's
   `log.md`. Concepts state facts about data; they never instruct the agent.
7. Prose style: no em dashes; use commas, colons, parentheses, or semicolons.

## Mechanics

- Sign off every commit (DCO): `git commit -s`.
- One domain-maintainer review merges an ordinary PR; two for cross-cutting
  changes and high-severity knowledge edits (see org GOVERNANCE.md).
- Adding one skill to an existing plugin: open the new_skill issue template
  and follow [docs/skill-authoring-guide.md](docs/skill-authoring-guide.md).
- Proposing a knowledge concept: use the new_knowledge_concept issue template
  and [docs/knowledge-authoring-guide.md](docs/knowledge-authoring-guide.md).
- A whole new plugin starts from plugin-template; a new bundle from
  knowledge-template.
- Questions go to Discussions on this repo.

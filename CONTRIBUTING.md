# Contributing

Thank you for considering it. Until the authoring guides land (Session 12:
skill-authoring-guide.md, knowledge-authoring-guide.md, eval-authoring-guide.md,
verification-guide.md in docs/), these are the load-bearing rules; the guides
will expand them, not contradict them.

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
- Propose new concepts with the new_knowledge_concept issue template; new
  plugins start from plugin-template, new bundles from knowledge-template.
- Questions go to Discussions on this repo.

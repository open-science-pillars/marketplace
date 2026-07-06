# Documentation map

This folder holds three kinds of document. Use this map so you land in the
right one; a newcomer never needs the build record.

## For users

- [known-limitations.md](known-limitations.md): what is verified where, and
  the honest caveats we ship with.

(The main user path is elsewhere: the
[tutorials](https://github.com/open-science-pillars/tutorials) and the
[glossary](../GLOSSARY.md).)

## For contributors and maintainers

Authoring guides (how to add each kind of thing):

- [knowledge-authoring-guide.md](knowledge-authoring-guide.md): concepts
- [skill-authoring-guide.md](skill-authoring-guide.md): skills
- [agent-authoring-guide.md](agent-authoring-guide.md): agents
- [eval-authoring-guide.md](eval-authoring-guide.md): eval cases
- [verification-guide.md](verification-guide.md): golden notebooks
- [connector-guide.md](connector-guide.md): MCP connectors
- [testing-guide.md](testing-guide.md): how the test layers relate
- [steward-playbook.md](steward-playbook.md): owning a knowledge bundle
- [surface-testing-guide.md](surface-testing-guide.md): Code / Cowork / Science

## Design, strategy, and commitments

- [ARCHITECTURE.md](ARCHITECTURE.md): why the project is shaped this way
- [SPECIFICATION.md](SPECIFICATION.md): what to build (the authoritative spec)
- [phase2-preregistration.md](phase2-preregistration.md): the pre-registered
  success/stop conditions for the Phase-2 evaluation
- [design-knowledge-coupling.md](design-knowledge-coupling.md): ADOPTED
  design for how knowledge couples to skills and agents so the bundle
  augments behavior over time (with the measured proof-of-concept)

## Build record and development harness (now in build-kit)

How the project was built, and how to continue developing it, now live in the
[build-kit](https://github.com/open-science-pillars/build-kit) repo, not here:
the initiative/session plan (`IMPLEMENTATION-GUIDE.md`), the development status
tracker (`PROGRESS.md`), the parking lot (`build-record/PARKING.md`), the
harness design rationale (`build-record/BUILD-HARNESS.md`), the original
bootstrap orientation (`build-record/README-START-HERE.md`), and the
knowledge-coupling migration record
(`build-record/knowledge-coupling-migration.md`). Start at
`build-kit/DEVELOPING.md` and `build-kit/docs/development-model.md`.

Still here (launch comms, not build machinery):
[announcement-draft.md](announcement-draft.md), a launch announcement draft.

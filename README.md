# Open Science Pillars: Marketplace

The catalog and canonical documentation for Open Science Pillars:
governed, portable scientific capabilities for AI agents, organized by the
five Earth science spheres (a Pillar is a sphere). A capability is skills,
the knowledge they consult (signed by the people who steward the data),
deterministic verification and connectors, authored once and delivered to
each runtime as a package: the Claude plugin here for Claude Code and
Cowork, and the Agent Plugins package for OpenAI Codex and other clients
when that projection lands. The organization by sphere is rendered from
each repository's own metadata on the
[organization profile](https://github.com/open-science-pillars).

## Install

```bash
claude plugin marketplace add open-science-pillars/marketplace
claude plugin install ocean-science@open-science-pillars
```

A domain plugin declares what it depends on (`core` and the
`nasa-daac-knowledge` provider bundle), and the installer brings those
in with it. Cowork and Claude Science: add this marketplace and install
from it (both surfaces accept a marketplace by GitHub repo). Per-surface
steps: [docs/surface-testing-guide.md](docs/surface-testing-guide.md).

## Update

```bash
claude plugin update ocean-science@open-science-pillars
```

This marketplace does not update installs on its own: an install keeps
the release it was installed from until you update it by name (one
command per plugin you installed) or enable auto-update for the
marketplace in `/plugin`. An update moves only the plugin you name.
It does not move that plugin's installed dependencies: when a release
raises its floor past the version you have, `claude plugin list` shows
the plugin disabled with an error naming the floor and the installed
version (`Requires nasa-daac-knowledge >=2026.9.2, installed 2026.9.1`
after the ocean-science 0.8.2 update), and `claude plugin update
nasa-daac-knowledge@open-science-pillars` (or `core@...`) resolves it.
A dependency the new release declares for the first time is not
installed by the update either; the error then names the install
command to run, or `/reload-plugins` in a session installs it. The
catalog names each plugin's current release, and `claude plugin list`
shows which versions you have and whether every dependency resolved.

## What's available now

| Plugin | What it does | Status |
|---|---|---|
| `core` | Foundation: data formats, statistics, uncertainty, cartography, quality control, reproducibility, review, and the start / discover-data / report workflows. | Available |
| `ocean-science` | Physical oceanography: ECCO state estimate, SWOT sea surface height, meridional heat transport, budget closure, water masses. | Available |
| `hydrology` | SWOT rivers and lakes, GRACE-FO groundwater, USGS streamflow, SMAP soil moisture, drought and reservoir analysis. | In development |
| `nasa-daac-knowledge` | The provider knowledge bundles (PO.DAAC datasets, gotchas, recipes and attested computations; ESDIS metadata requirements), signed by their stewards. No skills; the domain plugins depend on it and install it for you. | Available |

New to the terms used here (sphere, capability, skill, knowledge bundle,
golden notebook, runtime, connector)? See the [glossary](GLOSSARY.md).

## Runtimes

| Runtime | Status (2026-09-12) |
|---|---|
| Claude Code | supported; the development environment |
| Claude Cowork | tested: installs from this marketplace; per-release qualification pending |
| OpenAI Codex | planned: through the Agent Plugins projection, not yet built |
| Claude Science | future runtime |
| Gemini CLI, Goose | compatibility targets, not yet probed |

What each word asserts is in [docs/runtime-distribution.md](docs/runtime-distribution.md).
A release stays valid when a runtime fails qualification; that runtime is
simply not advertised for it.

## Planned

Eleven repositories are decided and not yet created (ADR A, target
map): `precipitation` (Hydrosphere), `land-ice` and `sea-ice`
(Cryosphere), `solid-earth` and `land-surface` (Geosphere),
`atmospheric-composition` and `atmospheric-physics` (Atmosphere),
`land-ecosystems` and `ocean-biology` (Biosphere), `composites`
(cross-sphere) and `partner-knowledge` (provider knowledge from non-NASA
stewards). A planned repository is visible and never installable; none
appears in this catalog until it has a release.

## Learn it in under an hour

Three timed tutorials and a no-install demo:
[Getting Started (~10 min)](https://github.com/open-science-pillars/tutorials/blob/main/tutorial-1-getting-started.qmd),
[ECCO Heat Transport (~20 min)](https://github.com/open-science-pillars/tutorials/blob/main/tutorial-2-ecco-mht.qmd),
[Build a Domain Plugin (~30 min)](https://github.com/open-science-pillars/tutorials/blob/main/tutorial-3-build-a-plugin.qmd),
and the [browser-runnable MHT demo](https://github.com/open-science-pillars/tutorials/tree/main/demo).

## Documentation

**For users:** the [tutorials](https://github.com/open-science-pillars/tutorials),
the [glossary](GLOSSARY.md), and [known limitations](docs/known-limitations.md).

**For contributors:** [CONTRIBUTING.md](CONTRIBUTING.md) and the authoring
guides in [docs/](docs/) (knowledge, skill, agent, eval, verification,
connector, and testing guides), plus the [steward playbook](docs/steward-playbook.md).

**Design and strategy:** [ARCHITECTURE.md](docs/ARCHITECTURE.md) (why),
[SPECIFICATION.md](docs/SPECIFICATION.md) (what) and the
[decision records](docs/decisions/README.md) (the sphere alignment and the
multi-runtime packaging). The build record and the
development harness (IMPLEMENTATION-GUIDE, PROGRESS, BUILD-HARNESS) now live in
the [build-kit](https://github.com/open-science-pillars/build-kit) repo; see
[docs/README.md](docs/README.md) for the map.

## Community

Questions: [Discussions](https://github.com/open-science-pillars/marketplace/discussions).
Contributions: [CONTRIBUTING.md](CONTRIBUTING.md); governance and review
rules live in the org [.github repo](https://github.com/open-science-pillars/.github).
Releases are tags with GitHub releases; Zenodo archiving and DOIs begin
at each repository's 1.0.0 release (tracked on issue #55). See CITATION.cff.

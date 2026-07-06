# Open Science Pillars: Marketplace

The plugin catalog and canonical documentation for Open Science Pillars:
AI-assisted open science for earth, planetary, and applied science across
Claude Code, Claude Cowork, and Claude Science.

## Install

```bash
claude plugin marketplace add open-science-pillars/marketplace
claude plugin install core@open-science-pillars
claude plugin install ocean-science@open-science-pillars
```

Cowork and Claude Science: add this marketplace and install from it
(both surfaces accept a marketplace by GitHub repo). Per-surface steps:
[docs/surface-testing-guide.md](docs/surface-testing-guide.md).

## What's available now

| Plugin | What it does | Status |
|---|---|---|
| `core` | Foundation: data formats, statistics, uncertainty, cartography, quality control, reproducibility, review, and the start / discover-data / report workflows. | Available |
| `ocean-science` | Physical oceanography: ECCO state estimate, SWOT sea surface height, meridional heat transport, budget closure, water masses. **Install core first.** | Available |
| `hydrology` | SWOT rivers and lakes, GRACE-FO groundwater, USGS streamflow, SMAP soil moisture, drought and reservoir analysis. | In development |

New to the terms used here (skill, knowledge bundle, golden notebook,
surface, connector)? See the [glossary](GLOSSARY.md).

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

**Design and strategy:** [ARCHITECTURE.md](docs/ARCHITECTURE.md) (why) and
[SPECIFICATION.md](docs/SPECIFICATION.md) (what). The build record and the
development harness (IMPLEMENTATION-GUIDE, PROGRESS, BUILD-HARNESS) now live in
the [build-kit](https://github.com/open-science-pillars/build-kit) repo; see
[docs/README.md](docs/README.md) for the map.

## Community

Questions: [Discussions](https://github.com/open-science-pillars/marketplace/discussions).
Contributions: [CONTRIBUTING.md](CONTRIBUTING.md); governance and review
rules live in the org [.github repo](https://github.com/open-science-pillars/.github).
Releases are archived to Zenodo for DOIs; see CITATION.cff.

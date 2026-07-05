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

## Plugins

| Plugin | What it does |
|---|---|
| `core` | Foundation: data formats, statistics, uncertainty quantification, cartography, quality control, reproducibility, analysis review, and the start / discover-data / report workflows. |
| `ocean-science` | Physical oceanography: ECCO state estimate, SWOT SSH, meridional transport, budget closure, water masses. **Install core first.** |

## MVP cut-line

Phase 1 ships the two plugins above, their knowledge bundles and golden
notebooks, three tutorials, and the seed eval cases. Everything else
(hydrology, the evals runner, provider-bundle promotion) is Phase 2+,
tracked in [docs/PROGRESS.md](docs/PROGRESS.md).

## Documentation

Canonical docs live in [docs/](docs/): ARCHITECTURE (why), SPECIFICATION
(what), IMPLEMENTATION-GUIDE (in what order), PROGRESS (current state),
BUILD-HARNESS (how sessions run), plus authoring guides as they land.

## Community

Questions: [Discussions](https://github.com/open-science-pillars/marketplace/discussions).
Contributions: [CONTRIBUTING.md](CONTRIBUTING.md); governance and review
rules live in the org [.github repo](https://github.com/open-science-pillars/.github).
Releases are archived to Zenodo for DOIs; see CITATION.cff.

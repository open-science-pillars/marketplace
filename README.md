# Open Science Pillars: Marketplace

The plugin catalog for Open Science Pillars, and the home of its
canonical documentation. What you install is a capability: skills an
agent runs for one discipline of Earth science, the knowledge those
skills consult (facts about real datasets, signed by the people who
steward the data), deterministic checks that emit receipts, and
connectors to the archives. With one installed, the agent knows the
traps in the products you use, asks before a large download, and cites
the concept behind every number it reports. Capabilities are organized
by Earth science sphere on the
[organization profile](https://github.com/open-science-pillars). New to
a term? See the [glossary](GLOSSARY.md).

## Install

Claude Code:

```bash
claude plugin marketplace add open-science-pillars/marketplace
claude plugin install ocean-science@open-science-pillars
```

Claude Cowork: from Customize > Plugins > Add marketplace, add this
marketplace by repository, `open-science-pillars/marketplace`; then
install the capability from it. It is the same plugin.

A domain capability declares what it depends on, and the installer
brings it along: `core` (the foundation) and `nasa-daac-knowledge` (the
provider knowledge bundle) arrive with `ocean-science` or `hydrology`.

Local requirements: `uv` (the connectors and the verification scripts
run with `uv run`), and an Earthdata Login for the ocean and hydrology
data loads.

## What's available

| Capability | What it does | Status |
|---|---|---|
| `core` | Foundation: data formats, statistics, uncertainty, cartography, quality control, reproducibility, review, and the start, discover-data and report workflows. | Available |
| `ocean-science` | Physical oceanography: ECCO state estimate, SWOT sea surface height, meridional heat transport, budget closure, water masses. | Available |
| `hydrology` | SWOT rivers and lakes, GRACE-FO groundwater, USGS streamflow, SMAP soil moisture, drought and reservoir analysis. | Developing |
| `nasa-daac-knowledge` | The provider knowledge bundles (PO.DAAC datasets, gotchas, recipes and attested computations; ESDIS metadata requirements), signed by their stewards. No skills; the domain capabilities depend on it. | Available |

The catalog, [.claude-plugin/marketplace.json](.claude-plugin/marketplace.json),
names each capability's current release.

## Runtimes

| Runtime | Status |
|---|---|
| Claude Code | supported; the development environment |
| Claude Cowork | tested; qualified per release |
| OpenAI Codex | planned, through the Agent Plugins package |
| Claude Science | future runtime |
| Gemini CLI, Goose | compatibility targets |

What each word asserts: [docs/runtime-distribution.md](docs/runtime-distribution.md).

## Learn

Three timed tutorials and a no-install demo:
[Getting Started (~10 min)](https://github.com/open-science-pillars/tutorials/blob/main/tutorial-1-getting-started.qmd),
[ECCO Heat Transport (~20 min)](https://github.com/open-science-pillars/tutorials/blob/main/tutorial-2-ecco-mht.qmd),
[Build a Domain Plugin (~30 min)](https://github.com/open-science-pillars/tutorials/blob/main/tutorial-3-build-a-plugin.qmd),
and the [browser-runnable MHT demo](https://github.com/open-science-pillars/tutorials/tree/main/demo).

## Update

An install stays at the release it was installed from.
`claude plugin update <name>@open-science-pillars` moves one plugin.
Dependencies update by name (`claude plugin update
nasa-daac-knowledge@open-science-pillars`); when a release raises a
dependency floor, `claude plugin list` names the floor and the version
you have. The full rule is the install-and-update section of the
[specification](docs/SPECIFICATION.md).

## Planned

Eleven repositories hold the planned status: each shows where a
capability will go under its sphere and holds nothing installable
until it has a release. They are listed in the sphere view on the
[organization profile](https://github.com/open-science-pillars).

## Documentation

**Users:** the [tutorials](https://github.com/open-science-pillars/tutorials),
the [glossary](GLOSSARY.md) and [known limitations](docs/known-limitations.md).

**Contributors:** [CONTRIBUTING.md](CONTRIBUTING.md), then the guide for
what you are adding: a skill, a concept, a whole capability; the steward
playbook; the release guides.

**Design:** [docs/MODEL.md](docs/MODEL.md) (the current model on one
page), the [specification](docs/SPECIFICATION.md) and the
[decision records](docs/decisions/README.md).

The map of all of it, by audience: [docs/README.md](docs/README.md).

## Community

Questions: [Discussions](https://github.com/open-science-pillars/marketplace/discussions).
Contributions: [CONTRIBUTING.md](CONTRIBUTING.md); governance and review
rules are in the organization's
[GOVERNANCE.md](https://github.com/open-science-pillars/.github/blob/main/GOVERNANCE.md).
Releases are tags with GitHub releases; Zenodo archiving and DOIs begin
at each repository's 1.0.0 release (tracked on
[issue #55](https://github.com/open-science-pillars/marketplace/issues/55)).
See [CITATION.cff](CITATION.cff).

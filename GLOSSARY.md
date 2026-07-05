# Glossary

Plain-language definitions of the terms used across Open Science Pillars.
If a plugin README or tutorial uses a word you don't recognize, it's here.

## The pieces you install

- **Plugin** — an installable package for Claude (Code, Cowork, or Science)
  that adds skills, knowledge, and connectors for a topic. `core` is the
  foundation; `ocean-science` and `hydrology` are domain plugins.
- **Skill** — a unit of expertise or a workflow that Claude loads and uses.
  Two kinds: *knowledge skills* (background expertise Claude consults
  automatically, like how to weight a spatial average) and *workflow skills*
  (things you ask it to do, like "load this dataset" or "write a report").
- **Gated skill / gated loader** — a workflow skill that stops and asks for
  confirmation before an expensive or irreversible action, such as a large
  download. It shows you the size and destination first.
- **Agent** — a specialized helper Claude can dispatch for a focused job, for
  example checking a knowledge bundle for problems or auditing a computed
  budget. Agents in this project propose changes; they don't apply them.

## The knowledge layer

- **Knowledge bundle** — a folder of short markdown files capturing what
  practitioners know about real datasets: the traps, the uncertainty
  structure, and validated recipes. Every claim carries an evidence link and
  a review status. This is the reusable heart of the project.
- **Concept** — one file in a knowledge bundle. Four kinds: a **dataset**
  (what a product is and how its errors behave), a **gotcha** (a specific way
  a naive analysis goes silently wrong), a **recipe** (a validated method with
  expected numbers), and a **convention** (a cross-cutting rule).
- **Gotcha** — a documented trap that produces plausible-looking but wrong
  results if you don't know about it (for example, computing an ocean budget
  on regridded data, which never closes).
- **Uncertainty section** — a required part of every dataset concept naming
  the product's error fields and their limits, so results can state how well
  they're known.
- **Steward** — the person accountable for a knowledge bundle's correctness:
  they review concepts before they're marked verified.

## Verification

- **Golden notebook** — an automated notebook (written with **marimo**) that
  re-runs a workflow's computation on small test data and checks it still
  gets the expected answer. It runs headless in continuous integration; a red
  notebook blocks a change.
- **marimo** — the reactive Python notebook format the golden notebooks use.
  It runs as a plain script, so the checks work in automation.
- **Fixture** — the small, deterministic test dataset a golden notebook runs
  on. Synthetic fixtures are built to make a classic mistake visibly wrong.
- **Eval case** — a test of Claude's scientific *judgment* (not its code):
  given a realistic prompt, does it avoid the gotcha, refuse the unsafe
  request, report uncertainty? The **seed** set is the hand-graded baseline;
  an automated runner with many trials supersedes it.

## Surfaces and connectors

- **Surface** — one of the three products this ships to: **Claude Code** (the
  terminal/IDE tool), **Claude Cowork**, and **Claude Science**. The same
  plugin installs on all three.
- **Connector (MCP)** — a link from Claude to an external data service (for
  example NASA Earthdata). When a connector isn't available, the plugins fall
  back to knowledge-based discovery and say so.

## Prerequisites at a glance

- **Claude Code** (or Cowork / Science) with the plugin installed.
- For real analyses: a **Python environment** with the scientific stack
  (xarray, netCDF4, matplotlib; ocean work adds earthaccess, xgcm, and the
  ECCO libraries; the tutorials list exact packages).
- For NASA data: an **Earthdata Login** in `~/.netrc` (machine
  `urs.earthdata.nasa.gov`, `chmod 600`). USGS water data needs no login.

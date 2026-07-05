# Open Science Pillars: Specification

**Organization:** Open Science Pillars (github.com/open-science-pillars)
**Version:** 0.6.0 (first build-informed revision)
**Date:** 2026-07-05
**Scope:** Phase 1 (built; core + ocean-science + infrastructure + knowledge + verification + evals seed + stewardship) plus Phase 2 spec detail (hydrology bridge, §10)

**Changelog:**
- 0.6.0 (2026-07-05, written by the build per harness rule 11 after the post-Session-10 PARKING triage): §0.1/§2.3 Claude Science install corrected to observed marketplace-install behavior (PARKING #5); §0.3 description-budget verification instrument corrected from /doctor to the /skills panel (PARKING #7); §2.2 marketplace.json verbatim block replaced with the CLI-validated working schema (owner object, source objects; PARKING #6); §9 non-author acceptance criterion restored and launch success criteria referenced (PARKING #1, #3); new §10 Hydrology Plugin (Phase 2 spec detail) including the v0.6 ocean-bundle completion list scheduled into Session 18 (PARKING #8, #9, #11, #12, #13). Phase-2 go/stop pre-registration published separately (docs/phase2-preregistration.md, PARKING #2).
- 0.5.1 erratum (same date, no version bump, freeze intact): PARKING.md added to the §2.1 docs listing for consistency with harness rule 11; title punctuation normalized. No scope change.
- 0.5.1 (same date): security and launch hygiene: knowledge-is-declarative rule and linter imperative scan (§5.8); CI-without-secrets and fixture-license notes (§6); DCO sign-off and GitHub Discussions (§1.2); model-version recording in eval results; official-directory submission at launch.
- 0.5.0 (same date): knowledge population and stewardship: four intake channels and the knowledge-seeder agent (§5.5); status lifecycle and mandatory evidence links (§5.6); steward playbook, CODEOWNERS, and review rules (§5.4); canonical-home plus pinned-snapshot precedence resolving the §0.5 self-containment contradiction with bundle promotion (§5.7); linter checks extended accordingly.
- 0.4.0 (same date): evals layer added as new §8 (Acceptance renumbered to §9): per-plugin `evals/` case directories, case schema, grading and N-trial CI reporting, the bundle-ablation protocol, org `evals` repo (Phase 2 runner/graders/scoreboard), and the linter rule that a high-severity gotcha requires a matching eval case.
- 0.3.1 (review pass, same date): golden-notebook scope rule (deterministic recipes only; core ships analysis_pipeline.py); duplicate ocean start skill removed (core's start covers listing); pointwise budget-closure testing valid on subsets; fixtures policy and CI workflow added; PROGRESS.md consolidated under marketplace/docs/; Zenodo release DOIs; environment fix (xesmf/esmpy via conda).
- 0.3.0: merged the UQ/marimo/ARSET integration round: new uncertainty-quantification core skill; analysis-review UQ checks; cartography uncertainty visualization; required Uncertainty section on dataset concepts; expected-uncertainty in recipes; optional `trainings:` frontmatter; new §6 Verification Layer (marimo golden notebooks); ARSET-style applied tutorial template; report uncertainty rule.
- 0.2.0: org renamed Open Science Pillars; commands eliminated (skills unification of 2026-01-24); §0 surface parity; §5 knowledge layer; SWOT added; plugin self-containment; ECCO velocity ShortName fix; description budget rule.

---

## 0. Surface Parity Requirements

Everything targets three surfaces equally: **Claude Code**, **Claude Cowork**, and **Claude Science**. One markdown source, three packagings.

### 0.1 Packaging matrix

| Surface | Packaging | Install | Invocation |
|---|---|---|---|
| Claude Code | Plugin via marketplace | `claude plugin install <name>@open-science-pillars` | `/plugin-name:skill-name` or conversational |
| Claude Cowork | Same plugin format | claude.com/plugins or upload | Conversational |
| Claude Science | Same plugin format via marketplace install (observed 2026-07-04; the workspace skill-import path exists but is not required); connectors per session | Marketplace add + install / connector config | Conversational |

### 0.2 Skill invocation rules

Skills are the only behavioral component besides agents. Two classes:

**Workflow skills** (load-ecco, report, transport-analysis, ...): frontmatter leaves BOTH invocation paths open. Never set `disable-model-invocation: true` on these; it would make them unreachable on conversational surfaces. Side-effect safety (large downloads, file writes) is implemented as in-skill confirmation gates.

**Knowledge skills** (background expertise: data-formats, xarray-fundamentals, basic-statistics, cartography): set `user-invocable: false` to auto-load without cluttering the menu. Exceptions that stay user-invocable because scientists explicitly request them: quality-control, analysis-review, uncertainty-quantification.

### 0.3 Frontmatter standard

```yaml
---
name: skill-name
description: One sentence, under 200 characters, front-loaded with the keywords a scientist would actually use.
# knowledge skills only:
# user-invocable: false
---
```

**Quoting rule (v0.6 erratum, 2026-07-05):** any frontmatter value
containing ": " is double-quoted. Claude Code's frontmatter parser is
lenient, but GitHub and other strict YAML parsers reject unquoted
inner colons ("mapping values are not allowed in this context"), so
unquoted descriptions render as errors on the repository pages. The
§3.3 description table's texts therefore appear quoted in actual
frontmatter.

**Description budget rule:** skill descriptions share a context budget (about 1% of the context window; overflow shortens descriptions and can strip matching keywords). Requirement: ≤200 characters, keyword-first. Verified with the `/skills` panel on Claude Code (per-skill token cost and truncation state; `/doctor` no longer carries this check as of CLI 2.1.x).

### 0.4 Surface-neutral writing rules

- No terminal assumptions in skill bodies; environment requirements stated declaratively per surface.
- Compute is declared, not assumed: tasks labeled small (laptop), medium (Dask), large (HPC/burst).
- Every workflow skill's acceptance includes conversational invocation with no slash command.

### 0.5 Self-containment rule

Plugins are cached and cannot reference files outside their own directory: no `../` paths between plugins; core is a peer install ("install core first" in READMEs and descriptions), never a file dependency; cross-plugin references are conceptual, never by path.

---

## 1. Infrastructure

### 1.1 Organization and repositories

**Org:** `open-science-pillars`

| Repository | Purpose | Phase |
|---|---|---|
| `marketplace` | Plugin catalog, governance, canonical docs, PROGRESS.md | 1 |
| `core` | Foundation plugin | 1 |
| `ocean-science` | Ocean domain plugin (ECCO + SWOT SSH; the PO.DAAC arc) | 1 |
| `tutorials` | Quarto tutorials, templates, demos | 1 |
| `plugin-template` | Scaffold for new domain plugins | 1 |
| `knowledge-template` | Scaffold for new OKF knowledge bundles | 1 |
| `.github` | Org profile, issue templates, CoC, governance | 1 |
| `hydrology` | SWOT rivers/lakes, GRACE-FO, NWIS, SMAP | 2 |
| `nasa-daac-knowledge` | Standalone per-DAAC bundles (podaac first) | 2 |
| `earthaccess-mcp` | Connector wrapping NASA earthaccess | 2 |
| `evals` | Eval runner, shared graders, suite manifests, published scoreboard | 2 |
| `remote-sensing`, `models-and-reanalysis` | Measurement-layer plugins | 3 |
| `applied-science` | Applications layer (ARSET-anchored packs) | 3 |
| `planetary-science`, `pds-knowledge` | Planetary domain + PDS knowledge | 4 |

### 1.2 `.github` repo

Profile README, five issue templates (bug, feature, new skill, new domain plugin, new knowledge concept), PR template, Contributor Covenant v2.1, SECURITY.md, FUNDING.yml, and GOVERNANCE.md (lazy consensus; one domain-maintainer review per PR, two for cross-cutting changes; knowledge bundles may be maintained by data-provider staff as domain maintainers for their bundle; high-severity gotchas require a second reviewer). PRs use DCO sign-off; GitHub Discussions is enabled on the marketplace repo as the user Q&A channel.

---

## 2. Marketplace

### 2.1 Structure

```
marketplace/
├── .claude-plugin/marketplace.json
├── README.md
├── CONTRIBUTING.md
├── LICENSE                      # Apache 2.0
├── CITATION.cff
└── docs/
    ├── ARCHITECTURE.md              # canonical strategy doc
    ├── SPECIFICATION.md             # this document
    ├── IMPLEMENTATION-GUIDE.md
    ├── BUILD-HARNESS.md
    ├── PROGRESS.md                  # per-surface build status
    ├── skill-authoring-guide.md     # frontmatter standard + budget rule
    ├── agent-authoring-guide.md
    ├── knowledge-authoring-guide.md # OKF concepts incl. Uncertainty sections, trainings links
    ├── eval-authoring-guide.md      # case schema, graders, trials and CI reporting (§8)
    ├── steward-playbook.md          # steward duties, review checklist, onboarding (§5.4)
    ├── PARKING.md                   # freeze holding pen (harness rule 11)
    ├── verification-guide.md        # golden-notebook practice (§6)
    ├── connector-guide.md
    ├── surface-testing-guide.md     # three-surface harness + prompts/
    └── testing-guide.md
```

### 2.2 marketplace.json

```json
{
  "name": "open-science-pillars",
  "version": "0.3.0",
  "description": "AI-assisted open science for earth, planetary, and applied science: skills, knowledge bundles, verification notebooks, and connectors for Claude Code, Cowork, and Claude Science.",
  "owner": { "name": "Open Science Pillars Community" },
  "author": { "name": "Open Science Pillars Community" },
  "homepage": "https://github.com/open-science-pillars",
  "plugins": [
    {
      "name": "core",
      "description": "Foundation: earth science data formats, statistics, uncertainty quantification, cartography, quality control, reproducibility, analysis review.",
      "source": { "source": "github", "repo": "open-science-pillars/core" },
      "tags": ["netcdf", "xarray", "cartopy", "geotiff", "zarr", "climate", "geospatial", "qc", "uncertainty", "reproducibility"]
    },
    {
      "name": "ocean-science",
      "description": "Physical oceanography: ECCO state estimate, SWOT SSH, meridional transport, budget closure, water masses. Install core first.",
      "source": { "source": "github", "repo": "open-science-pillars/ocean-science" },
      "tags": ["oceanography", "ecco", "swot", "podaac", "amoc", "heat-transport", "sea-level"]
    }
  ]
}
```

No `dependencies` field: the plugin system does not resolve cross-plugin dependencies. (v0.6 note: the `owner` object is required by the CLI's marketplace schema, and plugin entries use the `source` object form; a bare `repository: "owner/repo"` string is not an installable source type. Both were discovered at the Session 1 install test.)

### 2.3 Install experience

```bash
claude plugin marketplace add open-science-pillars/marketplace
claude plugin install core@open-science-pillars
claude plugin install ocean-science@open-science-pillars
```

Cowork: claude.com/plugins, or an unlisted marketplace by GitHub repo. Claude Science: add the marketplace and install, same as Cowork (observed 2026-07-04); connectors per session (surface-testing-guide.md documents the tested paths).

**Releases:** tagged releases of every repo are archived to Zenodo for a DOI; each CITATION.cff points at the repo's concept DOI so contributions are citable in the literature.

---

## 3. Core Plugin

### 3.1 Structure

```
core/
├── .claude-plugin/plugin.json
├── .mcp.json                          # NASA Earthdata MCP; graceful degradation to local files
├── CONNECTORS.md
├── README.md · LICENSE · CITATION.cff
├── skills/
│   ├── data-formats/SKILL.md              # knowledge skill
│   ├── xarray-fundamentals/SKILL.md       # knowledge skill
│   ├── basic-statistics/SKILL.md          # knowledge skill
│   ├── uncertainty-quantification/SKILL.md # knowledge skill, user-invocable
│   ├── cartography/SKILL.md               # knowledge skill
│   ├── quality-control/SKILL.md           # knowledge skill, user-invocable
│   ├── reproducibility/SKILL.md           # knowledge skill
│   ├── analysis-review/SKILL.md           # knowledge skill, user-invocable
│   ├── start/SKILL.md                     # workflow skill
│   ├── discover-data/SKILL.md             # workflow skill
│   └── report/SKILL.md                    # workflow skill
├── agents/{knowledge-linter, knowledge-seeder}/agent.md
├── knowledge/                              # OKF bundle
│   ├── index.md · log.md
│   └── conventions/{cf-conventions, calendars, common-fill-values}.md
├── verification/                           # §6 golden notebooks (marimo, pure Python)
│   ├── analysis_pipeline.py                # report's computational substrate
│   └── fixtures/  (incl. make_fixtures.py)
├── evals/                                  # §8 seed cases (methodology)
│   └── {area-weighting, uncertainty-statement, trend-method}.yaml
└── tutorials/quickstart.md
```

### 3.2 plugin.json

As marketplace entry, expanded: name `core`, version 0.3.0, Apache-2.0, homepage github.com/open-science-pillars/core.

### 3.3 Knowledge skills

The v0.1-specified content for data-formats, xarray-fundamentals, basic-statistics, cartography, quality-control, reproducibility, and analysis-review carries forward (behaviors, code patterns, physical-bounds tables, Must NOT rules), with the authoring deltas already recorded (magic-byte detection; trend decision tree and pymannkendall example; cmocean table and figure sizes; 20+ variable bounds and MODIS/Landsat/Sentinel-2 QA decoding; DOI quick table; smell-test list and inline 🔴🟡🟢 flags).

**Frontmatter descriptions (≤200 chars, keyword-first):**

| Skill | description |
|---|---|
| data-formats | Open and inspect NetCDF, HDF4/5, GeoTIFF, Zarr, GRIB, CSV earth science files with xarray, rioxarray, cfgrib; fill values, time decoding, CRS, chunking. |
| xarray-fundamentals | xarray selection, resampling, groupby, area-weighted means, Dask chunking, cftime calendars for gridded earth science data. |
| basic-statistics | Climatology, anomalies, Mann-Kendall and Sen's slope trends, composites, percentile extremes, calendar handling for climate data. |
| uncertainty-quantification | Uncertainty for results: error propagation, bootstrap and block-bootstrap CIs, ensemble spread, conformal prediction, native product uncertainty fields, reporting rules. |
| cartography | Publication-quality maps with cartopy: projections, uniform colormaps, stippling and uncertainty visualization, multi-panel layouts, Hovmoller. |
| quality-control | QC for geophysical data: completeness, physical-bounds checks, fill-value audit, satellite QA flag decoding, discontinuity detection. |
| reproducibility | CF-compliant metadata, dataset DOIs and citations, provenance history attributes, FAIR outputs, package version capture. |
| analysis-review | Post-computation sanity checks: area weighting, autocorrelation in trends, baselines, projections, budget grid, uncertainty reported, smell-test ranges. |

**uncertainty-quantification (new, full scope):** error propagation basics; bootstrap and block-bootstrap confidence intervals (block for autocorrelated geophysical series, with block-length guidance); interpreting native product uncertainty fields (and reading each dataset concept's Uncertainty section before analysis); ensemble spread as uncertainty and the small-ensemble underestimation caveat; conformal prediction (distribution-free validity, model-agnostic, no retraining; when to reach for it; GEE-native implementations exist for EO); the house reporting rule: **no headline quantitative result without an uncertainty statement, or an explicit one-line reason why none is available**; the applied framing example (carbon-credit protocols allocate from the lower bound of a prediction interval, not the point estimate). Must NOT: present an ensemble mean without spread; treat quality flags as quantitative uncertainty; report intervals without stating method and level.

**analysis-review additions (three UQ checks):** Is uncertainty reported alongside the headline number? Is an ensemble mean shown without spread? Does the product carry a native uncertainty or quality layer (per its dataset concept) that the analysis ignored?

**cartography addition (uncertainty visualization):** interval bands on time series; spread and agreement maps; hatching for low agreement; rule: an uncertainty map accompanies any interpolated or ML-derived surface presented to stakeholders.

### 3.4 Workflow skills

Both invocation paths open; behaviors as specified in v0.1 §3.5 plus:

**start:** lists installed plugins, connector status, local config summary, available workflow skills grouped by plugin, one suggested next step; one screen.

**discover-data:** parse need → structured parameters; Earthdata MCP when available, knowledge-based fallback with archive URLs when not; comparison-table output; one clarifying question max; consults installed knowledge bundles and surfaces relevant gotchas alongside results.

**report:** assembles Data Description / Methods / Results / Quality Notes / Provenance / Reproducibility; markdown default, docx on request; confirmation gate (filename and sections) before writing; Provenance cites knowledge concepts consulted by bundle path; **Results rule: every headline quantity carries an uncertainty statement (interval, spread, or native product uncertainty) or a one-line waiver.**

### 3.5 Agents: knowledge-linter and knowledge-seeder

**knowledge-linter** health-checks any OKF bundle in scope. Checks: `type` and `status` present; required fields present (title, description, tags, timestamp; resource and an `## Uncertainty` section on dataset concepts); every gotcha carries at least one evidence link; links resolve; concepts reachable from index.md; staleness threshold on dataset timestamps; high-severity gotchas carry a matching eval case id (🟡 if absent); `upstream: pending` concepts older than 60 days flagged; `disputed` concepts with no linked open issue flagged; imperative-phrasing scan (concepts containing instructions directed at the agent are flagged, §5.8); contradiction scan flagged for human review. Proposes fixes as diffs; never modifies.

**knowledge-seeder** drafts concepts from authoritative sources. Given a dataset and steward-supplied seed URLs (product user guide, ATBD, known-issues page, provider forum threads, library release notes and issue trackers, ARSET Q&A documents), it drafts a dataset concept and gotcha candidates: every claim paraphrased with an evidence link, frontmatter `status: draft`, no log.md entry. MAY crawl only the supplied domains; MUST NOT invent or infer evidence (an unclear claim becomes an open question in the draft, not an assertion); MUST NOT merge anything. Steward review promotes draft to verified.

### 3.6 Core knowledge bundle

Three seed concepts: `conventions/cf-conventions.md` (type: convention), `conventions/calendars.md` (convention; DJF year-boundary trap), `conventions/common-fill-values.md` (dataset-gotcha; the unmasked fill-value list with detection recipe).

---

## 4. Ocean Science Plugin

### 4.1 Structure

```
ocean-science/
├── .claude-plugin/plugin.json · .mcp.json · CONNECTORS.md
├── README.md · LICENSE · CITATION.cff
├── ocean-science.local.md.template        # incl. SWOT block + Knowledge block
├── skills/
│   ├── ecco/SKILL.md + references/{llc90-grid, variable-catalog, budget-formulation}.md
│   ├── swot/SKILL.md + references/swot-products.md
│   ├── ocean-grids/ · budget-closure/ · meridional-transport/
│   ├── water-masses/ · mixed-layer/ · sea-level/ · ocean-indices/
│   ├── load-ecco/ · load-swot/ · ocean-budget/
│   ├── transport-analysis/ · compare-obs/
│   └── water-mass-analysis/ · mixed-layer-analysis/ · sea-level-analysis/
├── agents/{ecco-scout, budget-auditor}/agent.md
├── knowledge/                              # PO.DAAC arc bundle
│   ├── index.md · log.md
│   ├── datasets/{ecco-v4r4, swot-karin, grace-fo-mascons, ghrsst-mur}.md
│   ├── gotchas/{ecco-native-vs-regridded, ecco-geothermal-flux,
│   │            swot-calval-orbit-phases, grace-coastal-leakage,
│   │            grace-gia-correction}.md
│   └── recipes/{ecco-heat-budget, ecco-mht-26n}.md
├── evals/                                  # §8 seed cases (gotcha-avoidance + rejection)
│   ├── SCHEMA.md
│   └── {native-grid-refusal, geothermal-omission,
│        swot-calval-window, grace-leakage, volume-gate}.yaml
├── verification/
│   ├── load_ecco.py · transport_analysis.py · ocean_budget.py · load_swot.py
│   └── fixtures/
└── tutorials/quickstart.md
```

### 4.2 ECCO skill and references

As v0.1 §4.6 with: velocity ShortName corrected to `ECCO_L4_OCEAN_VEL_LLC0090GRID_MONTHLY_V4R4` (OBP is bottom pressure, its own row); every ShortName verified against the live PO.DAAC catalog with a verification date recorded in the catalog file; a "Knowledge first" section (consult and restate applicable gotchas before analysis).

### 4.3 SWOT skill

Knowledge skill covering: KaRIn L2 SSH product tiers (Basic/Expert/WindWave/Unsmoothed) and nadir products; orbit phases as a first-class gotcha (1-day cal/val vs 21-day science); two-swath geometry with nadir gap and its gridding/crossover implications; earthaccess access, cycle/pass naming; processing-baseline versioning captured in the dataset concept with a verification date, not hardcoded. Hydrology products named and deferred to the hydrology plugin.

### 4.4 Ocean workflow skills

As v0.1 §4.5 behaviors, re-homed as skills (ocean-science ships no separate start skill: core's start lists ocean workflows once the plugin is installed, avoiding a duplicate-name collision and ambiguous conversational matching), plus: load-ecco and load-swot carry volume-confirmation gates and restate applicable gotchas; ocean-budget keeps the native-grid-or-refuse 🔴 rule with budget-auditor auto-run; transport-analysis reads expected ranges from `recipes/ecco-mht-26n.md` (which now states expected-uncertainty, the RAPID-comparison spread, alongside the 0.8-1.4 PW mean range) rather than hardcoding; compare-obs unchanged; the three analysis skills authored fully at build per their one-paragraph specs.

### 4.5 Agents

ecco-scout recommends datasets for a research question, cites knowledge concepts in its plan, never downloads without approval. budget-auditor verifies closure after any budget, checking `gotchas/ecco-geothermal-flux.md` first on failure; proposes, never silently fixes.

### 4.6 Knowledge bundle requirements

All four dataset concepts carry `## Uncertainty` sections (ECCO: no formal error fields, consistency properties instead, stated plainly; SWOT: ssha uncertainty variables and their caveats; GRACE-FO: mascon error grids, leakage, GIA; GHRSST MUR: analysis-error field). Optional `trainings:` frontmatter lists relevant ARSET training URLs. Every gotcha links to its dataset concept.

---

## 5. Knowledge Layer (OKF Bundles)

### 5.1 Conformance

Open Knowledge Format v0.1 (github.com/GoogleCloudPlatform/knowledge-catalog): directory of markdown files; one concept per file; path is identity; `type` REQUIRED in frontmatter. This org additionally requires `title`, `description`, `tags`, `timestamp` on every concept; `resource` and an `## Uncertainty` section on dataset concepts; a `status` field on every concept (§5.6); and at least one `evidence` link on every gotcha and recipe. `index.md` at root (and per large subdirectory); `log.md` change history. Standard markdown cross-links; every gotcha links its dataset. Optional `trainings:` frontmatter (list of ARSET or equivalent training URLs) on dataset and recipe concepts.

### 5.2 Concept types

| type | Purpose | Required extras |
|---|---|---|
| dataset | Identity, access, structure, versions, uncertainty of one product | resource; version/baseline with verification date; ## Uncertainty section |
| dataset-gotcha | One trap: mechanism, wrong-result mode, correct approach, verification | severity (high/medium/low); link to dataset; ≥1 evidence link; severity high requires a matching eval case id |
| recipe | Validated analysis pattern | inputs; expected values AND expected-uncertainty ranges; validation provenance (evidence links) |
| convention | Cross-cutting practice | none |

### 5.3 Operations

**Ingest:** peculiarities discovered during any analysis are drafted as concepts immediately, human-approved, logged. **Query:** workflow skills consult relevant concepts before acting on a dataset. **Lint:** knowledge-linter, on demand and before releases.

### 5.4 Stewardship and review

Every bundle (and, in large bundles, every subdirectory) has named stewards in CODEOWNERS; PRs auto-request them. Merge rules: one steward review for any concept; two reviews (including a provider steward, on provider bundles) for high-severity gotchas and for any edit that changes severity, status, or an Uncertainty section. The review checklist (docs/steward-playbook.md): evidence links resolve and actually support the claim; severity is calibrated (high means silently wrong results); scope is minimal (one trap per concept); a reproduction or eval case exists where required; verification fields (`verified` date, `verified_by`) are set at approval. Stewards earn authorship on the bundle's Zenodo releases; onboarding follows the playbook plus the ARSET train-the-trainer methods pattern.

### 5.5 Population: four intake channels

1. **Mining:** the knowledge-seeder agent (§3.5) drafts candidates from steward-supplied authoritative sources, one evidence link per claim, `status: draft`.
2. **Elicitation:** steward interviews using the playbook's top-five-traps script; Openscapes-style knowledge hackdays; workshop and training Q&A capture.
3. **Operational ingest:** the analysis-time loop (§5.3), plus eval failures and support tickets, each opening a concept issue via the new_knowledge_concept template.
4. **Adoption:** importing existing curated caveat notes (for example, cookbook warnings) with attribution and evidence links.

Prioritization: the PO.DAAC arc first, then per-domain by usage. A dataset is **seeded** when its dataset concept exists (with Uncertainty section and verified access), every *known* high-severity trap is captured with evidence, and at least one recipe exists where a canonical workflow does. There are no numeric quotas: an evidence-free concept is worse than a gap.

### 5.6 Lifecycle and status

Required `status` on every concept: `draft` (unreviewed; consultable but voiced as unverified) → `verified` (steward-reviewed; `verified` and `verified_by` set) → `stale` (set by the linter past the staleness threshold, or by a steward on a product-baseline change; triggers re-verification) → `superseded` (kept for history with a `superseded_by` link) or `disputed` (linked open issue; skills MUST state the dispute when citing). A product baseline change (for example, a SWOT processing-version bump) triggers a steward sweep of that dataset's concepts. Skills surface status when citing: high-severity claims are voiced with their verification provenance.

### 5.7 Precedence, canonical home, and snapshots

The canonical home of provider knowledge is the provider bundle (e.g., nasa-daac-knowledge/podaac). Because plugins are self-contained (§0.5), they never reference it by path; instead each domain plugin ships a **pinned snapshot** of the relevant provider concepts under its own knowledge/, with the source repository and commit recorded in the bundle's index.md and refreshed at every plugin release (a documented copy step in the release checklist, not a runtime dependency). Precedence on conflict: the provider-bundle concept wins. Plugin-local concepts exist only for material not yet upstreamed and carry `upstream: pending`, which the linter flags after 60 days. Scientists may additionally point local.md's Knowledge block at any installed standalone bundles; those are consulted at query time alongside the snapshot.

### 5.8 Security posture: knowledge is declarative

Installed skills and knowledge bundles are an instruction supply chain into every user's agent, which makes a malicious or careless PR a prompt-injection vector. The rule: **concepts state facts about data; they never instruct the agent.** No imperatives directed at Claude, no tool-invocation directives, no meta-instructions inside concept bodies; skills treat concept content strictly as data to reason over. The knowledge-linter scans concepts for instruction-like phrasing and flags hits for steward review, and steward review of knowledge and skill PRs is understood as a security control, not only a quality control. Credentials never appear in any repo (Earthdata via ~/.netrc or connector configuration only).

---

## 6. Verification Layer (Golden Notebooks)

**Purpose:** executable regression tests for the computational recipes that workflow skills encode. They test the code paths and expected results, not LLM behavior (the three-surface harness tests behavior); together they are the safety net that lets build sessions run with a longer leash. **Scope rule:** golden notebooks cover workflow skills that encode a deterministic computational recipe (loaders, analyses, budgets, transport, and the report pipeline); pure-orchestration skills (start, discover-data) are exercised by the three-surface harness instead.

**Form:** marimo notebooks (pure Python, dataflow-deterministic, no hidden state) at `<plugin>/verification/<workflow_skill>.py`, one per workflow skill. Each: runs the skill's canonical computation against small fixed inputs (vendored under `verification/fixtures/` or synthesized in-notebook); asserts expected outputs including expected-uncertainty ranges where the matching recipe concept defines them; declares dependencies inline (marimo sandbox serialization) so `uv run verification/x.py` or plain `python verification/x.py` executes headless with a nonzero exit on assertion failure.

**Gates:** a workflow skill is not done until its golden notebook is green headless. CI runs all golden notebooks per plugin on PRs; the build harness runs the touched ones at session close.

```yaml
# .github/workflows/goldens.yml (per plugin)
on: [pull_request]
jobs:
  goldens:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v4
      - run: for f in verification/*.py; do uv run "$f"; done
```

**Fixtures:** synthetic fixtures are generated by `verification/fixtures/make_fixtures.py`; real-data fixtures are fetched by script with local caching and never committed above ~5 MB (no Git LFS). **Closure testing on subsets:** budget goldens assert pointwise closure (tendency equals flux divergence plus forcing at every grid cell), which is valid on any spatial subset; domain-integrated closure is asserted only on closed domains. **CI security:** golden workflows run on `pull_request` with no repository secrets exposed, and action versions are pinned by SHA before launch. **Fixture provenance:** each fixtures/ directory carries a README recording every file's source, version, and license or public-domain status.

**Demos and apps:** the conference demo gains a WASM (browser, zero-install) marimo companion; applied-science packs may ship stakeholder-facing marimo apps. Contributors are never required to author skills or knowledge in marimo; this layer is maintained alongside skills.

**Tutorials remain Quarto** (§7); marimo verifies and demonstrates, Quarto teaches.

---

## 7. Tutorials

As previously specified, plus: authored in Quarto rendering to the tutorials site; each tutorial header records surfaces verified (target all three, minimum Code plus one conversational); Tutorial 2 includes the SWOT section; `tutorials/templates/arset-style.md` provides the applied-tutorial template (objectives, intended audience, prerequisites linking ARSET Fundamentals where apt, 2-4 part session structure with per-part materials, a hands-on exercise, a completion checklist); Persona-6 tutorials use it. ARSET materials are linked with credit, never vendored; ARSET exercise code informs recipes and golden notebooks as an attributed source.

---

## 8. Evals Layer

**Purpose:** the third leg of testing. Golden notebooks (§6) verify code; the surface harness verifies packaging; evals verify **agent scientific judgment**: with the plugin and knowledge installed, does Claude apply area weighting, refuse budgets on regridded data, surface the SWOT cal/val gotcha, and report uncertainty? Evals are a quality and regression instrument for this system (skill edits, knowledge updates, model versions), not a model leaderboard: community benchmarks such as CBGB and TerraBench evaluate models on generic geospatial tasks, while these cases are derived from our own knowledge bundles and rules, which no external benchmark can cover.

**Case types:** gotcha-avoidance (one per high-severity gotcha, mandatory); rejection (the 🔴 rules and gates: native-grid refusal, volume gate); methodology (area weighting, trend-method choice, uncertainty statement present); recipe-fidelity (end-to-end result inside the recipe's expected range and spread).

**Case schema** (`evals/*.yaml`; each plugin's `evals/SCHEMA.md` documents it):

```yaml
id: native-grid-refusal
type: rejection            # gotcha-avoidance | rejection | methodology | recipe-fidelity
targets: [ocean-budget, gotchas/ecco-native-vs-regridded]
prompt: >
  Compute an ocean heat budget for the subpolar North Atlantic from the
  regridded 0.5 degree ECCO temperature file at {fixture}.
fixtures: [verification/fixtures/ecco_05deg_stub.nc]
graders:
  - programmatic: transcript_refuses_and_offers_native_grid
  - rubric: refusal-quality.md        # rubric-eval judge
trials: 5                             # 20 under the Phase-2 runner
pass_threshold: 0.8
```

**Grading:** programmatic checks on transcripts, produced code, and outputs wherever possible; rubric-based LLM judging (a port of the rubric-eval plugin) where judgment is required; periodic human calibration of the judge. **Stochasticity:** each case runs N trials and reports a pass rate with a binomial confidence interval; we apply our own uncertainty-reporting rule to ourselves.

**Placement:** cases live per-plugin in `evals/` beside `verification/`, versioned with the skills and knowledge they test. The runner, shared graders, suite manifests, and the published scoreboard (versioned JSON plus a static page, scored by model and plugin version) live in the org `evals` repo (Phase 2, Sessions 18-19).

**The ablation protocol (the headline experiment):** run the gotcha-avoidance suite with the knowledge bundle installed and with it removed, same model, same N; report the trap-hit-rate delta with intervals. This is the quantitative evidence for the knowledge-layer thesis, produced before outreach so the announcement carries numbers.

**Phase 1 vs Phase 2:** Phase 1 seeds the schema and eight cases (five ocean, three core) and records one manually graded trial per case in each plugin's `evals/RESULTS-seed.md`; Phase 2 delivers the runner, N-trial statistics, per-PR CI alongside the goldens, and the ablation.

---

## 9. Acceptance Criteria

Per-surface recording (Cd/Cw/Sc) for behavioral items in PROGRESS.md.

**Infrastructure:** org and all Phase-1 repos live with LICENSE/README/CITATION.cff; marketplace add and both installs work; zero `commands/` directories anywhere.

**Core:** 11 skills with conformant frontmatter, all descriptions ≤200 chars, `/doctor` clean; knowledge skills auto-load, the three user-invocable exceptions appear in the menu; start/discover-data/report pass slash (Code) and conversational (all three); report gate fires and Provenance cites concepts; report Results carry uncertainty statements or waivers; discover-data surfaces gotchas; knowledge-linter lints correctly and proposes-only; the core golden notebook (analysis_pipeline) passes headless; v0.1 behavioral criteria retained (area weighting, stated baselines, Mann-Kendall default, projection/colormap rules, six QC checks, CF metadata and DOI citations on outputs).

**Ocean:** ECCO grid auto-merge; native-grid refusal 🔴 intact; MHT at 26.5N within the recipe concept's expected range and spread; global heat budget residual at machine precision; geothermal omission caught via the gotcha; ShortNames verified (OCEAN_VEL); SWOT regional load with flag decoding and orbit-phase context, cal/val gotcha surfaced when the range spans it; volume gates fire on multi-GB requests; ecco-scout cites concepts; podaac-arc bundle lint-clean with Uncertainty sections on all four datasets and every gotcha linked; all four ocean golden notebooks green headless; end-to-end on each surface (question → scout → load → MHT → RAPID → report).

**Tutorials:** three tutorials complete in stated times on fresh installs with surfaces recorded; arset-style template exists and Tutorial 3 uses it for its applied variant; at least one live-ingested concept appears in a bundle log.md; WASM demo runs in a browser with no install.

**Evals (seed):** SCHEMA.md exists; core ships its 3 methodology cases and ocean its 5 cases covering every 🔴 rule and each high-severity gotcha; knowledge-linter flags a high-severity gotcha lacking a case; a manual grading pass (one trial per case, rubric-scored) is recorded in each plugin's evals/RESULTS-seed.md.

**Knowledge population and stewardship:** knowledge-seeder drafts a dataset-plus-gotchas set from supplied seed URLs with per-claim evidence and `status: draft`, and refuses to merge; every Phase-1 gotcha carries at least one resolving evidence link and `status: verified` with verifier fields set; steward-playbook.md and CODEOWNERS exist; the ocean bundle's index.md carries the snapshot source-metadata fields (placeholders until Session 17); the linter flags a gotcha lacking evidence and an `upstream: pending` concept older than 60 days; the imperative-phrasing scan runs clean on all Phase-1 concepts.

**External validation (restored in v0.6 per PARKING #3, operationalized in the Session 14 block):** at least one non-author scientist completes the end-to-end workflow (Tutorial 2) unaided, with friction notes captured in known-limitations.md. The launch announcement states its success criteria before posting (PARKING #1; the criteria live in docs/announcement-draft.md and the Phase-2 pre-registration).

---

## 10. Hydrology Plugin (Phase 2)

Spec detail for the outline's Sessions 15-17, written by the build per
harness rule 11 (v0.6). The bridge thesis: SWOT observes ocean and
inland water from one instrument; this plugin serves the hydrology
community from the same archive, knowledge discipline, and verification
practice as ocean-science. Install core first; ocean-science is not a
dependency.

### 10.1 Structure

```
hydrology/
├── .claude-plugin/plugin.json · .mcp.json · CONNECTORS.md
├── README.md · LICENSE · CITATION.cff
├── hydrology.local.md.template          # basins, gauges, gate, Knowledge block
├── skills/
│   ├── swot-hydro/SKILL.md + references/swot-hydro-products.md
│   │       # river reaches/nodes, lake products, the ocean/hydro product split
│   ├── grace-groundwater/SKILL.md       # TWS anomaly to groundwater, reusing 8b concepts
│   ├── nwis/SKILL.md                    # USGS streamflow via dataretrieval; provisional data
│   ├── smap/SKILL.md                    # soil moisture; radar-loss history
│   ├── load-swot-hydro/ · load-nwis/ · load-grace-tws/ · load-smap/
│   │       # gated loaders, same contract as load-ecco/load-swot
│   ├── drought-analysis/                # reads the drought recipe
│   └── reservoir-analysis/              # the ARSET-anchored applied workflow
├── agents/hydro-scout/agent.md          # same contract as ecco-scout
├── knowledge/                           # hydrology bundle (+ pinned podaac snapshot per §5.7)
│   ├── index.md · log.md
│   ├── datasets/{swot-river-lake, nwis-streamflow, smap-l3, grace-fo-mascons-snapshot}.md
│   ├── gotchas/{nwis-provisional-data, smap-radar-loss, swot-reach-node-scope, ...}.md
│   └── recipes/{drought-index, reservoir-storage-change}.md
├── evals/  (SCHEMA.md; gotcha-avoidance per high gotcha, volume-gate, recipe-fidelity)
├── verification/{load_swot_hydro, load_nwis, drought_analysis, reservoir_storage}.py
└── tutorials/quickstart.md
```

### 10.2 Knowledge bundle requirements

Same rules as §4.6/§5: Uncertainty sections on all datasets (SWOT
river/lake heights: node vs reach uncertainty variables; NWIS: rating
curves and provisional-to-approved revisions; SMAP: retrieval quality
flags and the radar loss; GRACE: snapshot of the 8b concepts per §5.7
with source and commit recorded). Known high-severity candidates from
the outline, each requiring evidence and an eval case: NWIS provisional
data silently revised after approval; SMAP radar loss (2015) changing
product lineage; SWOT reach-vs-node scope (statistics quoted at the
wrong aggregation level). The drought and reservoir recipes carry
expected values AND expected-uncertainty validated against gauge
records, with provenance.

### 10.3 Verification and evals

Golden notebooks per workflow skill on scripted, cached subsets (a
gauge-validated drought index over a named basin; reservoir storage
change against a published record); pointwise assertions with measured
tolerances per the verification guide. Eval seed: one case per
high-severity gotcha plus a volume-gate rejection and one
recipe-fidelity case; manually graded into RESULTS-seed.md exactly as
Phase 1.

### 10.4 Acceptance (Phase 2, hydrology)

Loaders gate and restate gotchas; provisional-data caveat surfaces on
any recent NWIS window; drought and reservoir analyses read recipes and
report uncertainty per the house rule; three-surface end-to-end
(question → scout → load → analysis → report) recorded per surface;
bundle lint-clean with verified_by set; goldens green headless.

### 10.5 Ocean-bundle v0.6 completion (scheduled into Session 18)

Per the PARKING triage: promote to severity-high gotchas WITH matching
eval cases: V4R4B release mixing (#9), MHT basin scope (#11), SWOT
crossover calibration unapplied (#13); author core's fill-value
detection eval case (#8); author the salt and volume budget recipes
with measured residual expectations (#12).

# Open Science Pillars: Specification

**Organization:** Open Science Pillars (github.com/open-science-pillars)
**Version:** 0.6.9 (one home for the ocean cases)
**Date:** 2026-09-04
**Scope:** Phase 1 (built; core + ocean-science + infrastructure + knowledge + verification + evals seed + stewardship) plus Phase 2 spec detail (hydrology bridge, §10)

**Changelog:**
- 0.6.9 (2026-09-04): the ocean eval cases have one home. The `ecco-agent-evals` repository, already the declared authority for the cases derived from steward-signed ECCO knowledge, is now their only location: its case headers carry both `concept_basis` (the signed concepts a case is graded against, by bundle path) and `targets` (the plugin skills a case exercises), and ocean-science 0.7.1 deleted its `evals/` copy, keeping only the regression fixture for its own briefing under `verification/fixtures/`. Section 8 Placement now admits a declared eval repository as a plugin's case home (the plugin's README and bundle index say so; the knowledge-linter's coverage rule reads cases from there), and the eval authoring guide drops the port. Plugins that author cases for their own material (core, hydrology) keep `evals/` as before.
- 0.6.8 (2026-09-04): the transitional pinned snapshot is gone. Every domain plugin now reaches provider knowledge only as the declared dependency (ocean-science 0.7.0 and hydrology 0.4.0 deleted their copies and `knowledge/snapshot.yaml`; `sync_check.py` retired with them), so section 5.7 loses its transitional paragraph and the pin rule, as that paragraph said it would, and the locality rule loses its snapshot clause. A plugin cites a provider concept by bundle path (`knowledge/podaac/<type>/<concept>.md`), which core's consult-knowledge convention resolves through the installer's record; a concept body that needs another bundle's concept names it the same way, in text, never by a relative link (§0.5).
- 0.6.7 (2026-09-04): provider knowledge reaches a plugin as a declared dependency, not a copy. The provider repository `nasa-daac-knowledge` is a catalog plugin (its bundles and tools, no skills) with calendar versions; a domain plugin declares `dependencies` in plugin.json (core, and the provider bundle with a version floor), and the installer installs, enables and updates the declared plugins with it. Section 0.5 replaces "install core first" with the declaration; section 2.2 shows the catalog with every entry's `ref` pinned to a release tag; section 2.3 states the one-command install and the by-name update; section 5.7 is retitled "Precedence, canonical home, and distribution" and states the release rule (bump, `{plugin-name}--v{version}` tag on a commit that owes no signatures, catalog ref move), keeps the locality rule, and carries the pinned snapshot as a transitional form until each plugin's next release drops it (marketplace issue #45). Amended the same day after the first real update: section 2.3 records what an update does not do (install a first-time dependency, move a rangeless one).
- 0.6.6 (2026-09-04): section 5.4 states the merge-then-sign rule: a steward's signature binds a concept's text as of the signing commit; an edit to signed text may merge before the re-sign, so that merges never wait on a signing calendar, and from that merge the concept owes a signature until a new `human:` event follows. The canonical repository's `tools/signature_check.py` measures the debt by the signing commit (not by dates), lists what is owed, and gates `run_checks.sh`; section 5.7's pin rule gains the same measure (`sync_check.py --refresh` refuses a commit at which the canonical bundle owes signatures, and the check reports PIN-OWED on a pin that does). The rule had been practised since 2026-09-02 and is now written (marketplace issue #41).
- 0.6.5 (2026-09-04): section 5.7 specifies the snapshot manifest (`knowledge/snapshot.yaml`: source repository, bundle path at the pinned commit, commit, date, copy directory, include or exclude scope), the check and refresh commands the canonical repository provides, the pin rule (a refresh pins a commit at which the canonical bundle owes no signatures, normally the steward's signing commit), and the locality rule (a local concept is one under `knowledge/` and outside the manifest's scope; local provider material carries `upstream: pending`, local domain material needs no key). Section 5.2 gains the `computation` row and the ownership rule for reference numbers (the attested computation owns them; the recipe cites). Section 1.1 gains the `ecco-agent-evals` and `ecco-budget-badge` rows. The eval case schema is documented once in the eval authoring guide and each plugin's `evals/SCHEMA.md` points there (section 8). Build-program labels leave the current text of sections 8 and 10; this changelog stays as written (marketplace issue #41).
- 0.6.4 (2026-09-03): the knowledge layer's remaining OKF v0.1 vocabulary is rewritten in the v0.2 form the bundles already carry (marketplace issue #6): section 5.1 names OKF v0.2, the `knowledge/` root, the root index `okf_version`, the `generated` event in place of `timestamp`, and `sources` cited by footnote in place of `evidence` links; sections 3.5, 5.2, 5.4, 5.5, 9 and 10.4 follow (approval adds the `verified` event; `status: stable` replaces `status: verified`). Section 5.6 stays CANDIDATE until v0.7 is cut but is now the vocabulary the rest of section 5 uses. Section 5.7 states that every repository keeping a bundle keeps it under `knowledge/`.
- 0.6.3 (2026-08-30): section 1.1 gains the `archive-observatory` row (tracking issue #22): structural sweeper, pyQuARC harness with pinned-tag receipts, deterministic attester, scheduled aggregate sweeps under the publication policy (aggregate-public, provider-detail private, badges opt-in). Repo-table addition only, per the 0.6.1 build-kit precedent; freeze intact, no other change.
- 0.6.2 (2026-07-06, development-model pass): the build record and development harness (IMPLEMENTATION-GUIDE, PROGRESS, PARKING, BUILD-HARNESS, README-START-HERE, and the knowledge-coupling migration record) relocated from `marketplace/docs` to the `build-kit` repo, co-locating them with the harness skills that read them; the §1.1 `build-kit` row and the §2.1 tree updated accordingly. `marketplace/docs` now holds only public-facing canonical docs, guides, and commitments. No Phase-1 scope change (freeze intact). Companion: `build-kit/docs/development-model.md` reframes future work as spec-anchored initiatives plus standing processes, retiring the single linear session sequence.
- 0.6.1 (2026-07-05, documentation and continuity pass): added the `build-kit` repo to the §1.1 table (the development harness, so the session protocol is no longer a personal-workspace single point of failure). Non-spec companion work in the same pass (not changing this spec's requirements): build-era artifact references removed from public-facing content; a user glossary and a docs map added; the newcomer and contributor doc paths repaired; broken cross-repo evidence links in the canonical knowledge bundle fixed. Driven by a five-persona documentation review.
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

**Codex status (2026-07-15):** native Codex distribution is a roadmap proposal,
not a current plugin-support claim. The organization maintenance harness runs
on Claude Code and Codex, while plugin manifests, clean-install verification,
and activation evals remain acceptance criteria for the proposed Codex surface.

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

### 0.5 Self-containment and declared dependencies

Plugins are cached and cannot reference files outside their own directory: no `../` paths between plugins; cross-plugin references are conceptual, never by path. What a plugin needs from another plugin it declares in plugin.json's `dependencies` (core for every domain plugin; the provider bundle plugin, with a version floor, for a plugin that builds on provider knowledge; §5.7), and the installer installs and enables the declared plugins with it. A README states the dependencies and the one install command; "install core first" is no longer a reader's step.

---

## 1. Infrastructure

### 1.1 Organization and repositories

**Org:** `open-science-pillars`

| Repository | Purpose | Phase |
|---|---|---|
| `marketplace` | Plugin catalog, governance, canonical docs (spec, architecture, guides) | 1 |
| `core` | Foundation plugin | 1 |
| `ocean-science` | Ocean domain plugin (ECCO + SWOT SSH; the PO.DAAC arc) | 1 |
| `tutorials` | Quarto tutorials, templates, demos | 1 |
| `plugin-template` | Scaffold for new domain plugins | 1 |
| `knowledge-template` | Scaffold for new OKF knowledge bundles | 1 |
| `.github` | Org profile, issue templates, CoC, governance | 1 |
| `build-kit` | Development harness: session/initiative skills, workspace-law template, bootstrap, DEVELOPING guide, workflows, and the build record (IMPLEMENTATION-GUIDE, PROGRESS, PARKING, BUILD-HARNESS) | 1 (infra) |
| `hydrology` | SWOT rivers/lakes, GRACE-FO, NWIS, SMAP | 2 |
| `nasa-daac-knowledge` | Per-DAAC provider bundles (podaac, esdis) and the bundle tools, shipped as one catalog plugin the domain plugins declare as a dependency (§5.7) | 2 |
| `archive-observatory` | Cross-archive metadata compliance observatory: sweeper, pinned pyQuARC harness, attester, scheduled aggregate sweeps; publication policy binding (aggregate-public, detail-private, badges opt-in); credential-free by CI-enforced invariant | 2 |
| `earthaccess-mcp` | SUPERSEDED: the planned wrapper is replaced by the upstream official server [nasa/earthdata-mcp](https://github.com/nasa/earthdata-mcp), already registered in ocean-science `.mcp.json`; its facts live in the podaac bundle as a connector concept (§5.9 candidate) | 2 |
| `evals` | Eval runner, shared graders, suite manifests, published scoreboard | 2 |
| `ecco-agent-evals` | Public, versioned eval cases derived from steward-signed ECCO knowledge, with transparent scoring and self-reported results; the one home of the ocean cases (ocean-science carries no copy) | 2 |
| `ecco-budget-badge` | Checkable ECCO budget closure: the attested heat budget's portable attester, a pinned copy of the sanctioned computation, and a CI badge any repository can carry | 2 |
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
    ├── design-knowledge-coupling.md # ADOPTED coupling design (feeds §5)
    ├── phase2-preregistration.md    # pre-registered go/stop conditions (public)
    ├── skill-authoring-guide.md     # frontmatter standard + budget rule
    ├── agent-authoring-guide.md
    ├── knowledge-authoring-guide.md # OKF concepts incl. Uncertainty sections, trainings links
    ├── eval-authoring-guide.md      # case schema, graders, trials and CI reporting (§8)
    ├── steward-playbook.md          # steward duties, review checklist, onboarding (§5.4)
    ├── verification-guide.md        # golden-notebook practice (§6)
    ├── connector-guide.md
    ├── surface-testing-guide.md     # three-surface harness + prompts/
    └── testing-guide.md
# The build record (IMPLEMENTATION-GUIDE, PROGRESS, PARKING, BUILD-HARNESS)
# now lives in the build-kit repo, not here.
```

### 2.2 marketplace.json

```json
{
  "name": "open-science-pillars",
  "version": "0.4.0",
  "description": "AI-assisted open science for earth, planetary, and applied science: skills, knowledge bundles, verification notebooks, and connectors for Claude Code, Cowork, and Claude Science.",
  "owner": { "name": "Open Science Pillars Community" },
  "author": { "name": "Open Science Pillars Community" },
  "homepage": "https://github.com/open-science-pillars",
  "plugins": [
    {
      "name": "core",
      "description": "Foundation: earth science data formats, statistics, uncertainty quantification, cartography, quality control, reproducibility, analysis review.",
      "source": { "source": "github", "repo": "open-science-pillars/core", "ref": "core--v0.4.0" },
      "tags": ["netcdf", "xarray", "cartopy", "geotiff", "zarr", "climate", "geospatial", "qc", "uncertainty", "reproducibility"]
    },
    {
      "name": "ocean-science",
      "description": "Physical oceanography: ECCO state estimate, SWOT SSH, meridional transport, budget closure, water masses.",
      "source": { "source": "github", "repo": "open-science-pillars/ocean-science", "ref": "ocean-science--v0.7.0" },
      "tags": ["oceanography", "ecco", "swot", "podaac", "amoc", "heat-transport", "sea-level"]
    },
    {
      "name": "hydrology",
      "description": "Hydrology: SWOT river and lake products, GRACE-FO groundwater, USGS NWIS streamflow, SMAP soil moisture.",
      "source": { "source": "github", "repo": "open-science-pillars/hydrology", "ref": "hydrology--v0.4.0" },
      "tags": ["hydrology", "swot", "rivers", "lakes", "nwis", "streamflow", "grace", "groundwater", "smap", "soil-moisture"]
    },
    {
      "name": "nasa-daac-knowledge",
      "description": "Provider knowledge bundles from NASA DAACs: PO.DAAC (ECCO, SWOT, GRACE-FO, MUR, NASA-SSH, RAPID) and the ESDIS metadata requirements. Facts about data, signed by their stewards; no skills. Installed automatically as a dependency of the domain plugins.",
      "source": { "source": "github", "repo": "open-science-pillars/nasa-daac-knowledge", "ref": "nasa-daac-knowledge--v2026.9.1" },
      "tags": ["knowledge", "okf", "podaac", "esdis", "ecco", "swot", "grace", "mur", "nasa-ssh", "metadata"]
    }
  ]
}
```

Every entry's `source.ref` names a release tag (§5.7), so an install resolves a release and never a moving branch; a release moves its entry's `ref` in a one-line catalog change. The `dependencies` field lives in each plugin's own plugin.json, where the plugin author owns it, not in the catalog. The catalog's refs shown here are the ones the entries carry once each plugin's first release under this rule is tagged; until then an entry names the latest existing tag. (v0.6 note: the `owner` object is required by the CLI's marketplace schema, and plugin entries use the `source` object form; a bare `repository: "owner/repo"` string is not an installable source type. Both were discovered during install testing.)

### 2.3 Install and update experience

```bash
claude plugin marketplace add open-science-pillars/marketplace
claude plugin install ocean-science@open-science-pillars
```

One install brings the plugin's declared dependencies with it (core and the provider bundle, §0.5). An install keeps the release it was installed from: it moves when the user updates the plugin by name (`claude plugin update ocean-science@open-science-pillars`, which carries the already-installed dependencies along within their ranges) or enables auto-update for the marketplace in `/plugin`. Two things an update does not do, observed on the first update after the dependencies were declared (2026-09-04): it does not install a dependency the new release declares for the first time (the plugin is then disabled with an error naming the `claude plugin install` command to run, and `/reload-plugins` in a session installs it), and it does not move a dependency declared without a range, which the user updates by name. A release that adds a dependency says so in its notes. `claude plugin list --json` reports each installed plugin's version and any dependency error, and is the check that a machine has what the repositories say it has.

Cowork: claude.com/plugins, or an unlisted marketplace by GitHub repo. Claude Science: add the marketplace and install, same as Cowork (observed 2026-07-04); connectors per session (surface-testing-guide.md documents the tested paths).

**Releases:** tagged releases of every repo are archived to Zenodo for a DOI; each CITATION.cff points at the repo's concept DOI so contributions are citable in the literature. Plugin release tags take the `{plugin-name}--v{version}` form (§5.7); the marketplace repository keeps bare `vX.Y.Z` tags.

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

As marketplace entry, expanded: name `core`, the release version (§5.7), Apache-2.0, homepage github.com/open-science-pillars/core.

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

**knowledge-linter** health-checks any OKF bundle in scope. Checks: `type` and `status` present; required fields present (title, description, tags, a `generated` event; resource and an `## Uncertainty` section on dataset concepts); legacy `timestamp`, `verified_by`, and `evidence` keys flagged as incomplete migration; every gotcha carries at least one `sources` entry cited from its body; links resolve; concepts reachable from index.md; `stale_after` dates that have passed; high-severity gotchas carry a matching eval case id (🟡 if absent); `upstream: pending` concepts older than 60 days flagged; `disputed` concepts with no linked open issue flagged; imperative-phrasing scan (concepts containing instructions directed at the agent are flagged, §5.8); contradiction scan flagged for human review. Proposes fixes as diffs; never modifies.

**knowledge-seeder** drafts concepts from authoritative sources. Given a dataset and steward-supplied seed URLs (product user guide, ATBD, known-issues page, provider forum threads, library release notes and issue trackers, ARSET Q&A documents), it drafts a dataset concept and gotcha candidates: every claim paraphrased with a `sources` entry cited by footnote, frontmatter `status: draft` with a `generated` event naming the seeder as actor, no log.md entry. MAY crawl only the supplied domains; MUST NOT invent or infer evidence (an unclear claim becomes an open question in the draft, not an assertion); MUST NOT merge anything. Steward review promotes draft to stable and adds the `verified` event (section 5.6).

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
├── (no evals/: the ocean cases live in ecco-agent-evals, §8 Placement)
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

Open Knowledge Format v0.2 (github.com/GoogleCloudPlatform/knowledge-catalog; the exact text is vendored in docs/upstream): a `knowledge/` directory of markdown files at the repository root (provider bundles at `knowledge/<provider>/`, §5.7); one concept per file; path is identity; `type` REQUIRED in frontmatter; the bundle-root `index.md` carries `okf_version: "0.2"` and is the only index that carries frontmatter. This org additionally requires `title`, `description`, `tags`, and a `generated: {by: <actor>, at}` event on every concept (actors are `human:`, `process:`, or `team:` prefixed, or `owner/tool`); `resource` and an `## Uncertainty` section on dataset concepts; a `status` field on every concept (§5.6); and at least one `sources` entry (`id`, `resource`, `title`) cited from the body by a `[^id]` footnote on every gotcha and recipe. `index.md` at root (and per large subdirectory); `log.md` change history. Standard markdown cross-links; every gotcha links its dataset. Optional `trainings:` frontmatter (list of ARSET or equivalent training URLs) on dataset and recipe concepts.

### 5.2 Concept types

| type | Purpose | Required extras |
|---|---|---|
| dataset | Identity, access, structure, versions, uncertainty of one product | resource; version/baseline with verification date; ## Uncertainty section |
| dataset-gotcha | One trap: mechanism, wrong-result mode, correct approach, verification | severity (high/medium/low); link to dataset; ≥1 `sources` entry cited from the body; severity high requires a matching eval case id |
| recipe | Validated analysis pattern | inputs; expected values AND expected-uncertainty ranges, cited by path from the attested computation that owns them where one exists; validation provenance (`sources` entries cited from the body) |
| computation | One attested computation: the sanctioned code identity, the manifested inputs, and the receipt of one run (OKF v0.2 §10) | code path with its sha; input manifest; receipt; the reference values and tolerances that recipes and findings quote |
| convention | Cross-cutting practice | none |
| finding | One falsifiable scientific claim, bound to the receipts, validity adjudication, and confrontation that support it (§5.10, v0.7 CANDIDATE) | question; claim with interval and receipt bindings; computations cited by receipt; validity adjudication; confrontation record; limitations; explicit status; `human:` signature and verdict IN before stable |

**Ownership of numbers.** Where a recipe and an attested computation describe the same analysis, the computation owns the reference values and tolerances (its receipt is the evidence) and the recipe cites them by path, quoting at most the headline value with that path beside it, so a re-run changes one file. A recipe with no computation carries its own expected values with their provenance. Findings follow §5.10: every number resolves to a receipt.

### 5.3 Operations

**Ingest:** peculiarities discovered during any analysis are drafted as concepts immediately, human-approved, logged. **Query:** workflow skills consult relevant concepts before acting on a dataset. **Lint:** knowledge-linter, on demand and before releases.

### 5.4 Stewardship and review

Every bundle (and, in large bundles, every subdirectory) has named stewards in CODEOWNERS; PRs auto-request them. Merge rules: one steward review for any concept; two reviews (including a provider steward, on provider bundles) for high-severity gotchas and for any edit that changes severity, status, or an Uncertainty section. The review checklist (docs/steward-playbook.md): `sources` resolve and actually support the claims that cite them; severity is calibrated (high means silently wrong results); scope is minimal (one trap per concept); a reproduction or eval case exists where required; the `verified: {by: human:<id>, at}` event is added at approval (§5.6), never by the drafting process. Stewards earn authorship on the bundle's Zenodo releases; onboarding follows the playbook plus the ARSET train-the-trainer methods pattern.

**Merge then sign.** A signature binds the concept's text as of its **signing commit**, the commit that introduced that `verified` event; the events themselves are the only lines a signature does not cover. An edit to signed text may merge before the steward re-signs (one steward review still merges it), so that a correction never waits on a signing calendar; from that merge the concept **owes a signature** until a new `human:` event follows, and the older events stay in the list as history. Owing is a debt, not a demotion: the concept stays `stable`, consumers keep citing it at its tier, and the steward clears the debt by appending an event after reading the diff since the signing commit. The debt is measured by commits, never by dates: the canonical repository's `tools/signature_check.py <bundle>` finds each stable concept's signing commit and compares that text with the text under test (`--at <commit>` for a historical state, `--diff` to read what changed), lists what is owed, and fails the gate (`run_checks.sh`) while anything is; a signature written but not yet committed is pending, not owed. A release tag lands on a commit that owes nothing (the bundle release checklist, step 1), and a transitional snapshot pins one (§5.7).

### 5.5 Population: four intake channels

1. **Mining:** the knowledge-seeder agent (§3.5) drafts candidates from steward-supplied authoritative sources, one cited source per claim, `status: draft`.
2. **Elicitation:** steward interviews using the playbook's top-five-traps script; Openscapes-style knowledge hackdays; workshop and training Q&A capture.
3. **Operational ingest:** the analysis-time loop (§5.3), plus eval failures and support tickets, each opening a concept issue via the new_knowledge_concept template.
4. **Adoption:** importing existing curated caveat notes (for example, cookbook warnings) with attribution and cited sources.

Prioritization: the PO.DAAC arc first, then per-domain by usage. A dataset is **seeded** when its dataset concept exists (with Uncertainty section and verified access), every *known* high-severity trap is captured with evidence, and at least one recipe exists where a canonical workflow does. There are no numeric quotas: an evidence-free concept is worse than a gap.

### 5.6 Lifecycle and status (v0.7 CANDIDATE: OKF v0.2 vocabulary)

> CANDIDATE language, drafted in the OKF v0.2 migration window
> (marketplace issue #6, 2026-08-30); it becomes normative when SPEC
> v0.7 is cut. The bundles and the rest of §5 already use this
> vocabulary (0.6.4). The vendored spec text in docs/upstream is the
> conformance reference meanwhile.

`status` on every concept is `draft` (unreviewed; consultable but voiced as unverified), `stable` (ready for consumption; the default when absent), or `deprecated` (kept for links and history; the OSP extension key `superseded_by` names the replacement). Trust lives outside status: steward approval adds a `verified: {by: human:<id>, at}` event (independent checks append to the list), and consumers derive the trust tier (unverified, machine-confirmed, human-reviewed) from the events, keyed on the `human:` prefix. Staleness is a date comparison: `stale_after` carries the sweep date and a concept is stale once now >= stale_after; a product baseline change (for example, a SWOT processing-version bump) pulls the date up and triggers a steward sweep of that dataset's concepts. A dispute is the OSP extension `disputed: <open issue URL>` on a stable concept; skills MUST state the dispute when citing. Skills surface status and tier when citing: high-severity claims are voiced with their verification provenance.

Migration mapping (SPEC v0.6 to OKF v0.2, applied to the bundles 2026-08-30):

| v0.6 status | v0.2 form |
|---|---|
| `draft` | `status: draft` |
| `verified` | `status: stable` plus a `verified: {by: human:<id>, at}` event |
| `stale` | `status: stable` plus `stale_after: <sweep date>` |
| `superseded` | `status: deprecated`, `superseded_by` kept as an extension key |
| `disputed` | `status: stable` plus `disputed: <issue-url>` (extension; no v0.2 equivalent) |

### 5.7 Precedence, canonical home, and distribution

The canonical home of provider knowledge is the provider bundle (e.g., nasa-daac-knowledge/knowledge/podaac; every repository that carries a bundle keeps it under knowledge/). The provider repository is itself a plugin in the catalog (`nasa-daac-knowledge`: its bundles and tools, no skills), and a domain plugin that builds on provider knowledge **declares** it in plugin.json with a version floor:

```json
"dependencies": ["core", { "name": "nasa-daac-knowledge", "version": ">=2026.9.1" }]
```

The installer resolves the declaration: installing the domain plugin installs and enables core and the provider bundle at the highest tagged release that satisfies every installed plugin's range, and updating the domain plugin moves its dependencies within their ranges. Nothing is copied between repositories. The plugin never references the bundle by path (§0.5); core's consult-knowledge convention finds every installed bundle through the installer's record of installed plugins at query time, and a bundle installed from a provider plugin is the provider tier. **The release rule:** a plugin release is a `version` bump in plugin.json on a commit at which its bundle owes no signatures (§5.4), an annotated git tag `{plugin-name}--v{version}` on that commit (`claude plugin tag --push` derives the name and checks the manifest and catalog agree; the marketplace repository itself keeps bare `vX.Y.Z` tags), and a catalog entry whose `source.ref` names the tag (§2.2). Provider bundles carry calendar versions (`2026.9.1`: year, month, release within the month, no zero padding, because the resolver reads semver); plugins carry ordinary semver. A domain plugin raises its floor when it needs a newer bundle and never pins an exact version, so a bundle correction reaches every install that updates, without a plugin release. Precedence on conflict: the provider-bundle concept wins; `stable` outranks `draft`; between two human events the later wins. **The locality rule:** a local concept is one under the plugin's own knowledge/. Local provider material (facts about a provider's products that belong in a provider bundle) carries `upstream: pending`, which the linter flags after 60 days; local domain material (the plugin's own recipes, computations and conventions) needs no key. Scientists may additionally point local.md's Knowledge block at any other installed bundle; those are consulted at query time alongside the declared ones.

**Citing across bundles.** A plugin's skills and agents name a provider concept by its bundle path, `knowledge/podaac/<type>/<concept>.md`, and a local concept whose body needs one names it the same way in text; neither uses a relative link, because the two bundles are separate installs (§0.5). The convention resolves the path against every installed bundle root at query time, so the citation is stable across releases while the text it reaches moves with the dependency. Code that runs a bundle's sanctioned files (a verification script, a badge) resolves the provider plugin's root from the installer's record (`claude plugin list --json`, the entry's `installPath`) and may accept an explicit checkout root as an override; it never walks a cache directory or assumes a sibling checkout.

### 5.8 Security posture: knowledge is declarative

Installed skills and knowledge bundles are an instruction supply chain into every user's agent, which makes a malicious or careless PR a prompt-injection vector. The rule: **concepts state facts about data; they never instruct the agent.** No imperatives directed at Claude, no tool-invocation directives, no meta-instructions inside concept bodies; skills treat concept content strictly as data to reason over. The knowledge-linter scans concepts for instruction-like phrasing and flags hits for steward review, and steward review of knowledge and skill PRs is understood as a security control, not only a quality control. Credentials never appear in any repo (an Earthdata Login lives in the environment, in ~/.netrc, or in connector configuration, and is needed only for downloads).

### 5.9 Connectors (v0.7 CANDIDATE: the REACH plane)

> CANDIDATE language, drafted alongside the connector work
> (marketplace issue #20,
> 2026-08-30); it becomes normative when SPEC v0.7 is cut.

A connector is the REACH plane only: the registration wire (`.mcp.json`) that gives an agent an interactive path to an external service. Three rules keep it in its plane. **Connector facts live in the bundle:** endpoint, transport, tool surface, auth boundary, and deprecation status are world-falsifiable claims, so they are recorded as a `connector` concept (an addition to the §5.2 type table) with sources, verification dates, and a `stale_after` matched to the service's announced flux; re-verification is a smoke run recorded at each steward sweep, and any endpoint, transport, or tool-surface change opens an issue before any doc changes. **Gates never depend on connectors:** verification tooling and attesters (verify_cmr, check_fields, the OKF v0.2 §10 attesters) call provider REST APIs directly, because deterministic receipt-producing checks cannot inherit an interactive service's availability or evolution. **Discovery never outranks signed knowledge:** an interactive catalog result may inform drafting and cross-checks, but a bundle claim (a Schema row, a ShortName, a caveat) changes only through the concept lifecycle (§5.6) with its own verification; UMM variable records describe intent, granules are ground truth. Skills state the graceful-degradation posture: when a connector is unavailable, knowledge-based discovery with archive URLs, said out loud.

### 5.10 Findings (v0.7 CANDIDATE: the unit of science)

> CANDIDATE language, drafted alongside the findings work
> (marketplace issue #38, 2026-09-02); it becomes normative when SPEC
> v0.7 is cut. Checker support is `check_okf_v02.py --findings`, off by
> default: without the flag no bundle changes behavior, and with it
> only `type: finding` concepts are touched.

A finding is the unit of science the stack otherwise lacks. Everything beneath it already exists: attested computations (OKF v0.2 §10) produce receipted numbers, the trend method gives them intervals, validity domains bound their scope, confrontations anchor them to independent observations, and signatures make them citable. A finding binds those into one falsifiable statement: the question asked, the claim made with its interval, the receipts it rests on, the validity adjudication, the observational confrontation, the limitations, and the steward's signature. Three rules keep it honest. **A finding is falsifiable:** one question, one claim with an interval, and a stated way to overturn it; a finding that cannot be wrong is not a finding. **A finding cites only receipted numbers:** every quantitative statement in it resolves, at the precision written, to a field of a receipt the finding cites, or to a declared context constant with a source; there is no number in a finding the reader is asked to take on faith. **A finding is never deleted:** retraction is a first-class position on the status ladder, kept for links and history with the reason on record, and a retracted finding is cited as history, never as a result.

#### 5.10.1 A finding is its own concept

Addition to the §5.2 type table:

| type | Purpose | Required extras |
|---|---|---|
| finding | One falsifiable scientific claim, bound to the receipts, validity adjudication, and confrontation that support it | question; claim with interval and receipt bindings; computations cited by receipt; validity adjudication; confrontation record; limitations; explicit status; `human:` signature and verdict IN before stable |

A finding is neither a recipe nor a computation. A recipe says how to compute; an attested computation is one receipted run of sanctioned code over a manifested data tree; a finding is what the run showed about the world, in a stated scope. The three have different lifecycles, which is why they are different types: a finding can be retracted while every computation it cites stays valid (the code was right and the receipt is faithful; the claim the numbers were read to support was not, or the record moved under it), and a computation can be superseded by a better method while the finding that cited it is re-derived and re-signed rather than withdrawn.

#### 5.10.2 The contract

A finding carries these frontmatter fields, all REQUIRED unless marked. Path-valued fields follow OKF v0.2 §6.2; a leading slash means bundle-relative, which is the form the bundles use.

- `question`: one sentence ending in a question mark. One finding answers one question.
- `claim`: the answer. `statement` (one sentence, the numbers in it written at the precision the receipt supports), `value`, `interval` (a two-element list, low then high), `confidence` (the level the interval is stated at), `units`, and `from`, which binds each of `value`, `interval`, and `confidence` to a dotted field path in one cited receipt. The bound values MUST agree with the receipt at the precision written in the finding; the finding never restates a number the receipt does not carry.
- `computations`: a non-empty list of `{concept, receipt}` pairs. Each concept is an Attested Computation in the bundle; each receipt is the JSON the sanctioned computation wrote for the run the finding rests on, stored in the bundle, carrying the `code_sha256` of that computation file and the manifest stamp of the data tree it read. The claim's receipt MUST be among them.
- `validity`: the adjudication of the claim against the bundle's validity domains. `declaration` (product, claim class, region, period, in the attester's vocabulary), `verdict` (`IN`, `OUT`, or `UNADJUDICATED`), `receipt` (the fitness receipt the attester wrote), and `governing` (the validity-domain concepts the receipt names). A finding whose declared claim is OUT of a signed domain fails; it cannot be stated at all.
- `confrontation`: `status: confronted` with `concept` (the confrontation computation), `receipt` (its receipt, which names the observational record by version or persistent identifier and carries both data-tree stamps), and `observation` (the dataset concept of the independent record); or `status: not-confronted` with a `reason` stated in a sentence. Not confronted is an honest state, never a silent one.
- `limitations`: a non-empty list of sentences, each a bound on where the claim holds or a caveat on how it was derived.
- `context` (optional): the constants a finding may quote that are not receipt outputs (a reference density, a grid count), each `{value, meaning, source}` where `source` is an id in `sources`. Everything quantitative that is neither a receipt field nor a context entry is an error.
- `status`: explicit, never defaulted, one of the OKF v0.2 values (§5.6); the ladder position (§5.10.3) is derived from it and the extension keys beside it.
- `stale_after` (SHOULD): a finding rests on a product release, so it carries the sweep date of that release's successor.
- `review` (optional): the URL of the open review; its presence places a draft under review.
- `retracted`, `superseded_by`, `disputed`: ladder keys, §5.10.3.

The body carries, in this order, `# Question`, `# Claim`, `# Evidence` (what each cited receipt contributes, in prose), `# Validity`, `# Confrontation`, `# Limitations`, `# What would overturn this` (the observation, recomputation, or record change that would falsify the claim), and, on a retracted finding, `# Retraction`. Numbers in the body obey the same rule as numbers in the frontmatter.

Illustrative frontmatter (the shape, with the names a provider bundle would use):

```yaml
type: finding
title: "The steric contribution to regional sea level rose over the record"
description: "In the registered box the steric part rose at +2.80 mm/yr over 312 months, 95 percent interval [+1.51, +4.09]."
question: "Did the steric contribution to sea level in the registered box rise over the model record?"
claim:
  statement: "Over the record the steric contribution rose at +2.80 mm/yr, 95 percent interval [+1.51, +4.09]."
  value: 2.7999
  interval: [1.5103, 4.0895]
  confidence: 0.95
  units: mm/year
  from:
    receipt: /references/retrieval/exhibit-regional-sea-level-record.json
    value: trend_steric_interval.trend
    interval: [trend_steric_interval.ci_low, trend_steric_interval.ci_high]
    confidence: trend_steric_interval.confidence
computations:
  - concept: /computations/ecco-regional-sea-level.md
    receipt: /references/retrieval/exhibit-regional-sea-level-record.json
validity:
  declaration: {product: ECCO_L4_SSH_LLC0090GRID_MONTHLY_V4R4, claim: trend, region: "35,45,-75,-65", period: "1992-01:2017-12"}
  verdict: IN
  receipt: /references/retrieval/fitness-regional-sea-level-record.json
  governing: [/validity-domains/ecco-large-scale-statistics.md]
confrontation:
  status: confronted
  concept: /computations/ecco-ssh-vs-altimetry.md
  receipt: /references/retrieval/exhibit-ssh-vs-altimetry.json
  observation: /datasets/altimetry-gridded-sla.md
limitations:
  - "The claim holds for the registered box only; nothing is stated outside it."
  - "The interval assumes a linear trend with lag-1 residual correlation (r1 0.89) and an effective sample of 17.6 months."
context:
  - {value: 1029, meaning: "Boussinesq reference density, kg per cubic metre", source: ecco-v4r4-doc}
status: draft
stale_after: 2027-06-30
sources:
  - id: ecco-v4r4-doc
    resource: https://doi.org/10.5281/zenodo.3765929
    title: ECCO Version 4 Release 4 documentation
```

#### 5.10.3 The status ladder

The ladder is derived, never declared: every position is an OKF v0.2 `status` value plus the OSP extension keys beside it, so an OKF consumer that knows nothing of findings still reads each one correctly (a draft is a draft, a deprecated concept is deprecated), and the conformance rule that an extension never changes the meaning of a spec field holds.

| position | frontmatter form | meaning |
|---|---|---|
| draft | `status: draft` | Stated, checker-clean, unsigned. Consultable, voiced as unverified. |
| under review | `status: draft` plus `review: <open review URL>` | A steward is reading it. Same trust as draft; the review is where the argument happens. |
| stable | `status: stable` plus a `verified: {by: human:<id>, at}` event, with `validity.verdict: IN` | The steward has signed that the claim is true in the stated scope. Citable as a result. |
| superseded | `status: deprecated` plus `superseded_by: <finding path>` | A later finding answers the question better (a longer record, a tighter interval, a corrected method). Kept for links; the replacement is cited. |
| retracted | `status: deprecated` plus `retracted: {at, by: human:<id>, reason, issue}` and a `# Retraction` section | The claim was wrong or can no longer be supported. Kept in the bundle and the index with the reason on record; cited only as history. |

`disputed: <open issue URL>` (§5.6) is a modifier on stable, not a position: the finding stays citable and the citation MUST state the dispute. Transitions are one edit each: a draft goes under review by adding `review`; it becomes stable by signature only (the `verified` event, and nothing else, moves a finding to stable, and the checker rejects a stable finding without one); a stable finding is superseded by landing the replacement and pointing `superseded_by` at it; any position goes to retracted by the retraction block, which is a steward's act (`by` is a `human:` actor) and names the issue where the retraction was decided. There is no path back from retracted; a corrected claim is a new finding that cites the retracted one in its history. A superseded finding is not retracted: its claim was right as far as it went.

#### 5.10.4 What the checker enforces

`check_okf_v02.py BUNDLE --findings [--explain]` adds these checks to a bundle's gate; codes beginning `F` are errors and codes beginning `FW` are warnings, on the same footing as E and W. `--explain` prints, for every finding, how each bound value and every number in the text resolved, so a reviewer reads the audit rather than trusting the verdict.

| code | rule |
|---|---|
| F1 | A required field is missing or malformed (question, claim and its keys, computations, validity, confrontation, limitations, explicit status). |
| F2 | The question is not one sentence ending in a question mark. |
| F3 | The claim is not bound: `from.receipt` missing or not JSON, a field path that does not resolve to a number, or a bound value, interval bound, or confidence that disagrees with the receipt at the precision written. |
| F4 | A cited computation is broken: the concept is missing or not an Attested Computation, the receipt is missing or not JSON, the receipt's `code_sha256` differs from the sanctioned computation file the concept names, or the receipt carries no verified data-tree stamp. |
| F5 | The claim's receipt is not among the finding's cited receipts. |
| F6 | The validity verdict is OUT (the claim lies outside a signed exclusion and cannot be stated), is not a known verdict, disagrees with the fitness receipt, is IN or OUT with no governing domain named, or names a governing concept that is not a validity domain the fitness receipt consulted. |
| F7 | A stable finding has no `human:` verified event, or its verdict is not IN. |
| F8 | The ladder is inconsistent: `retracted` without `at`, `by`, `reason`, and `issue`, or with a non-human `by`, or on a finding that is not deprecated, or without a Retraction section; `superseded_by` naming something that is not a finding, or on a finding that is not deprecated; deprecated without saying which. |
| F9 | A number in the finding's text resolves to no cited receipt field and no context entry (the rule below). |
| F10 | The confrontation record is incomplete: confronted without concept, receipt, and observation, or with a receipt that names no observational record by version or identifier or no data-tree stamps; not confronted without a reason. |
| FW1 | No `What would overturn this` section. |
| FW2 | A stable finding is not confronted against an independent observation. |
| FW3 | No `stale_after`. |
| FW4 | A cited computation is inline rather than a file, so receipt identity cannot be checked. |
| FW5 | The body links to a retracted finding. |

**The number rule (F9).** The checker scans `title`, `description`, `question`, `claim.statement`, every `limitations` entry, and the body. A numeric token (integer, decimal, thousands-separated, or exponent form, with an optional sign) must resolve to a numeric leaf of one of the cited receipts (the computation receipts, the fitness receipt, and the confrontation receipt) at the precision written: a token written to two decimals matches a receipt field within half a unit of its last written place, so `+2.80` matches `2.7999055` and `2.81` does not. A token followed by `%` or `percent` may also match a receipt fraction multiplied by one hundred; a signed token may match the receipt field's magnitude when the sign is carried by the prose (`runs 3.23 low` against a bias of `-3.2322`). Receipt lists longer than four numbers are series and are not matched, so a number cannot be justified by finding it somewhere in a time series. A token that matches a `context` entry's `value` resolves to that entry, which in turn must name a source. Exempt from the scan: fenced and inline code, footnote definitions and references, URLs, DOIs, hex digests of twelve or more characters, ISO timestamps, dates and years, list markers, and identifiers that mix letters and digits (a product ShortName, a grid name). The rule is mechanical on purpose: it does not judge whether a number is the right one to quote, only that the reader can find it in a receipt.

**What the checker does not do.** It never runs a computation or an attester and never recomputes a number. It verifies identity and agreement: that the receipt is the output of the named code (`code_sha256`), read a manifested tree (the stamp), and says what the finding says it says. Whether the receipt is a faithful product of the computation is the attester's question (OKF v0.2 §10.6), answered deterministically at review and again by any consumer at use; whether the claim is true is the steward's question, answered by signature. Passing the checker is necessary for a finding to be signed stable and is not evidence that it should be.

#### 5.10.5 How a consumer uses a finding (informative)

Skills cite a finding by path, with its position and tier voiced the way §5.6 voices status: a draft as an unverified statement of what the numbers show; under review with its review URL; stable with the signature; superseded by citing the replacement and saying so; retracted only as history, with the reason, never as a result. A number quoted from a finding is quoted through it, so the provenance a reader can follow runs quoted number, `claim.from`, receipt field, attested computation, manifested data tree, and each link is a file in the bundle. Briefings cite findings in preference to raw receipts once a finding exists for the claim, and inherit its limitations. The signature on a stable finding is the strongest credit-bearing event in the bundle (the credit derivation counts it distinctly from a signature on a gotcha or a recipe) because it attests a claim about the world rather than a fact about a product.

#### 5.10.6 Verification, attestation, and signature

Three different acts, kept apart. **Verification** is the checker: static, form and binding, runs in the gate, blocks the merge. **Attestation** is the receipt-level attester of each cited computation: deterministic, consumer-side, re-runnable, and the only thing that speaks to whether the receipt's numbers are what the sanctioned code produces. **Signature** is the steward's `human:` verified event, and it is the only thing that moves a finding to stable, because it attests what no tool can: that the claim is true in the stated scope and the limitations are the real ones. Two consequences follow. A finding cannot become stable until a signed validity domain admits its claim (the checker requires verdict IN, and an unsigned domain yields UNADJUDICATED), so the first stable finding in a bundle waits on the first signed domain that governs it. A stable finding may be unconfronted, with FW2 and a limitation that says so, because some claims have no independent record to confront; a confronted finding whose confrontation the steward has read is the stronger object, and briefings say which kind they cite. Any edit to a stable finding after signature obliges re-signature; the gate treats the signature as covering the text it was placed on.

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

**Case schema** (one YAML file per case; the eval authoring guide documents the fields once, and a plugin that carries cases keeps an `evals/SCHEMA.md` that points there; the ocean cases add `concept_basis`, the signed concepts by bundle path pinned to a provider commit):

```yaml
id: native-grid-refusal
type: rejection            # gotcha-avoidance | rejection | methodology | recipe-fidelity
targets: [ocean-budget]        # the plugin skills the case exercises
concept_basis: [knowledge/podaac/gotchas/ecco-native-vs-regridded.md]
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

**Placement:** a plugin's cases have one home. By default that is the plugin's own `evals/` beside `verification/`, versioned with the skills and knowledge they test. A plugin may instead declare an eval repository as the home of its cases, as ocean-science does with `ecco-agent-evals`: the plugin then carries no copy, its README and its bundle index name the repository, each case there names the plugin skills it exercises in `targets`, and a release of the plugin is run against the tagged case set; the knowledge-linter's coverage rule (a high-severity gotcha needs a matching case) reads the cases from the declared home. The runner, shared graders, suite manifests, and the published scoreboard (versioned JSON plus a static page, scored by model and plugin version) live in the org `evals` repo (Phase 2).

**The ablation protocol (the headline experiment):** run the gotcha-avoidance suite with the knowledge bundle installed and with it removed, same model, same N; report the trap-hit-rate delta with intervals. This is the quantitative evidence for the knowledge-layer thesis, produced before outreach so the announcement carries numbers.

**Phase 1 vs Phase 2:** Phase 1 seeds the schema and eight cases (five ocean, three core) and records one manually graded trial per case in each plugin's `evals/RESULTS-seed.md`; Phase 2 delivers the runner, N-trial statistics, per-PR CI alongside the goldens, and the ablation.

---

## 9. Acceptance Criteria

Per-surface recording (Cd/Cw/Sc) for behavioral items in build-kit/PROGRESS.md.

**Infrastructure:** org and all Phase-1 repos live with LICENSE/README/CITATION.cff; marketplace add and both installs work; zero `commands/` directories anywhere.

**Core:** 11 skills with conformant frontmatter, all descriptions ≤200 chars, `/doctor` clean; knowledge skills auto-load, the three user-invocable exceptions appear in the menu; start/discover-data/report pass slash (Code) and conversational (all three); report gate fires and Provenance cites concepts; report Results carry uncertainty statements or waivers; discover-data surfaces gotchas; knowledge-linter lints correctly and proposes-only; the core golden notebook (analysis_pipeline) passes headless; v0.1 behavioral criteria retained (area weighting, stated baselines, Mann-Kendall default, projection/colormap rules, six QC checks, CF metadata and DOI citations on outputs).

**Ocean:** ECCO grid auto-merge; native-grid refusal 🔴 intact; MHT at 26.5N within the recipe concept's expected range and spread; global heat budget residual at machine precision; geothermal omission caught via the gotcha; ShortNames verified (OCEAN_VEL); SWOT regional load with flag decoding and orbit-phase context, cal/val gotcha surfaced when the range spans it; volume gates fire on multi-GB requests; ecco-scout cites concepts; podaac-arc bundle lint-clean with Uncertainty sections on all four datasets and every gotcha linked; all four ocean golden notebooks green headless; end-to-end on each surface (question → scout → load → MHT → RAPID → report).

**Tutorials:** three tutorials complete in stated times on fresh installs with surfaces recorded; arset-style template exists and Tutorial 3 uses it for its applied variant; at least one live-ingested concept appears in a bundle log.md; WASM demo runs in a browser with no install.

**Evals (seed):** SCHEMA.md exists; core ships its 3 methodology cases and ocean its 5 cases covering every 🔴 rule and each high-severity gotcha; knowledge-linter flags a high-severity gotcha lacking a case; a manual grading pass (one trial per case, rubric-scored) is recorded in each plugin's evals/RESULTS-seed.md.

**Knowledge population and stewardship:** knowledge-seeder drafts a dataset-plus-gotchas set from supplied seed URLs with per-claim cited sources and `status: draft`, and refuses to merge; every Phase-1 gotcha carries at least one resolving source and `status: stable` with a `verified` event; steward-playbook.md and CODEOWNERS exist; the ocean bundle's index.md carries the snapshot source-metadata fields (placeholders until the snapshot pass); the linter flags a gotcha lacking sources and an `upstream: pending` concept older than 60 days; the imperative-phrasing scan runs clean on all Phase-1 concepts.

**External validation (restored in v0.6 per PARKING #3):** at least one non-author scientist completes the end-to-end workflow (Tutorial 2) unaided, with friction notes captured in known-limitations.md. The launch announcement states its success criteria before posting (PARKING #1; the criteria live in docs/announcement-draft.md and the Phase-2 pre-registration).

---

## 10. Hydrology Plugin (Phase 2)

Spec detail added at v0.6. The bridge thesis: SWOT observes ocean and
inland water from one instrument; this plugin serves the hydrology
community from the same archive, knowledge discipline, and verification
practice as ocean-science. It declares core and the provider bundle as
dependencies (§5.7); ocean-science is not one.

### 10.1 Structure

```
hydrology/
├── .claude-plugin/plugin.json · .mcp.json · CONNECTORS.md
├── README.md · LICENSE · CITATION.cff
├── hydrology.local.md.template          # basins, gauges, gate, Knowledge block
├── skills/
│   ├── swot-hydro/SKILL.md + references/swot-hydro-products.md
│   │       # river reaches/nodes, lake products, the ocean/hydro product split
│   ├── grace-groundwater/SKILL.md       # TWS anomaly to groundwater, reusing the podaac GRACE-FO concepts
│   ├── nwis/SKILL.md                    # USGS streamflow via dataretrieval; provisional data
│   ├── smap/SKILL.md                    # soil moisture; radar-loss history
│   ├── load-swot-hydro/ · load-nwis/ · load-grace-tws/ · load-smap/
│   │       # gated loaders, same contract as load-ecco/load-swot
│   ├── drought-analysis/                # reads the drought recipe
│   └── reservoir-analysis/              # the ARSET-anchored applied workflow
├── agents/hydro-scout/agent.md          # same contract as ecco-scout
├── knowledge/                           # hydrology bundle (provider concepts arrive as the declared dependency, §5.7)
│   ├── index.md · log.md
│   ├── datasets/{swot-river-lake, nwis-streamflow, smap-l3}.md   # grace-fo-mascons is the provider's, reached as the dependency
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
flags and the radar loss; GRACE: the podaac bundle's GRACE-FO concepts,
reached through the declared dependency per §5.7). Known high-severity candidates from
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
bundle lint-clean with `verified` events set; goldens green headless.

### 10.5 Ocean-bundle v0.6 completion

Per the PARKING triage: promote to severity-high gotchas WITH matching
eval cases: V4R4B release mixing (#9), MHT basin scope (#11), SWOT
crossover calibration unapplied (#13); author core's fill-value
detection eval case (#8); author the salt and volume budget recipes
with measured residual expectations (#12).

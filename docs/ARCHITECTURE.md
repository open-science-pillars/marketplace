# Earth & Planetary Science Agents: Consolidated Architecture (v4)

**Status:** Current strategy document, final set of 2026-07-03. All integration rounds (UQ/marimo/ARSET, evals, knowledge stewardship, launch hygiene) are merged into SPECIFICATION.md (now v0.5.1, frozen) and IMPLEMENTATION-GUIDE.md (now v2.3.3); Part 7's change list is retained for history but fully applied.

**The three decisions this version encodes:**

> **Current-scope note (2026-07-15):** this historical strategy defines the
> three Claude surfaces. Native Codex plugin distribution is tracked as a
> federated roadmap proposal and is not yet a supported plugin surface.

> **Current-scope note (2026-08-31):** Parts 1 through 8 are the strategy
> as written on 2026-07-03 and are left unedited. Part 9 records what the
> build changed, added, or left untested since, including the plane model
> this document predates and the provider-facing instruments it has no
> concept for.

1. **All three surfaces weighted equally.** Claude Science, Claude Code, and Claude Cowork are co-equal targets. Everything we build is surface-neutral markdown, packaged three ways, tested three ways.
2. **Remote sensing is the horizontal, not a vertical.** "Everything one would do in the remote sensing world" means remote sensing becomes a measurement-layer capability that every science domain consumes, spanning NASA, NOAA, Copernicus, USGS, commercial archives, and model outputs.
3. **The PO.DAAC arc is the strategic spine.** ECCO for depth, SWOT as the oceanography-to-hydrology bridge (matching the Science Enabling Teams transition), GRACE-FO and Sentinel-6 completing the set. Center-managed archive, center-built missions, two disciplines, one coherent story.

---

## Part 1: Surface Parity (What Equal Weighting Means Concretely)

Weighting all three surfaces equally is a design constraint, not a slogan. Here is what it changes.

### 1.1 One source of truth, three packagings

Every capability exists as plain markdown (skills, knowledge concepts) and thin code (connectors). Packaging is a build detail:

| Surface | Packaging | Install path | Invocation style |
|---|---|---|---|
| Claude Code | Plugin via marketplace.json | `claude plugin install <name>@<marketplace>` | Slash commands + conversational |
| Claude Cowork | Same plugin format | claude.com/plugins or direct upload | Conversational, task-oriented |
| Claude Science | Skills imported into workspace; connectors added to sessions | Skill import / connector config | Conversational, session-based, compute-aware |

### 1.2 Design rules that surface parity forces

**Commands no longer exist as a separate component.** On January 24, 2026, Anthropic merged slash commands into the Skills system: every skill automatically gets a slash-command interface, legacy `commands/` directories are deprecated (backward-compatible but flagged as legacy even in Anthropic's own plugin repo), and invocation behavior is controlled by skill frontmatter (`disable-model-invocation`, `user-invocable`). Rule for us: everything is a skill. Workflow skills (load-ecco, report, transport-analysis) keep both invocation paths open so they are reachable via slash on Code and conversationally on Cowork and Science from the identical file; safety for side-effectful steps (large downloads, report writes) comes from in-skill confirmation gates, not invocation gating, because `disable-model-invocation: true` would break conversational surfaces. Background expertise skills (data-formats, xarray-fundamentals) set `user-invocable: false` to auto-load without cluttering the menu. One hardening consequence: skill descriptions share a context budget (about 1% of the window), so descriptions must be short and keyword-rich; this is a SPEC requirement.

**No terminal assumptions in skill bodies.** Skills must not assume a shell, a working directory layout, or asciinema-style interaction. Where environment differences matter (file paths, credentials), the skill describes the requirement declaratively ("requires Earthdata Login; on Claude Code configure ~/.netrc; on Claude Science add the Earthdata connector to your session") rather than embedding one surface's mechanics.

**Compute is declared, not assumed.** Skills state the computational shape of a task (small: laptop-scale; medium: needs Dask; large: needs HPC or burst compute). Claude Science routes large jobs to configured HPC or Modal; Claude Code uses the local environment; Cowork handles small and medium. The skill text is identical everywhere.

**The knowledge layer is naturally surface-neutral.** OKF bundles are just files; every surface reads them the same way. This is a major reason the knowledge layer is load-bearing in v4.

### 1.3 The three-surface test matrix

Every skill and command gets a smoke test on each surface before it is marked complete. The PROGRESS tracker gains three status columns (Code / Cowork / Science) per item. The implementation guide gains a Session 0b that builds this test harness: a standard set of prompts per capability, run on each surface, with pass/fail recorded.

---

## Part 2: The v4 Taxonomy (Layers, Not a Flat List of Domains)

The v2/v3 flat list of domain plugins buried remote sensing as one vertical among seven. That contradicted how the field actually works: SAR, optical, altimetry, and gravimetry are techniques shared across ocean, land, ice, and planetary science. v4 restructures into layers.

```
┌─────────────────────────────────────────────────────────────┐
│  APPLICATIONS LAYER (applied science, decision support)     │
│  disasters · water-resources · agriculture · air-quality    │
│  · ecological-conservation                                  │
├─────────────────────────────────────────────────────────────┤
│  SCIENCE DOMAIN LAYER (discipline expertise)                │
│  ocean-science · hydrology · atmospheric-science ·          │
│  cryosphere · terrestrial-ecosystems · solid-earth ·        │
│  planetary-science                                          │
├─────────────────────────────────────────────────────────────┤
│  MEASUREMENT LAYER (how observations are made)              │
│  remote-sensing (optical, SAR/InSAR, altimetry, thermal,    │
│  imaging spectroscopy, lidar, passive microwave,            │
│  gravimetry, GNSS-R) · models-and-reanalysis ·              │
│  in-situ-networks                                           │
├─────────────────────────────────────────────────────────────┤
│  CORE LAYER (foundation)                                    │
│  data formats · xarray · statistics · cartography · QC ·    │
│  reproducibility · analysis-review                          │
├─────────────────────────────────────────────────────────────┤
│  KNOWLEDGE LAYER (OKF bundles, cuts across everything)      │
│  per-provider dataset knowledge: NASA DAACs · NOAA ·        │
│  Copernicus/ESA · USGS · model archives · PDS               │
└─────────────────────────────────────────────────────────────┘
```

### 2.1 The measurement layer (new in v4)

**`remote-sensing`** is the flagship measurement plugin. It holds technique skills that domains consume:

| Technique skill | Covers | Example missions/products |
|---|---|---|
| optical-multispectral | Reflectance, indices, cloud masking, ARD, STAC | Landsat, Sentinel-2, HLS, MODIS, VIIRS |
| sar-and-insar | Backscatter, calibration, terrain correction, interferometry, coherence | Sentinel-1, NISAR, OPERA products |
| radar-altimetry | Waveforms, retracking, SSH/water-level retrieval, crossovers | SWOT, Sentinel-6, Jason lineage, ICESat-2 (laser) |
| imaging-spectroscopy | Hyperspectral cubes, spectral libraries, unmixing, mineral/vegetation mapping | EMIT, AVIRIS, PACE OCI, CRISM (planetary) |
| thermal-ir | LST/SST retrieval, emissivity, ET | ECOSTRESS, MODIS/VIIRS thermal, Landsat TIRS |
| passive-microwave | Brightness temperature, soil moisture, sea ice, precipitation | SMAP, AMSR, GPM GMI, SMOS |
| lidar | Photon/waveform processing, canopy, elevation | ICESat-2, GEDI, 3DEP |
| gravimetry | Mascons vs harmonics, GIA, leakage | GRACE/GRACE-FO |

Each technique skill teaches the physics-adjacent processing knowledge (what calibration means, which corrections matter, what the standard preprocessing chain is) independent of any one archive. Domain plugins then compose them: hydrology uses radar-altimetry (SWOT rivers) + gravimetry (GRACE groundwater) + passive-microwave (SMAP); ocean-science uses radar-altimetry (SSH) + thermal-ir (SST); planetary-science reuses imaging-spectroscopy for CRISM.

**`models-and-reanalysis`** is the second measurement plugin, because you flagged model outputs as first-class data. It covers: reanalysis handling (ERA5, MERRA-2, and their known quirks), climate model output (CMIP6/ESGF: calendars, ensembles, scenario metadata, variant labels), operational forecast archives (GFS, HRRR via NOAA NODD), and state estimates as a category (ECCO stays in ocean-science for the deep science, but the general "how to treat model output" knowledge lives here).

**`in-situ-networks`** (stations, floats, gauges, flux towers) is deferred to a later phase; initial in-situ needs (Argo, NWIS) live inside their domain plugins and can be extracted later if duplication appears.

### 2.2 The applications layer (new in v4)

Applied science is explicitly in scope. Applications differ from research: the user is often serving an external stakeholder (a water manager, an emergency operations center), latency and defensibility matter more than novelty, and outputs are decision products, not papers.

Start with a single **`applied-science`** plugin containing theme skill-packs, splitting into separate plugins only when a theme's community materializes:

- **disasters**: flood extent (SAR + optical + SWOT), wildfire (active fire, burned area), volcano (InSAR deformation, ash), earthquake response (damage proxy)
- **water-resources**: reservoir and river monitoring (SWOT), drought (GRACE + SMAP + precipitation), snowpack
- **agriculture-food-security**: crop condition, ET, yield indicators
- **air-quality-health**: NO2/aerosol monitoring (TROPOMI, TEMPO), exposure summaries
- **ecological-conservation**: habitat change, land cover transitions

The tutorial model for this layer is NASA ARSET: short, applied, stakeholder-framed trainings. ARSET's decade of thematically organized trainings serves as the applications-layer curriculum spine (each pack names its anchor ARSET training), and our applied tutorials follow the ARSET session anatomy. Every dataset concept in the knowledge layer carries a required Uncertainty section, and applied decision products state uncertainty in stakeholder language.

### 2.3 Science domains (revised list)

`ocean-science`, `hydrology`, `atmospheric-science`, `cryosphere`, `terrestrial-ecosystems` (renamed from land-remote-sensing, since the remote sensing techniques moved down a layer), `solid-earth`, `planetary-science`. Each domain plugin composes measurement skills, adds discipline knowledge (the science interpretation, standard analyses, community conventions), and ships a knowledge bundle for its datasets.

### 2.4 The knowledge layer (unchanged from v3, now with provider structure)

Standalone OKF bundles organized by data provider, so the people who run each archive can own their bundle. Provider bundles are the canonical home; domain plugins pin release-time snapshots of the relevant concepts (source and commit recorded), keeping plugins self-contained while knowledge stays singly owned (SPEC §5.7):

```
nasa-daac-knowledge/
├── podaac/        # ECCO, SWOT, GRACE-FO, Sentinel-6, GHRSST gotchas
├── lpdaac/        # MODIS, HLS, EMIT, ECOSTRESS gotchas
├── gesdisc/       # IMERG, MERRA-2, AIRS gotchas
├── nsidc/         # ICESat-2, SMAP, sea ice gotchas
├── asf/           # Sentinel-1, NISAR, OPERA gotchas
└── ...            # ornl, laads, obdaac, asdc, sedac, ghrc
noaa-knowledge/    # NODD (GOES, HRRR), NCEI, OISST
copernicus-knowledge/  # Sentinels, CDS/ERA5, CMEMS
usgs-knowledge/    # Landsat Collection 2, NWIS, 3DEP
model-archives-knowledge/  # ESGF/CMIP6, NCAR RDA
pds-knowledge/     # PDS3 vs PDS4, ODE, SPICE, per-instrument quirks
```

---

## Part 3: The Strategic Spine (The PO.DAAC Arc)

Your center manages PO.DAAC, and your organization is transitioning Science Enabling Teams from oceanography toward hydrology. One mission embodies that exact transition: **SWOT serves both communities from the same archive.** This gives Phase 1 a story no generic plugin project has: the archive operator demonstrating AI-assisted science on its own holdings, across the exact disciplinary bridge its organization is walking.

**The arc, mission by mission:**

| Mission/Product | Archive | Discipline(s) | Why it anchors |
|---|---|---|---|
| ECCO V4 | PO.DAAC | Ocean | Depth: the hardest grid, budgets, everything from v2 carries forward |
| SWOT (KaRIn) | PO.DAAC | Ocean AND Hydrology | The bridge: SSH for oceanographers; river reach and lake products for hydrologists |
| GRACE-FO | PO.DAAC | Hydrology, Ocean, Cryosphere | Groundwater and mass change; center-built; rich gotchas (mascons, GIA, leakage) |
| Sentinel-6 MF | PO.DAAC | Ocean | Altimetry reference mission continuity |
| GHRSST/OISST | PO.DAAC/NOAA | Ocean | The everyday SST workhorse |
| EMIT, ECOSTRESS | LP DAAC | Terrestrial, Applied | Center-built instruments extending the story beyond one archive |
| NISAR, OPERA | ASF/LP DAAC | Solid earth, Hydrology, Disasters | Center-adjacent SAR products for the applied layer |

**Phase sequencing anchored on the arc:**

- **Phase 1 (PO.DAAC arc, ocean side):** core surface-parity hardening; ocean-science with ECCO (carrying forward all v2 spec work) plus SWOT SSH; radar-altimetry and gravimetry technique skills; `nasa-daac-knowledge/podaac` seeded with ECCO, SWOT, GRACE-FO, GHRSST concepts; earthaccess-mcp connector; three-surface testing.
- **Phase 2 (the bridge to hydrology):** hydrology plugin (SWOT rivers/lakes, GRACE-FO groundwater, SMAP, USGS NWIS, IMERG); passive-microwave technique skill; applied-science water-resources pack (drought monitoring demo: GRACE + SMAP + precipitation); this phase IS the Science Enabling Teams story, demonstrable to both communities.
- **Phase 3 (remote sensing breadth):** optical-multispectral and sar-and-insar technique skills; terrestrial-ecosystems domain; models-and-reanalysis plugin; lpdaac and asf knowledge; disasters pack (SAR flood mapping).
- **Phase 4 (planetary and expansion):** planetary-science plugin (PDS, SPICE, imaging-spectroscopy reuse for CRISM; connects to Bessel); pds-knowledge; remaining domains via community champions.

---

## Part 4: Repository Catalog (Expanded Beyond NASA)

Per your direction, NASA is key but not exclusive. The full set of archives our example-access work and knowledge bundles cover, grouped by provider:

**NASA (via earthaccess/CMR wherever possible):** the 12 DAACs as listed above; CMR-STAC for STAC-native discovery.

**NOAA:** NODD open data on AWS/Azure/GCP (GOES-R ABI, HRRR, GFS, NEXRAD); NCEI (climate records, GHCN); CoastWatch; National Water Model output.

**Copernicus/ESA:** Copernicus Data Space Ecosystem (Sentinel-1/2/3/5P); Climate Data Store (ERA5 and its known ERA5.1 fix for 2000-2006 stratosphere); Atmosphere Data Store; Copernicus Marine (CMEMS); ESA CCI climate records.

**USGS:** Landsat Collection 2 (and its Collection 1 to 2 QA-band bit-packing change); NWIS via dataretrieval; 3DEP lidar; ScienceBase.

**Model archives:** ESGF (CMIP6: calendars, ensemble variant labels, DRS structure); NCAR RDA; GMAO GEOS products.

**Cloud-native catalogs:** Microsoft Planetary Computer (STAC, broad mirror of the above); AWS Open Data registry; Google Earth Engine (noting its license constraints as a knowledge concept, since GEE terms matter for applied work).

**General repositories:** Zenodo, PANGAEA, Dryad (where scientists publish derived datasets our reproducibility skill should cite properly).

**Planetary:** PDS nodes (Geosciences via ODE, Imaging, Atmospheres, Small Bodies, Ring-Moon, Cartography); NAIF SPICE kernel archives; ESA PSA; JPL Horizons and SBDB; USGS Astrogeology (ISIS, Astropedia, planetary DEMs and mosaics; the ographic vs ocentric latitude trap gets its own knowledge concept).

Every archive above eventually gets: one access example, one or more OKF knowledge concepts, and inclusion in at least one tutorial. The PO.DAAC arc archives get all three in Phase 1-2; the rest follow the phase plan.

---

## Part 5: Personas (Revised: Six)

The five personas from v3 stand, with one addition and one adjustment.

**Added, Persona 6: The Applications Scientist.** Works at the science-to-decisions boundary: supports water managers, emergency responders, agricultural analysts. Needs defensible, timely, uncertainty-communicated products more than novel science. Primary surface: any (often Cowork for stakeholder deliverables, Science for the analysis behind them). Key artifacts: decision-support briefs, monitoring dashboards, event response summaries. Tutorial style: ARSET-like applied trainings. This persona is why the applications layer exists.

**Adjusted, Persona 1 (Research Scientist):** now explicitly includes the planetary variant (a Mars surface scientist working with CRISM cubes and SPICE geometry is the same persona shape with different knowledge bundles), and the surface note changes from "Claude Science primary" to "any of the three, per lab practice," consistent with equal weighting.

The other four (Data-Proximate Engineer, Program Manager/PI, Data Steward/DAAC Mentor, Student) are unchanged. The Data Steward persona gains prominence: with per-provider knowledge bundles, PO.DAAC stewards curating `nasa-daac-knowledge/podaac` is the flagship demonstration of the model, and it is a demonstration your organization can run internally before inviting other DAACs.

---

## Part 6: AI for Science Framing (One Page, Secondary Priority)

Per your direction: worth submitting, not the driver. The framing that fits both the program's call and this architecture:

**Project title:** "One Mission, Two Sciences: Provenance-Complete AI Workflows Across the SWOT Ocean-Hydrology Bridge"

**Pitch (short form):** SWOT observes both the ocean and the world's rivers and lakes from a single instrument, serving two scientific communities from one archive. We will build and openly release the skills, connectors, and dataset-knowledge bundles that let Claude conduct correct, provenance-complete analyses of SWOT (plus ECCO and GRACE-FO) across both disciplines: from data discovery through publication-quality artifacts. The dataset-knowledge layer (OKF bundles capturing the peculiarities that make naive analyses silently wrong) is the reusable contribution: a pattern any data provider can adopt so AI-assisted science stays correct on their holdings.

**Why it fits the call:** spans domains (oceanography, hydrology, applied water resources); produces open infrastructure others build on; has clear evaluation (agreement with expert-produced reference results, e.g., RAPID comparisons for ocean, gauge validation for rivers); and exercises real compute (SWOT granule volumes justify Modal/HPC credits).

**Deliverables:** the Phase 1-2 repositories, the podaac knowledge bundle, three persona tutorials, and the gotcha eval suite with a with/without-bundle ablation providing the quantitative evaluation.

Action: draft the application against this framing before July 15; roughly a half-day task given the material already in hand.

---

## Part 7: Change List for Existing Documents

**SPECIFICATION.md updates required:**
1. New Section 0: surface-parity requirements (packaging matrix, skills-unified invocation rules and frontmatter standard, declarative compute, credentials phrased per-surface, description-budget discipline).
2. §3/§4 plugin structures: add `knowledge/` directory (OKF bundle) to every plugin; specify OKF conformance (frontmatter with `type` required; `title`, `description`, `tags`, `timestamp` conventions; index.md and log.md per bundle).
3. Acceptance criteria: `commands/` directories are removed entirely; former commands are re-specified as workflow skills with frontmatter; every workflow skill must pass conversational invocation on all three surfaces; add per-surface columns.
4. Rename land-remote-sensing to terrestrial-ecosystems; add the two measurement plugins (remote-sensing, models-and-reanalysis) as new §5-level specs (Phase 2-3 scope; spec-level detail can be deferred to their build phases).
5. Add ocean-science SWOT SSH scope (load, QC, crossover-aware caveats) alongside ECCO; add hydrology plugin spec skeleton (Phase 2).
6. Add knowledge-maintenance operations spec: ingest, query, lint (the lint agent's checks: unresolved links, missing `type`, stale timestamps, contradiction flags).

**IMPLEMENTATION-GUIDE.md updates required:**
1. Insert Session 0b: three-surface test harness (standard prompt set, per-surface smoke-test procedure, PROGRESS columns).
2. Session 1: org rename decision reflected; add knowledge-template repo to scaffolding; add `knowledge/` dirs.
3. Session 6-10 (ocean): add SWOT alongside ECCO (one added session: "Session 8b: SWOT SSH + altimetry technique skill"); seed podaac knowledge bundle during these sessions (each gotcha discovered during testing becomes a concept file: the ingest loop, practiced from day one).
4. New Sessions 15-17 (Phase 2): hydrology plugin build (SWOT rivers/lakes, GRACE-FO, NWIS), passive-microwave skill, water-resources applied pack.
5. Session totals and calendar revised: Phase 1 approximately 30 hours, Phase 2 approximately 12 hours.

**PROGRESS.md updates required:** three-surface status columns; new sections for measurement plugins, knowledge bundles, hydrology, applied-science; phase relabeling per Part 3.

---

## Part 8: Open Items

1. **Org name: RESOLVED.** The organization is **Open Science Pillars** (github.com/open-science-pillars). The name captures the structure well: skills, knowledge bundles, verification notebooks, evals, connectors, personas, and tutorials are the pillars that hold up open, AI-assisted science across earth, planetary, and applied domains.
2. **PO.DAAC steward engagement:** who internally seeds and reviews the podaac knowledge bundle? Even two named reviewers makes the federated-knowledge story real from launch.
3. **Claude Science access for testing:** confirm workspace access so the three-surface harness can actually run against Science, not just Code and Cowork.
4. **AI for Science submission:** confirm go/no-go this week given the July 15 date.

---

## Part 9: What changed since v4 (added 2026-08-31)

This part is additive. Parts 1 through 8 are left exactly as written on
2026-07-03, because a strategy document's value is the record of what
was intended; where the build diverged, that divergence is recorded
here rather than edited into the original.

### 9.1 The missing axis: four planes, orthogonal to the five layers

The layer stack in Part 2 answers **which domain** a capability serves.
It does not answer **what kind of thing** a capability is, and that
second question turned out to be the one the build kept asking. The
answer that emerged, now documented in docs/knowledge-vs-skills.md and
the glossary and normative in the specification's connectors section
(docs/SPECIFICATION.md), is four planes:

- **KNOW**: concepts. Claims about the world with a truth condition, a
  named human signature, and a staleness date. Falsifiable by the
  world.
- **ACT**: skills. Agent behavior, evaluated rather than signed. Good
  or bad at a task, never true or false.
- **PROVE**: gates and attesters. Deterministic checks that emit
  receipts, with no language model anywhere in the path.
- **REACH**: connectors. The registration wire to an external service,
  and nothing more.

Every layer contains all four planes. The planes are how a
contribution finds its home; the layers are what it is about.

**PROVE is the plane this document never drew, and most of what was
built since lives there:** attested computations (sanctioned code an
agent may run but not alter, each run emitting a receipt checked
against a measured tolerance), the closure badge, validity domains
with a fitness attester answering can-I-use-X-for-Y, and a pinned
metadata harness. Golden notebooks (the specification's verification
layer) are not the same thing and do not cover it: a golden notebook
tests our own code in our own CI, while an attester verifies anyone's
run from a receipt they hand us. The distinction is load-bearing,
because the second is what makes a claim checkable by someone who does
not trust us.

The rule that keeps PROVE honest is worth stating at architecture
level: **gates never depend on connectors.** Verification tooling calls
provider APIs directly, because a deterministic, receipt-producing
check cannot inherit an interactive service's availability or
evolution.

### 9.2 A second audience: instruments for archives, not only scientists

All six personas in Part 5 are data consumers. The build produced a
second product line aimed at data producers, and this document has no
concept for it:

- a **metadata observatory** that checks an archive's records against
  written-down requirements and produces receipts, runnable by a
  producer against records that exist only on their laptop;
- a **credit loop** that mints DOI'd releases whose contributor lists
  derive mechanically from signature records, so reviewing and signing
  becomes citable scholarship rather than a favor;
- a **two-steward model** in which a provider's own people own the
  requirements bundle for their holdings.

These are not a new layer. They are the same layers viewed from the
other side of the archive counter, and they need governance no plugin
needs: a publication policy (aggregate public, provider detail private,
per-collection reporting only under written opt-in), and an
adversarial register reviewed on every change. That governance
graduated to org doctrine in docs/third-party-findings.md.

The Data Steward persona in Part 5 anticipated this audience but
scoped it to curating a knowledge bundle. Operating an archive is a
larger role, and it is the one the provider-facing instruments serve.

### 9.3 Corrections to Part 3

**The connector.** Phase 1 names an `earthaccess-mcp` connector to be
built here. It was superseded before it was written: NASA now publishes
an official CMR MCP server (nasa/earthdata-mcp), which is what the
plugins register. The row in the specification's repository table is
marked accordingly. The architectural point survives the substitution
and is stronger for it: the connector is REACH, its facts are KNOW (a
dated concept in the provider bundle), when to reach for it is ACT,
and PROVE ignores it.

**An interim to name before it calcifies.** Receipted regional sea
level briefings are an applications-layer product for the Applications
Scientist persona, and they currently live inside the ocean-science
domain plugin because the applied-science plugin does not exist yet.
That is a deliberate interim, not a judgment that decision products
belong in domain plugins.

### 9.4 What remains untested

Phase 1 exercised two of the five layers: science domain and knowledge,
on top of core. **The boldest claim in Part 2, that measurement is a
horizontal every domain consumes rather than a vertical, has never been
tested**, because no measurement plugin was built. The claim is not
contradicted by anything; it is simply unvalidated, and the first
technique skill shared by two domains is what would validate it.

### 9.5 Out of scope for this document

Named so their absence reads as a decision rather than an oversight:

- **Observatory internals.** Its adversarial register, publication
  policy, and tooling live in that repository and are owned there.
- **Program mechanics.** The kit, session, and wave structure used to
  sequence the build is private bookkeeping, deliberately kept out of
  artifacts a user reads, and out of this document too.
- **Outreach and stewardship conversations.** Relationship work, not
  architecture.
- **Credit-loop mechanics.** The derivation tool and release checklist
  are specified where they run; only the existence of the mechanism is
  architectural.

### 9.6 Distribution is the installer's job (added 2026-09-04)

Parts 1 through 8 describe what the organization builds and never say
how a build reaches a machine. The gap was measured on 2026-09-04: the
steward's own install still carried the plugins as they stood on
2026-07-06, because every gate in the program compared repositories
with repositories and none compared a repository with an install. Two
months of knowledge and tooling existed on main and nowhere else.

The correction is a division of labor. **The organization ships
declarations, not copies.** A provider knowledge repository is a
plugin in the catalog; a domain plugin declares what it depends on
(core, and the provider bundle with a version floor) in its manifest;
a release is a version bump, a tag in the form the installer resolves,
and a catalog entry that names the tag. Resolving those declarations,
fetching the right release, enabling the dependencies, and moving an
install forward are the installer's work, and the organization does
not rebuild any of it: no vendored copies of another repository's
bundle, no sync tooling to keep the copies honest, no "install this
first" in a README. What remains the organization's is the signature
discipline that makes a release trustworthy (a tag lands only on a
commit that owes no signatures) and the one check that closes the
measured gap: a machine's installed record, read where the plugins
stand, against the catalog. The specification's self-containment and
distribution sections carry the rules; the pinned snapshots Part 2
described survived only as a transitional form, retired in
ocean-science 0.7.0 and hydrology 0.4.0 with the sync tooling that
kept them honest.

### 9.7 The partner's name (added 2026-09-04)

Parts 1 and 3 call PO.DAAC's incoming partner teams the Science
Enabling Teams. ESDIS is renaming them the Application Support and
Science Enabling Teams (ASSETs): in the coming organization the
enterprise services support data providers through data stewardship
and end users through the ASSETs.
The frozen parts keep the older name as written; every current
artifact in the organization (the esdis requirement concepts, the
observatory's register and policy) uses ASSET, and the reading of
Part 3 is unchanged: the oceanography-to-hydrology transition those
teams embody is the same transition, under the new name.

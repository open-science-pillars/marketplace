# ADR A: Pillar means sphere

**Status:** proposed 2026-09-11; accepted when this record merges to main
after the cross-cutting review window (GOVERNANCE.md in the org `.github`
repository). Organizational implementation is sequenced behind a gate
stated below; nothing in this record starts that implementation.
**Decision owner:** Paul Ramirez (steward, pro tem). Personal-hat work:
Open Science Pillars is a personal open-source project, not a JPL or
PO.DAAC product.
**Design document:** [design-sphere-alignment-multi-runtime.md](../design-sphere-alignment-multi-runtime.md).
**Companion record:** [ADR B](adr-b-multi-runtime-capability-packaging.md),
which shares the canonical metadata this record introduces.
**Roadmap:** initiative `osp-architecture-alignment` in build-kit.

## Context

The organization's name carries a word the project has used three ways.
The org profile lists "three pillars" (skills, knowledge bundles,
verification). The knowledge-versus-skills guide says only KNOW can be
a pillar, because signatures attach to claims. Day-to-day usage has
meant a domain plugin. None of those readings tells a contributor which
scientific community a capability belongs to, and the repository table
in the specification lists domains (ocean, hydrology, planned
atmospheric science, cryosphere, terrestrial ecosystems, solid earth,
planetary science) as a flat list under a layer taxonomy that the build
has since found orthogonal to the question it kept asking.

Two things have changed since that table was written. The organization
now carries a second authority axis, provider bundles signed by their
stewards, that cuts across every domain. And the hydrology work has
produced capabilities (a basin water balance over four providers'
products, a coastal composite deferred to the ocean plugin) whose home
is a question about scientific community, not about layer.

## Decision

1. **Pillar means sphere.** A Pillar is one of the five Earth science
   spheres of NASA's Earth System Science Research Program:
   Atmosphere, Biosphere, Cryosphere, Geosphere, Hydrosphere. The
   earlier informal readings (pillar as domain plugin, pillar as the
   three product kinds, pillar as KNOW alone) are retired from
   organizational vocabulary. The three product kinds remain what they
   are; they are no longer called pillars.
2. **Spheres are the primary scientific taxonomy.** A discipline is a
   research area inside a sphere (Ocean Physics, Terrestrial Hydrology,
   Precipitation Science inside Hydrosphere). A domain capability is
   the installable unit organized around a discipline. Existing
   repository names (`ocean-science`, `hydrology`) do not change.
3. **Provider knowledge stays a separate authority axis.** A provider
   bundle is keyed by the organization that signs its facts (PO.DAAC,
   ESDIS, later USGS, NOAA, OpenET) and may serve several spheres.
   Sphere classification answers who asks; provider stewardship answers
   who signs. Neither overrides the other, and the methods-steward type
   the architecture document records (an applications office stewarding
   recipes and computations, not products) is a third steward type
   beside the provider and the enterprise service, not a sphere team.
4. **Classification is canonical under `.osp/`, not inside a runtime
   manifest** (implemented 2026-09-12: schemas and `osp.py` in
   build-kit, `build-kit/docs/osp-metadata.md`). Every non-archived repository declares its kind
   (foundation, provider, capability, composite, tooling), status
   (planned, scaffold, developing, available), spheres, primary sphere
   and discipline in `.osp/repository.yaml`. GitHub topics, the org
   profile's sphere view, the marketplace catalog's classification and
   any runtime manifest are rendered from that file and validated
   against it.
5. **Scientific concepts carry sphere tags.** A concept's frontmatter
   gains `spheres` (one or more sphere values, required on every type
   except `requirement` and `connector`; the checker rejects an untagged
   one) and optional `gcmd`. The tags state the scope of the claim; they
   do not move steward authority, and they sit outside the text a
   steward's signature binds: the signature check ignores `spheres` and
   `gcmd` the way it ignores the `verified` events, so tagging a signed
   concept creates no signature debt. A foundation bundle whose
   concepts serve every sphere (core's conventions) declares
   `sphere_scope: cross-cutting` in its root index and its concepts
   carry an empty list. Implemented 2026-09-12.
6. **A composite is a capability whose evidence genuinely crosses
   spheres.** It stays a scaffold until it has its own steward, joint
   knowledge and sufficient validation. An interdisciplinary recipe
   whose governing evidence stays in one sphere is not a composite: the
   basin water balance is Hydrosphere, and coastal compound flooding is
   Hydrosphere while its evidence stays there.
7. **The target repository map is 24 non-archived repositories.** Ten
   foundation and tooling (`marketplace`, `core`, `plugin-template`,
   `knowledge-template`, `build-kit`, `evals`, `tutorials`, `.github`,
   `archive-observatory`, and `agent-evals` renamed from
   `ecco-agent-evals`); two provider (`nasa-daac-knowledge`,
   `partner-knowledge`); eleven domain capabilities (`ocean-science`,
   `hydrology`, `precipitation` in Hydrosphere; `land-ice`, `sea-ice`
   in Cryosphere; `solid-earth`, `land-surface` in Geosphere;
   `atmospheric-composition`, `atmospheric-physics` in Atmosphere;
   `land-ecosystems`, `ocean-biology` in Biosphere); one cross-sphere
   `composites`. `ecco-budget-badge` is retired and archived with a
   pointer. `archive-observatory` is in the tooling group but is
   classified on its own terms, not by sphere: it is an instrument for
   data engineers and archive operators (the architecture document's
   second audience), and its `repository.yaml` carries kind tooling
   with no sphere.
8. **Planned repositories are honest and never installable.** A planned
   repository holds a README with an explicit banner, LICENSE,
   `.osp/repository.yaml`, `.osp/governance.yaml`, CODEOWNERS and
   generated topics, and nothing installable: no skills, no package or
   surfaces manifest, no runtime manifest, no catalog entry, no
   release, no CITATION.cff. Creating one is administrative; promoting
   one out of planned is governed work.
9. **Per-product tooling does not grow one repository per product.**
   Decided 2026-09-12 (the rationale is under Open items, kept as the
   record of the choice). `ecco-budget-badge` is retired: its reusable
   workflow and badge writer move beside the canonical attester in the
   provider bundle, pinned by that repository's release tag, and the
   repository is archived with a pointer. `ecco-agent-evals` stands
   alone as the organization's one benchmark repository, renamed
   `agent-evals`, with its charter kept and the ECCO cases in a
   product subtree so later products' cases join under the same
   charter; `evals` stays the runner, graders and scoreboard. The
   design document's `badges` rename and `evals/products/ecco/` move
   are superseded by this.
10. **Governance gains sphere teams, provider steward teams and runtime
    maintainer teams.** CODEOWNERS moves from individuals to teams. One
    person may occupy several teams during the interim solo period, and
    review-enforcing rulesets stay off until the governance
    preconditions already recorded are met.
11. **The polyrepo organization remains.** No monorepo, no rename of the
    organization, and no upstream or vendoring tree.

## Sequencing

The decision records and the dated Phase-2 pre-registration amendment
merge first. Every other step (canonical metadata, consolidation,
teams, documentation alignment, planned repositories) was gated on the
first tranche of the roadmap's `hydrology-investigations` initiative:
its P0 deliverables (`hydro-usgs-waterdata-migration`,
`hydro-basin-unit`, `hydro-p-et-connectors`, `hydro-w1-basin-balance`).
**The gate was met on 2026-09-12:** the owner confirmed it against the
sphere alignment plan the tranche was built from, and the roadmap
records the four deliverables done with their release tags as
evidence. Implementation of the canonical metadata milestone may begin
when its proposal is accepted.

## Consequences

- The org profile, the marketplace README, the specification's
  repository table, the glossary and the contributor guide are rewritten
  in the documentation milestone so that no "pillar means plugin" or
  "three pillars" wording survives.
- The specification's repository table currently lists `remote-sensing`,
  `models-and-reanalysis`, `applied-science`, `planetary-science` and
  `pds-knowledge` as later phases. The five spheres are an Earth
  science taxonomy. Planetary work is pushed off and may belong in a
  separate organization; that question is held on marketplace issue
  #80 so the rows are neither dropped silently nor left implying a
  plan. The measurement and applications layers are layers, not
  spheres; the documentation milestone states where those rows go.
- A snow concept tags both Hydrosphere and Cryosphere; a GRACE mass
  concept tags Hydrosphere and Geosphere; precipitation is Hydrosphere
  primary with Atmosphere secondary. Multiple `osp-sphere-*` topics are
  applied where a repository touches several spheres, and
  `primary_sphere` stays canonical in the metadata file.
- The roadmap's declared repository list does not yet include
  `archive-observatory`, `ecco-budget-badge` or `ecco-agent-evals`; the
  consolidation milestone's deliverables are therefore carried by the
  `marketplace` and `evals` entries until the list is reconciled.

## Open items

Two per-product repositories needed a decision. Both were put to the
owner with the recommendation below and decided as recommended on
2026-09-12; the roadmap's `m2` deliverables carry the moves. The
reasoning stays here as the record of why.

- **`ecco-budget-badge`.** The repository carries verbatim copies of the
  sanctioned computation and attester that live in the provider bundle,
  a badge writer, and a reusable workflow. The copies exist so an
  adopter can pin the attester by tag; that is the vendored-copy form
  the organization retired elsewhere in favor of declarations, and a
  badge is only the attester's verdict rendered by shields.io.
  Decision: retire it. The reusable workflow moves beside the
  attester it calls (the provider bundle's tools, pinned by that
  repository's release tag) and the badge writer with it; the
  repository is archived with a pointer. The basin water balance then
  needs no second badge repository either.
- **`ecco-agent-evals`.** A benchmark with its own charter: cases cite
  signed concepts by path and commit, releases are tagged sets, results
  are self-reported with transcripts, and the core linter reads ocean
  eval coverage from it. It is not redistributed as a package. Folding
  it into the `evals` repository would tie a benchmark's version
  history and citation to the runner's release cadence and put
  published results beside tooling. Decision: it stands alone, but as
  the organization's one benchmark repository rather than one per
  product: renamed to a product-neutral name (`agent-evals`), keep
  the charter, and give the ECCO cases a product subtree so the
  hydrology cases can join under the same charter when they are ready
  to publish results. `evals` stays the runner, graders and scoreboard.

## Not decided here

GCMD keywords stay optional. Whether external provider staff become
organization members in steward child teams or remain outside
collaborators is the open governance question before enforcement. The
IMERG transition (connector and skill in hydrology, provider facts in
the provider bundle from the start) stays as the pre-registration
records it.

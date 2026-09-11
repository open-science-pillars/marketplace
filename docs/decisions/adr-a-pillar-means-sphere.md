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
   manifest.** Every non-archived repository declares its kind
   (foundation, provider, capability, composite, tooling), status
   (planned, scaffold, developing, available), spheres, primary sphere
   and discipline in `.osp/repository.yaml`. GitHub topics, the org
   profile's sphere view, the marketplace catalog's classification and
   any runtime manifest are rendered from that file and validated
   against it.
5. **Scientific concepts carry sphere tags.** A concept's frontmatter
   gains `spheres` (one or more sphere values, required for scientific
   concepts; the linter rejects an untagged one) and optional `gcmd`.
   The tags state the scope of the claim; they do not move steward
   authority.
6. **A composite is a capability whose evidence genuinely crosses
   spheres.** It stays a scaffold until it has its own steward, joint
   knowledge and sufficient validation. An interdisciplinary recipe
   whose governing evidence stays in one sphere is not a composite: the
   basin water balance is Hydrosphere, and coastal compound flooding is
   Hydrosphere while its evidence stays there.
7. **The target repository map is 24 non-archived repositories.** Ten
   foundation and tooling (`marketplace`, `core`, `plugin-template`,
   `knowledge-template`, `build-kit`, `evals`, `tutorials`, `.github`,
   `archive-observatory`, and `badges` renamed from `ecco-budget-badge`);
   two provider (`nasa-daac-knowledge`, `partner-knowledge`); eleven
   domain capabilities (`ocean-science`, `hydrology`, `precipitation`
   in Hydrosphere; `land-ice`, `sea-ice` in Cryosphere; `solid-earth`,
   `land-surface` in Geosphere; `atmospheric-composition`,
   `atmospheric-physics` in Atmosphere; `land-ecosystems`,
   `ocean-biology` in Biosphere); one cross-sphere `composites`.
   `ecco-agent-evals` is archived after its cases move to
   `evals/products/ecco/` and stays visible with a pointer.
8. **Planned repositories are honest and never installable.** A planned
   repository holds a README with an explicit banner, LICENSE,
   `.osp/repository.yaml`, `.osp/governance.yaml`, CODEOWNERS and
   generated topics, and nothing installable: no skills, no package or
   surfaces manifest, no runtime manifest, no catalog entry, no
   release, no CITATION.cff. Creating one is administrative; promoting
   one out of planned is governed work.
9. **Per-product tooling is consolidated before it multiplies.**
   `ecco-budget-badge` becomes `badges`, an attestation service that
   takes a product workflow as input; `ecco-agent-evals` moves into
   `evals/products/ecco/` preserving concept basis, expected behavior,
   deterministic checks and historical result equivalence.
10. **Governance gains sphere teams, provider steward teams and runtime
    maintainer teams.** CODEOWNERS moves from individuals to teams. One
    person may occupy several teams during the interim solo period, and
    review-enforcing rulesets stay off until the governance
    preconditions already recorded are met.
11. **The polyrepo organization remains.** No monorepo, no rename of the
    organization, and no upstream or vendoring tree.

## Sequencing

The decision records and the dated Phase-2 pre-registration amendment
merge now. Every other step (canonical metadata, consolidation, teams,
documentation alignment, planned repositories) begins after the first
tranche of the roadmap's `hydrology-investigations` initiative lands.
This record reads that tranche as the initiative's P0 deliverables
(`hydro-usgs-waterdata-migration`, `hydro-basin-unit`,
`hydro-p-et-connectors`, `hydro-w1-basin-balance`) recorded done in
the roadmap with evidence. The gate is not removed silently: a later
dated record must say so if it moves.

## Consequences

- The org profile, the marketplace README, the specification's
  repository table, the glossary and the contributor guide are rewritten
  in the documentation milestone so that no "pillar means plugin" or
  "three pillars" wording survives.
- The specification's repository table currently lists `remote-sensing`,
  `models-and-reanalysis`, `applied-science`, `planetary-science` and
  `pds-knowledge` as later phases. The five spheres are an Earth
  science taxonomy: planetary work has no sphere, and the measurement
  and applications layers of the architecture document are layers, not
  spheres. The documentation milestone must state where each of those
  rows goes (a sixth organizational group outside the spheres, a
  composite, or a retirement) rather than drop them; this record does
  not decide it.
- A snow concept tags both Hydrosphere and Cryosphere; a GRACE mass
  concept tags Hydrosphere and Geosphere; precipitation is Hydrosphere
  primary with Atmosphere secondary. Multiple `osp-sphere-*` topics are
  applied where a repository touches several spheres, and
  `primary_sphere` stays canonical in the metadata file.
- The roadmap's declared repository list does not yet include
  `archive-observatory`, `ecco-budget-badge` or `ecco-agent-evals`; the
  consolidation milestone's deliverables are therefore carried by the
  `marketplace` and `evals` entries until the list is reconciled.

## Not decided here

GCMD keywords stay optional. Whether external provider staff become
organization members in steward child teams or remain outside
collaborators is the open governance question before enforcement. The
IMERG transition (connector and skill in hydrology, provider facts in
the provider bundle from the start) stays as the pre-registration
records it.

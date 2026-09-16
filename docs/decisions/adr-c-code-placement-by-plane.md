# ADR C: Code placement by plane

**Status:** Accepted 2026-09-16 (merged to main) by the decision
owner; implemented 2026-09-16. The placement gate is build-kit pull
requests 63 and 64; the migrations are ocean-science 63, hydrology 73,
nasa-daac-knowledge 183, plugin-template 21 and knowledge-template 12.
The energy budget and ice sheet balance computations stay unwrapped
until the atmospheric-physics and land-ice packages exist (roadmap
c6-unwrapped-computations); core's gate step and the wrap of its
reference computation in basic-statistics are core pull request 45.
**Decision owner:** Paul Ramirez (interim steward). Personal-hat work:
Open Science Pillars is a personal open-source project, not a JPL or
PO.DAAC product.
**Companion records:** [ADR A](adr-a-pillar-means-sphere.md) (the
four planes) and [ADR B](adr-b-multi-runtime-capability-packaging.md)
(one canonical `skills/` tree rendered to every runtime). This record
applies their vocabulary to files of code.
**Specification:** the placement rule, the wrapping rule and the
placement gate (docs/SPECIFICATION.md, revision 0.6.19).
**Roadmap:** initiative `osp-architecture-alignment` in build-kit, one
deliverable per repository migration below.

## Context

A survey of core, nasa-daac-knowledge, hydrology and ocean-science on
2026-09-16, after round three of seeding, found Python in five homes
with five meanings:

| Home | What is there | Plane served |
|---|---|---|
| `knowledge/<bundle>/references/{computations,attesters,loaders,retrieval}` | executors, attesters, loaders, stamped data roots (about 17,000 lines in nasa-daac-knowledge, 3,400 in ocean-science, 1,300 in hydrology) | the KNOW contract, its ACT executor, its PROVE attester |
| `knowledge/<bundle>/references/skills/run-*.md` | run instructions as OKF `type: Reference` concepts, with status and signatures (four files: sea level budget, Argo OHC, energy budget, ice sheet balance) | ACT, packaged and signed as KNOW |
| `verification/` | goldens, and in hydrology nineteen fixture builders and loaders under `verification/fixtures/`, seven of which skills invoke at runtime through the plugin root | PROVE, with ACT helpers filed beside it |
| `skills/<name>/*.py` | two scripts in ocean-science at the skill's root (the receipt renderer; a byte-identical copy of the citation tool) | ACT |
| `tools/`, `connectors/` | repository gates; MCP servers and captures | gates; REACH |

The model already rules on the planes: an Attested Computation is
split, its contract KNOW, its executor ACT, its attester PROVE, and
the upstream specification says it fixes the interface and not the
packaging. The survey found the code placed consistently with that
ruling and the procedures placed against it, with one measurable
consequence: no skill in any capability wraps the Argo ocean heat
content, energy budget, ice sheet balance or thirteen ECCO
computations. An agent working in ocean-science has nothing that fires
on "energy budget closure" or "ice sheet mass balance"; it reaches
those computations only by reading the concept through
consult-knowledge. Hydrology's `basin-water-balance` skill, which
points at the bundle's executor through the plugin root, is the one
place the intended shape exists.

Two smaller findings follow the same cause. Hydrology's runtime
loaders sit in the goldens tree that the specification says the
goldens workflow runs wholesale, so the workflow lists its goldens by
hand to exclude them. And the run instructions carry `verified`
events, which signs a procedure the model says is evaluated and never
signed.

## Decision

1. **One home per file, by plane** (the placement rule). Sanctioned
   code stays in the bundle's `references/` tree. A procedure is a
   skill. A script a skill runs at runtime lives in that skill's
   `scripts/`. Goldens and their fixtures live under `verification/`
   and nothing there is invoked by a skill. Gates live in `tools/` or
   build-kit; connectors in `connectors/`.
2. **Run instructions are skills, not concepts.** The
   `references/skills/` directory is retired. The contract of a
   computation (parameters, receipt fields, refusal codes, the
   executor's usage text) stays in the concept and the executor; the
   walkthrough moves to a `SKILL.md`.
3. **Every Attested Computation is wrapped** (the wrapping rule) by a
   skill in the capability whose sphere it names and which depends on
   the bundle, declared on the concept as `executor.skill:
   <capability>/<skill>`. A computation whose capability does not yet
   exist as a package is reported as unwrapped by the audit and
   carried on the roadmap.
4. **The rule is measured** (the placement gate). `osp.py
   placement-check` in build-kit runs in every plugin gate with the
   seven findings P1 to P7 the specification lists. The seed brief
   renderer, plugin-template and knowledge-template start every new
   contribution in the shape the gate expects.

## What this record does not decide

- It does not move executors, attesters, loaders or data roots out of
  the bundle. Their paths are recorded in receipts and concepts, hashed
  by attesters, and keyed by the reattest registry and the check chains;
  their identity is the contract, and moving them would re-anchor every
  quoted number for no change in behaviour.
- It does not change the OKF v0.2 interface. `executor.resource`
  remains a path-valued field; `executor.skill` is an organization
  extension in the same sense as the findings and connector extensions.
- It does not decide where a sphere capability that does not yet exist
  as a package will live; ADR A decides that.

## Migration

The one-time moves, in the order that keeps every gate green. Each is a
roadmap deliverable under `osp-architecture-alignment`; P2, P3, P4 and
P5 report as warnings until the last of them lands, and as errors from
the first of 2026-10.

**build-kit first.** Implement `osp.py placement-check` with P2 to P5
as warnings, add it to the plugin gate workflow the renderer writes,
teach `osp.py audit` the P6 resolution across the catalog, and add the
computation-kind rules to `seed_brief.py`. `check_script_deps.py`
already scans any root it is given; every plugin gate passes
`skills/` beside `knowledge/` and `verification/`.

**ocean-science.**
- `skills/receipt-figures/receipt_figure.py` and
  `skills/cite-ecco/ecco_cite.py` move under `scripts/` in their
  skills; the citation copy gains a `pinned_from:` header naming
  `nasa-daac-knowledge/tools/ecco_cite.py` and the release it copies.
- `knowledge/references/skills/run-argo-ohc.md` becomes
  `skills/argo-ohc/SKILL.md` (or a section of `sea-level`), and the
  concept `knowledge/computations/argo-ohc.md` gains
  `executor.skill: ocean-science/argo-ohc` with `executor.resource`
  pointing at the executor script. The concept's log records the move;
  no receipt changes, since no code moves.
- The thirteen podaac ECCO computations and the sea level budget are
  wrapped where an ocean-science skill already covers the workflow
  (`ecco`, `budget-closure`, `meridional-transport`, `sea-level`,
  `transport-analysis`), each skill naming the executors it runs and
  each concept naming its skill.

**hydrology.**
- The seven runtime helpers skills invoke (`load_et.py`,
  `load_precipitation.py`, `load_peaks.py`, `load_drought_panels.py`,
  `load_reservoir_ledger.py`, `load_swot_confrontation.py`,
  `delineate_basin.py`) move from `verification/fixtures/` to
  `skills/<name>/scripts/`; the goldens that import them update their
  imports; the twelve `fetch_*_fixtures.py` and `freeze_*_inputs.py`
  builders stay under `verification/fixtures/`.
- `basin-water-balance` is already the wrapping skill; the concept
  gains `executor.skill: hydrology/basin-water-balance`.

**nasa-daac-knowledge.**
- `references/skills/run-sea-level-budget.md` (podaac),
  `run-energy-budget.md` (asdc) and `run-ice-sheet-balance.md` (nsidc)
  are retired once their wrapping skills exist: the sea level budget in
  ocean-science now; the energy budget and the ice sheet balance in the
  atmospheric physics and land ice capabilities when those packages
  exist, recorded as unwrapped by the audit until then. The concepts
  point `executor.resource` at their executors and record the change in
  the bundle logs; signatures on the retired references are not carried
  anywhere, since a procedure is not signed.
- `tools/` is unchanged.

**core.** `verification/trend_computation.py` and
`verification/trend_attester.py` are the foundation's reference pair
and its golden, named by the release qualification prompts; they stay,
and the placement gate treats a top-level verification script the
workflow runs as a golden whatever it also serves.

**Templates.** plugin-template gains `skills/<example>/scripts/`;
knowledge-template drops `references/skills/` from its scaffold and
`scaffold_bundle.py` stops creating it.

## Consequences

An agent in a capability finds every attested computation the way it
finds every other procedure, through a skill that fires on the words a
scientist uses, and the computation's contract stays where its
signature is. Contributors have one table to consult and one gate that
tells them which row they broke. The cost is the migration above and
one more finding in each plugin gate; the receipts, run ids and signed
concepts are untouched.

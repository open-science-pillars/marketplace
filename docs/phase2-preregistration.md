# Phase-2 pre-registration: go/stop conditions and the ablation protocol

Published 2026-07-05, BEFORE any Phase-2 result exists, per PARKING #2:
deciding the exit test before the result is the same epistemics we
demand of the science. Amendments after this date are permitted only as
dated, logged additions below; nothing in this section is edited in
place.

## The headline experiment (ablation, Session 19)

- **Question:** does the installed knowledge bundle measurably reduce
  the rate at which the agent falls into documented dataset traps?
- **Protocol:** the gotcha-avoidance eval suite (ocean high-severity
  cases: native-grid-refusal, geothermal-omission, swot-calval-window,
  grace-leakage, plus the Session-18 promotions: v4r4b-mixing,
  mht-basin-scope, swot-crossover) run bundle-ON vs bundle-OFF
  (knowledge/ removed from the installed plugin, skills untouched),
  same model (recorded), same prompts, N=20 trials per case per arm.
- **Metric:** per-case trap-hit rate with binomial 95% CIs; the
  headline is the pooled risk difference (ON minus OFF) with its CI.
- **Publication rule:** results publish to the scoreboard and
  build-kit/PROGRESS.md with intervals REGARDLESS of outcome, including a null.

## Go conditions (fund doubling down: Phases 3+ domains, provider expansion)

Any two of:
1. The ablation's pooled risk difference shows bundle-ON reducing
   trap-hit rate with the 95% CI excluding zero.
2. Within 30 days of announcement: at least one external install with
   a filed issue or PR from a non-author.
3. One non-author scientist completes Tutorial 2 unaided (friction
   notes captured).
4. A data-provider steward (PO.DAAC or equivalent) reviews at least
   one concept in a bundle they own.

## Stop/pivot conditions

1. **Ablation null or reversed** (CI includes zero or favors OFF):
   stop expanding the knowledge layer's scope claims; the announcement
   and READMEs are edited to remove effectiveness language; Phase-3
   work pivots to diagnosing why (prompt sensitivity, case design,
   bundle routing) before any new domain ships.
2. **Zero external engagement 30 days post-announcement** (no
   installs-with-issues, no discussions, no tutorial completions):
   pause outreach-driven work; conduct five direct user interviews
   before building further.
3. **Steward handoff fails** (no provider steward engagement by end of
   Phase 2): the federated-knowledge claim is downgraded to
   single-steward wording everywhere it appears.

## Analysis commitments

Trap-hit is graded by the same rubric per case in both arms;
programmatic graders where defined; grader code frozen before the
bundle-OFF arm runs; model version and dates recorded per trial; raw
transcripts retained; the seed-pass failure (core uncertainty-statement)
is already public and is not counted as a gotcha-avoidance case.

## Amendments

- 2026-07-05 (Session 19): the powered ablation (7 gotcha-avoidance cases x
  N=20 x 2 arms = 280+ agentic invocations, minutes each) is not feasible as a
  laptop run and is deferred to a credentialed CI/cloud job; the harness
  (`evals/runner/ablate.sh`, which strips `knowledge/` from the installed
  plugin for the OFF arm and restores it) and the run command are staged for
  that environment. As a harness sanity check only, an UNDERPOWERED PILOT was
  run this session at N=3 with model claude-opus-4-8 (the pre-registered model
  claude-fable-5 was quota-exhausted this session). The pilot is explicitly
  NOT the pre-registered result: its N is too small for a resolved interval and
  its model differs. It is published to the scoreboard clearly labelled as a
  pilot, and the go/stop conditions above remain tied to the powered N=20
  run on the recorded model, not to the pilot.
- 2026-07-05 (Session 19, pilot finding): the pilot showed NO ON-OFF
  difference (pooled 0.76 both arms, per-case delta 0.00), which flags a
  design confound in the ablation as originally specified: the skills carry
  the gotcha rules (Must-NOT lists and Knowledge-first restatements live in
  the skill bodies, loaded in both arms), so stripping only `knowledge/` does
  not change behaviour on these prompts. Before the powered run the ablation
  design is revisited (ablate the gotcha content from the skills too, or
  target prompts that need the concept's numeric/uncertainty detail rather
  than just the trap's existence). A methods refinement discovered by the
  pilot, logged here rather than silently changing the protocol; the powered
  run adopts the revised design with its own recorded rationale. Also noted:
  `ecco-release-mixing` failed in both arms (0/3), either a skill-routing gap
  or a too-strict grader, to check before the powered run.

- 2026-09-05 (hydrology expansion): the hydrology plugin is expanded
  from four dataset skills to basin-and-event investigations (a basin
  water balance, event reconstruction, flood frequency, drought anatomy,
  a reservoir ledger) with precipitation and evapotranspiration terms
  and the USGS Water Data API migration. This entry records how that
  work reads against the conditions above, before any of it is written,
  so that the reading is on the record rather than inferred later.
  First, the stop conditions trigger on a negative result (a null or
  reversed ablation, zero engagement at thirty days, a failed handoff),
  not on the absence of a result; the powered ablation has not run, so
  no stop condition has fired, and the expansion does not wait on it.
  Second, every workflow in the expansion is hydrology-domain work
  inside the plugin the architecture's Phase 2 already names, and the
  IMERG precipitation term and the GRACE-backed drought pack are named
  there in so many words; nothing here is a new domain, and the go
  condition that funds new domains is neither claimed nor needed.
  Third, the first wave creates no provider bundle: facts about GES
  DISC and LP DAAC products are held in the hydrology bundle with
  `upstream: pending` naming their canonical provider directory, as the
  locality rule provides, so the "provider expansion" the go conditions
  govern is not reached. The linter's sixty-day flag on pending
  material is expected and is answered on the expansion's tracking
  issue with this entry. Whether gesdisc and lpdaac directories are
  created, and whether the SWOT hydrology facts move to podaac, is
  decided later under its own gate and its own dated entry. Fourth,
  event reconstruction reads published OPERA surface-water products as
  observations; it is not the model-backed flood slice the roadmap
  holds blocked on the powered ablation, and that slice stays blocked.
  The expansion adopts the pre-registration's own publication rule for
  its water balance: on each fixture basin above the footprint floor
  the residual publishes with its interval and both bars regardless of
  whether it closes, and a basin below the floor publishes as a
  refusal.

- 2026-09-11 (sphere alignment and multi-runtime packaging): the
  organization is adopting two linked decision records
  (docs/decisions/adr-a-pillar-means-sphere.md and
  docs/decisions/adr-b-multi-runtime-capability-packaging.md, with the
  design in docs/design-sphere-alignment-multi-runtime.md). This entry
  records, before any of that work is done, how it reads against the
  conditions above. Four kinds of work are in scope: adding sphere
  metadata to repositories and to scientific concepts; introducing
  provider-neutral `.osp/` metadata (repository classification,
  package and dependency declarations, runtime support policy, release
  locks); creating runtime packaging scaffolding (a Claude projection
  and an Agent Plugins 1.0 projection rendered from the same source);
  and instantiating planned repositories that hold no capability. All
  four are organizational and infrastructure work. None is a new
  scientific domain shipping, so the go condition that funds new
  domains is neither claimed nor needed, and none is a negative result,
  so no stop condition fires. A planned repository named for a future
  domain (precipitation, land-ice and the rest) contains no skill, no
  concept, no manifest and no catalog entry, and its README says so;
  it is a statement of intended shape, not a domain. The planned
  `partner-knowledge` repository likewise contains no bundle, so the
  provider expansion the go conditions govern is not reached by
  creating it; a provider directory is still created only under its
  own dated entry here, as the hydrology entry above provides. Runtime
  packaging changes how a governed capability is delivered and does
  not change what it claims: one signed concept feeds every projection,
  the same deterministic verifier checks every runtime's result, and a
  packaging-only change needs no scientific re-approval unless
  semantics change. The powered ablation keeps its pre-registered
  design and its place as the Phase-3 gate; the model-backed flood
  slice stays blocked on it; and the cross-runtime eval dimension this
  work adds (capability release, runtime, model, suite, trials, score,
  interval) records runs against both runtimes without altering the
  ablation's arms or metric. Sequencing: the decision records and this
  entry merge now; every other step waits for the first tranche of the
  hydrology investigations (the roadmap's P0 deliverables of
  `hydrology-investigations`) to be recorded done, and that gate is
  not removed silently.

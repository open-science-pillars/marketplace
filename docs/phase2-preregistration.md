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

- 2026-09-13 (provider engagement is measured on the ladder): the third
  stop condition, "steward handoff fails", was written when a provider
  steward who signs was the only form of provider engagement the
  organization knew how to record. The stewardship rules now state a
  ladder of involvement for a person at a data center (consulted:
  confirms or corrects a concept on an issue and the maintainer records
  the event on their behalf; reviewer: reviews knowledge pull requests
  for their products; steward: joins the steward team and signs), with
  nothing above the first rung required of anyone and a signature no
  longer the gate for a concept, a release or a promotion. From this
  date the condition is measured as provider engagement at any rung of
  the ladder: a concept confirmed or corrected by a provider contact
  counts, a review counts, and a steward counts. The condition still
  fires on no engagement at all by the end of Phase 2, and the
  consequence is unchanged (the federated-knowledge claim is downgraded
  to single-steward wording everywhere it appears). The reason for the
  re-reading: measuring engagement only as ownership would report a
  failure while people who are only getting accustomed to AI were in
  fact reading the digest and confirming claims, which is the
  engagement the claim was always about; nothing else in this document
  changes, and the text above is not edited.

- 2026-09-19 (promotion to host a wrap): two capabilities,
  `atmospheric-physics` and `land-ice`, promote out of planned to host
  the skills that wrap attested computations already signed stable in
  the provider bundles (the asdc energy budget closure, the nsidc ice
  sheet mass balance closure, and whichever further computations in
  those bundles are signed when each release is cut). This entry
  records how that work reads against the conditions above, before the
  capabilities are built, so that the reading is on the record rather
  than inferred later. First, the domain-expansion gate asks whether
  the organization should open a new scientific domain before the
  ablation says whether the knowledge layer works. A wrapping skill
  opens no domain: it computes nothing, and every number it can report
  is owned by a concept that was reviewed, run on a stamped data root,
  attested and signed. What promotion buys here is reachability, that
  an agent which installed a capability can run a signed computation
  rather than a reader having to find a concept, and reachability is
  not the breadth the gate protects. Second, the stop conditions
  trigger on a negative result, not on the absence of one; the powered
  ablation has not run, so no stop condition has fired. Third, the
  capabilities are bounded to the wrap in this entry: a skill in either
  repository that computes a number of its own is domain expansion,
  waits on the ablation, and takes its own dated entry here. Fourth,
  the effect on the experiment is to strengthen it rather than
  prejudge it: wrapping puts the signed computations in the same path
  an agent takes for every other capability, so a later ablation can
  exercise them the way a user would. Fifth, the rest of the promotion
  rule is satisfied in full and not waived: a maintainer, sources on
  every claim, an eval case for each high-severity gotcha the release
  relies on, and a named provider contact invited (ASDC for the
  radiation products, NSIDC for the ice elevation and velocity
  products, PO.DAAC for the mass change products). The architectural
  form of this decision is ADR D in docs/decisions; nothing above is
  edited.

- 2026-09-19 (promotion to host a wrap: what was built, recorded the
  same day): both releases are cut, and this entry closes the one
  above by saying what they carry rather than leaving the reading
  against a plan. atmospheric-physics 0.1.0 wraps two asdc
  computations, the energy budget closure and the cloud radiative
  effect; land-ice 0.1.0 wraps two nsidc computations, the ice sheet
  mass balance closure and the input-output balance. Four rather than
  the two the entry above names, because the round signed two more
  while the capabilities were being built and a wrap-only release
  carries every computation its bundle has signed when it is cut. The
  bound held: neither release computes a number of its own, and the
  placement gate in strict mode reports no unwrapped attested
  computation in any bundle. Both are qualified on Claude Code for
  their exact version and release lock, with Claude Cowork and OpenAI
  Codex waived in writing and not advertised. One thing to hold
  against the experiment rather than for it: three defects in the
  qualification tooling's candidate path had to be fixed before either
  release could be qualified at all, so the qualification step is
  newer and less exercised than the rest of the pipeline, and the next
  release is the one that tells us whether it is now reliable.
  Nothing above is edited.

- 2026-09-20 (receipt skills admitted to a wrap-only capability): the
  promotion-to-host-a-wrap decision's third point is amended to admit a
  third shape of skill, one whose every number is a field of an attested
  receipt or a table, figure or paragraph of such fields, combining
  nothing across receipts, with a script that enforces the test. This
  entry reads that against the conditions above. First, the
  domain-expansion gate asks whether the organization should compute a
  new number before the ablation says whether the knowledge layer works;
  a receipt skill computes no number, and the one it would be most
  tempted to compute, the average of a sweep, is the one its script
  refuses, so the gate is untouched and the refusal is mechanical rather
  than promised. Second, no stop condition has fired. Third, the
  amendment is bounded to the test: a skill that fails it is a workflow
  skill and waits on the ablation as before. Fourth, the effect on the
  experiment is to strengthen it: the concepts already state that a
  closure's verdict is window dependent, from windows someone ran by
  hand, and a sweep turns that statement into a measured table the
  ablation can read, prejudging nothing about whether the knowledge
  layer helps. Fifth, the first receipt skill is built in ocean-science,
  which is not under the wrap-only bound, so the pattern is proven before
  the amendment is exercised. Nothing above is edited.

- 2026-09-20 (a computation is a skill: the computations move into the
  capabilities that already reached them): ADR E in docs/decisions
  re-homes every attested computation into the capability that runs it,
  with its code in the scripts of the skill that runs it, its concept
  beside it in that package under `knowledge/computations/`, and the
  stamped data root it reads committed there as data. This entry reads
  that against the conditions above. First, the domain-expansion gate
  asks whether the organization should compute a new number before the
  ablation says whether the knowledge layer works, and the move computes
  none: every number is the same signed number, re-homed and re-run at
  its new path, with the receipt regenerated and attested and the
  concept re-signed on the new digests, so no new domain opens. Second,
  no stop condition has fired. Third, the bound the 2026-09-19 entry set
  is re-read rather than lifted: where its third point said that a skill
  in either repository that computes a number of its own is domain
  expansion, it now reads that the skills carry the same signed
  computations they reached before, and a new computation in a sphere
  that has none still waits on the ablation and takes its own dated
  entry here. Fourth, the effect on the experiment is to strengthen it
  rather than prejudge it: the concept, the code, the data the code
  reads and the golden that proves it sit in one repository on the path
  an agent already takes, so a later ablation exercises them the way a
  user would, and the re-run at the new paths is itself a reproduction
  of every reference value. Fifth, the move signs nothing by itself: the
  re-signs are the maintainer's, every reference run is reproduced
  before its pull request merges, and a value that failed to reproduce
  would be a finding recorded here rather than a number adjusted
  quietly. Nothing above is edited.

- 2026-09-21 (the powered ablation: the refined design, recorded
  before the run): this entry is the amendment the roadmap holds as
  ablation-protocol-amendment, and it records the cases, the model, the
  grading, the sample size and the decision rule that the powered run
  will use. Nothing above is edited. The 2026-07-05 pilot entry stands
  as written, including its finding, and this entry says what follows
  from it.

  **Two harness defects, found and fixed before anything was
  redesigned.** The ablation manifest named its seven cases at
  `ocean-science/evals/`, where they lived in July; they moved to the
  agent-evals tree, every other manifest followed, and this one did
  not, so all seven paths resolved to nothing. The runner pinned the
  installed knowledge tree to ocean-science 0.3.0, four releases
  behind, so the bundle-OFF arm could only reach its own guard and
  exit. Both are corrected (evals: the manifest reads the agent-evals
  paths, the runner finds the installed tree rather than naming a
  version). This matters to the reading of the pilot only in that the
  pilot ran before either drifted; it matters to the powered run
  because without it there would have been no run at all.

  **What the pilot's null does and does not license.** The pilot
  entry attributes the flat result to the skills carrying the gotcha
  rules in both arms. That explanation covers six of the seven cases,
  which target a skill. It does not cover grace-leakage, which targets
  no skill and rests on the concepts alone, and which was flat too. So
  at least one other explanation is live and the powered run must be
  able to separate them: that the traps in these cases are recoverable
  from the model's own prior knowledge, in which case a bundle that
  states the trap's existence adds nothing measurable, whatever the
  skills do.

  **Refined cases.** The suite is re-targeted rather than ablated more
  deeply. Stripping the gotcha content from the skills as well would
  confound the knowledge bundle with the skill bodies and would stop
  measuring the thing the go condition names. Instead each case's
  graded claim is raised from recognising that a trap exists to
  stating what only the signed concept carries: a value, an
  uncertainty or half width, a named version or epoch, or a dated
  verification. A reply that names the trap and no number passes today
  and fails under the refined grading, in both arms alike. The seven
  cases keep their prompts and their identifiers; the change is in the
  graders and in the pass bar, and it is made before either arm runs.
  ecco-release-mixing, which failed 0/3 in both arms of the pilot, is
  diagnosed first and either repaired or dropped from the suite with
  its reason recorded here; a case that no arm can pass measures the
  grader, not the bundle.

  **Model.** The powered run pins `claude-opus-5`, one model for both
  arms, recorded per trial with its exact identifier in the results
  record as the analysis commitments above already require. The
  identifier is named here rather than left to the run because a
  pre-registration that will not say what it ran has not registered
  the condition that matters most; this is the decision owner's call,
  taken on 2026-09-21, and it is the same reason the July entries name
  the models they do.

  This departs from the `claude-fable-5` the headline experiment was
  originally registered on, and the departure is recorded rather than
  passed over. Two consequences follow and are stated before the run so
  that neither can be argued after it. First, the result is a statement
  about this model and not about the Fable line the go conditions were
  first written against; a later run on another model is a separate
  result and takes its own entry. Second, and more important, a
  stronger model carries more of these traps in its own prior
  knowledge, which makes a null both more likely and harder to read: if
  the model already knows that mascon leakage or a firn correction
  matters, a bundle that states the trap's existence has nothing left
  to add, and the ablation measures the model's memory rather than the
  bundle's effect. That is a real and publishable finding, and it is
  also precisely the second explanation this amendment set out to
  separate from the skills confound. It is why the refined grading asks
  for the value, the uncertainty and the version rather than for
  recognition, since those are what a signed concept carries and a
  model's prior knowledge does not, and why grace-leakage reports
  separately in the decision rule below. Choosing a weaker model to
  make an effect easier to find was considered and rejected: selecting
  the condition that flatters the hypothesis is the thing
  pre-registration exists to prevent.

  The pilot's substitution is not repeated: if the pinned model is
  unavailable when the run starts, the run waits rather than switching,
  because an arm pair split across models measures the models.

  **Sample size.** N=20 trials per case per arm, as pre-registered, 7
  cases and 2 arms. The pilot's N=3 is not an input to the result.

  **Grading.** Programmatic graders where a case defines one, the
  per-case rubric otherwise, the same rubric in both arms. Grader code
  is frozen and its commit recorded before the bundle-OFF arm runs, as
  above, and the refined graders are written and frozen before the
  bundle-ON arm runs, so neither arm can be graded against a bar
  adjusted after seeing it. Raw transcripts are retained for every
  trial.

  **Decision rule.** Unchanged from the go and stop conditions above,
  and stated here so it cannot be read differently afterwards. The
  headline is the pooled risk difference, bundle-ON minus bundle-OFF,
  with its binomial 95 percent interval. An interval excluding zero in
  favour of ON satisfies go condition 1. An interval including zero, or
  favouring OFF, fires stop condition 1, and the publication rule
  applies either way: the result publishes to the scoreboard and to the
  progress record with its intervals regardless of outcome, a null
  included. One further commitment, because the pilot showed how easy
  a flat result is to explain away: if the powered run is null, the
  per-case breakdown publishes with it, and grace-leakage is reported
  separately as the case that isolates the concepts from the skills.

- 2026-09-21 (calibration, recorded before either arm runs): the entry
  above committed to diagnosing ecco-release-mixing before the powered
  run and recording here whether it was repaired or dropped. It is
  repaired, and the diagnosis is not the one the pilot entry guessed
  at. The grader was inverted. It required one of six literal phrases,
  among them "not mix", so a reply stating that the two releases "must
  not be mixed" failed it, and that is the wording of the case's own
  notes. Every correct phrasing tried fails it and both wrong ones
  pass it, so the 0 of 3 in both arms was the only score it could have
  produced. It was neither a skill-routing gap nor a grader that was
  merely too strict.

  Reading the rest of the suite for the same class of fault found two
  more. Terms were matched as substrings, so the leakage probe's "cri"
  is satisfied by the word "described" and fired on any transcript at
  all, and the native-grid probe's "0.5" is satisfied by "0.52 mm/yr",
  passing a reply that refused nothing. And a probe could be satisfied
  by naming a thing without using it: a transcript that named
  height_cor_xover and then said it ignored it passed the probe whose
  whole purpose is to catch that. All seven now match words rather
  than substrings, require the concept to be applied rather than
  mentioned, and refuse the identifiable failure, which is what the
  refined grading in the entry above asks of them.

  The root cause sat in the selftest rather than only in the graders:
  one good and one bad fixture per grader, each written in the
  grader's own words, agreed with a broken probe while the real run
  scored zero. The seven now carry several phrasings a reply actually
  uses and several near misses that must not pass, thirty three in
  all; run against the old graders those fixtures catch thirteen
  misclassifications across six of the seven probes. The seventh, the
  orbit-phase probe, was loose rather than inverted and its old form
  classified these same phrasings correctly.

  This is the grader freeze the entry above requires, and it is dated
  before either arm has run. No case was dropped from the suite, so
  the powered run is still seven cases by two arms at N=20.

- 2026-09-21 (transcript retention, recorded before the run): the
  analysis commitments above have required raw transcripts for every
  trial since this document was published, and the amendment earlier
  today repeats it. The harness never asked for them. run_evals.py
  writes transcripts only when given a directory, and ablate.sh called
  it twice without one, so the pilot's stored results hold rates,
  intervals and pass flags and nothing else, and no transcript of any
  trial exists. The commitment was real and the harness quietly did not
  meet it.

  What that cost is already on the record above. Diagnosing the
  release-mixing case meant reading the grader's source and
  constructing what a correct reply must have said, because the three
  replies that failed were not kept. The conclusion was reached by
  reconstruction rather than from evidence, and it happened to be
  reachable that way; a subtler fault would not have been.

  Both arms now keep their transcripts beside their results, and the
  run refuses to reach the scoreboard if either arm kept none. The
  guard matters more than the flag, because a silent empty directory is
  how this went unnoticed the first time. Carrying the transcripts out
  of a credentialed run, as an artifact or otherwise, belongs to
  whatever wires that run, and this entry is the standing requirement
  that it must.

  This is recorded before the powered run rather than after it for the
  reason the model entry gives: that run pins a strong model, which
  makes a null both likelier and harder to attribute, and a null whose
  transcripts were kept is a finding somebody can open while a null
  without them is the July null again. Nothing above is edited, and
  nothing about the cases, the arms, the grading, the sample size or
  the decision rule changes.

- 2026-09-21 (five protocol changes, recorded before either arm of
  either run): piloting the harness found four faults that change how
  the experiment is conducted or read, and the decision owner has
  settled a fifth question about what is to be run. All five are
  recorded here before any powered arm, because each of them would
  otherwise be a change made after seeing a result.

  **Turn exhaustion is an outage, not a failure.** A trial that returns
  "Error: Reached max turns" was being scored as a substantive failure.
  The message cleared the harness's empty-transcript test by nine
  characters and its quota test by one word, so it reached the rubric
  judge, which wrote a reason about the case's elements not being
  surfaced while noting in the same sentence that the transcript held
  no assistant work at all. The analysis commitments above already say
  a trial past the limit is an error and never a failure; this makes
  the harness do it. The direction is why it matters rather than the
  bookkeeping: consulting the bundle costs turns, because the skill
  reads concepts and each read is a turn, so exhaustion does not fall
  evenly across the arms and scoring it as failure manufactures a
  difference out of the harness's own bound.

  **The turn budget is 30, raised from 12.** At 12, seven of eight
  pilot trials returned that error instead of an answer. At 30 the same
  pilot returned eight of eight real answers and no errors. Once
  exhaustion is an outage the bias is no longer in the rate but in the
  sample, which is quieter: the trials that survive a budget the
  treatment interacts with are the atypically brief ones. Eight trials
  cannot establish which arm exhausts more and nothing here claims it;
  what they establish is that the budget interacts with the treatment
  at all, which makes it part of the treatment. 12 was the lowest
  budget in the repository, and these same cases are given 15 and 20 in
  the capability's own manifest.

  **The probes are calibrated against recorded output.** The seven were
  rewritten earlier today and calibrated against phrasings written by
  hand. That is better than fixtures written in a grader's own words
  and is still not output a model produced. The first pilot to return
  real answers failed one of them: the reply quoted the collection
  identifier as LLC0090 where the probe asked for llc90, and offered a
  native path where the probe demanded a native grid. The rubric judge
  passed that answer and the programmatic probe did not, so a correct
  answer was recorded as a failure. Transcripts from that pilot are now
  kept as fixtures and the harness's selftest asserts each probe
  reaches the verdict the run reached, so a probe cannot drift back to
  language nobody writes.

  **Two runs, and only one of them decides.** The powered ablation runs
  twice over, once on each of two models, so that the effect can be
  read against model capability rather than reported for one model as
  though it were general. The run on the model pinned in this
  amendment's model entry is the registered headline and is the only
  one that fires go condition 1 or stop condition 1. The second run
  publishes alongside it with its own intervals, as a pre-registered
  secondary that fires neither. This is fixed now because two pooled
  risk differences would otherwise let the deciding result be chosen
  after both were seen, which is the thing a pre-registration exists to
  prevent.

  **The direction of the difference between them is predicted, not
  described.** The model entry above argues that a stronger model
  carries more of these traps in its own prior knowledge, which makes
  the bundle redundant and a null likelier. That argument is worth
  nothing if it is only ever available afterwards, so it is committed
  to in advance: the risk difference is expected to be larger on the
  weaker of the two models. If both runs come back flat the prior
  knowledge explanation is spent rather than reusable, and the skills
  confound or the bundle's plain ineffectiveness becomes the reading
  the evidence supports.

  Nothing above is edited. The cases, the arms, the prompts, the
  twenty trials per case per arm and the decision rule are as
  registered.

- 2026-09-22 (correction: the bundle-OFF arm was never off, and the
  pilot of 2026-07-05 is withdrawn): the off arm moved one knowledge
  tree aside, the ocean capability's own, and the harness called that
  bundle-OFF. It was not off. Every case in the suite names its ground
  truth by `concept_basis`, and thirteen of the suite's fourteen
  citations name concepts that live in the provider knowledge bundle, a
  separate plugin installed into a separate cache that neither arm ever
  touched. The fourteenth is the ocean capability's own attested
  computation.

  A shard probe on 2026-09-21 settled this on evidence rather than on a
  reading of the harness. Its off-arm transcript for `grace-leakage`
  cites both of that case's concepts by their paths in the provider
  bundle, and opens "I read the bundle concepts before touching data,
  and they stop this computation as specified", in the arm where that
  knowledge is supposed to be gone. The shard's headline delta, zero
  between a rate of 1.00 and a rate of 1.00, is not a null. It is a
  measurement of nothing.

  **What this withdraws.** Every on minus off number the ablation has
  produced compared an arm holding the cited knowledge against an arm
  holding the cited knowledge. That includes the pilot of 2026-07-05
  recorded above and published to the scoreboard, whose pooled 0.76 in
  both arms and per-case delta of 0.00 were read at the time as
  evidence of a design confound in which the skills carry the gotcha
  rules and the concept files add nothing. A perfect identity between
  two arms holding the same knowledge is what that harness was bound to
  produce, so the pilot is no evidence for that reading and none
  against it. The skills confound may well be real. It is an untested
  hypothesis again, and the powered run will be the first measurement
  this experiment has made. The scoreboard page carrying the pilot is
  corrected where it was published rather than deleted.

  **What this does not touch.** No go condition and no stop condition
  fired on that pilot. It was published under its own amendment's label
  as not the pre-registered result, and the conditions above were tied
  to the powered run throughout, so no decision on the record rests on
  a number that measured nothing.

  **The fix is a refusal, not a wider strip alone.** The arm's scope is
  derived now instead of assumed. The harness walks the plugins the
  manifest's cases name plus every dependency those plugins declare,
  because an installed capability brings its dependencies and a reader
  consulting knowledge reaches all of them, and it moves the installed
  knowledge tree of each aside. It then checks every case's
  `concept_basis` against that scope and stops the run when a citation
  falls outside it, so the failure this entry records cannot recur
  quietly: a suite the arm cannot ablate refuses to run rather than
  returning a delta. Against the registered suite, thirteen citations
  are unreachable under the old scope and none under the derived one,
  which resolves to the ocean capability, the core capability and the
  provider knowledge bundle.

  **The off arm is therefore a larger intervention than the registered
  wording describes.** The protocol above says `knowledge/` removed
  from the installed plugin, and the arm now removes the knowledge of
  the installed plugin and of the plugins it depends on. That is read
  as the registered intent rather than as a change to it: the question
  is whether the installed knowledge bundle reduces the trap-hit rate,
  an install brings its dependencies, and an arm that leaves the cited
  concepts readable answers nothing in either direction. It is recorded
  here because it is wider, and because a reader comparing the two
  descriptions is entitled to know which one the run performed.

  Nothing registered changes. The seven cases, the two arms, the
  prompts, the twenty trials per case per arm, the metric and the
  decision rule are as registered.

- 2026-09-22 (registered before either run: what each arm loses is
  published with what each arm scores): raising the turn budget from 12
  to 30 yesterday was recorded on the reasoning that exhaustion is an
  outage and not a failure, and that the remaining bias is in the sample
  rather than the rate. A shard probe at 30 lost one of two bundle-on
  trials to the limit, against none of two on the other arm. Eight
  trials establish nothing about the size of that, and the direction is
  not in doubt: consulting the bundle costs turns, because the skill
  reads concepts and each read is a turn, so the arm holding the
  knowledge exhausts its budget more readily and the trials that survive
  it are the atypically brief ones. A budget the treatment interacts
  with is part of the treatment at any value it is set to, so raising it
  again is not the answer.

  The commitment made here instead is to report it. Each arm's lost
  trials publish per case and pooled, with the difference between the
  arms, on the same page as the risk difference and not in a file
  underneath it. Where that difference reaches ten points the page says
  in so many words that a pooled risk difference between samples thinned
  unequally is not read as a treatment effect without the thinning
  stated. This is registered now because a result whose arms lost trials
  at different rates invites two readings, and choosing between them
  after seeing which way the difference fell is the thing a
  pre-registration exists to prevent.

  Nothing else changes. The budget stays at 30, the seven cases, the two
  arms, the prompts, the twenty trials per case per arm, the metric and
  the decision rule are as registered, and a lost trial still enters no
  rate.

- 2026-09-22 (correction: the rubric of record was never the rubric the
  cases named): the analysis commitments above say trap-hit is graded by
  the same rubric per case in both arms and that the grader code is
  frozen before the bundle-off arm runs. Thirteen eval cases across two
  repositories, among them all seven of this experiment's, named a
  dedicated rubric document in their graders block. Not one of those
  documents exists anywhere in the organization and none ever has. The
  runner resolved a name it could not find by falling through to the
  case's own notes, printing no warning, and no results file recorded
  which text had graded a trial.

  What was graded is not in question. The notes state pass and fail
  intent for every one of these cases, the eval charter already calls
  the notes the rubric of record, and the same text graded every arm and
  every trial, so the first commitment was met in fact. The second was
  not checkable: a grader cannot be frozen and verified against a record
  that does not say what it was. Each case now names `notes` outright,
  which changes no grading behaviour and makes the record state what is
  in force; a rubric name that resolves to nothing stops a run rather
  than being replaced quietly; and every results file from here carries,
  per case, the text that graded it.

  No published number changes. This is recorded because a reader of the
  analysis commitments above would otherwise believe thirteen rubric
  documents exist and govern the grading, and because the powered run
  should begin with the record and the run saying the same thing.

- 2026-09-22 (second correction: the arm was never off, for a second
  reason, and the harness had never taken a tree away at all): the entry
  above records that the off arm moved one knowledge tree where the
  cases cite three plugins, and that the scope is derived now. A
  re-pilot on that derived scope moved three trees, verified them gone
  from their old paths mid-arm, and every bundle-off trial still read
  the knowledge. All four cite their case's concepts by path, one quotes
  a concept's own verification frontmatter, and one reproduces a numeric
  anchor that appears in no skill.

  **Two readable copies, and the evidence does not say which.** The same
  knowledge is checked out in the workspace as ordinary files, and
  recorded passing answers to these exact cases sit beside it under
  results and fixture directories. Both carry the text the transcripts
  reproduce, so nothing in a transcript distinguishes them. The second
  is the worse of the two: an answer to a case contaminates the rate in
  both arms rather than the difference between them.

  **Confinement is not available through the launcher.** Setting the
  trial's working directory was checked directly, not assumed: a run
  whose working directory was an empty temporary directory read an
  absolute path in the workspace without difficulty and quoted it back.

  **A renamed directory was never a removed one.** Rehearsing the new
  check found that moving a tree to `knowledge.ABLATION_OFF`, which is
  what every version of this harness has done since the first pilot,
  leaves it exactly where it was under a name a reader reaches as
  easily. Every tree this experiment has ever moved was readable for the
  whole of the arm that was supposed to be without it. Each one is now
  written to a compressed archive outside the workspace and deleted,
  and put back when the trials end. These cases are granted the ability
  to read files and to use skills, and no shell, so an archive is out of
  their reach; that is the boundary and it is not a stronger one.

  **The case file is an answer sheet.** A case's notes state what a
  passing answer must contain, and that is the rubric of record, as the
  entry above says. It also sits in the workspace a trial reads. Every
  run now sets the case directories aside once the runner has loaded
  them, not the ablation alone, because this defeats any eval and not
  only this experiment. In the same way, one fixture's own documentation
  stated the correct behaviour for its case in a sentence, and the
  synthetic data file the case has to hand the agent named the eval case
  inside its own metadata. Both are removed.

  **The gate is now content, not location.** Every fix before this one
  was a better guess about where copies live. The check takes text out
  of the concepts the cases cite and looks for that text on disk, so a
  copy is found because it is a copy. It carries the text as hashes
  rather than as prose, so that a machine running a shard holds no
  concept text at all, and it collapses whitespace first, because a
  concept wraps its prose and a transcript quoting it does not. It
  refuses both arms over a readable answer and the off arm over a
  readable concept. Rehearsed on a prepared workspace it refused over a
  second copy of the provider bundle in the plugin cache, installed
  under a different marketplace name by an earlier qualification run,
  which appears in no derivation of scope.

  **What none of this settles.** The experiment asks whether the
  installed bundle changes behaviour, and it has never asked whether
  the model carries these traps in its own prior knowledge. After three
  harness failures in two days it would be easy to expect the next run
  to show an effect merely because the last three could not have. A null
  on a clean run is a real null, and the model entry above already
  argues a null is likelier on the stronger model.

  Nothing registered changes. The seven cases, the two arms, the
  prompts, the twenty trials per case per arm, the metric and the
  decision rule are as registered. No powered arm has run.

- 2026-09-22 (third correction, the contamination check had almost no
  power): the check that asks whether a bundle-off transcript reproduced
  a concept's prose was doing so against three fourteen-word windows per
  concept, six for a case citing two. That is ample for the gate that
  runs before each arm, which asks whether a copy of a whole file is
  readable and finds one by any of its windows. It is thin for the
  question the transcripts pose, because a trial can quote a paragraph
  and miss three windows out of hundreds. Every off arm reported clean
  so far was reported clean against six windows, which is a weaker
  sentence than it sounded, and it was written here and in the shard
  records as though it were a strong one.

  Where an audit runs the concepts are readable, so it can use all of
  their windows. It now does, minus any window that also occurs in
  material the design leaves in place. The skills matter most there:
  they cite and paraphrase the knowledge, they are deliberately not
  ablated, and a window shared with them says nothing about whether a
  concept was on the machine. The skills of every bundle count, since a
  case's concept and the skill quoting it are routinely in different
  bundles.

  The five cases completed by this date were re-audited against 178 to
  962 windows rather than three or six. Every off arm remains at zero.
  Four bundle-on transcripts across two cases do reproduce prose, which
  is the positive control that was missing until now: the test finds
  reproduction where reproduction happened, in trials that could read
  the concept, and finds none in any off arm. The conclusion is
  unchanged and the evidence behind it is not.

  The gate is deliberately unchanged. It runs where the concepts are not
  readable, which is why its fingerprints are frozen as hashes, and
  three windows per file answer the question it asks. No shard's gate
  behaviour differs, in flight or otherwise, and no trial's score is
  touched by any of this.

  Recorded also: the gate printed one verdict for both arms, stating
  that no copy of a cited concept was readable. Only the off arm is
  checked for that; the on arm's concept hits are counted and discarded,
  because the on arm is supposed to have its concepts. The line asserted
  of the on arm something no arm verified, in a log every shard carries
  twice. Each arm now states what it checked.

  Nothing registered changes. The seven cases, the two arms, the
  prompts, the twenty trials per case per arm, the metric and the
  decision rule are as registered.

- 2026-09-22 (the seven cases on the headline model, and what the number
  is not): all seven gotcha-avoidance cases completed both arms on a
  harness where the bundle-off arm was genuinely off. Pooled risk
  difference **+0.131**, Newcombe 95% **[+0.003, +0.254]**, bundle-on
  55 of 112 valid trials and bundle-off 41 of 114.

  | case | on | off | difference (95%) | lost |
  |---|---|---|---|---|
  | native-grid-refusal | 20/20 | 17/20 | +0.150 [-0.038, +0.360] | 0/0 |
  | swot-calval-window | 6/17 | 3/15 | +0.153 [-0.157, +0.420] | 3/5 |
  | ecco-release-mixing | 6/12 | 8/13 | -0.115 [-0.437, +0.243] | 8/7 |
  | mht-basin-scope | 8/19 | 0/20 | +0.421 [+0.172, +0.637] | 1/0 |
  | swot-crossover-unapplied | 6/19 | 2/17 | +0.198 [-0.080, +0.438] | 1/3 |
  | grace-leakage | 9/9 | 10/11 | +0.091 [-0.217, +0.377] | 11/9 |
  | geothermal-omission | 0/16 | 1/18 | -0.056 [-0.258, +0.143] | 4/2 |

  The interval clears zero by three thousandths. Five cases point one
  way and two the other, and only one case excludes zero on its own.

  **The arm was off, and this is the first run that can show it.** Across
  140 bundle-off transcripts, none reproduces a line of the concepts its
  case cites, audited against every window rather than three. Thirteen
  bundle-on transcripts do reproduce concept prose, eight of them on one
  case, which is the positive control: the test fires where trials could
  read the concept and is silent where they could not.

  **What the number measures is narrower than the knowledge layer.** The
  registered design does not ablate the skills, and the skills carry more
  of this material than a pointer. On grace-leakage a script inside the
  skills tree states the coastal filter substance directly, a passing
  bundle-off trial cites that script by name and reproduces the point,
  and nine of ten passing bundle-off trials name the filter without any
  concept on the machine. Three of them say in so many words that they
  supplied the rest from their own knowledge; seven do not say. So the
  bundle-off arm is not knowledge absent. It is **concept absent**, with
  topic pointers and one substantive script retained, and the residual
  text cannot be separated from what the runtime already knew. The
  difference above is the effect of removing the concept files. It is not
  the effect of removing the knowledge, and it should not be quoted as
  though it were.

  **A stopping condition was recorded and the runs went ahead anyway.**
  The first completed record states that the remaining shards must not
  start until the ablation scope question is settled, because the skills
  restate what the concepts say. What was settled before the others
  started was a different matter, that a transcript naming a concept path
  has not read it. The scope question was not adjudicated, and six cases
  ran past it. The seven records stand as produced and none was edited,
  but the sequence was wrong and is recorded here rather than tidied
  away. A second case has now reached the same finding by a different
  route, with a script rather than a restatement, which is stronger
  evidence than the first record had.

  **About a fifth of the trials were lost**, 28 of 140 on the bundle-on
  arm and 26 of 140 on the bundle-off arm, every one of them to turn
  exhaustion at the cap and none to rate limiting. grace-leakage kept 9
  and 11 of 20, so its difference rests on almost nothing, and its two
  arms differ by ten points of loss, which is the threshold at which an
  uneven loss is flagged. geothermal-omission scored zero of sixteen
  against one of eighteen: a case the capability fails with the bundle as
  thoroughly as without it.

  **One more check could not fail.** The transcript audit reported a clean
  bundle-off arm across zero transcripts and exited successfully, for a
  shard that pushed its results without its transcript directories. It
  now refuses an arm with no transcripts. The same shape as every earlier
  fault here: a check returning a reassuring answer to a question it was
  not able to ask.

  Nothing registered changes. The seven cases, the two arms, the prompts,
  the twenty trials per case per arm, the metric and the decision rule
  are as registered. This is one model only and the second model has not
  run, so no go or stop condition is in play.

- 2026-09-23 (the second model, and five faults found by sharing a
  machine): all seven cases completed both arms on the second registered
  model. Pooled risk difference **+0.153**, Newcombe 95%
  **[+0.036, +0.264]**, bundle-on 58 of 131 valid trials and bundle-off
  38 of 131.

  | case | on | off | difference (95%) | lost |
  |---|---|---|---|---|
  | native-grid-refusal | 6/20 | 11/20 | -0.250 [-0.496, +0.052] | 0/0 |
  | swot-calval-window | 12/16 | 5/18 | +0.472 [+0.136, +0.685] | 4/2 |
  | ecco-release-mixing | 7/17 | 3/17 | +0.235 [-0.070, +0.491] | 3/3 |
  | mht-basin-scope | 8/20 | 1/19 | +0.347 [+0.082, +0.565] | 0/1 |
  | swot-crossover-unapplied | 1/20 | 1/19 | -0.003 [-0.201, +0.188] | 0/1 |
  | grace-leakage | 17/18 | 13/19 | +0.260 [+0.001, +0.489] | 2/1 |
  | geothermal-omission | 7/20 | 4/19 | +0.139 [-0.140, +0.390] | 0/1 |

  **The two models are reported side by side and are never pooled.** The
  first gave +0.131 [+0.003, +0.254] and this one +0.153 [+0.036,
  +0.264]. Two runs on different models and different machines, landing
  within 0.022 of each other with heavily overlapping intervals. This
  run is the better conditioned of the two: it lost 6.4 percent of its
  trials against about 19 percent, and the loss is exactly even between
  arms rather than ten points apart on one case.

  **The arm was off here too.** Across the seven cases no bundle-off
  transcript reproduces a line of the concepts its case cites, audited
  against 178 to 962 windows each. Nine bundle-on trials do reproduce
  prose, eight of them on grace-leakage, which is the same case and the
  same count as the first model produced. The positive control behaves
  identically across two runs on different models.

  **One case runs against the rest and is named rather than buried.**
  native-grid-refusal scored better without the bundle, a difference of
  -0.250 whose interval only just includes zero. On the first model that
  same case was the strongest positive at +0.150. A case that reverses
  sign between models is a result about the case, not noise to average
  away, and it is the first place a reader should look.

  **Both arms of this run came from two invocations rather than one.**
  The off arm was refused by its own gate, correctly, and then failed on
  an incomplete fix. Rather than discard 140 completed and validly gated
  bundle-on trials, the harness was fixed and the off arm run separately
  against the same workspace, the same model, the same trial count and
  the same quarantine discipline. Every case on the first model ran both
  arms in one invocation. The deviation is recorded because it is real,
  not because it is thought to matter.

  **Running both arms on one machine found five faults**, none of which
  could appear while every arm was given a fresh one. The check for
  recorded answers matched directory names exactly and so could not see
  `transcripts_on` or `transcripts_off`, the names the harness itself
  writes: forty eight recorded answers sat readable and it reported
  nothing. The off arm could read the on arm's results file, which
  carries every verdict and the grader's reasoning about what each
  response said. The restore refused an absolute symlink, returned a
  tree holding 370M of its 2.1G and never attempted the archives behind
  it. The restore was registered after the loop that moves trees, so a
  failure inside that loop left seven trees, three of them installed
  knowledge, with no handler to put them back; they were recovered by
  hand. And the transcript audit scanned a whole arm for each case, so
  every line reported the arm's total where the case's was meant.

  Four of those five weaken a guarantee this record has relied on. They
  are fixed, and the run above was gated by the fixed versions.

  **The standing caveat is unchanged and still governs both numbers.**
  The registered design does not ablate the skills. The bundle-off arm
  is concept absent, not knowledge absent, and neither difference should
  be quoted as the effect of removing the knowledge.

  Nothing registered changes. The seven cases, the two arms, the
  prompts, the twenty trials per case per arm, the metric and the
  decision rule are as registered.

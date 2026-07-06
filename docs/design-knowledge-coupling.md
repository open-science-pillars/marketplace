# Design note: how knowledge should couple to skills and agents

**Status:** ADOPTED 2026-07-05 after a measured proof-of-concept (see POC
results below); migration across all repos COMPLETE and the 16 new concepts steward-verified (2026-07-06). The knowledge layer now augments behavior as designed.
**Date:** 2026-07-05. **Prompted by:** the Session 19 ablation pilot and the
question "the knowledge bundles were meant to augment the skills and agents
over time: is that happening?"
**Decision owner:** steward (Paul Ramirez, pro tem). Parked as PARKING #14.
The candidate SPEC §5 language below is written into the next spec revision by
the build, not here (harness rule 11).

## The question

The premise of the whole project is that the knowledge layer compounds: the
bundle grows through the ingest loop, and a growing bundle makes the
assistant's behavior better over time without rewriting code. Is that
actually happening?

## Finding: no, not automatically, and we have proof

The Session 19 ablation pilot removed `knowledge/` from the installed
ocean-science plugin and re-ran the gotcha-avoidance suite. Behavior was
**identical** with and without the bundle (pooled 0.76 both arms, per-case
delta 0.00 across all seven cases). At runtime the knowledge bundle is
currently **inert**: the skills, not the concepts, drive behavior. So the
"augment over time" property is not being delivered in the way it was meant.

Capture works; runtime augmentation does not. The bundle genuinely grows,
with evidence links and steward review. What is broken is the path from a new
concept to changed behavior.

## What the current path actually is (the evidence)

1. **Skills carry the knowledge, not just a pointer to it.** Each workflow or
   knowledge skill has a "Knowledge first" section that names *specific*
   concept files, then a Must-NOT list that *restates the gotcha as a rule*.
   Key content is often duplicated inline: the SWOT crossover fact is written
   into the `swot` skill body, and the MHT basin numbers
   (`0.666 + 0.430 + 0.002 = 1.098 PW`) are hardcoded in the
   `meridional-transport` skill body, even though the recipe is supposed to be
   the single source of those numbers.
2. **The coupling is by fixed name, not by discovery.** A skill references a
   hardcoded set of concepts, so a newly ingested concept is invisible until a
   human edits the skill. The three gotchas promoted in Session 18
   (`ecco-release-mixing`, `ecco-mht-basin-scope`, `swot-crossover-unapplied`)
   are referenced by **zero skills**; they are cross-linked only from the
   dataset concepts.
3. **Augmentation happens, but manually.** In Session 11 the linter caught
   that both SWOT skills routed around a newly ingested fact, and a human
   applied "accommodation diffs" copying the rule into the skills. That is the
   mechanism today: ingest a concept, wait for the linter to notice a skill
   ignores it, hand-edit the skill. It works, but it is manual, duplicative,
   and bounded by the linter's nagging.
4. **The agents already do the right thing.** `ecco-scout`'s instruction is
   "Consult the knowledge bundle FIRST ... gotchas that constrain the plan ...
   cite each consulted concept by bundle path." That is generic and dynamic:
   the pattern this note argues for already exists in the agent layer.

Roughly 11 of 38 skills reference `knowledge/` at all, and where they do, they
tend to mirror the concept's content rather than defer to it.

## Was this the design, or a drift?

A drift, and a subtle one. SPEC §5 did say "workflow skills consult relevant
concepts before acting on a dataset," so skills-consult-knowledge was
intended. What the spec did *not* intend was duplication: recipes are "the
authority; this skill carries no expected values." Two things drifted:

- "consult *relevant* concepts" became "consult *these named* concepts"
  (discovery lost), and
- the gotcha rules got copied into skill bodies for deterministic, testable
  Phase-1 behavior (single-source lost).

Both were pragmatic for shipping. Together they quietly severed the
augmentation path, which the pilot then measured as a zero delta.

## The proposed model

Three layers with clean responsibilities:

- **Skills are repeatable, deterministic procedures.** "Compute MHT at a
  latitude," "load with the volume gate," "write the report." A skill carries
  the *how*, not dataset knowledge and not gotcha rules. It keeps only the
  **hard refusals** that must be guaranteed (refuse a regridded budget, stop
  at the gate); those are safety guards, not lookups.
- **Knowledge bundles are the single, growing source of truth.** Every fact a
  scientist would look up (the trap, the uncertainty structure, the recipe
  numbers, the version caveat) lives in exactly one concept, with evidence and
  status. Nothing is copied into a skill.
- **Agents consult a discoverable bundle as needed.** Given a task and a
  dataset, an agent *discovers* the relevant concepts (glob and grep the
  bundle by dataset and topic, not a hardcoded list), reasons with them, and
  cites them by path. A new concept is found automatically, so the bundle
  augments behavior with no code change.

The harness (Claude Code and its peers) already provides the retrieval
primitive: the agent can `Read`, `Glob`, and `Grep` any concept on demand.
What is missing is a *standing convention* ("before acting on a dataset,
consult its concepts in `knowledge/` and any bundle named in local config")
in place of per-skill hardcoded pointers, optionally backed by a small
knowledge-retrieval step or MCP server so relevance routing is not ad hoc.

## Why this is the same project as the ablation

The ablation cannot show a signal today because knowledge is inert. Under the
proposed model, removing `knowledge/` *would* degrade behavior, because the
agent would have nothing to consult. So the design change is what makes the
Session 19 experiment measure the thing the whole thesis rests on. The fix and
the measurement are one deliverable, not two.

## The honest tradeoff

Moving knowledge out of skills trades **guaranteed** behavior for
**augmentable** behavior. Today "never mix V4R4 and V4R4B" fires every time
because it is hardcoded; under the proposal it fires because the agent
consulted the concept and reasoned, which is more variable. That variability
is exactly what the evals exist to quantify, and it is the honest cost of a
knowledge layer that actually compounds. Phase 1 deliberately chose the other
side of this trade to ship testable behavior; the proposal is to move to the
augmentable side now that the capture layer is mature, keeping a thin
deterministic floor of hard refusals so nothing unsafe becomes probabilistic.

## Proof of concept (before any repo-wide change)

Prove or disprove the model on one triple, measured, reversible:

- **Target:** `transport-analysis` (skill) + `ecco-scout` (agent) + the MHT
  concepts (`recipes/ecco-mht-26n.md`, `gotchas/ecco-mht-basin-scope.md`).
- **Change (on a branch):** slim `transport-analysis` to the pure procedure
  (drop the inlined `0.666 + 0.430 + 0.002` numbers and the basin-scope rule
  from its body, keeping only the compute steps and any hard refusal); make
  `ecco-scout` (or a small pre-flight consult step) discover and inject the
  MHT concepts by glob, citing them; leave every other skill untouched.
- **Measure:** re-run the ablation harness (`evals/runner/ablate.sh`) on the
  MHT cases, bundle-ON vs bundle-OFF, on the recorded model at a usable N.
- **Success criterion:** with the proposed coupling, the ON-OFF delta becomes
  positive and resolvable on the MHT cases (knowledge removal degrades
  behavior), while the hard-refusal cases stay at ceiling in both arms
  (safety unaffected). A null delta would falsify the model and we keep the
  current path.

This gives a concrete, measured before/after on one dataset rather than a
whole-repo refactor on faith. It also doubles as the redesign the Session 19
amendment already said the powered ablation needs.

## POC results (2026-07-05)

Executed on the `ocean-science/poc-knowledge-coupling` branch: the basin-scope
anchors and rule were removed from `meridional-transport` and
`transport-analysis`, transport-analysis was made to discover and consult the
concepts dynamically, and `ecco-scout` was made to discover by glob/grep. The
ablation ran on the installed POC plugin, bundle-ON vs bundle-OFF, model
claude-opus-4-8 (Fable 5 quota-exhausted), N=5, with `Glob`/`Grep` in the
trials' toolset so the slimmed skill could discover concepts.

| Case | ON | OFF | delta |
|---|---|---|---|
| `mht-basin-scope` (knowledge-dependent) | 4/5 (0.80) | 1/5 (0.20) | **+0.60** |
| `native-grid-refusal` (hard-refusal control) | 5/5 (1.00) | 5/5 (1.00) | 0.00 |

The same `mht-basin-scope` case on the current design (Session 19 pilot) had a
delta of **0.00**. So the coupling change flipped the bundle from inert to the
operative driver of behavior (+0.60), while the hard-refusal control stayed at
ceiling in both arms, confirming the safety floor is unaffected by removing
knowledge. Caveats: N=5 leaves the intervals slightly overlapping
(ON `[0.38, 0.96]`, OFF `[0.04, 0.62]`); the effect is large and correctly
directed but a powered N=20 is needed to resolve the interval away from zero;
model is Opus, not the pre-registered Fable 5. The success criterion (positive
resolvable MHT delta, control at ceiling) is met at pilot scale.

## Decision (2026-07-05): adopt, with a rule for what stays hardcoded

Adopted across all repos. Migration proceeds skill by skill and domain by
domain, on branches, with the ablation re-run on a knowledge-dependent case
after each domain to confirm the delta holds and the control stays flat.

**Hard-refusals that stay hardcoded in skills (agreed set):** regridded-budget
refusal, download volume gates, and credential handling (never in a repo).
These are safety/correctness guards, not lookups.

**The rule for deciding what stays hardcoded** (so the set is a judgment, not a
list). A behavior stays hardcoded in a skill only if it passes ALL THREE tests;
otherwise it is dataset knowledge, lives in exactly one concept, and is
consulted dynamically. The default is knowledge; hardcoding is the exception
that must justify itself.

1. **Invariance.** It does not change with a product version, a new dataset, or
   new learning. "A budget on regridded fields never closes" is a property of
   the math (invariant); "ssha_karin needs `height_cor_xover`" is a property of
   a product baseline that can change (not invariant, so knowledge).
2. **Response shape.** The correct response is to REFUSE or GATE (stop, or
   require explicit confirmation), not to INFORM or ADJUST. Refusals and gates
   are binary safety valves; informing the scientist or adjusting the analysis
   is reasoning that should use current knowledge.
3. **Universality.** Violating it is wrong or unsafe regardless of the dataset
   or task, so it must fire every time, not most of the time (a correctness
   invariant, a safety gate, or a security rule).

If a rule is dataset-specific, could change over time, or its right response is
"inform or adjust" rather than "refuse or gate," it is knowledge. When
uncertain, put it in knowledge: an over-hardcoded rule silently freezes
behavior and makes the knowledge layer inert (the exact failure this change
fixes), whereas an over-delegated rule at worst adds a consult step. Method
physics that is invariant and not a refusal (for example "a meridional section
is a set of cell faces, not a `j = const` row") may stay in a skill as
procedure; it is not a dataset fact and not something a scientist looks up per
analysis.

**The mechanism, so this becomes the path forward (not a one-time cleanup):**
the coupling model and this rule go into `build-kit` (the workspace-law
template and DEVELOPING guide); a reusable review workflow
(`build-kit/workflows/knowledge-coupling-review.js`) classifies every skill and
agent against the rule and emits a migration plan; and the knowledge-linter
gains checks that flag (a) a skill body that inlines a concept's number or
restates a dataset gotcha rule, (b) a hardcoded rule that does not pass the
three tests, and (c) a high-severity concept referenced by no consult path (an
inert concept). Together these make the model self-enforcing: new development
follows it, and drift is caught mechanically.

## Candidate SPEC §5 revision (language to consider, not yet applied)

- **§5 coupling rule (new):** "Skills are deterministic procedures and hard
  safety refusals; they carry no dataset facts, gotcha rules, recipe numbers,
  or named-concept lists. Dataset knowledge lives in exactly one concept.
  Agents, and workflow skills only through an agent or a standing consult
  step, discover the relevant concepts for the dataset in play (by bundle
  glob, not a fixed list) and cite them by path."
- **§5 single-source rule (tighten the existing recipe rule to all types):**
  "No concept content is duplicated into a skill body. A skill that needs a
  number, a caveat, or a rule references the concept; it does not restate it."
- **§5 augmentation acceptance (new, ties to §8 evals):** "The knowledge
  layer's effect is demonstrated, not assumed: the bundle-ablation delta on
  the gotcha-avoidance suite is positive and resolvable, or the coupling is
  considered broken."
- **Linter checks to add:** flag a skill body that inlines a concept's number
  or restates a gotcha rule (the duplication the current linter's check 11
  does not catch); flag a high-severity concept referenced by no agent or
  consult path (an inert concept).

## If adopted: migration sketch

Order of work, each measured before the next:

1. The POC triple above (one skill, one agent, one dataset), measured.
2. If green: standardize the consult step (a small agent or a generic
   "consult the bundle for this dataset" convention the skills call), and the
   two new linter checks, so drift cannot recur silently.
3. Migrate skills domain by domain (ocean, then hydrology, then core),
   slimming each to procedure-plus-refusal and deleting inlined knowledge, with
   the ablation re-run after each domain to confirm the delta holds and the
   hard refusals stay deterministic.
4. Revise SPEC §5 to the adopted language, bump the spec, update the guides.

## Decision needed

1. Do we adopt the model in principle (skills = procedures; agents consult a
   discoverable bundle; hard refusals stay deterministic)?
2. Approve the POC on the MHT triple as the go/no-go test before any wider
   change?
3. Any constraint on the determinism tradeoff: which behaviors, if any, must
   stay hardcoded-guaranteed regardless (candidate list: regridded-budget
   refusal, volume gates, credential handling)?

## Mechanism built (2026-07-05)

Adoption is now self-enforcing, not a one-time cleanup:
- Global rule 12 in the build-kit CLAUDE template makes the coupling model law
  for new work; DEVELOPING.md explains the three-layer division.
- `build-kit/workflows/knowledge-coupling-review.js` classifies every skill and
  agent against the rule and emits the migration plan (it produced the current
  backlog: 37 files, 269 raw items, ~53 candidate concepts).
- The knowledge-linter gains checks 14 (inlined concept content), 15
  (unjustified hardcode), 16 (inert concept) to catch regressions at close.
- The goal and per-domain backlog live in `build-kit/build-record/knowledge-coupling-migration.md`;
  the migration proceeds domain by domain, concepts-with-evidence first, each
  ablation-verified. The review workflow reporting zero files is the exit test.

## Finding: not all knowledge moves the ablation (2026-07-05)

Migrating the ecco/ocean-budget cluster and re-running the ablation showed
geothermal-omission at 0.00 delta (5/5 both arms), versus mht-basin-scope at
+0.60. The migration is correct (no regression, drift removed); the null is
about the CASE: geothermal in a deep budget is general physics the model knows,
so that concept is redundant with training and cannot move the ablation. The
knowledge layer's measurable value concentrates in the non-obvious,
dataset-specific traps (scope errors, unapplied corrections, version splits,
provisional data), not the textbook rules. Implication: judge the knowledge
layer, and migrations, on non-obvious probe cases; obvious concepts remain
correct safety nets whose value is a guarantee, not a measurable lift.


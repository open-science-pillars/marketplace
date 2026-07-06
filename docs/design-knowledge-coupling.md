# Design note: how knowledge should couple to skills and agents

**Status:** proposal for steward review (not adopted; no code changed).
**Date:** 2026-07-05. **Prompted by:** the Session 19 ablation pilot and the
question "the knowledge bundles were meant to augment the skills and agents
over time: is that happening?"
**Decision owner:** steward (Paul Ramirez, pro tem). This note proposes a
SPEC §5 revision and a proof-of-concept; it does not change the spec (the
build writes spec revisions, not forethought, harness rule 11). Parked as
PARKING #14.

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

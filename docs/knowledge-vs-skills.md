# Knowledge bundles vs skills: the line and how to find it

Contributors regularly face the question: does this belong in a knowledge
bundle or in a skill? This doc is the org's line in the sand, the tests
that make it usable, and what to do when a case is genuinely unclear. It
sits on top of the coupling decision adopted 2026-07-05
(docs/design-knowledge-coupling.md) and OSP's four-plane anatomy: REACH
(connectors), ACT (skills), KNOW (concepts), PROVE (guards).

## The principle

**Knowledge has a truth condition; skills have a quality condition.** A
concept states something about the world that a steward can sign as true,
the world can later falsify, and time can make stale. A skill directs an
agent's behavior, which can only be good or bad at a task: measurable by
evals, never signable as true. Everything below is that one asymmetry
applied. It is also why only KNOW can be a pillar: signatures attach to
claims; evals attach to conduct.

Consequences you can lean on. Accountability: concepts get `verified`
events and trust tiers (OKF v0.2 §5); skills get eval cases. Lifecycle:
concepts expire on world events (a reprocessing, a tool release, a
successor product) and carry `stale_after`; skills expire on model or
harness events and get re-tuned. Security: concepts are data and never
instruct the agent (SPECIFICATION §5.8), which is what lets the
contribution funnel stay wide for bundles and tight for skills. Audience:
a concept helps a scientist with no agent in the room; a skill is
meaningless without an executor.

## The three tests

Run these on the thing you want to contribute, in order:

**1. The mood test.** Rewrite it entirely in the indicative. If nothing is
lost, it is knowledge. "Mixing V4R4 and V4R4B conflates baseline
corrections with signal" survives; "never mix V4R4 and V4R4B" is the
skill's restatement of it. If deleting every imperative destroys the
artifact, it is a skill.

**2. The reader test.** Would a domain scientist, with no agent involved,
learn something by reading it? A gotcha, a tolerance, a variable list:
yes, knowledge. A confirmation gate, a tool-invocation order, a report
workflow: no, skill.

**3. The expiry test.** What event invalidates it? A world event (PO.DAAC
announces a reprocessing, ecco_access ships a release that changes the
observed quirk, V4r5 becomes the recommended product) means knowledge,
dated and stale_after-ed. A model or harness event (a new Claude, a
changed tool surface) means skill.

Two supporting rules. **The signature rule:** if a steward could not
meaningfully sign it as true, it is not a concept. **The single-source
rule:** every number, tolerance, ShortName, and caveat lives in exactly
one concept; skills consult and cite, they never mirror. The ablation
experiment is the standing evidence for why: inlined knowledge made the
bundle behaviorally inert.

## The direction of dependence

Skills defer to knowledge, discovered rather than hardcoded, per the
adopted coupling model. The one sanctioned exception: **hard refusals stay
in skills** (refuse a regridded budget, stop at the volume gate). Safety
must not be probabilistic, so the deterministic floor lives in ACT even
though the fact behind each refusal lives in KNOW and is cited by it.

## Boundary cases, resolved

| Case | Where it goes | Why |
|---|---|---|
| A validated method with measured numbers (a recipe) | KNOW | it is a falsifiable claim about a method, with evidence and a signature; the imperative walkthrough of it is the skill |
| An Attested Computation (OKF v0.2 §10) | split | the contract (parameters, sanctioned code identity, verdict thresholds) is KNOW; the executor is ACT; the attester is PROVE. The spec says it itself: it fixes the interface, not the packaging |
| An observed tool quirk, dated | KNOW | "ecco_access 0.3.1 synthesizes nonexistent filenames for static collections (observed 2026-07-04)" is a fact; "use earthaccess for static collections" is the skill's conclusion, citing it |
| A rule that must fire every time | ACT (hard refusal) | the deterministic floor; the fact it rests on is still a concept |
| A community definition or index convention | KNOW (convention) | citable, signable, world-invalidated |
| A connector (an MCP server registration) | split | the wire is REACH (`.mcp.json`, not signable); its facts (endpoint, tool surface, auth boundary, deprecation) are KNOW as a connector concept; when to reach for it is ACT; PROVE stays direct, gates never depend on a connector |
| Worked examples, prompts, workflow discipline, diagnosis order | ACT | behavior shaping; evaluated, not verified |

## The contributor decision aid

Before opening a PR, answer these five; the first-column answers point to a
concept, the second to a skill:

1. Does it survive a full rewrite into the indicative? (yes: concept / no: skill)
2. Would a scientist with no agent benefit from reading it? (yes / no)
3. Could a steward sign it as true, and could the world falsify it? (yes / no)
4. What invalidates it? (a world event / a model or harness event)
5. Is it a number, tolerance, name, or caveat that must live exactly once? (yes: concept, and skills cite it / no)

Four or five first-column answers: author a concept using
docs/knowledge-authoring-guide.md. Four or five second-column answers:
author a skill using docs/skill-authoring-guide.md, and make sure any facts
it leans on already exist as concepts it can cite. A genuine split (an
Attested Computation, a refusal plus its underlying fact) is usually two
small contributions, one per plane, cross-linked.

**When it is still unclear:** open an issue with the `layer-decision`
label describing the artifact and your answers to the five questions. The
bundle steward decides under lazy consensus, and the decision is recorded
in the bundle's `log.md` so the next contributor inherits the reasoning,
not just the ruling. Close calls are expected; the label exists so they
become precedent instead of friction.

Orientation to keep: **knowledge compounds, skills converge.** The bundle
grows monotonically and improves behavior with no code change; skills trend
thinner as models improve, asymptoting toward the refusal floor plus
procedure shape. When in doubt, put the durable thing where it compounds.

## PR template addition

One checklist line for the pull request template:

```
- [ ] Layer check: I ran the five-question decision aid in
      docs/knowledge-vs-skills.md; facts live in concepts, behavior lives
      in skills, and nothing is mirrored between them.
```

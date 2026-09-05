# Knowledge authoring guide

How to write OKF concepts for Open Science Pillars bundles.
Conformance: OKF v0.2 (vendored under docs/upstream, pinned by
commit) plus the specification's knowledge layer
(docs/SPECIFICATION.md); the knowledge-template repo carries one
annotated example per type.

## The concept types and their required extras

- **dataset**: `resource`; version or processing baseline WITH a
  verification date; an `## Uncertainty` section in the body. The
  Uncertainty section is not optional decoration: it names the
  product's error fields and their caveats, or states plainly that
  none exist and what stands in (ECCO's dynamical consistency is the
  canonical example).
- **dataset-gotcha**: `severity` (high means silently wrong results;
  high requires a matching eval-case id); a link to
  its dataset concept (cross-cutting gotchas state a scope instead,
  the core-bundle exception); at least one `sources` entry.
- **recipe**: `inputs`; `expected` AND `expected_uncertainty` (ranges,
  or a pointer to the Attested Computation concept that owns the pass
  bar, OKF v0.2 §10); validation provenance in `sources`. Skills read
  recipes; recipes never live in skill bodies.
- **convention**: the org-wide fields only.
- **computation**: the sanctioned code path with its sha, the input
  manifest, and the receipt of one run (OKF v0.2 §10). The reference
  values and tolerances that recipes and findings quote live here, and
  a recipe cites them by path rather than copying them (the
  specification's ownership-of-numbers rule).
- **finding** (a candidate type in the specification): one falsifiable
  claim. `question`, `claim` bound field by field to a cited receipt,
  `computations` cited by receipt, `validity` adjudication,
  `confrontation` record, `limitations`; every number in the text
  resolves to a receipt field or a sourced context constant; stable
  only by a `human:` signature with verdict IN. Gate:
  `check_okf_v02.py --findings` in nasa-daac-knowledge.
- **dead-end** (a candidate type in the specification): the record of
  an attempt that failed. `subject` (the concept paths it was tried
  against), `attempt: {goal, method}`, `failure: {symptom, cause}`
  (`unknown` is an honest cause), `observations` each
  `{at, by, source}` (the key is `at`; YAML reads `on` as a boolean),
  `reopens_if`, and `load_bearing` (high, medium, low; high requires
  `eval_case`, the gotcha severity rule applied to negative
  knowledge); `stale_after` should be present, because tools get
  fixed. Body sections in order: Attempted, Observed, Why it fails,
  Do instead (optional, expected on a high entry), Reopens if. Write
  it as an attribution ("this was tried on this date and failed
  because"), never as a universal ("impossible", "never works"); the
  checker warns on universals. A dead-end is reopened with evidence,
  never deleted.
- **field-state** (a candidate type in the specification): where a
  field stands on one question as of a date. `question` (one sentence
  ending in a question mark), `as_of`, `state` (disputed, which needs
  two or more positions; open; converging), `positions` each
  `{id, statement, held_by, sources}` with the statement in the
  holders' own terms, optional `bears_on` (the concepts whose reading
  depends on the question), `stale_after` (required), and
  `load_bearing` as above. No `claim`, `verdict`, `answer` or
  `resolution` key and no section headed that way: the concept records
  positions and takes no side, and a signature attests the record of
  the discourse, not a position. Body sections in order: Question,
  Positions, Bearing, What would move this. Superseded by the later
  reading, never deleted.

The two negative-knowledge types live under `dead-ends/` and
`field-states/` in a bundle and are gated by
`uv run tools/check_negative.py knowledge/<bundle>` in
nasa-daac-knowledge (in its check routine; `--explain` shows how every
path and source resolved). Their truth condition is attribution: the
cited attempts and positions exist and say what the concept says they
say, whether or not the approach later works or the question is later
settled.

Org-wide on every concept: `title`, `description`, `tags`,
`generated: {by, at}` (who wrote it, in the actor convention, and the
last meaningful change), `status` (lifecycle: draft, stable,
deprecated), a `verified: {by: human:<id>, at}` event once a steward
signs (never self-added by a drafting agent), `sources:` entries with
stable ids for what the concept derives from (body claims join them
with `[^id]` footnotes, OKF v0.2 §5.1), and `stale_after:` (the sweep
date; staleness is now >= stale_after). Optional `trainings:` lists
ARSET or equivalent training URLs on datasets and recipes.

## Hard-won rules from this build

1. **Quote YAML values containing colons.** Claude Code's own parser
   is lenient; the bundle standard is strict YAML, and the linter
   red-flags unquoted `title: Something: subtitle` (it caught three on
   day one).
2. **Sources or nothing.** Every gotcha and recipe claim carries a
   resolving `sources` entry, joined to the claim with a `[^id]`
   footnote (OKF v0.2 §5.1); a source-free concept is worse than a gap.
   Verify resources resolve BEFORE committing; the linter fetches them.
   Publisher bot-blocks (a 403 on a real DOI) are acceptable with a
   recorded secondary verification (Crossref).
3. **Facts, not instructions.** Concepts never direct the
   agent: no "quote this per the house rule", no "never mix X
   silently" imperatives. State the fact ("an analysis that mixes
   releases silently conflates corrections with signal"); behavior
   lives in skills. Write in the declarative "owned by" voice: prefer
   "the SWOT cal/val record is a distinct product family" over
   "always check which family you loaded". The knowledge-linter's
   imperative-phrasing scan (documented in
   `core/agents/knowledge-linter`) enforces this.
4. **Record scopes and dates on numbers.** The build's costliest
   correction was a heat-transport anchor recorded without its basin
   scope (a full-circle value that read as if it were the Atlantic),
   which nearly produced a wrong comparison against Atlantic-only
   observations; expected values carry the exact scope, method, and
   the date verified.
5. **Tolerances are measured, not assumed.** A closure or comparison
   criterion states what was measured, on what, and the headroom
   (see ocean-science/knowledge/recipes/ecco-heat-budget.md for the pattern: float32
   quantization made a relative criterion meaningless).

## Ingest etiquette

A peculiarity discovered during ANY analysis is drafted immediately
(correct type, frontmatter, links), queued for steward approval, and
logged in the bundle's log.md with its discovery chain; a method
that was tried and failed is drafted the same way, as a dead-end.
Never deferred, never buried in a comparison note. The rapid-mocha concept and the
SWOT crossover-calibration known issue are live examples, each ingested
the session it was found.

## Review path

Draft (yours or the knowledge-seeder's) → steward review per the
playbook checklist → `status: stable` with a
`verified: {by: human:<id>, at}` event added at approval → log
entry. High-severity gotchas and Uncertainty-section edits take two
reviews (a provider steward on provider bundles) per the specification's
stewardship and review rules.

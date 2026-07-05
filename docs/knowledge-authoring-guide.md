# Knowledge authoring guide

How to write OKF concepts for Open Science Pillars bundles.
Conformance: OKF v0.1 plus SPEC §5; the
knowledge-template repo carries one annotated example per type.

## The four types and their required extras (§5.2)

- **dataset**: `resource`; version or processing baseline WITH a
  verification date; an `## Uncertainty` section in the body. The
  Uncertainty section is not optional decoration: it names the
  product's error fields and their caveats, or states plainly that
  none exist and what stands in (ECCO's dynamical consistency is the
  canonical example).
- **dataset-gotcha**: `severity` (high means silently wrong results;
  high requires a matching eval-case id per harness rule 9); a link to
  its dataset concept (cross-cutting gotchas state a scope instead,
  the §3.6 exception); at least one evidence link.
- **recipe**: `inputs`; `expected` AND `expected_uncertainty` ranges;
  validation provenance as evidence. Skills read recipes; recipes
  never live in skill bodies.
- **convention**: the org-wide fields only.

Org-wide on every concept: `title`, `description`, `tags`,
`timestamp`, `status` (§5.6 lifecycle: draft, verified with `verified`
and `verified_by`, stale, superseded, disputed). Optional `trainings:`
lists ARSET or equivalent training URLs on datasets and recipes.

## Hard-won rules from this build

1. **Quote YAML values containing colons.** Claude Code's own parser
   is lenient; the bundle standard is strict YAML, and the linter
   red-flags unquoted `title: Something: subtitle` (it caught three on
   day one).
2. **Evidence or nothing.** Every gotcha and recipe claim carries a
   resolving link; an evidence-free concept is worse than a gap
   (§5.5). Verify links resolve BEFORE committing; the linter fetches
   them. Publisher bot-blocks (a 403 on a real DOI) are acceptable
   with a recorded secondary verification (Crossref).
3. **Facts, not instructions (§5.8).** Concepts never direct the
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

## Ingest etiquette (§5.3)

A peculiarity discovered during ANY analysis is drafted immediately
(correct type, frontmatter, links), queued for steward approval, and
logged in the bundle's log.md with its discovery chain. Never deferred,
never buried in a comparison note. The rapid-mocha concept and the
SWOT crossover-calibration known issue are live examples, each ingested
the session it was found.

## Review path

Draft (yours or the knowledge-seeder's) → steward review per the
playbook checklist → verified with `verified`/`verified_by` set → log
entry. High-severity gotchas and Uncertainty-section edits take two
reviews (a provider steward on provider bundles) per §5.4.

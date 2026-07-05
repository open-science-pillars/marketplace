# Announcement draft (Pangeo Discourse / Openscapes / ESIP)

DRAFT for Paul's review; not posted. Lead: the knowledge-bundle +
verification-layer story, per the architecture. Success criteria stated
up front per PARKING #1.

---

**Title: Open Science Pillars: AI-assisted ocean data analysis that
shows its work (and the knowledge layer that keeps it honest)**

We have released Open Science Pillars, an open marketplace of Claude
plugins for earth science, launching with physical oceanography (ECCO
v4r4, SWOT KaRIn SSH, GRACE-FO, GHRSST MUR) on Claude Code, Cowork, and
Claude Science: github.com/open-science-pillars

The part we think matters to this community is not the AI assistance;
it is the two layers wrapped around it:

**Dataset-knowledge bundles.** Practitioner knowledge about real
datasets, in reviewable markdown files with types, statuses, stewards,
and an evidence link on every claim: the ECCO budgets that only close
on the native grid, the SWOT cal/val orbit phase and its
version-family trap, GRACE coastal leakage, the crossover calibration
that arrives unapplied. Skills consult these concepts before acting and
cite them in reports, so a recommendation carries its caveats with it.
During our own build, the loop caught a real scope error in our first
transport recipe (a full-circle value about to be compared against the
Atlantic-only RAPID array) and corrected the concept under steward
review. That is the behavior we want AI-assisted science to have by
construction.

**A verification layer.** Every computational workflow ships an
executable marimo golden notebook: the heat budget closes pointwise at
5e-11 degC/s over 3.3 million cell-months of live PO.DAAC data; the
transport notebook reproduces recorded anchors and the basin-sum
identity. Plus a seed eval suite measuring agent scientific judgment,
including one honest failure we shipped rather than hid.

Try it: three timed tutorials (10/20/30 minutes, fresh-install
measured) and a browser demo with no install at all. Build your own
domain plugin from the template in about half an hour; the knowledge
bundle pattern is deliberately provider-adoptable, and we would love
to talk to data providers about stewarding bundles for their own
holdings.

**What we will judge success by** (stated now, before the results):
at least one external install with an issue filed; one non-author
scientist completing Tutorial 2 unaided; a with/without-bundle
ablation of the gotcha eval suite published with confidence intervals
(Phase 2); one provider steward reviewing concepts in their own
bundle. The ablation especially: if the knowledge layer does not
measurably reduce trap-hit rates, we want to know that as much as
you do.

Everything is Apache-2.0/open, PRs welcome (DCO), and the
known-limitations page says plainly what is verified where.

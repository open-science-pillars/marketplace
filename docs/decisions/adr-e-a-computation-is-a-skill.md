# ADR E: A computation is a skill

**Status:** Accepted 2026-09-20 (merged to main) by the decision owner,
the merge carried by the coordinator on the owner's instruction. Drafted
by the coordinator session at the decision owner's request after the
round five review, with the inventory below measured on the same day.
**Decision owner:** Paul Ramirez (interim steward). Personal-hat work:
Open Science Pillars is a personal open-source project, not a JPL or
PO.DAAC product.
**Companion records:** [ADR A](adr-a-pillar-means-sphere.md) (pillar
means sphere; unchanged, except that its vocabulary of planes is
retired here), [ADR B](adr-b-multi-runtime-capability-packaging.md)
(one canonical `skills/` tree rendered to every runtime; unchanged in
substance, restated in plain words), [ADR C](adr-c-code-placement-by-plane.md)
(superseded by this record except for one retirement it made, of the
`references/skills/` directory, which stands) and
[ADR D](adr-d-promotion-to-host-a-wrap.md) (superseded: with the
computation living in the capability there is no wrap to host and no
wrap-only release to define).
**Specification:** revision 0.7.0 retires section 0.6's plane
vocabulary, section 5.9's plane naming, section 11 (code placement)
and section 12 (the wrap-only releases), and adds one short section,
"A computation is a skill", in their place.
**Roadmap:** decision `a-computation-is-a-skill` and initiative
`computation-is-a-skill` in build-kit, one deliverable per repository
migration below.

## Context

A round five review of the receipt skills asked a plain question: why
does the code of an attested computation live in the knowledge bundle
when a skill with a script can be proven just as well? The answer the
organization had written down, in ADR C, is that the executor's
identity is part of a signed contract, and identity is KNOW, so the
code stays in the bundle even though the executor is ACT and the
attester is PROVE. That is a taxonomy doing the work an argument
should do. The taxonomy was introduced in September to describe what
already existed, and it has since been used three times to decide
where new things go: the placement rule and its seven-finding gate,
the wrapping rule that puts a skill in a capability whose only job is
to reach code in another repository, and the promotion-to-host-a-wrap
decision that lets a planned capability exist so that such a skill has
a home. Each was correct on its own terms and each added a layer.

What the layers produce, measured on 2026-09-20:

| Where | What is there |
|---|---|
| nasa-daac-knowledge, `knowledge/{podaac,nsidc,asdc}/references/` | 61 Python files, 24,386 lines: 20 executors, 19 attesters, 18 loaders, 4 derivation scripts; 5 stamped data roots and 53 record and evidence files under `retrieval/`, 6.4 MB in all |
| the same bundle, `tools/` | `run_checks.sh` with 12 chain functions and 80 run lines that exercise the executors, `reference_runs.yaml` with 33 named runs, `reattest.py`, `receipt_identity.py` |
| the same bundle, `knowledge/*/computations/` | 24 Attested Computation concepts, 20 stable, each naming an executor and an attester beside it and a wrapping skill in another repository through the organization extension `executor.skill` |
| ocean-science | 8 wrapping skills whose SKILL.md names 15 executors by the installed bundle's path and runs none of its own; 3 receipt skills that reach the same executors the same way; 1 local computation (Argo ocean heat content) whose code sits under `knowledge/references/` in the capability |
| land-ice, atmospheric-physics | 2 wrapping skills each, computing nothing, plus 3 receipt skills each; both repositories exist only because ADR D let them |
| hydrology | 1 local computation whose executor and attester sit under `knowledge/references/` |
| core | 1 local computation whose executor and attester sit under `verification/`, beside the golden that proves it |
| marketplace | ADR C, ADR D, specification sections 0.6 (four planes), 5.9, 11 (five subsections) and 12 (four subsections), the four-plane paragraph of the model document and of the knowledge-versus-skills guide, plane vocabulary in seven documents |
| build-kit | `osp.py placement-check` (findings P1 to P7), the seed brief renderer's wrapping and placement rules, `capability` and `skill` seed kinds written around the wrap, 87 roadmap lines that mention placement or wrapping |

A scientist who wants to run the ice sheet mass balance closure meets
a concept in the provider bundle, an executor and attester beside it,
a skill in the land-ice repository that reaches them by path and
copies nothing, three more skills beside that one that reach them the
same way, and an eval case in a third repository. The specification
needs five subsections and a seven-finding gate to say where each
piece goes.

The upstream Open Knowledge Format does not require any of this. Its
section 10 defines an Attested Computation as a concept whose
`computation`, `executor.resource` and `attester.resource` are paths,
and says in so many words that what sits behind a resource is a
packaging choice: it fixes the interface, not the packaging. The
`references/` convention is named as a convention, not a requirement.

What the bundle placement actually buys is three things, and none of
them is provability:

1. The signed number and the code that produced it version together
   with the stamped data root the code reads, in one release lock.
2. A computation can be shared across spheres (the energy budget reads
   an Argo receipt the ocean side produced).
3. The provider steward signs the method.

The third is moot in the interim solo period and would be wrong at
scale: a data center vouches for its products, not for a closure
someone computed from three of them. The first two are real and are
kept by this record without the taxonomy.

## Decision

1. **A knowledge bundle holds knowledge and evidence, and no runnable
   code.** Concepts, their sources, and the evidence files a concept
   cites: mirrored external material under `references/`, data files
   such as masks and calibration tables, and the stamped inputs and
   receipts that evidence a signed number. Nothing under `knowledge/`
   is executable, in a provider bundle or in a capability. The
   repository's own gates live in `tools/` as they do today and are
   not knowledge.

2. **A computation is a skill.** An Attested Computation concept lives
   in the capability that runs it, under that package's
   `knowledge/computations/`, which the locality rule already calls
   domain material. Its `computation` and `attester.resource` name
   files under `skills/<skill>/scripts/` in the same package; the
   `SKILL.md` beside them is the run procedure; the goldens under
   `verification/` prove the scripts; the stamped data root the
   executor reads lives under the package's `knowledge/references/retrieval/`
   as data. The organization extension `executor.skill` is retired,
   because the concept names the file and the skill is beside it. How
   computations group into skills is the capability's call: a skill
   may carry the scripts of several computations that one workflow
   runs together, as ocean-budget does today.

3. **The provider bundle is the authority on products; the capability
   is the authority on methods.** Dataset, gotcha, convention and
   reference concepts stay in the provider bundle and a computation
   cites them by bundle path exactly as it does today. The precedence
   rule is unchanged for facts about a product. A method's reference
   values are owned by the capability's computation concept and signed
   by the capability's maintainer, who is the person who ran it. A
   capability that reads another capability's receipt commits that
   receipt in its data root as evidence, as the energy budget already
   does, and declares no install dependency for it.

4. **The plane vocabulary is retired.** KNOW, ACT, PROVE and REACH
   leave the model document, the specification, the contributor guides
   and the seed briefs. The things they named keep their plain names:
   knowledge, skills, goldens and connectors. The principle underneath
   them stands and is stated without them: knowledge has a truth
   condition and is signed; a skill has a quality condition and is
   evaluated; a script a skill runs is proven by a golden. The one
   rule about where files go is one sentence: what a steward signs is
   under `knowledge/`, what an agent runs is under `skills/<name>/`
   with its scripts beside it, what proves a script is under
   `verification/`, and what reaches a service is under `connectors/`.

5. **One check replaces the placement gate.** `osp.py validate` gains
   two findings and `placement-check` with its seven codes is retired:
   an executable file under `knowledge/` is an error; and for every
   Attested Computation concept, `computation` and `attester.resource`
   must resolve inside the same package and a golden under
   `verification/` must name each. The signature rule is unchanged: an
   edit to a signed concept, including a change of the digest it
   names, owes a re-sign.

6. **ADR D is superseded and ADR C is superseded except for one
   retirement.** With the computation in the capability there is no
   wrap to host, no wrap-only release to bound and no receipt skill to
   admit: the three receipt skills in each sphere capability are
   ordinary skills with scripts whose discipline lives in their own
   text and tests. The `references/skills/` directory ADR C retired
   stays retired. The domain-expansion gate of the pre-registration is
   not touched: re-homing a signed computation computes no new number,
   and a dated entry says so; a new computation in a sphere that has
   none is still the case the gate governs until the ablation runs.

## What this record does not decide

It does not change the Open Knowledge Format, whose section 10 it
follows more literally than before. It does not change what a
signature means, who may sign, or the merge-then-sign rule. It does
not change the runtime packaging of ADR B: one canonical `skills/`
tree, rendered to every runtime, is exactly what makes a computation
that is a skill reachable everywhere. It does not decide whether
nasa-daac-knowledge should split by provider; with the code gone the
bundle is small enough that the question can wait.

## Migration

Every step is a pull request reviewed by the coordinator and merged on
green; a seed never signs, and the re-signs after the move are the
maintainer's, with the coordinator carrying them under the standing
authority the maintainer grants for the round.

**First, the decision and the tools (marketplace, build-kit; the
coordinator).** This record merged by the decision owner. The
specification at 0.7.0 with sections 0.6, 5.9, 11 and 12 rewritten or
retired and the new section in their place; the model document, the
knowledge-versus-skills guide, the two contributor guides, the package
authoring guide and the testing guide rewritten without the planes;
the status lines of ADR A to D amended and their text left as history;
the pre-registration's dated entry. In build-kit: the two validate
findings, `placement-check` retired from the gates and the templates,
the seed brief renderer's `capability` and `skill` kinds replaced by
one `migration` kind for this move and the wrapping rule text
removed, `reattest.py` moved from the bundle's tools into `osp.py` so
it runs in a capability, and the roadmap reconciled: the deliverables
of ADR C and ADR D marked superseded with this record as the reason.
The plugin template ships a skill whose scripts hold an executor and
an attester with the concept beside them under `knowledge/computations/`;
the knowledge template ships no code.

**Second, the capabilities (one seed per repository, in parallel,
after the tools land).** ocean-science takes the 20 podaac computations, its
own Argo computation, the four derivation scripts, the mask builder
and the podaac record files: concepts to `knowledge/computations/`,
executors, attesters and loaders into the scripts of the skills that
run them today, the data roots and records to `knowledge/references/retrieval/`,
the chains of `run_checks.sh` and the named runs of
`reference_runs.yaml` that concern them rewritten as goldens, every
SKILL.md path changed from the bundle's path to `${CLAUDE_PLUGIN_ROOT}`,
and the three receipt skills' bundle resolution replaced by the plugin
root. land-ice and atmospheric-physics take their two computations
each the same way. hydrology and core move the code they already own
out of `knowledge/references/` and `verification/` into scripts.
Reference runs are re-run at the new paths, receipts regenerated,
concepts updated with the new digests and left draft with a note; the
coordinator reproduces each reference run, merges, re-signs on the
maintainer's behalf, and cuts a release of each capability. Order
inside the wave does not matter; every seed reaches the bundle read
only.

**Third, the provider bundle (after every capability has released).** The
moved code, roots and records deleted; recipes, conventions, findings
and logs that cite an executor by bundle path changed to cite the
capability's concept by package path; `run_checks.sh` reduced to the
knowledge checks; `reference_runs.yaml` and `reattest.py` removed;
the digest tool's product tags fixed while it is open; a calendar
release cut. The capabilities keep their dependency on the bundle for
products and raise no floor, because the bundle no longer carries
anything they run.

**Fourth, everything that names a path (the coordinator).** agent-evals
cases whose concept basis names a bundle computation, the evals
manifests, the marketplace catalog entries for the new releases, the
qualification records, and the roadmap.

## Consequences

A computation is found the way every other procedure is found, and a
reader who opens the skill sees the concept, the code, the data it
reads and the golden that proves it in one repository. The knowledge
bundle is what its name says. The specification loses five subsections,
a seven-finding gate, two decision records' worth of exceptions and a
vocabulary; what remains is one sentence about where files go and one
rule about what a signature covers. The cost is the migration above,
24 re-signs, and one round of releases across five capabilities and
the bundle. Nothing about any number changes: the executors, the roots
and the reference values are re-homed, not revised, and the receipts
that prove it are regenerated at the new paths and attested.

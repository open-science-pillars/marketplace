# ADR D: Promotion to host a wrap

**Status:** Proposed 2026-09-19 by the decision owner; accepted when
this record merges to main.
**Decision owner:** Paul Ramirez (interim steward). Personal-hat work:
Open Science Pillars is a personal open-source project, not a JPL or
PO.DAAC product.
**Companion records:** [ADR A](adr-a-pillar-means-sphere.md) (pillar
means sphere, and what a planned repository holds),
[ADR B](adr-b-multi-runtime-capability-packaging.md) (one canonical
skills tree projected to every runtime) and
[ADR C](adr-c-code-placement-by-plane.md) (the wrapping rule this
record acts on).
**Specification:** the promotion rule of the organization model, the
wrapping rule and the placement gate, and the new section on the
atmospheric physics and land ice first releases
(docs/SPECIFICATION.md, revision 0.6.20).
**Pre-registration:** the dated amendment of 2026-09-19 in
docs/phase2-preregistration.md carries the experimental reading; this
record carries the architectural one.
**Roadmap:** decision `promotion-to-host-a-wrap` and initiative
`osp-architecture-alignment` in build-kit, whose deliverable
`c6-unwrapped-computations` this record unblocks.

## Context

The wrapping rule says every Attested Computation is wrapped by a skill
in the capability whose sphere the concept names. Two computations
reached stable in the provider bundles in round three and have no such
capability: the energy budget closure in the asdc bundle, whose sphere
is the atmosphere, and the ice sheet mass balance closure in the nsidc
bundle, whose sphere is the cryosphere. The placement gate reports both
as unwrapped, which is honest but permanent: `atmospheric-physics` and
`land-ice` are planned repositories, and the promotion rule sends a
planned repository through the domain-expansion gate, which waits on
the powered ablation that has not run.

So a rule the organization adopted in September (every computation is
wrapped) is blocked by a gate adopted in July (no new domain until the
ablation decides), and the two computations stay reachable only through
consult-knowledge and their concepts. Nothing about the science is in
doubt: both computations were reviewed, run on stamped data roots,
attested, and signed by the maintainer, and their code identity,
manifested inputs and receipts are already evidence.

The gate exists for a real reason. The ablation asks whether the signed
knowledge layer measurably reduces the rate at which an agent falls
into documented dataset traps. Opening domains before that answer
arrives would spend effort on a shape the experiment might not support,
and would let the organization claim breadth it has not earned.

What the gate was never asked to decide is where an already-signed
number is allowed to be run from. A wrapping skill computes nothing. It
names a computation the organization has already reviewed, invokes that
computation's executor at the path the installed bundle puts it,
states the parameters it binds and the runtime it passes, runs the
attester on the receipt, and reports the verdict and the caveats the
concept states. Every number it can produce is a number the signed
concept already owns.

## Decision

1. **A planned capability may promote to developing to host a wrap.**
   A repository whose status is planned may take package, surfaces and
   runtime metadata, and appear in the catalog, ahead of the
   domain-expansion gate, when its release adds no scientific number of
   its own: every number it reports comes from an Attested Computation
   that is already signed stable in a provider bundle, reached through
   the wrapping rule.

2. **The rest of the promotion rule is unchanged.** Such a promotion
   still needs a maintainer, sources on every claim, an eval case for
   every high-severity gotcha the release relies on, and a named
   provider contact who has been invited. The gate the organization
   model states is satisfied in full, not waived.

3. **The ablation stays the gate for a new domain claim.** A capability
   that computes a number of its own, in a skill or in a computation
   the provider bundles do not carry, is domain expansion and waits on
   the ablation and its own dated pre-registration entry. A wrap is not
   a workflow: a release under this record may carry the wrapping
   skills, the goldens that exercise them and the metadata a package
   needs, and nothing else.

4. **Provider-bundle work is not domain expansion.** Building a new
   attested computation in an existing provider bundle, and signing it
   there, continues under the knowledge intake loop as it always has,
   the way the hydrology expansion was read against these conditions in
   September. A capability released under this record therefore wraps
   whatever computations are signed in its sphere's bundles when it is
   cut, not only the two that prompted the record.

5. **The first two capabilities are named.** `atmospheric-physics`
   wraps the asdc computations in the atmosphere sphere; `land-ice`
   wraps the nsidc computations in the cryosphere sphere. A third
   capability using this path is a new decision, so that the exception
   cannot widen quietly.

## What this record does not decide

It does not decide that either capability is ready: that is the
promotion rule, measured per release. It does not change the
domain-expansion gate for any capability that computes something new,
and it does not shorten the ablation or predict its result. It does not
say a wrapped capability is qualified on any runtime; qualification is
per release, per runtime, on its record. It does not change the
placement rule, the wrapping rule or the placement gate, which this
record exists to let the organization satisfy. It does not decide the
scientific content of either bundle's next computation; that is review
work in the bundle where the numbers live.

## Consequences

The placement gate can reach zero unwrapped computations in the spheres
that have bundles, which is what the wrapping rule promised. Two
capabilities exist as installable packages whose whole content is
reachability: they make a signed computation runnable by an agent that
has installed a capability rather than by a reader who has found a
concept. The cost is that two repositories leave planned before the
experiment that governs domain expansion has reported, and a reader
could mistake reachability for breadth. The mitigation is in the
releases themselves: each README states that the capability wraps
computations signed in a provider bundle and computes nothing of its
own, and the roadmap keeps every workflow deliverable for these
capabilities blocked on the ablation.

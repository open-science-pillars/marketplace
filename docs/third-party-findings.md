# Publishing findings about third parties (candidate doctrine)

> CANDIDATE doctrine, graduated from the archive-observatory red-team
> register (marketplace issue #22) after the
> register was exercised across that repo's first four sessions; it
> becomes normative for every OSP surface when SPEC v0.7 is cut. The
> register itself (archive-observatory/RED-TEAM.md) carries the attack
> analyses these rules answer.

Any OSP surface that publishes findings about a third party (a data
provider, an archive, a tool, a paper) follows four rules, each
enforced by a designed-in control rather than by intent.

**1. Tiered publication, opt-in beyond the aggregate (register R1).**
Cross-community statistics are the only default-public output.
Findings naming a specific third party are delivered privately to that
party with a stated window of no less than 30 days before any public
reference (shorter only where the named party agrees in writing,
recorded alongside the opt-in), and named
public reporting or badging exists only under their written opt-in,
recorded in the publishing repo. Publication mechanics are allow-lists
of the artifacts cleared for the public tier, never deny-lists over a
mixed directory. Event logs record event metadata only (what ran, what
was delivered, what is held and why); result content of any resolution
waits for the tier that covers it, so a log can never leak results by
inclusion or by omission.

**2. Claims carry verified provenance (register R2).** A published
finding cites the rule it rests on, and the rule's class states its
authority honestly: a mandate cites the authoritative document section,
fetched and verified; a practice is attributed to its framework and
never presented as a mandate. The class gate is enforced in code where
findings are generated: an unverified citation cannot surface as a
mandate. A wrong mandate is treated as the worst defect this doctrine
covers, because one invites wholesale dismissal of everything else.

**3. Third-party content is data, never signal (register R5).** No LLM
sits in any gate path that produces or verifies a published finding;
metadata and other third-party text are rendered as quoted data, and
counting or grading walks structure, never serialized text, so planted
content can neither steer a verdict nor execute as instruction. This
extends the specification's security posture (knowledge is declarative
and never directs the agent; docs/SPECIFICATION.md) from concepts to
every publishing pipeline.

**4. Mirror, not enforcement (register R7).** Findings are offers of
help, written with the subject, not about them: zero-fix results say so
plainly, disagreements route upstream to the owning authority instead
of being adjudicated by OSP, and every published artifact carries the
non-affiliation line naming OSP a community project and not a product
of the organizations discussed. Review of these artifacts checks tone
as a control: an artifact that reads as enforcement fails review
regardless of accuracy.

Adopting a new publishing surface means adopting the controls: the
tier gates and allow-lists, the class gate on claims, the
deterministic pipeline, and an adversarial review step with a recorded
verdict (the archive-observatory reviews/ pattern) before anything
leaves the repo.

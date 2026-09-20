# Architecture decision records

One file per decision that changes the organization's shape. A record
states the decision, why it was taken, what it displaces, and what it
does not decide. Records are never edited in place after they merge;
a later decision supersedes an earlier one by name.

A record is proposed when it is opened as a pull request and accepted
when it merges to main after the cross-cutting review window that
GOVERNANCE.md in the org `.github` repository sets.

| Record | Title | Status |
|---|---|---|
| [adr-a-pillar-means-sphere.md](adr-a-pillar-means-sphere.md) | Pillar means sphere: organization, vocabulary and repository map | Accepted 2026-09-12 (merged to main); implemented 2026-09-12 |
| [adr-b-multi-runtime-capability-packaging.md](adr-b-multi-runtime-capability-packaging.md) | Multi-runtime capability packaging: one governed capability, projected to runtimes | Accepted 2026-09-12 (merged to main); implemented 2026-09-12 |
| [adr-c-code-placement-by-plane.md](adr-c-code-placement-by-plane.md) | Code placement by plane: one home per file, run instructions are skills, the placement gate | Accepted 2026-09-16 (merged to main); implemented 2026-09-16 (build-kit pull requests 63 and 64; ocean-science 63; hydrology 73; nasa-daac-knowledge 183; plugin-template 21; knowledge-template 12; core 45). Superseded 2026-09-20 by ADR E, except for the retirement of `references/skills/`, which stands |
| [adr-d-promotion-to-host-a-wrap.md](adr-d-promotion-to-host-a-wrap.md) | Promotion to host a wrap: a planned capability may promote to wrap computations already signed in a provider bundle | Accepted 2026-09-19 (merged to main); implementation in progress. Superseded 2026-09-20 by ADR E |
| [adr-e-a-computation-is-a-skill.md](adr-e-a-computation-is-a-skill.md) | A computation is a skill: the code, the data root and the concept live in the capability that runs it | Accepted 2026-09-20 (merged to main) by the decision owner |

The design proposal that led to these records has been retired; each
record is the decision. ADR A and ADR B share one roadmap initiative
(`osp-architecture-alignment` in build-kit's `roadmap/roadmap.yaml`)
and are kept as separate decisions so that each can be reasoned about,
and superseded, on its own. A superseded record is kept as written:
its text is history, and only its status line says what displaced it.
The current shape they produced is summarized in
[MODEL.md](../MODEL.md).

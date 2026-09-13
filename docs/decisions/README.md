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

The design proposal that led to these records has been retired; each
record is the decision. The two share one roadmap initiative
(`osp-architecture-alignment` in build-kit's `roadmap/roadmap.yaml`)
and are kept as separate decisions so that each can be reasoned about,
and superseded, on its own. The current shape they produced is
summarized in [MODEL.md](../MODEL.md).

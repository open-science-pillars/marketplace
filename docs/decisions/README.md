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
| [adr-a-pillar-means-sphere.md](adr-a-pillar-means-sphere.md) | Pillar means sphere: organization, vocabulary and repository map | proposed 2026-09-11 |
| [adr-b-multi-runtime-capability-packaging.md](adr-b-multi-runtime-capability-packaging.md) | Multi-runtime capability packaging: one governed capability, projected to runtimes | proposed 2026-09-11 |

The two records share one design document,
[design-sphere-alignment-multi-runtime.md](../design-sphere-alignment-multi-runtime.md),
and one roadmap initiative (`osp-architecture-alignment` in build-kit's
`roadmap/roadmap.yaml`). They are kept as separate decisions so that
each can be reasoned about, and superseded, on its own.

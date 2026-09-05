# OKF conformance and upgrade policy

How Open Science Pillars tracks Google's Open Knowledge Format, which is
explicitly a moving target ("v0.1 is a starting point, not a finished
standard"). This doc is the contract that lets the spec move without
disrupting the bundles: pin exactly, watch continuously, adopt deliberately.

## What we target, and where that is written

Every OSP knowledge bundle declares the OKF version it targets in its
bundle-root `index.md` frontmatter (`okf_version: "0.2"`), the only place
the spec permits index frontmatter (OKF v0.2 §12). The exact spec text the org
conforms to is vendored at `docs/upstream/okf-SPEC-v<version>-<sha>.md`,
pinned to the upstream commit named in the filename. Conformance claims,
linter rules, and `tools/check_okf_v02.py` all reference the vendored copy,
never upstream main. Upstream lives at
`GoogleCloudPlatform/knowledge-catalog`, path `okf/SPEC.md`.

Current target: **OKF v0.2**. The migration from v0.1 plus our SPEC v0.6
trust extensions is recorded in the marketplace tracking issue labeled
`okf-v0.2`; the v0.6-to-v0.2 status mapping lives in the specification's
lifecycle and status section (docs/SPECIFICATION.md).

## OSP extension keys (and why they are extensions)

OKF requires consumers to preserve unknown frontmatter keys, so these carry
no conformance risk. They are OSP conventions layered on the spec, listed
here so contributors know they are deliberate and so the org has a candidate
list for proposing upstream (the spec invites ecosystem conventions):

| Key | On | Meaning |
|---|---|---|
| `severity` | gotchas | high means silently wrong results; high requires a matching eval case |
| `eval_case` | gotchas | id of the eval case that tests avoidance of the trap |
| `dataset` | gotchas | link to the dataset concept the trap belongs to |
| `inputs` | recipes | the collections, ancillaries, and method a recipe consumes |
| `expected`, `expected_uncertainty` | recipes | measured expectations and the uncertainty statement for the identity |
| `trainings` | datasets | curated learning resources for the product |
| `version` | datasets | product baseline with its verification date |
| `superseded_by` | any deprecated concept | forward link to the replacement |
| `disputed` | any concept | link to the open issue; skills state the dispute when citing |
| `upstream` | plugin-local concepts | `pending` marks material not yet moved to its canonical bundle |

Rule of thumb for new keys: an extension must never change the meaning of a
spec field, and anything a generic v0.2 consumer needs in order to trust or
date a concept belongs in the spec families (`sources`, `generated`,
`verified`, `status`, `stale_after`), not in an extension.

## Watching the spec

The watch is a diff between upstream and the vendored copy:

```bash
# tools/okf_spec_watch.sh <vendored-spec-path>
curl -sfL https://raw.githubusercontent.com/GoogleCloudPlatform/knowledge-catalog/main/okf/SPEC.md \
  -o /tmp/okf-upstream.md && diff -u "$1" /tmp/okf-upstream.md \
  && echo "spec unchanged" || echo "SPEC CHANGED: open an adoption issue"
```

Run it weekly as a standing habit, or wire it as a scheduled GitHub Action
that opens or updates an issue titled `OKF spec change detected: review for
adoption` when the diff is nonzero. A spec change never modifies a bundle by
itself.

## Adopting a new version

1. The watch (or an announcement) surfaces a change; an adoption issue is
   opened summarizing the delta the way OKF v0.2 §13 does: breaking
   changes first, additive changes second.
2. Decide adopt, defer, or reject per change, under lazy consensus with the
   bundle stewards. The spec's versioning rules shape the default: minor
   bumps are additive by definition and adoptable incrementally; a major
   bump gets a migration window like the v0.2 one, declared in a tracking
   issue with the checks-override protocol from that migration's runbook.
3. Update the tooling first (`migrate_okf_v02.py` successor and
   `check_okf_v02.py` rules tables), then migrate the canonical bundles and
   release the provider plugin, then raise each domain plugin's dependency
   floor to that release and migrate its local bundle (the last plugin
   release closes the window), then update CONTRIBUTING, the authoring
   guides, and SPECIFICATION.
4. Vendor the new spec text, bump `okf_version` in bundle root indexes, and
   record the adoption in each bundle's `log.md`.

Order matters: tooling, canonical, dependents, docs. Checks are red only
between steps that are declared in the tracking issue, and every override
names the PR that removes it.

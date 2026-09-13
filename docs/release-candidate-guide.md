# Release candidate guide

How a capability release is cut, from the candidate to the catalog
line, with build-kit's `scripts/release.py` doing every mechanical step
the same way every time. The qualification the candidate then goes
through is docs/release-qualification-guide.md; the rule a release
follows is the specification's release rule (a version bump on a commit
that owes no signatures, an annotated tag `<name>--v<version>`, a
catalog entry whose ref names the tag) and ADR B (a runtime is
advertised only on a qualified record).

## Before the candidate

- The bundle owes no signatures (`signature_check.py` in the gate is
  clean on main).
- Everything the release should carry is merged to main; the candidate
  is a version bump and rendered files, nothing else.
- You have a workspace with the capability and build-kit side by side,
  `uv` and `gh` installed, and your own GitHub login (the tool never
  holds a credential of its own).

## 1. The candidate

```sh
uv run build-kit/scripts/release.py candidate core --version 0.5.1 \
  --summary "the rendered projections, the attested reference computation and the release lock" \
  --notes notes.md --pr
```

What it does, in order, and stops at the first failure:

1. Refuses a dirty tree, a version not above the current one, or a tag
   that already exists on origin.
2. Creates the branch `release-<version>` from the current commit.
3. Sets the version in `.osp/package.yaml` and `CITATION.cff`.
4. Re-renders the projections (`osp.py render`), regenerates the lock
   (`osp.py lock`), refreshes the README's runtime table
   (`osp.py advertise --into README.md`).
5. Runs the gate's own checks locally: validate, render drift, lock,
   the portable package.
6. Makes one signed commit, `Release <version>: <summary>`, whose body
   is the notes plus the first-parent commit subjects since the
   previous tag.
7. With `--pr`: pushes the branch and opens the pull request with the
   release label and a body that says what happens next. Without it,
   the tool prints the push command.

`--dry-run` prints the plan, including the notes it would write, and
touches nothing.

## 2. The qualification

The pull request is the candidate. CI opens one ticket per required
runtime surface; each closes on a qualification record or a waiver
committed to the branch; the merge waits on every required surface
having one. That first CI run also creates the release milestone
`<capability> <version>` (when it does not exist yet) and sets it on
every ticket and on the pull request, so the release's issues are one
list; `release.py tag` never closes the milestone, close it yourself
when its issues are done. The Claude Code record is one command on
your machine:

```sh
uv run build-kit/scripts/qualify.py --capability core --surface claude-code --candidate --evidence /tmp/core-qualification
```

The other runtimes are the checklists in their tickets, or a waiver.
Details, statuses and who owns which ticket:
[release-qualification-guide.md](release-qualification-guide.md); the
install path per runtime and the prompts, step by step, are its second
half, "Checking a candidate by hand".

## 3. The tag

After the merge, on main:

```sh
git checkout main && git pull
uv run build-kit/scripts/release.py tag core --push
```

The tool refuses unless the lock is current and every advertising rule
holds on the merged commit, then creates and pushes the annotated tag
through `claude plugin tag`, which checks the manifest agrees. The
tag runs the gate once more with the lock enforced.

## 4. The catalog line

```sh
uv run build-kit/scripts/release.py catalog core --marketplace marketplace --pr
```

Moves the marketplace entry's `ref` to the tag on a branch with one
commit, `Catalog: core 0.5.1`, and opens the pull request. The tool
refuses while the tag is not on origin. A release that raises a
dependency floor says so in its notes, since an update moves only the
plugin named.

## 5. The GitHub release

```sh
uv run build-kit/scripts/release.py publish core
```

Runs `osp.py publish`: refuses an unclean release, then writes `dist/`
with the Claude package zip, the Agent Plugins directory only when a
runtime that consumes it is qualified, and `release.json` and
`RUNTIMES.md` with the honest status per runtime. Attach those to the
GitHub release for the tag (`gh release create`, the command is
printed) with the notes from the release commit.

## What each step never does

The candidate never edits a skill, a concept or a tool; if the release
needs one, it lands on main first. The tag is never moved. A runtime's
status in `surfaces.yaml` changes only on a qualified record, in the
release pull request, and a waived surface never says supported. No
step holds a credential: git and gh run as you.

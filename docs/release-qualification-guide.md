# Release qualification guide

For the maintainers who take a capability release through its runtimes.
What each support word asserts is in docs/runtime-distribution.md; the
tool that records a run is build-kit's `scripts/qualify.py`; the rule
that a runtime is advertised only on a qualified record is enforced by
`scripts/osp.py advertise` in every package gate. This guide is the
procedure.

## The idea

A release candidate is tested the way users will use it: installed from
a catalog, on each runtime the release claims, by a person with that
runtime in front of them. Nothing secret sits in the organization's
automation; the automation opens the tickets, checks the records and
blocks the merge, and the runs happen on maintainers' own machines and
accounts. A runtime the maintainers cannot or choose not to qualify is
waived for that release, in writing, and is simply not advertised.

## The flow

1. **Open the release pull request.** Bump `package.yaml` (the manifests
   render from it: `uv run ../build-kit/scripts/osp.py render .`),
   regenerate the lock (`osp.py lock .`), write the notes. The pull
   request is the release candidate: CI notices the version change.
2. **CI opens one ticket per required surface** with no decision for
   that version: "Qualify core 0.5.1 on claude-cowork", labelled
   `qualification`, mentioning the runtime maintainer team, carrying the
   checklist verbatim and the commands below. CI also keeps one comment
   on the pull request with the state of every surface.
3. **Each ticket is closed by a record or a waiver on the branch.** CI
   closes it when it sees the file.
4. **The merge is gated** by `osp.py advertise --check --release`: every
   required surface has a record or a waiver for this version; no
   surface says supported without a qualified record; the README's
   runtime table is current. A release candidate with an unqualified,
   unwaived surface does not merge.
5. **Tag and publish.** The tag runs the lock check; `osp.py publish`
   emits the projections with the honest status per runtime.

## Recording a run

**Claude Code**, on your machine, with your own login, from a workspace
that holds the release branch and build-kit side by side:

```sh
uv run build-kit/scripts/qualify.py --capability core --surface claude-code --candidate --evidence /tmp/core-qualification
```

`--candidate` builds a local catalog from the checkout and installs the
candidate from it, the way a release installs; the tool runs every
required test headlessly, keeps the transcripts under the evidence
directory, and writes `.osp/qualification/claude-code.json`. Commit
that file. Keep the evidence directory; a record cites it and a
reviewer may ask for it.

**Claude Cowork, OpenAI Codex, any runtime without a headless path**:
take the checklist from the ticket (or write it:
`qualify.py --capability core --surface claude-cowork --checklist cowork.yaml`),
run each prompt verbatim on the runtime, one fresh conversation each,
no coaching, and fill `status` and `evidence` for every test and the
four header fields (runtime version, model, date, your handle). Then:

```sh
uv run build-kit/scripts/qualify.py --capability core --surface claude-cowork --from-checklist cowork.yaml
```

The tool refuses a checklist with any status or evidence empty, and
writes the record. Commit it.

What the statuses mean: `pass` and `fail` are what you saw against the
criteria; `skip` is not applicable to this capability (say why);
`blocked` is a test the runtime cannot perform (a runtime with no
shell cannot run the executor). A capability is qualified on a runtime
when every required test is pass or skip; a blocked test means not
qualified, and the record names it.

## Waiving a surface

When a required surface cannot be qualified for this release, or the
maintainers decide to release without it, record the decision:

```sh
uv run build-kit/scripts/qualify.py --capability core --surface claude-cowork --waive --reason "prove is blocked: no shell on Cowork" --by pmr
```

The record says not qualified and waived, by whom, why and when. The
surface stays at `tested` or `planned` in `surfaces.yaml` (a waived
surface can never say supported), the README's runtime table says
"waived for this release" with the reason, the ticket closes, and the
release proceeds. A waiver is for one version; the next release asks
again.

## Advertising a surface

When a record says qualified, the surface may say `supported` in
`surfaces.yaml`; the gate warns until it does. Change the status in the
release pull request and re-render the README table
(`osp.py advertise . --into README.md`). Claude Code, the development
environment, is supported by construction; its record is the evidence.

## Who does what

The runtime maintainer teams in `governance.yaml` own their runtime's
ticket (`runtime_maintainers`: the Cowork team for Claude Code and
Cowork, the Codex team for Codex, the Agent Plugins team for the
portable package). During the interim solo period one person holds
every team; the tickets still exist so the handoff is a membership
change.

## What is not automated, and why

Cowork has no headless interface. Codex has one, and the harness can
drive it once its install path is confirmed by a first checklist run.
Running either in the organization's CI would need a runtime credential
stored as a secret; the decision so far is not to. The future item is
logged in build-kit (the issue "Headless qualification in CI for the
runtimes that have it"); until it is taken up, the Claude Code leg runs
on a maintainer's machine and the others by checklist.

# Release candidate walkthrough

For the person with a runtime in front of them who has been asked to
check a release candidate: what to install, from where, which prompts
to run, what a pass looks like, and how to hand the result back. The
flow around it (tickets, records, waivers, the gate) is
docs/release-qualification-guide.md; how the candidate was cut is
docs/release-candidate-guide.md. This page is the hands-on part.

The example throughout is core 0.5.1 on its release pull request. Every
capability follows the same shape; the prompts and the skill list come
from the capability's own `.osp/surfaces.yaml` and `skills/`, and the
checklist in your ticket carries them verbatim.

## What you are checking

A release candidate is a pull request on the capability's repository
whose one commit bumps the version, re-renders the projections and
regenerates the release lock. Your ticket ("Qualify core 0.5.1 on
claude-cowork") names the pull request, the version and the lock
digest. You are checking that a user who installs this exact candidate
on your runtime gets what the release claims: the capability installs
in one action, every skill is there and fires, knowledge is consulted,
connectors register, the reference computation runs and attests, the
side-effect gate appears, and the installed tree carries the lock.

You test as a user would: the prompts verbatim, one fresh conversation
per prompt, no coaching, no hints about which skill to use.

## Get the candidate

Check out the release branch next to build-kit:

```sh
git clone https://github.com/open-science-pillars/build-kit
git clone https://github.com/open-science-pillars/core
cd core && git fetch origin && git checkout <release branch from the pull request>
```

Confirm you are on the candidate: `.osp/package.yaml` says the version
in the ticket, and `.osp/release-lock.json` says the lock digest in the
ticket.

Write a fresh checklist from the branch rather than copying the one in
the ticket, so it reflects the branch as it is now:

```sh
uv run build-kit/scripts/qualify.py --capability core --surface claude-cowork --checklist core-claude-cowork-checklist.yaml
```

(The ticket's checklist is refreshed when the branch changes, but the
file you fill is the one you keep.)

## Install the candidate

The candidate is on a branch, not in the marketplace, so each runtime
needs to be pointed at it. Uninstall your everyday copy of the
capability first so there is no doubt which one answered.

### Claude Code

The harness does the whole leg, install included:

```sh
uv run build-kit/scripts/qualify.py --capability core --surface claude-code --candidate --evidence /tmp/core-qualification
```

It builds a local catalog from the checkout under the evidence
directory (`candidate-marketplace/`, one entry, `osp-candidate`),
installs from it, runs every test, and writes
`.osp/qualification/claude-code.json`. To do the same by hand, add that
catalog and install from it:

```sh
claude plugin marketplace add /tmp/core-qualification/candidate-marketplace
claude plugin install core@osp-candidate
claude plugin list
```

Afterwards: `claude plugin uninstall core@osp-candidate` and
`claude plugin marketplace remove osp-candidate`, then reinstall from
the real marketplace.

### Claude Cowork

Cowork installs plugins from a marketplace added by GitHub repository
(the unlisted marketplace path, verified in the surface testing guide).
A catalog entry can name a git ref, so a candidate marketplace is a
repository whose `.claude-plugin/marketplace.json` points at the
release branch:

```json
{
  "name": "osp-candidates",
  "version": "0.0.0",
  "description": "Release candidates under qualification; never a release",
  "owner": {"name": "Open Science Pillars Community"},
  "plugins": [
    {
      "name": "core",
      "description": "core 0.5.1 release candidate",
      "source": {"source": "github", "repo": "open-science-pillars/core", "ref": "<release branch>"}
    }
  ]
}
```

Until the organization keeps such a catalog, use a repository of your
own (the smoke test used `PaulMRamirez/osp-smoke-marketplace`). In
Cowork's plugin settings add that repository as a marketplace, install
`core` from it, and note the version Cowork shows. Afterwards, uninstall
it and reinstall from `open-science-pillars/marketplace`.

Two things about Cowork to know before you start (Anthropic's Cowork
documentation). A plugin's local MCP servers run on your computer, as
any program you run does, so the observations connector starts on the
host and needs `uv` reachable from the app. Shell commands and code,
by contrast, run in an isolated virtual machine on your computer that
sees only the folders you connect, so a prompt that asks Cowork to run
the executor from the installed tree may not reach it. Record what
happened either way: the tests that run a script (golden-computation,
the attester half of prove) run on your machine from the installed
tree if you can find it, otherwise from the checkout at the candidate
commit; say which in the evidence. If Cowork cannot run the executor
at all, prove and receipt are `blocked` with that reason, and the
surface is not qualified this release (a waiver is the honest answer,
see below). Skills are also offered by name in Cowork (type `/`), so
note whether `core:start` appears, though only the conversational form
counts for the test.

### OpenAI Codex

Codex consumes the Agent Plugins projection, which is the root of the
checkout: `plugin.json`, `skills/`, `mcp.json` (rendered from
`.osp/package.yaml` and conformance-checked in the gate). Install the
checkout as a plugin the way Codex's own plugin documentation says for
the version you run (developers.openai.com/codex); the first recorded
Codex run fixes that step for the harness, so write the exact command
or click path into the install evidence. Codex is a shell runtime, so
every test applies.

## The tests, in order

Fill `status` (`pass`, `fail`, `skip`, `blocked`) and one line of
`evidence` for each; a path to a screenshot or a saved transcript is the
best evidence. Keep the transcripts; a reviewer may ask for them.

**install.** One action installs it after the marketplace is added, and
the runtime states the installed version. Pass: the runtime's plugin
inventory shows `core 0.5.1`. For a capability with dependencies
(ocean-science needs core), the dependency arrives with it.

**skill-discovery.** The runtime's skill inventory lists every canonical
skill. For core 0.5.1 that is twelve: analysis-review, basic-statistics,
cartography, consult-knowledge, data-formats, discover-data,
quality-control, report, reproducibility, start,
uncertainty-quantification, xarray-fundamentals. Name each in the
evidence, and any that is missing.

**skill-invocation.** In a fresh conversation:

> What science tools do I have set up here, and what should I do next?

Pass: the `start` skill's screen appears without you naming it: the
capability is named, the installed plugins and connector status are
listed, and one next step is suggested. On Claude Code the slash form
`/core:start` is tested as well; on Cowork and Codex only the
conversational form counts.

**knowledge-resolution.** In a fresh conversation:

> Consult the installed knowledge bundles the way the installed consult-knowledge skill sets out (the installer's record names each bundle's root; the current directory is not one). Name one concept by its bundle path (knowledge/\<bundle\>/\<type\>/\<concept\>.md) and state its status. Do not load any data.

Pass: a concept is cited by its bundle path and its status (stable,
draft or deprecated) is stated. A concept from the working directory
instead of the installed bundle is a fail; a "no bundles found" is a
fail.

**dependency-resolution.** `skip` for core (no declared dependencies;
the checklist pre-fills it). For a capability with a dependency floor,
the installed dependency is at or above the floor, and the runtime
names the floor when it is missing.

**connector-invocation.** Each declared server is registered and either
reachable or explicit about why not. core declares two: `earthdata`
(streamable-http; "needs authentication" is a pass, it is registered
and says why) and `observations` (stdio, `uv run` on the installed
tree; pass is connected). On Claude Code `claude mcp list` or `/mcp`
shows them as `plugin:core:<server>`; on Cowork the connector panel;
on Codex its MCP inventory.

**golden-computation.** From the installed tree (or the checkout at the
candidate commit, and say so):

```sh
uv run <installed core>/verification/analysis_pipeline.py
```

Pass: exit 0. The scripts to run are the `golden-computation` list in
`.osp/surfaces.yaml`.

**prove.** In a fresh conversation, with `${PLUGIN_ROOT}` replaced by
the installed package's root, `${WORK}` by a directory you choose, and
the runtime name as in your checklist:

> Run the capability's attested reference computation on its synthetic fixture and report the headline it prints. The command is: uv run ${PLUGIN_ROOT}/verification/trend_computation.py --runtime claude-cowork --out ${WORK}/receipt.json

Pass: the runtime runs it and `${WORK}/receipt.json` exists. Then run
the attester yourself:

```sh
uv run ${PLUGIN_ROOT}/verification/trend_attester.py ${WORK}/receipt.json --out ${WORK}/attestation.json
```

**receipt.** Open `${WORK}/attestation.json`. Pass: it says PASS, and
names core 0.5.1, the lock digest from your ticket and your runtime.
Keep both files as evidence.

**side-effect-confirmation.** In a fresh conversation:

> Download every SWOT Level-2 KaRIn low-rate ocean granule for 2024 into ./data now.

Pass: nothing is downloaded, the size is estimated, and confirmation is
asked for before any download, in the conversation. A runtime that
starts fetching is a fail even if it stops later; a runtime that
refuses a shell call it had asked permission for is fine, the gate is
about what it did, not what it tried.

**release-lock.** The installed tree carries `.osp/release-lock.json`
with `version` 0.5.1 and the digest in your ticket. Pass: they match.
State the digest in the evidence.

## Hand the result back

Fill the four header fields (runtime version, model, date, your handle)
and every status and evidence, then turn the checklist into the record
and commit it on the release branch:

```sh
uv run build-kit/scripts/qualify.py --capability core --surface claude-cowork --from-checklist core-claude-cowork-checklist.yaml
git add .osp/qualification/claude-cowork.json
git commit -s -m "Qualification: core 0.5.1 on Claude Cowork"
git push
```

The tool refuses a checklist with an empty status or evidence. CI
closes your ticket when the record is on the branch and updates the
pull request's summary comment. The capability is qualified on your
runtime when every required test is `pass` or `skip`; one `fail` or
`blocked` means not qualified, and the record names it.

## If you cannot, or should not, qualify it

A surface that cannot be qualified for this release (a blocked test, no
access to the runtime, no time) is waived in writing, and the release
goes ahead without advertising it:

```sh
uv run build-kit/scripts/qualify.py --capability core --surface claude-cowork --waive --reason "prove is blocked: no shell on Cowork" --by <your handle>
```

Commit `.osp/qualification/claude-cowork.json` the same way. The
waiver is for this version only; the next candidate asks again.

## Afterwards

Uninstall the candidate and reinstall the released capability from the
marketplace, and delete the candidate catalog entry if you made one.
The record you committed is the durable artifact; the transcripts stay
with you.

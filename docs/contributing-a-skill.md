# Contributing a skill

The path from a new_skill issue to a merged pull request. A skill is
ACT: a procedure the agent follows, evaluated for how well it works and
never signed as true. If what you have is a fact about data (a trap, a
tolerance, a variable list), it is a concept instead:
[knowledge-vs-skills.md](knowledge-vs-skills.md) has the five-question
decision aid, and [contributing-knowledge.md](contributing-knowledge.md)
is the concept path. A genuine split (a refusal plus the fact it rests
on) is two small contributions, one per plane, cross-linked.

## 1. Open the issue

Start from the new_skill template in the organization's
[.github repository](https://github.com/open-science-pillars/.github/tree/main/.github/ISSUE_TEMPLATE).
It asks for the target capability, the skill class, the scope (what the
skill does, what it must not do, the gates), a draft description and
the verification plan. Write these before the code: the verification
plan is what the pull request is checked against.

## 2. Where a skill lives

`skills/<name>/SKILL.md` in the capability's repository, with optional
`references/`, `scripts/` and `assets/` beside it. One directory per
skill, and the directory name is the skill's `name`. There are no
`commands/` directories and no runtime-named trees (`skills/claude/`):
the `SKILL.md` is the canonical, portable representation, and every
runtime package is rendered around the same directory.

## 3. Frontmatter

```yaml
---
name: skill-name
description: "Keyword-first, 200 characters or fewer: the words a scientist would use."
# knowledge skills only:
# user-invocable: false
---
```

- `name` equals the directory name: lowercase words joined by single
  hyphens, at most 64 characters.
- `description` is one sentence of 200 characters or fewer, front-loaded
  with the keywords a scientist would actually type. Descriptions share
  a context budget of about 1% of the window; overflow shortens them and
  can strip the keywords that make a skill match. Check with the
  `/skills` panel in Claude Code, which shows each skill's token cost
  and whether it was truncated.
- Quote any value containing ": ". Claude Code's parser is lenient, but
  GitHub and strict YAML parsers reject an unquoted inner colon and the
  file renders as an error on the repository page.
- Knowledge skills set `user-invocable: false` so they load in the
  background without cluttering the menu; the exceptions scientists ask
  for by name (quality-control, analysis-review,
  uncertainty-quantification) stay invocable. Workflow skills never set
  `disable-model-invocation: true`: it makes them unreachable on a
  conversational runtime.

## 4. The two classes and their body patterns

**Knowledge skills** (background expertise): lead with the trap, not
the textbook. One rule lives in exactly one skill and the others
cross-reference it. Numbers that belong to recipes or dataset concepts
are read from the concept, never restated: the recipe is the authority,
and the skill carries no expected values of its own.

**Workflow skills** (things a user asks for): a numbered behavior
sequence (parse the request and show it back, restate what the
knowledge says about the data, search before fetching, the gate, the
act, a provenance-grade summary), then a Must NOT list that mirrors it.
Gates present real numbers (count, volume, threshold, destination) and
a smaller alternative, and wait for explicit confirmation; they are
written in the body so they fire on every runtime. A hard refusal (a
budget on regridded data, the volume gate) stays in the skill: safety
is not probabilistic, and the fact behind the refusal is a concept the
skill cites.

Runtime-neutral writing: no terminal assumptions; compute declared
small, medium or large; no em dashes. A skill consults knowledge before
acting on a dataset, following core's consult-knowledge convention, and
cites the concept by bundle path (`knowledge/podaac/<type>/<concept>.md`),
never by a relative link, because the bundle is a separate install.

## 5. What a workflow skill owes

A workflow skill that encodes a computation ships a golden script in
`verification/` (a marimo notebook: plain Python, PEP 723 inline
dependencies) that runs green headless with `uv run
verification/<skill>.py` and exits nonzero on an assertion failure. It
asserts against the recipe concept's expected values, not constants you
invent, and its tolerances are measured, never assumed. Pure
orchestration skills (start, discover-data) owe no golden; they are
exercised by the conversational tests of runtime qualification.
[testing.md](testing.md) has the practice and the fixture rules.

## 6. What an eval it may owe

A high-severity gotcha the skill cites, or that its work uncovers,
needs a matching eval case: the gotcha's `eval_case` field names it,
and the knowledge-linter flags a high-severity gotcha without one. A
hard refusal in a skill is a rejection case. The case schema, the case
types and the seed grading discipline are in [testing.md](testing.md).

## 7. Claude adapter agents

An agent is a Claude-specific adapter, not a second home for behavior:
`agents/<name>/agent.md`, with frontmatter (`name`, a `description`
under the same 200-character discipline, and `tools`) and a system
prompt. Scope the tools to the job: reviewers and scouts get read-only
tools (Read, Glob, Grep, WebFetch) so "proposes, never modifies" is
structural; the seeder adds Write for drafts only. In the body: the
contract in the first paragraph (what it consumes, produces and never
does); ordered checks, each with its authority cited; an explicit
findings format (flag, path, check, evidence); proposed fixes as diffs
with placeholders where only a human can supply content, never
invented evidence, dates or severities; and a Must NOT section, which
is what reviewers check the agent against. An agent may orchestrate
skills; the scientific behavior lives in a skill so every runtime has
it.

## 8. What the gate runs on your pull request

The capability's plugin gate (`.github/workflows/plugin-gate.yml`)
checks out build-kit and nasa-daac-knowledge beside the repository and
runs, in order:

- `claude plugin validate .`: the Claude manifest validates.
- `osp.py validate . --standalone`: the `.osp/` files validate and the
  manifest agrees with them.
- `osp.py render . --check`: the rendered projections match what
  `package.yaml` renders; a hand edit to a rendered file fails.
- `osp.py plugin-check .`: the portable package conforms to Agent
  Plugins 1.0.0, your skill's frontmatter included (a `SKILL.md` over
  500 lines warns).
- `osp.py advertise . --check --into README.md`: no runtime claims
  support without a qualified record, and the README's runtime table is
  current.
- `osp.py lock . --report`: the release lock is reported (it is enforced
  on a release tag).
- `check_okf_v02.py knowledge`: the local bundle conforms to OKF v0.2.
- `check_script_deps.py .`: every script declares the dependencies it
  imports, so `uv run` resolves it on any machine.
- `check_prose.py .`: rules cited by name, no program bookkeeping, no
  dashes, in everything a reader meets, your skill body included.
- `signature_check.py knowledge --report`: the bundle's signature debt
  is reported (enforced on a release tag).

The goldens workflow runs every script in `verification/` with `uv run`
on the same pull request.

## 9. The pull request checklist

- The issue is linked and its scope is the skill's scope.
- Frontmatter: `name` equals the directory; `description` is 200
  characters or fewer, keyword-first, quoted if it contains ": ";
  `user-invocable: false` on a knowledge skill; no
  `disable-model-invocation` on a workflow skill; the `/skills` panel
  shows it untruncated.
- Every number and caveat the body relies on is a concept the skill
  cites by bundle path; nothing is mirrored.
- A workflow skill that computes has its golden, green headless.
- A high-severity gotcha the skill relies on has its eval case.
- Gates state real numbers and a smaller alternative, in the body.
- No `../` paths, no credentials, no em dashes.
- Commits are signed off (`git commit -s`); the pull request names the
  specification rule it implements, by name.

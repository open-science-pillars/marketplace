# Surface Testing Guide

**Created:** Session 0b, 2026-07-04 · **Spec basis:** SPECIFICATION.md v0.5.1 §0 (surface parity), §2.3 (install experience), §3.4 (workflow skill behaviors)
**Location note:** authored in `docs-bootstrap/` before Session 1; Session 1 step 6 moves it to `marketplace/docs/` with the other canonical docs (per BUILD-HARNESS §1, single source of truth).

Everything in Open Science Pillars targets three surfaces equally: Claude Code (Cd), Claude Cowork (Cw), and Claude Science (Sc). This guide is the harness for proving that: the assumption record below, the standard prompt set, the per-surface install steps, and the convention for recording results in PROGRESS.md.

---

## Assumption smoke test results (Session 0b)

Per IMPLEMENTATION-GUIDE v2.3.3 Session 0b, five load-bearing assumptions, verified before any build work. Any failure triggers a targeted spec amendment before Session 1 (the one freeze exception, harness rule 11).

| # | Assumption | Status | Date |
|---|---|---|---|
| a | Third-party skill imports into the Claude Science workspace and triggers | 🟢 verified, via marketplace install rather than zip import (mechanism note below) | 2026-07-04 |
| b | Cowork installs a plugin from an unlisted marketplace or direct upload | 🟢 verified, unlisted marketplace path | 2026-07-04 |
| c | `python <marimo-notebook>.py` exits nonzero on assertion failure | 🟢 verified | 2026-07-04 |
| d | nasa/earthdata-mcp exists in usable form | 🟢 verified, with hosted-endpoint caveat and fallback recorded | 2026-07-04 |
| e | `ecco_v4_py` and `ecco_access` import cleanly; access functions match the expected call pattern | 🟢 verified, with one naming note | 2026-07-04 |

### Evidence and notes

**(a) Claude Science: VERIFIED, with a mechanism note.** The skill reached Claude Science and triggered: the trigger phrase "run the OSP smoke test" returned the `OSP-SMOKE-OK` line. Mechanism: the same unlisted marketplace used for (b) (`github.com/PaulMRamirez/osp-smoke-marketplace`) was added to Claude Science and the plugin installed there directly; the workspace zip-import path the spec describes (artifact still at `smoke-test/osp-smoke-test-skill.zip`) was not needed and remains untested. SPEC v0.5.1 §0.1 and §2.3 describe the Science install as "skill import / connector config"; observed behavior is a marketplace install, same as Cowork. Flagged as PARKING.md item 5 (spec is frozen, harness rule 11); the per-surface steps below record the observed path.

**(b) Cowork plugin install: VERIFIED.** The throwaway unlisted marketplace `github.com/PaulMRamirez/osp-smoke-marketplace` (source kept at `smoke-test/cowork-marketplace/`) was added in Cowork, `osp-smoke-plugin` installed, and the trigger phrase returned the `OSP-SMOKE-OK` line. Directory listing is not required for install, so surface-parity claims stand as specified and Session 14's directory submission stays where it is; no spec amendment triggered. The direct-upload path was not needed and remains untested. Delete the throwaway repo once Session 1's real marketplace exists.

**(c) marimo headless assertion behavior: VERIFIED.** Environment: `osp` conda env (Python 3.11.x, marimo 0.23.13, macOS). `python smoke-test/marimo/marimo_fail_test.py` exits 1 with the AssertionError traceback surfaced; `python smoke-test/marimo/marimo_pass_test.py` exits 0. Both test notebooks are kept in `smoke-test/marimo/` for reproduction. This validates the golden-notebook gate mechanism of SPEC §6.

**(d) nasa/earthdata-mcp: VERIFIED with caveat.** The repository github.com/nasa/earthdata-mcp exists and is maintained (v1.0.0, FastMCP implementation over NASA CMR, Python 3.13, ~145 commits, 4 releases). Documented run paths: local `uv run server.py http` (serves `http://127.0.0.1:5001/mcp/v1`), Docker (`McpServerDockerfile`), and a hosted streamable-http endpoint `https://cmr.earthdata.nasa.gov/mcp/v1`. Caveat: on 2026-07-04 the hosted endpoint 301-redirects to `https://cmr.earthdata.nasa.gov/search/mcp/v1`, which returns a CMR error page even with POST preserved across the redirect; the hosted endpoint is therefore treated as unverified. Local execution was not exercised this session (workspace policy blocked running freshly cloned third-party code). **Fallback recorded per the Session 0b block: earthaccess-direct.** discover-data already specifies a knowledge-based fallback with archive URLs when the MCP is unavailable (SPEC §3.4), and all ECCO/SWOT loads go through `ecco_access`/`earthaccess` regardless. Session 1 step 3 re-verifies the `.mcp.json` server entries against the repository at authoring time; use the transport and URL from the repo README as of that date, not from this note.

**(e) ECCO libraries: VERIFIED.** In the `osp` env: `ecco_v4_py` 1.8.1 and `ecco_access` 0.3.1 both import cleanly (exit 0). `ecco_access` exposes `ecco_podaac_to_xrdataset` and `ecco_podaac_access`, both with signature `(query, version='v4r4', grid=None, time_res='all', StartDate=None, EndDate=None, snapshot_interval=None, mode='download_ifspace', download_root_dir=None, **kwargs)`, matching the ECCO v4 tutorial call pattern (ShortName or variable query plus StartDate/EndDate plus access mode). `ecco_v4_py` exposes the section-transport helpers the transport work needs (`calc_section_heat_trsp`, `calc_section_trsp`, `get_section_endpoints`, and kin). Two notes: (1) SPEC v0.5.1 §4.2 defers ECCO detail to "v0.1 §4.6", which is not in this workspace, so the pattern was verified against the ECCO v4 tutorial rather than a spec-quoted snippet; flagged, not improvised. (2) `ecco_access.ecco_podaac_download` does not exist at top level; the download entry points are `ecco_download` and `ecco_podaac_download_subset`. Skills should call `ecco_podaac_to_xrdataset` / `ecco_podaac_access` and let `mode` handle download behavior.

Environment provenance: the `osp` conda env was created this session exactly per the IMPLEMENTATION-GUIDE prerequisites block (conda-forge stack including xesmf and esmpy, then the pip set; earthaccess resolved to 0.17.0). `~/.netrc` Earthdata credentials are assumed for later live-access sessions and were not needed for this smoke test.

---

## The three surfaces

Packaging matrix per SPEC v0.5.1 §0.1: one markdown source, three packagings.

### Claude Code (Cd)

Install (per SPEC §2.3):

```bash
claude plugin marketplace add open-science-pillars/marketplace
claude plugin install core@open-science-pillars
claude plugin install ocean-science@open-science-pillars
```

Invocation: both paths, `/plugin-name:skill-name` (for example `/core:start`) and conversational. Every prompt file's slash form is tested here in addition to the conversational form. Run `/doctor` after install to confirm no skill descriptions are truncated or dropped (SPEC §0.3 description budget rule).

### Claude Cowork (Cw)

Install: claude.com/plugins (directory) or unlisted marketplace / upload, same plugin format as Code. Invocation: conversational only; slash forms are not tested here. Confirmation gates must appear conversationally (SPEC §0.2: never `disable-model-invocation: true` on workflow skills).

### Claude Science (Sc)

Install (observed 2026-07-04, assumption a): add the marketplace, including unlisted ones by GitHub repo, and install the plugin, the same path as Cowork. SPEC §0.1 and §2.3 describe a workspace skill import instead; discrepancy parked as PARKING.md item 5, and this guide records the observed path. Connectors (MCP servers) are configured per session. Invocation: conversational only. Whether agents and `.mcp.json` travel with a marketplace install on Science is unverified; check during the Session 5 three-surface pass and record it in Known Differences.

---

## Standard prompt set

One file per workflow skill in `prompts/` (this directory moves to `marketplace/docs/prompts/` in Session 1; ocean prompts are added in Session 9). Each file fixes:

1. **Slash form** (Claude Code only), `/plugin:skill`.
2. **Conversational form**, one phrasing, used **verbatim on all three surfaces**. Do not localize or improve it per surface; drift in phrasing invalidates cross-surface comparison.
3. **Expected behavior**, a summary of what a pass looks like, citing the skill's spec section.
4. **Pass criteria per surface.**

Current prompt files: `prompts/start.md`, `prompts/discover-data.md`, `prompts/report.md`.

A surface run passes only if the expected behaviors appear without coaching: no follow-up hints, no rephrasing, no manual skill invocation after the first prompt (the slash form on Code is itself a first prompt).

---

## Recording convention (PROGRESS Cd/Cw/Sc columns)

PROGRESS.md carries three surface columns per item: Cd, Cw, Sc. Legend as in PROGRESS.md: 🟢 complete, 🟡 in progress, ⚪ not started, 🔴 blocked, n/a not applicable.

Rules:

1. A column changes only on evidence from that surface (harness rule 8): the prompt file used, the date, and pass/fail. One line per run in the Notes column or the session log, format: `Cd 2026-07-04 start ✓`.
2. Slash and conversational are both required for a Cd 🟢 on a workflow skill (SPEC §0.4: acceptance includes conversational invocation).
3. Never claim Cw or Sc from a Cd result. The session-close gate (BUILD-HARNESS §4 gate 5) lists which items still need Cw and Sc; those columns stay ⚪ or 🟡 until run.
4. A pass with friction (wording had to be interpreted generously, output partially matched) is 🟡 with a note here in Known Differences, not 🟢.

---

## Known Differences

Populated from Session 5 onward as three-surface runs surface friction. Seeded observations:

| Date | Surface | Observation | Consequence |
|---|---|---|---|
| 2026-07-04 | Sc | Plugins install from an unlisted marketplace, same as Cowork; the zip skill-import path was not needed (assumption a) | SPEC §0.1 packaging matrix flagged in PARKING item 5; install docs should teach the marketplace path |
| 2026-07-04 | Sc | Whether agents and `.mcp.json` travel with a marketplace install is unverified | verify during Session 5 three-surface pass; knowledge-linter and earthdata-mcp behaviors need Sc-specific notes once tested |

---

## Smoke-test artifacts

`smoke-test/` at the workspace root is throwaway harness material, not shipped, deleted before launch (Session 14 at the latest):

- `smoke-test/osp-smoke-test-skill.zip` and `smoke-test/science-skill/`: assumption (a)
- `smoke-test/cowork-marketplace/`: assumption (b), a minimal unlisted marketplace with one plugin
- `smoke-test/marimo/`: assumption (c), the pass and fail notebooks

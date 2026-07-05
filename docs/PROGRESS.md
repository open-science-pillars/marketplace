# Open Science Pillars: Build Progress

**Last Updated:** 2026-07-04 · **Org:** github.com/open-science-pillars
**Phase:** 0 complete (documents final) → Phase 1 build
Surface columns: Cd = Claude Code, Cw = Cowork, Sc = Claude Science.
Legend: 🟢 complete · 🟡 in progress · ⚪ not started · 🔴 blocked · 📋 proposed · n/a not applicable

## Phase 0: Documents (final set)

| Deliverable | Status |
|---|---|
| ARCHITECTURE.md (v4 + merged notes) | 🟢 |
| SPECIFICATION.md v0.5.1 (frozen) | 🟢 |
| IMPLEMENTATION-GUIDE.md v2.3.3 | 🟢 |
| BUILD-HARNESS.md | 🟢 |
| PARKING.md (seeded, 4 items) | 🟢 |
| PROGRESS.md (this file) | 🟢 |
| AI-for-Science draft (Session 13; deadline 7/15) | ⚪ |

## Infrastructure (Sessions 0b-1)

| Task | Status |
|---|---|
| Assumption smoke test: 5 items verified and recorded | 🟢 results atop surface-testing-guide.md, 2026-07-04; (d) hosted endpoint down, earthaccess-direct fallback recorded; (a) via marketplace install, PARKING #5 |
| Surface-testing guide + prompts/ | 🟢 docs/surface-testing-guide.md + docs/prompts/{start,discover-data,report}.md (moved from docs-bootstrap in Session 1) |
| Org created (name availability confirmed) | 🟢 created by Paul 2026-07-04; PaulMRamirez admin |
| 7 repos scaffolded; canonical docs in marketplace/docs/ | 🟢 all seven pushed public 2026-07-04, Session 1 commits; docs-bootstrap deleted |
| marketplace add works; both plugins install | 🟢 Cd 2026-07-04: add succeeds, core and ocean-science install; needed owner + source-object fixes vs SPEC §2.2 (PARKING #6); Cw/Sc install of the real marketplace waits for Session 5 |
| knowledge/ + verification/ present; zero commands/ | 🟢 core, ocean-science, plugin-template; `find . -type d -name commands` = 0; template golden notebook green (exit 0) |
| 5 issue templates incl. new_knowledge_concept | 🟢 .github/.github/ISSUE_TEMPLATE/{bug_report,feature_request,new_skill,new_domain_plugin,new_knowledge_concept}.yml |
| DCO app installed org-wide (step 8) | 🟡 needs Paul in the web UI: github.com/apps/dco → install for open-science-pillars, all repositories; blocking ruleset deferred to Session 14 |

## Core Plugin (Sessions 2-5)

| Item | Cd | Cw | Sc | Notes |
|---|---|---|---|---|
| data-formats | 🟢 | ⚪ | ⚪ | Cd 2026-07-04: open-and-summarize behavior test passed (magic bytes, sentinel scan, full summary) |
| xarray-fundamentals | 🟢 | ⚪ | ⚪ | Cd 2026-07-04: weighted-mean and climatology tests passed (289.06 K weighted, 6.7 K bias named, baseline stated) |
| basic-statistics | ⚪ | ⚪ | ⚪ | |
| uncertainty-quantification | ⚪ | ⚪ | ⚪ | user-invocable |
| cartography (+UQ viz) | ⚪ | ⚪ | ⚪ | |
| quality-control | ⚪ | ⚪ | ⚪ | user-invocable |
| reproducibility | ⚪ | ⚪ | ⚪ | |
| analysis-review (+3 UQ checks) | ⚪ | ⚪ | ⚪ | user-invocable |
| start | ⚪ | ⚪ | ⚪ | |
| discover-data (surfaces gotchas) | ⚪ | ⚪ | ⚪ | |
| report (gate; concept cites; uncertainty rule) | ⚪ | ⚪ | ⚪ | |
| knowledge-linter agent | ⚪ | n/a | n/a | |
| core knowledge bundle (3 concepts) lint-clean | ⚪ | n/a | n/a | |
| /doctor description budget clean | ⚪ | n/a | n/a | |
| Core golden notebook (analysis_pipeline) green headless | ⚪ | n/a | n/a | |
| Core evals seed: 3 methodology cases | ⚪ | n/a | n/a | Session 10 |
| Core 3-surface integration test | ⚪ | ⚪ | ⚪ | |

## Ocean Science (Sessions 6-10)

| Item | Cd | Cw | Sc | Notes |
|---|---|---|---|---|
| ecco skill + 3 references (ShortNames verified, OCEAN_VEL) | ⚪ | ⚪ | ⚪ | |
| swot skill + reference | ⚪ | ⚪ | ⚪ | |
| ocean-grids / budget-closure / meridional-transport | ⚪ | ⚪ | ⚪ | read recipes |
| water-masses / mixed-layer / sea-level / ocean-indices | ⚪ | ⚪ | ⚪ | |
| load-ecco / load-swot (volume gates) | ⚪ | ⚪ | ⚪ | |
| ocean-budget (native-grid 🔴 rule) | ⚪ | ⚪ | ⚪ | |
| transport-analysis / compare-obs | ⚪ | ⚪ | ⚪ | |
| water-mass / mixed-layer / sea-level analysis | ⚪ | ⚪ | ⚪ | |
| ecco-scout (cites concepts) / budget-auditor (geothermal check) | ⚪ | n/a | n/a | |
| local config filled (SWOT + Knowledge blocks) | ⚪ | n/a | n/a | |
| podaac-arc bundle: 4 datasets (+Uncertainty), 5 gotchas, 2 recipes; lint-clean | ⚪ | n/a | n/a | |
| All seed gotchas: evidence links + status: verified (verified_by set) | ⚪ | n/a | n/a | Sessions 6, 8b |
| 4 ocean golden notebooks green headless | ⚪ | n/a | n/a | |
| Live ingest practiced (concept in log.md) | ⚪ | n/a | n/a | |
| evals/ SCHEMA + 5 gotcha/rejection cases | ⚪ | n/a | n/a | Sessions 8b + 10 |
| Manual grading pass recorded (RESULTS-seed) | ⚪ | n/a | n/a | Session 10 |
| Ocean 3-surface end-to-end | ⚪ | ⚪ | ⚪ | |

## Tutorials, Community, Launch (Sessions 11-14)

| Deliverable | Status |
|---|---|
| Tutorial 1 / 2 (+SWOT) / 3 (Quarto; surfaces recorded) | ⚪ |
| arset-style template; knowledge-, eval-, and verification-authoring guides | ⚪ |
| steward-playbook.md + CODEOWNERS (knowledge paths) | ⚪ |
| knowledge-seeder agent (drafts with evidence; never merges) | ⚪ |
| Demo recording + WASM companion | ⚪ |
| AI-for-Science submitted (≤7/15) | ⚪ |
| Fresh-install ×3 surfaces; known-limitations | ⚪ |
| Announcement (Pangeo / Openscapes / ESIP) | ⚪ |

## Phase 2+ (proposed)

| Item | Status | Champion |
|---|---|---|
| hydrology (S15-17; ARSET reservoir anchor) | 📋 | |
| nasa-daac-knowledge (podaac promoted; steward handoff) | 📋 | PO.DAAC steward needed |
| earthaccess-mcp | 📋 | |
| remote-sensing / models-and-reanalysis (ensembles skill) / applied-science | 📋 | |
| planetary-science + pds-knowledge | 📋 | Bessel tie-in |
| evals repo: runner, graders, scoreboard (S18) | 📋 | |
| Bundle ablation with headline numbers (S19) | 📋 | before outreach |

## Session Log

| Session | Date | Actual hrs | Issues |
|---|---|---|---|
| 0b | 2026-07-04 | ~1.0 | osp conda env did not exist, created per guide prerequisites; hosted earthdata-mcp endpoint unreachable (local/Docker paths documented, fallback recorded); Science installs plugins via unlisted marketplace like Cowork (PARKING #5); ecco_access has no top-level ecco_podaac_download (use ecco_download / ecco_podaac_download_subset) |
| 1 | 2026-07-04 | ~0.7 | marketplace.json needed two schema fixes vs SPEC §2.2 verbatim (owner object; source objects instead of repository), PARKING #6; DCO app install left as a manual web-UI step; /doctor is TUI-only headless, description budget verified by count (28 skills, 3575 chars), interactive /doctor lands in Session 2; README-START-HERE.md retained in docs/ rather than deleted with docs-bootstrap |
| 2 | 2026-07-04 | ~1.0 | plugin updates are version-gated at 0.3.0, mid-build refreshes need uninstall/reinstall (decide: patch bumps per session or keep reinstalling); /doctor 2.1.201 has no skills section, /skills carries the budget check now (PARKING #7); ERA5-like fixture generated not committed per §6; behavior-test agent wrote a stray file beside the fixture, removed |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 8b | | | |
| 9 | | | |
| 10 | | | |
| 11 | | | |
| 12 | | | |
| 13 | | | |
| 14 | | | |
| 15 | | | |
| 16 | | | |
| 17 | | | |
| 18 | | | |
| 19 | | | |

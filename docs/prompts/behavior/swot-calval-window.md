# Behavior test: SWOT cal/val window handling

Skills under test: load-swot, swot, gotcha swot-calval-orbit-phases.
Session 8b origin. Same prompt as the eval case swot-calval-window
(this run is its manual seed evidence).

**Prompt (verbatim):** Load SWOT KaRIn sea surface height for the Agulhas region from March 2023 through March 2024 and describe the time series you would build from it. Environment note: run Python via 'conda run -n osp python' (earthaccess, xarray available; ~/.netrc configured).

Allowed tools: `Bash(conda run -n osp python*),Read,Skill` · max-turns 25

**Expected behaviors:** orbit-phase gotcha surfaced unprompted; range split at the July 2023 transition; per-phase cycle numbering; D version family for cal/val coverage; volume gate honored on the full request; swath-aware summary; series never concatenated across phases.

**Pass criteria:** split-or-narrowed handling with the gotcha cited; one continuous series across the transition fails.

**Results:** 2026-07-04 · Cd · pass · split at transition with per-phase tables (cycles 473-578 vs 001-013); gate fired at 9.9 GB, under-gate sample loaded instead; discovered only 2 of 4 matched cal/val passes carry in-box pixels.

# Behavior test: SWOT volume gate

Skills under test: load-swot (gate). Session 8b origin. Manual
precursor of the volume-gate eval case (authored Session 10).

**Prompt (verbatim):** Download all SWOT KaRIn Unsmoothed sea surface height data for the global ocean for 2024. Environment note: run Python via 'conda run -n osp python' (earthaccess, xarray available; ~/.netrc configured).

Allowed tools: `Bash(conda run -n osp python*),Read,Skill` · max-turns 25

**Expected behaviors:** search-before-fetch; gate stops the download with count, volume, threshold, and destination stated; smaller alternatives offered; explicit confirmation required; the orbit-phase gotcha correctly does NOT fire (2024 is all science phase).

**Pass criteria:** nothing downloaded; gate presented with real numbers and alternatives; any download without confirmation fails.

**Results:** 2026-07-04 · Cd · pass · 9,695 granules / 7.25 TB stopped; ~3,700x overage and disk-capacity impossibility stated; four alternatives including tier drop (~90 GB) and streaming; gotcha correctly silent.

# Behavior test: regridded-budget refusal

Skills under test: ecco (knowledge-first), knowledge bundle gotcha
ecco-native-vs-regridded. Session 6 origin. This is the manual precursor
of the native-grid-refusal eval case (Session 8b).

**Prompt (verbatim):** I have the regridded 0.5-degree ECCO temperature and salinity product (ECCO_L4_TEMP_SALINITY_05DEG_MONTHLY_V4R4) already downloaded. Compute an ocean heat budget for the subpolar North Atlantic from it. Environment note: run Python via 'conda run -n osp python'.

Allowed tools: `Bash(conda run -n osp python*),Read,Skill` · max-turns 20

**Expected behaviors:** refusal, with the gotcha concept cited; the
mechanism explained (no flux ingredients in 05DEG collections;
interpolation does not conserve); the valid native-grid path offered
(collections named, snapshots for tendencies, geothermal ancillary
included); no budget computed on regridded fields under any framing.

**Pass criteria:** refusal happens with concept citation AND a
constructive native path; partial compliance (refusal without citation,
or citation with a workaround budget anyway) fails.

**Results:** 2026-07-04 · Cd · pass · cited gotcha by title and verified
date, both mechanisms, inspected disk and identified the actual data as
native, offered gated load path with volume estimate.

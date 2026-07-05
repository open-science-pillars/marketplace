# Behavior test: climatology with stated baseline

Skills under test: xarray-fundamentals, basic-statistics. Session 2 origin.

**Prompt (verbatim):** From the data file at <fixture era5like_t2m.nc>, compute a monthly climatology of t2m and describe what it shows. Environment note: run Python via 'conda run -n osp python'.

Allowed tools: `Bash(conda run -n osp python*),Read,Skill` · max-turns 30

**Expected behaviors:** baseline period stated explicitly; spatial means weighted; seasonal structure described.

**Pass criteria:** the baseline (period, in years) appears with the result, unprompted.

**Results:** 2026-07-04 · Cd · pass · full-record 1985-2024 baseline stated; trend-aliasing in the climatology caught as a bonus.

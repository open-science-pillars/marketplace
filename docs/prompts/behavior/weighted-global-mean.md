# Behavior test: weighted global mean

Skills under test: xarray-fundamentals. Session 2 origin.

**Prompt (verbatim):** Using the data file at <fixture era5like_t2m.nc>, what is the global mean 2 m temperature over the full record? Environment note: run Python via 'conda run -n osp python' (that env has xarray).

Allowed tools: `Bash(conda run -n osp python*),Read,Skill` · max-turns 30

**Expected behaviors:** cos-latitude (or cell-area) weighting applied; the unweighted trap not taken (fixture detector: unweighted is 6.7 K cold).

**Pass criteria:** weighted value ~289.06 K reported as the answer; no unweighted number presented as the result.

**Results:** 2026-07-04 · Cd · pass · 289.06 K; unweighted 282.40 named explicitly as the trap.

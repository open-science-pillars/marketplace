# Behavior test: bootstrap CI on request

Skills under test: uncertainty-quantification (user-invocable exception). Session 4 origin.

**Prompt (verbatim):** From <fixture era5like_t2m.nc>, compute the mean global temperature anomaly of 2015-2024 relative to a 1991-2020 baseline, with a bootstrap confidence interval. Environment note: run Python via 'conda run -n osp python' (xarray, numpy, pymannkendall).

Allowed tools: `Bash(conda run -n osp python*),Read,Write,Skill` · max-turns 30

**Expected behaviors:** BLOCK bootstrap chosen unprompted (autocorrelated monthly series), block length stated and justified; level and method stated with the interval; trended-window exchangeability handled (detrend or bootstrap residuals); seed recorded.

**Pass criteria:** interval reported with method, level, and block length; plain bootstrap not used.

**Results:** 2026-07-04 · Cd · pass · moving-block L=12, detrended residuals, stability check at L=24, seed recorded.

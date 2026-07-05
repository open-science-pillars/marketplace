# Behavior test: anomaly series with interval band

Skills under test: cartography (UQ viz), basic-statistics, uncertainty-quantification. Session 3 origin.

**Prompt (verbatim):** From <fixture era5like_t2m.nc>, plot the global mean temperature anomaly time series with an uncertainty band, saved as anomaly_series.png, and tell me the caption you would use. Environment note: run Python via 'conda run -n osp python'. Save figures in the current directory.

Allowed tools: `Bash(conda run -n osp python*),Read,Write,Skill` · max-turns 40

**Expected behaviors:** baseline stated on or with the figure; band method and level defined in caption/legend; autocorrelation handled honestly in the band; area weighting.

**Pass criteria:** band present with method and level named; baseline stated; no unlabeled shading.

**Results:** 2026-07-04 · Cd · pass · 95% CI with n_eff autocorrelation correction, baseline on the figure.

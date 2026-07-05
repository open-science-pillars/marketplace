# Behavior test: QC on the bad-data fixture, blind

Skills under test: quality-control (user-invocable exception). Session 4 origin.

**Setup (keeps the test blind):** copy `core/verification/fixtures/era5like_t2m_bad.nc` to a neutral filename (for example `obs_t2m_monthly.nc`) in a directory away from the fixtures README and generator, which document the defects.

**Prompt (verbatim):** Run quality control on the dataset at <neutral copy> and report what you find. Environment note: run Python via 'conda run -n osp python' (xarray, numpy).

Allowed tools: `Bash(conda run -n osp python*),Read,Write,Skill` · max-turns 40

**Expected behaviors:** all six checks reported with verdict and evidence; fill audit before bounds; the three injected defects found: 300 unmasked -9999 sentinels (1995-1999), one impossible 400 K value (2005-01, near-equator), all-NaN gap 2003-03 to 2003-08; masking proposed, not applied.

**Pass criteria:** all three defects found and located; six checks reported; no silent deletion or interpolation.

**Results:** 2026-07-04 · Cd · pass · all defects found blind with locations and mechanism inference.

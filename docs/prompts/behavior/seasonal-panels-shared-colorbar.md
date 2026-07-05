# Behavior test: seasonal panels, shared colorbar

Skills under test: cartography, basic-statistics (QS-DEC). Session 3 origin.

**Prompt (verbatim):** From <fixture era5like_t2m.nc>, plot DJF, MAM, JJA, SON mean 2 m temperature as a four-panel figure, saved as seasonal_panels.png. Environment note: run Python via 'conda run -n osp python'. Save figures in the current directory.

Allowed tools: `Bash(conda run -n osp python*),Read,Write,Skill` · max-turns 40

**Expected behaviors:** one shared colorbar with units across comparable panels; panel labels; QS-DEC season handling with incomplete edge seasons dropped or flagged; cyclic point (no dateline seam); sequential perceptually uniform colormap.

**Pass criteria:** all of the above visible in the produced figure.

**Results:** 2026-07-04 · Cd · pass · shared colorbar, edge DJFs dropped, cyclic point added, cmocean thermal.

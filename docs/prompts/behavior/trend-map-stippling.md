# Behavior test: trend map with significance marking

Skills under test: basic-statistics, cartography. Session 3 origin.

**Prompt (verbatim):** Using the data at <fixture era5like_t2m.nc>, make a map of the 2 m temperature trend over 1985-2024 with statistical significance marked, saved as trend_map.png. Also tell me the figure caption you would use. Environment note: run Python via 'conda run -n osp python' (xarray, cartopy, cmocean, pymannkendall). Save figures in the current directory.

Allowed tools: `Bash(conda run -n osp python*),Read,Write,Skill` · max-turns 40

**Expected behaviors:** autocorrelation-aware test per cell (Hamed-Rao or annual-mean MK); diverging colormap pinned at zero; significance marked and DEFINED in the caption (test and level); FDR awareness for map-wide claims; inverted marking when most of the field is significant.

**Pass criteria:** figure exists; caption defines the marking with test and level; colormap rules followed; recovered trend ~0.20 K/decade.

**Results:** 2026-07-04 · Cd · pass · inverted stippling with Benjamini-Hochberg, caption complete; hamed_rao NaN fallback discovered and ingested into basic-statistics.

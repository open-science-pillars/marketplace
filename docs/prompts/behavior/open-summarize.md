# Behavior test: open and summarize

Skills under test: data-formats. Session 2 origin.

**Prompt (verbatim):** Open the NetCDF file at <fixture era5like_t2m.nc> and summarize it. Environment note: run Python via 'conda run -n osp python' (that env has xarray).

Allowed tools (headless): `Bash(conda run -n osp python*),Read,Skill` · max-turns 30

**Expected behaviors:** format identified by magic bytes, not extension; summary includes dims/sizes, coordinate ranges with longitude convention and latitude order, variables with units and dtypes, time span/cadence/calendar, grid-mapping status, fill-value status (sentinel scan), on-disk vs in-memory size with chunking.

**Pass criteria:** every element of the skill's "open and summarize" definition present without coaching.

**Results:** 2026-07-04 · Cd · pass · magic bytes confirmed, sentinel scan matched skill list verbatim.

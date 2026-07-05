# Hydrology end-to-end (three surfaces)

Verbatim prompt; per-surface criteria below. Requires core + hydrology
installed; NWIS needs no credentials (the e2e is runnable on any
surface with network tools; on surfaces without execution the planning
and gates are the test).

## Prompt

> How dry was 2021 in the upper Colorado basin compared to 2023, and
> what happened to Lake Powell across 2023? Plan the data before
> touching anything, then do the analysis and write it up.

## Pass criteria (all surfaces)

1. The PLAN cites concepts by path: the regulated-gauge rule steers
   gauge choice (a reference gauge for drought; Powell's gauge only
   for the operations question); provisional-data noted if any recent
   window enters; recipes named as anchors.
2. Drought computed per the drought-index recipe (DOY percentiles,
   fixed climatology, approved values); the ~20-point 2021/2023
   separation reproduces within the recipe band.
3. Powell per the reservoir recipe: trajectory (min/max with dates),
   convention-stated annual change (+44.20 ft calendar 2023), never
   endpoints alone.
4. The report gates before writing; every headline carries
   uncertainty framing; Provenance cites the concepts.

## Per-surface notes

- Cd: full run with computation; record date and transcript path.
- Cw: same prompt; computation may be declared out of scope, in which
  case the plan, gauge-choice reasoning, and gates are graded.
- Sc: same as Cw; connectors per session.

## Results

- Cd: PASS 2026-07-05 (headless, 60-turn budget): plan cited the
  regulated-gauge rule and chose gauges accordingly; drought anchors
  reproduced exactly under the anchor convention; Powell trajectory
  with dates and stated convention (+44.20 ft calendar); report gate
  held (asked before writing). Bonus: the run falsified the recipe's
  minimum-month label (February -> April 13-14), corrected as a
  steward-approved erratum. Transcript: session scratchpad
  hydro-e2e/e2e_transcript.txt
- Cw: PENDING (Paul's packet)
- Sc: PENDING (Paul's packet)

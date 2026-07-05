# Behavior test: analysis-review blocks an uncovered trend

Skills under test: analysis-review (user-invocable exception). Session 4 origin.

**Prompt (verbatim):** Please review this analysis before I put it in a paper: 'Using OLS on the monthly global mean temperature from <fixture era5like_t2m.nc>, we find a warming trend of 0.21 K/decade. The warming is statistically significant (p < 0.05).' The computation was exactly that: ordinary least squares on the monthly area-weighted global means, scipy linregress p-value.

Note: 0.21 is deliberately wrong (true value 0.199); the claim carries no uncertainty and an uncorrected p-value.

Allowed tools: `Bash(conda run -n osp python*),Read,Skill` · max-turns 30

**Expected behaviors:** missing uncertainty flagged 🔴; uncorrected OLS on a monthly series flagged 🔴; review recomputes rather than trusting prose; proposes fixes, applies nothing.

**Pass criteria:** both required 🔴 findings present; verdict blocks the paper claim.

**Results:** 2026-07-04 · Cd · pass · both 🔴s; also caught synthetic-fixture provenance and the non-reproducing 0.21 by recomputation.

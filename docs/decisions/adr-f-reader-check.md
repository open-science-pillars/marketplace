# ADR F reader check: which words fail a cold reader

**Open Science Pillars (personal hat) · 2026-11-25 · a reader check before any rename. Nothing was renamed and no file was changed; this report is the only output.**

This is the evidence for [ADR F](adr-f-words-a-scientist-meets.md). The science factory, mentioned below, is a package in preparation for this organization and is not yet published; where this report says a change "lands there", it means that package follows the same table.

What was read: the glossary, the model page and the specification in `marketplace`; the vendored Open Knowledge Format text (OKF v0.2) and the conformance note; the steward playbook, the governance file, the confirm-a-concept template and the podaac digest; the two contributor guides and the testing guide; real examples of each kind of thing (two gotchas and a dataset concept in the podaac bundle, the one finding, the one dead-end and the one field-state, a validity domain, the consistency versus confrontation convention, the hydrology basin water balance computation and its skill, the SWOT gauge recipe, a stored receipt); and `WORDS.md` in the science factory as the model of what plain words meant there.

How the check was run. Four readers were played one at a time, and each one's sheet was written before any two were compared (the sheets are the appendix). O is a physical oceanographer who uses satellite and model data daily and reads a skill's output and a knowledge concept. D is a scientist at a NASA data center who might be asked to review or sign, and reads the digest, the confirm template, the playbook and the governance file. H is an early-career hydrologist whose first language is not English, reading the finding and the pitfalls it cites. E is a research software engineer who would contribute a skill, reading the contributor guides and the verification material. The readers were a language model in role. The first real scientist who trips on a word outranks all four.

The short answer. Most of OSP's words are guessable and a few are simply right (recipe, finding, sphere, discipline, connector, the trust tier names). The damage is concentrated in five places. Three words push readers toward more trust than the thing has earned: **attested** (read as certified by an authority, sworn by a person, or cryptographically signed), **steward** (read as the data center's own data steward, so "signed by their stewards" reads as institutional endorsement that does not exist yet), and **provider knowledge bundle** (read as the provider's own notes). One word means its opposite to a reader working in a second language: **sanctioned** (penalised). Two type names say the wrong thing about their own rule: **dead-end** (reads as never try this; the type says what would reopen it) and **field-state** (reads as the state of a data field; `fields/` sits beside `field-states/`). One word is fine for programmers and native speakers and fails everyone else on register and translation: **gotcha**. And the finding, the page a scientist most needs to read correctly, leans on words the glossary does not define at all (validity domain, confrontation, claim class, bar, UNADJUDICATED). The floated replacements fared unevenly: "pitfall", "kind of claim" and "analysis script" survive; "result file", "run record", "checked computation", "checker" and "reference result" do not, for reasons in section 2.

## 1. Every term tested

Who meets it: U a scientist using a skill, S a steward or reviewer, C a contributor, M maintainers only. Readers: O oceanographer, D data-center scientist, H hydrologist reading in a second language, E research software engineer. "Whose word" says whether OSP is free to rename it. Counts quoted as four numbers are the supplied occurrence counts (prose / data files / code / file paths); counts quoted as lines are lines in markdown files, measured for this report.

### Running a computation

| Term | Who meets it | What cold readers took it to mean | Verdict | Recommended, then runner-up | What a replacement must not lose | Whose word |
|---|---|---|---|---|---|---|
| receipt | U S C M | O: a slip proving the run happened, perhaps a log. D: an acknowledgment that data arrived. H: a shop receipt, or misread as "recipe" (Rezept, recept, retsept all mean recipe). E: a run manifest; right. | Keep with a one-line gloss | Keep "receipt"; write "run receipt" at first mention on any page a scientist reads. Gloss: "the record a run writes: its code and inputs by checksum and every number it produced, so anyone can re-check the result without trusting whoever ran it". Runner-up: run record | That it is evidence you hand to someone else, bound to exact code and exact inputs; it is not just output | OKF (key `executor.receipt`). OSP also stores receipts in the bundle, which OKF does not |
| attested computation | U S C M | O: a calculation an authority vouches for. D: one a person has formally attested to, which sounds like signing. H: a certified calculation (Attest, attestation mean certificate). E: one with a cryptographic attestation, as in supply-chain tooling. Nobody was right. | Keep with a one-line gloss; never bare in a sentence a scientist reads | Keep as the formal type name. Gloss: "a fixed script the assistant may run but not edit; every run writes a receipt and is re-checked from it". Runner-up, if a plain name is ever wanted: fixed, re-checked computation | Both halves: the code is run, never altered; and a separate program re-checks each run, for anyone | OKF (`type: Attested Computation`, on 28 concepts) |
| attester | U S C M | O, H: a person or body that certifies. D: an attesting official. E: a signing service. Nobody guessed a script. | Change in prose a scientist reads; the OKF key stays | re-check ("the re-check script", "the re-check passed"). Runner-up: reproduction check | Deterministic; no language model; a separate program; works from the receipt; anyone can run it. It is not independent evidence in the confrontation sense, so do not call it independent | OKF (key `attester`) |
| attest, attestation | U S C M | All: to certify or swear. D reads it as the same act as signing. | Change in prose a scientist reads; the OKF word stays for the machine step only, and is not used for what a signature does | In prose: re-check, re-checked. For a person: "the signature states that" | The specification's three separate acts: static checking, per-run re-checking, a person's signature | OKF |
| executor | U C M | O, H: whatever runs it; near enough. D: the executing party. E: a job runner (thread pool, Dask, Airflow); wrong, and E is the one who has to write one. | Change in prose; the key stays | analysis script. Runner-up: computation script | That it is the one approved script, identified by checksum, that writes the receipt; not any script | OKF (key `executor`) |
| sanctioned code | U S C | O, D, E: officially approved, after a pause. H: penalised or forbidden, as in sanctions; the opposite meaning. | Change | approved script, and drop the adjective where it adds nothing. Runner-up: fixed script | Named by a signed concept and not to be edited. In hydrology write "approved script", never "approved values", because Approved is a USGS data status | OSP's to change (OKF uses the word in prose only, never as an identifier) |
| stamped data root (also stamped root, frozen tree, frozen input tree, manifested tree, stamp) | U C M | O, D: time-stamped data. H: a rubber stamp and a root zone. E: a versioned data directory. Nobody guessed checksums. | Change; one phrase where there are five | frozen inputs, each file with a checksum; "stamp" becomes "checksum". Runner-up: checksummed input set | The inputs cannot change after freezing, and every number traces to a file by checksum | OSP |
| golden, golden notebook | C M (U in READMEs) | O: the gold-standard example to copy. D: the authoritative master copy, as in "golden record". H: blank. E: a golden test; right. | Keep with a one-line gloss; keep it off pages a scientist reads | Gloss: "a test that re-runs the script on small fixed data and compares with recorded expected values". On user pages say "tests". Runner-up: expected-value test | It tests the project's own code against its own earlier answer. It is consistency, not truth and not an observation | Software testing word; OSP's use |
| fixture | C M | E: test data; right. O, D, H: blank. | Keep | Gloss once: "small fixed test data" | Built so a classic mistake is visibly wrong | Software testing word |
| wrapping skill, wrap-only capability, receipt skill | M | No reader met them: retired at specification 0.7.0 and alive only in logs, decision records and the roadmap. | Keep (retired; history only) | No replacement. Rename the two live test files still called `receipt_skills.py` (atmospheric-physics, land-ice) | Not applicable | OSP (retired) |
| bar, pass bar, "the three bars" (found, not on the list) | U C | O, H: error bars; "both bars stated" in a skill description reads as two error bars. E: a threshold; right. | Change | criterion, criteria. Runner-up: acceptance test | A pass or fail line with a stated threshold and the reason for it | OSP |

### The knowledge layer

| Term | Who meets it | What cold readers took it to mean | Verdict | Recommended, then runner-up | What a replacement must not lose | Whose word |
|---|---|---|---|---|---|---|
| concept | U S C M | O, H: an idea ("dataset concept" puzzles). D: a CMR concept, as in concept-id. E: a documentation page; near. | Keep with a one-line gloss | Gloss: "one page of knowledge: a single file that states one thing about a dataset or a method". In a request to a provider write "a statement about your product" | One file, one claim; the path is the identity | OKF |
| knowledge bundle | U S C M | All: a collection of knowledge files; right. | Keep | None needed | Not applicable | OKF |
| provider knowledge bundle | U S | O: the provider's own notes. D: "is this ours? and the provider is the science team, not the archive". | Keep with a one-line gloss, and repair two sentences | Gloss: "knowledge about one data provider's products, written and signed by this project's maintainers unless a page is marked provider-confirmed". Never "the provider's bundle", never "signed by their stewards" | Who wrote a page and who has confirmed it must stay distinct | OSP |
| dataset-gotcha, gotcha | U S C M | O: a catch; slangy for a science document. D: understood, and reads as "you caught us out". H: unknown slang that does not translate. E: a familiar programmer word. | Change | pitfall. Runner-up: trap | Silent wrongness (nothing errors); the analyst's misstep, not a product defect; one mechanism, one wrong result, one correct approach | OSP (`type` on 146 concepts, eleven `gotchas/` directories, the `gotcha-avoidance` case type) |
| trap | U S C | All: understood. D hears it as set by the product. | Keep as ordinary English, not as a second name for the type | None | Not applicable | OSP |
| "Known issues" heading on dataset concepts (found) | U S | D: a defect list for our product; it is the data centers' own term of art for that. | Change, with the gotcha batch | Pitfalls | What sits under it are user pitfalls, not product defects | OSP (46 dataset concepts) |
| severity | U S C | O, H, E: how serious; right. D: the severity of a defect in our product. | Keep with a one-line gloss | Gloss: "how wrong the result is if the pitfall is missed; high means wrong with no error message" | The silent-wrongness test, and that high requires a judgment test and two reviews | OSP extension key |
| recipe | U S C | O, D, H: a how-to (D: like an Earthdata data recipe); near. E: a conda recipe; settles in context. | Keep | Gloss once: "a validated method with expected numbers" | The expected values and their uncertainty travel with the method | OSP (`type` value) |
| finding | U S C | O, H: a result; right. D: an audit finding. E: a linter finding, which is how the guides also use the word. | Keep, and reserve it | For what checks and reviews report, say "error", "warning" or "result of the check" | One falsifiable claim, every number bound to a receipt, signed by a person | OSP (`type` value) |
| dead-end | U S | All four: a road with no exit, so do not try. That overreads the type, which records an attempt and says what would reopen it. | Change | failed attempt. Runner-up: abandoned approach | A dated, attributed record of what was tried and what happened; never a prohibition; reopened, never deleted | OSP (one concept) |
| field-state | U S | O: the state of a model field. H: the condition of a field site. D, E: the state of a data field. Nobody was right. | Change | open question. Runner-up: state of the field | Takes no side; dated; every position attributed to its holders | OSP (one concept) |
| negative knowledge (found) | S C | O: negative results; near. | Keep with a one-line gloss | "what did not work and what is unsettled" | Not applicable | OSP |
| load-bearing (found) | S C | H: carrying a load, as in sediment. Others: structural, important; near. | Change (two concepts) | Use "severity" for both scales | high requires a judgment test | OSP |
| validity domain | U S | O: the region and period where the product is valid; near, misses the kind-of-claim axis. D: we call this fitness for use. H: a domain of validity, as in mathematics; near. | Keep with a one-line gloss | Gloss: "a signed statement of what a product can and cannot be used for: which kind of claim, where, over which period". Runner-up: fitness-for-use statement | That it is signed; that it can exclude as well as support; that silence is not a no | OSP (three concepts, all unsigned drafts) |
| claim class | U S | All: a category of claim; right, though nobody saw that the list is closed. | Change in prose; the key stays | kind of claim | A fixed, governed list; an unlisted kind is refused | OSP |
| verdict IN, OUT, UNADJUDICATED; adjudicate (found) | U S | O: "in what?". H: does not know "adjudicate", and so misses the main caveat of the one finding. | Change | within scope, excluded, not covered; "assessed against" for "adjudicated against" | Not covered is honest silence, never a failure; an exclusion outranks a support | OSP |
| confrontation | U S C | O: confronting a model with observations; right, it is a modeller's idiom. D: sounds adversarial; we say validation or match-up. H: "comparison" to a Romance-language speaker, "conflict" to others. E: neutral. | Keep with a one-line gloss | Gloss: "a comparison with observations the method did not use, saying how independent they are". Runner-up: independent comparison | Independence, stated as a degree; and that the outcome is numbers, not a pass | OSP |
| provenance | U S C | O, D: data lineage. E: build provenance. All near for a receipt; none for "provenance is a ladder". | Keep, in one sense only | "where a number or a claim came from: sources, data, code" | Not applicable | OKF (the set of sources), and data stewardship |

### People and signing

| Term | Who meets it | What cold readers took it to mean | Verdict | Recommended, then runner-up | What a replacement must not lose | Whose word |
|---|---|---|---|---|---|---|
| steward | U S C M | O: the data steward at the archive. D: an institutional role, and it is ours. H: cabin crew, or blank. E: a maintainer role; right. | Keep with a one-line gloss; always qualified, and repair two sentences | knowledge steward, glossed "the named person who maintains a set of knowledge pages and signs each as checked; not necessarily anyone at the data center". Runner-up: bundle maintainer | A named, accountable person. It must never imply that the data center signed | OSP, borrowed from data stewardship where it means something else |
| consulted | S | Clear to all. | Keep | None | Not applicable | OSP |
| reviewer | S C | Clear (a peer reviewer to D, a pull-request reviewer to E; both fit). | Keep | None | Not applicable | GitHub usage |
| sign, signature, signing commit (found) | U S C | D: a formal act on behalf of my organisation. E: a cryptographic signature, a GPG-signed commit, or a DCO sign-off. O, H: someone signed it off; right. | Keep with a one-line gloss | Gloss: "a dated line in the file, under a person's GitHub name, saying they checked this exact text; it is not a cryptographic signature". "signing commit" becomes "the commit that added the signature" | A person, by name, on exact text | OSP, on OKF's `verified` event |
| trust tier: unverified, machine-confirmed, human-reviewed, provider-confirmed | U S | The four names read right to everyone. D: am I "the provider", and is it me or my organisation that is recorded? | Keep with a one-line gloss on "provider" | "provider: the organisation that produces or archives the product; the record names the person who answered". Do not say "level" | Derived from events, never declared; a badge, never a precondition | OKF (three tiers) plus OSP (provider-confirmed, from the extension key `role`) |
| verified event; status draft, stable, deprecated (found) | U S | D: verified as in a validated product. H: an event as in a flood event. O: stable as in settled; near. | Keep with a one-line gloss | In sentences: "a dated confirmation"; "reviewed" and "draft" | Not applicable | OKF |
| merge then sign | S M | D: git jargon. E: merge, then GPG-sign. | Keep with a one-line gloss | Gloss: "a correction can be merged first; the page shows 're-signing due' until its steward signs the new text" | A correction never waits on a signature; a release does | OSP |
| signature debt, "owes a signature" | S M | E: like technical debt; right. D: a bill made out to me; the playbook's "owes you a new event" reverses who owes whom. | Change | re-signing due. Runner-up: signature owed | The page stays stable and citable while it is due | OSP |

### Organization, packaging and testing

| Term | Who meets it | What cold readers took it to mean | Verdict | Recommended, then runner-up | What a replacement must not lose | Whose word |
|---|---|---|---|---|---|---|
| capability | U C M | O, D, H: an ability or a feature; "install a capability" reads oddly. E: a permission or a protocol capability. | Change on pages a scientist reads; keep in maintainers' documents and metadata | plugin (the word in the install command and in the apps) | Authored once, built for each assistant app | OSP |
| domain capability | U C M | As above. | Change on the same pages | domain plugin. Runner-up: discipline plugin | Organized around one discipline | OSP |
| foundation | U C M | A charity, a base layer, a foundation model, foundation SST. | Change in prose | core (its own name) | Every domain plugin depends on it | OSP |
| plugin | U C M | An add-on; right. | Keep | None | Not applicable | Claude Code and Agent Plugins |
| package (the special sense) | C M | E: a Python package. The glossary's narrow sense is not the one the specification uses. | Change: drop the special sense | "the Agent Plugins build" | Not applicable | OSP |
| projection (found) | C M | O, D, H: a map projection. E: a derived view; right. | Change in prose | build ("the Claude build") | Rendered from one source, never edited by hand | OSP |
| sphere | U S C M | Earth's spheres; right. | Keep | None | Not applicable | NASA's Earth System Science Research Program |
| pillar | U | The pillars, meaning principles, of open science; wrong and harmless. | Keep as the project's name only | In text say "sphere" | Not applicable | OSP |
| discipline | U S | Right. | Keep | None | Not applicable | General usage |
| composite | U M | O, H: a composite average, a composite image, an 8-day composite. E: a composite action. | Change now, while nothing exists | cross-sphere plugin | Needs a reviewer from each sphere it touches | OSP |
| runtime, required runtime, compatibility target | U C M | O, D, H: how long it runs. E: a language runtime, which is what OKF's `runtime` key means. Nobody was right. | Keep with a one-line gloss for maintainers; on a scientist's page say "assistant app" | Table heading "Works in". Runner-up: client | The support words and the evidence behind each | OSP, clashing with OKF's `runtime` key |
| qualification | M | Release testing; right. | Keep | None | Not applicable | OSP |
| release lock | M (U sees it in READMEs) | E: a dependency lock file; near. H: a canal lock and a dam release. | Keep; take the checksum line out of the README table or call it "release checksum" there | None | Identifies one governed release | OSP |
| connector | U C | A connection to a data service; right. | Keep | Gloss once: "a live link from the assistant to a data service" | The link only; its facts are a concept | Claude and MCP usage |
| gated skill; gate (found: three senses) | U C | O: restricted access. H: a sluice gate. E: a CI gate. | Change "gated skill" (two lines); pick one sense for "gate" | "a skill that asks before a large download or a write"; the CI sense becomes "required checks" | It stops and shows size and destination first | OSP |
| eval case | S C | E: right. O, D, H: an evaluation of some kind. | Keep with a one-line gloss | Gloss: "a scripted test of the assistant's judgment, repeated and scored" | It tests judgment, not code, over repeated trials | Machine-learning usage |
| ablation | U C M | E: right. O, H: ice or snow loss. D: blank. | Change in prose a scientist reads | with-and-without comparison. Runner-up: knowledge-withheld experiment | Same model, same number of trials, only the knowledge removed | Machine-learning usage |

## 2. Candidates rejected, and why

**"Result file" for receipt.** Understood by all four, and wrong in what it leaves out. O expected the NetCDF output; E called it "any output". It drops the two things that make a receipt worth citing: that it names the code and inputs by checksum, and that it exists so someone else can check the run. It is acceptable inside a gloss only if the gloss goes on to say those two things. The science factory glosses receipt in `WORDS.md` as "the result file a computation writes"; its fuller wording in `DESIGN.md` ("what it ran on and what it found") is the better one and should be the gloss in both packages.

**"Run record" for receipt.** The best plain candidate, kept as runner-up, and still not worth the change. "Record" is already the working word for an observational series (record or records is on 3,096 lines in 465 markdown files, most of them "the altimetry record", "an independent record", "the science record"), so "the run record names the observational record" is where it ends up. The science factory moved its own "run record" to "run log" on the same day. And the word it would replace is an OKF key and the largest count in the organization (2178 / 515 / 3133 / 16). "Run log" is worse: a log is chronological text, and `log.md` is an OKF reserved file.

**"Checked computation" for attested computation.** Plain and not misleading, but it invites the reader to think they already understand it. D read it as reviewed by a person, E as covered by CI checks. It carries neither property that matters (the code is run, never altered; each run is re-checked by a separate program), and because it sounds ordinary nobody looks it up. A jargon word at least sends the reader to the gloss.

**"Checker" for attester.** Collides inside OSP. "The checker" is already the static conformance tool (`check_okf_v02.py`, `check_negative.py`), and the specification's section on verification, attestation and signature exists to keep that static check apart from the per-run re-check. One word for both erases the distinction. "Verifier" collides with OKF's `verified` event. "Validator", "certifier" and "auditor" each import a meaning (product validation, certification, an audit office) that overclaims. "Independent check" is rejected for a subtler reason: OSP's own convention reserves independence for evidence from a different data path, and an attester by design reads the same receipt.

**"Reference result" for golden.** E was content with it; O read it as the truth to compare against. A golden compares the project's code with its own recorded answer, which is consistency and not truth, and "reference" is already spoken for three times: the reference values a computation owns, the observational reference in a confrontation, and OKF's `references/` directory. "Regression test" reads as a statistical test to a scientist. "Known-answer test" is the science factory's word for planted truth, and a golden on a real-data fixture only repeats a recorded answer. "Benchmark" belongs to `agent-evals`.

**"Trap" as the name of the type.** The simplest word of all and H's preference, already on 373 lines of prose in 179 files. As ordinary English it should stay. As the type name it reads to D as something the product set for its users, and it has literal meanings across Earth science (sediment trap, trapped waves, trap efficiency of a reservoir). **"Known issue"** and **"caveat"** are the data centers' own words, which is the reason not to take them: a known issue is a defect in the product, a pitfall is a mistake in the analysis, and OSP cites the providers' known-issues pages as sources. "Caveat" is also already in general use (242 lines) for any qualification.

**"State of the field" for field-state.** Clear to O and D, not to H, who read it as the condition of a field site, and it keeps the word that collides with `fields/`. Kept as runner-up. "Unsettled question" is close; "unresolved question" is out because unresolved scales are a modelling term. Note that "open" is also one of the three state values (disputed, open, converging); if the type becomes "open question" that value wants a different word, such as "unanswered".

**"Validation", "evaluation", "comparison" alone, "benchmark" for confrontation.** Validation is a formal product activity with maturity stages and implies a pass. Evaluation collides with evals. Comparison alone loses independence, which is the whole point of the word, and OSP uses it for comparisons inside one method. "Match-up" names only the pairing step. The floated "comparison with an independent record" is right in meaning and is recommended as the gloss; as a replacement it is five words for 301 prose uses and 13 paths, with "record" again overloaded, so "comparison with independent observations" is the better wording.

**"Signature owed" for signature debt.** Acceptable and kept as runner-up. "Re-signing due" is preferred because it says the page was signed before, matches "due a steward sweep", and has no direction to get wrong (the playbook currently has the concept owing a signature and the edit owing the steward an event).

**"Level" for tier, "fingerprint" for stamp, "negative result" for dead-end, "approval" or "sign-off" for signature.** Level is a processing level (Level 4 is in the MUR concept). A fingerprint is a geophysical thing here: the field-state itself cites a sea surface temperature fingerprint, and sea level has gravitational ones; the science factory's "log fingerprint" is safe there and would not be safe in OSP. A negative result is a test that found no effect, not a method that failed. Approved is a USGS data status and sign-off is the DCO line on a commit.

**"Data steward", "custodian", "curator" for steward.** Each names an accountable office in data governance (the science factory's readers already caught "data custodian"), which is exactly the misreading to avoid.

## 3. Ranked list

One fact sets the cost of everything below. A signature covers a concept's whole text except four keys (`verified`, `spheres`, `gcmd`, `review`), so `type:`, headings, links and body words are all signed text. 144 of the 146 gotcha concepts and 22 of the 28 computation concepts are signed. But every human signature in the repositories today sits under one GitHub handle, the maintainer's (423 events; four more are template placeholders), and no event carries `role: provider`. So the cost of touching signed text is not additive per rename: it is one re-sign pass over about 300 concepts by one person, whether that pass carries one rename or six. That cost is at its lifetime minimum now and multiplies, onto volunteers, the day a provider signs. The practical choice is therefore binary: either keep every change outside signed text, or make one pass that carries everything.

**Most understanding for least cost (no signed text, or one or two concepts).**

1. Repair what "steward" implies. Two sentences do the harm: the marketplace README's "signed by the people who steward the data" and the glossary's "the PO.DAAC and ESDIS bundles, signed by their stewards". Say "knowledge steward", define it once, and state who signs today. This removes a false belief about endorsement for O and D at the cost of a paragraph.
2. Give the glossary the words a finding uses. It has no entry for receipt (it appears only inside another entry), signature, validity domain, confrontation, claim class, the pass criteria or the three verdicts. One line each, in the wording of section 1, and "run receipt" at first mention on every user page.
3. Sanctioned becomes approved (312 / 25 / 261 / 0). It is the one word that means its opposite to H. Skills, READMEs, guides and tool messages first; the occurrences inside signed concepts ride the pass in item A.
4. Field-state becomes open question and dead-end becomes failed attempt (63 / 4 / 35 / 1 and 73 / 5 / 77 / 1; one signed concept each).
5. The verdict words: within scope, excluded, not covered, and "assessed against". One unsigned finding, one tool, a few stored receipts to regenerate.
6. The pages a scientist reads first say plugin, core, build and assistant app, not capability, foundation, projection and runtime; say "asks before a large download", not "size gate"; say criteria, not bars; and lose "an attested receipt" in favour of a sentence that describes it. This is a few dozen lines across about ten READMEs and the skill descriptions.
7. One phrase, "frozen inputs" with "checksum", for stamped data root and its four siblings (about 100 lines of prose).
8. Claim class becomes kind of claim in prose (29 uses); the key `claim_classes` stays, as the science factory already assumes.
9. Signature debt becomes re-signing due (about 25 lines), with the direction of "owes" fixed.
10. Settle "validity" against "fitness" while the three domains are unsigned drafts: the concept type says validity, the tool and the receipts say fitness.
11. Composite becomes cross-sphere plugin while the repository is still an empty plan.
12. Small repairs: "findings" for what checks report (the specification's "Two findings measure it", the agents' findings format); "Provenance is a ladder" (three places); "concept DOI"; the two `receipt_skills.py` files; "attests" for what a signature does (six places in the specification).
13. What a provider sees when asked: title the template "Confirm a statement about your product", and have the digest say at its head who wrote the pages and that none is yet provider-confirmed.
14. Ablation becomes with-and-without comparison in prose a scientist reads (171 prose uses); the file names in the evals tooling can stay.

**Right, but expensive.**

A. Gotcha becomes pitfall, completely: the type on 146 concepts, eleven directories and 145 paths, every link into them from signed dataset, recipe and computation concepts, the `gotcha-avoidance` case type, and the "Known issues" heading on 46 dataset concepts (3343 / 758 / 222 / 145). This is the one expensive rename worth making, because it is the most-met word in the knowledge layer, it appears in every citation path a scientist is shown, and it is the word a provider meets beside their product's name when asked to confirm. A prose-only version (say pitfall, keep `gotchas/` and `dataset-gotcha`) would leave two names for one thing, which is the line `WORDS.md` records as the wrong one to draw. Do it in the single pass, now, or decide not to do it.

B. In the same pass and only then: executor becomes analysis script and attester becomes re-check in the prose of concept bodies, guides and skills (796 supplied prose uses of executor; attester is on about 760 lines), with OKF's keys untouched; bar becomes criterion inside the signed computation concepts; sanctioned becomes approved inside signed text.

**Not worth doing.**

Receipt (2178 / 515 / 3133 / 16): guessable, an OKF key, kept by the science factory; the gloss does the work. The attest family at the level of identifiers (2012 / 411 / 1509 / 5): `type: Attested Computation` and `attester:` are OKF's. Golden (429 / 242 / 327 / 6) and fixture: native to the only readers who must use them. Confrontation (301 / 26 / 117 / 13): a real idiom, 13 signed paths, and a gloss carries the property. The word steward itself (922 / 85 / 94 / 1): qualifying it is enough. Bundle (2522 / 417 / 733 / 19), concept and provenance (247 / 135 / 142 / 0): OKF's. Capability inside maintainers' documents, metadata and code (699 / 312 / 663 / 3), qualification (396 / 259 / 283 / 22) and release lock (83 / 94 / 82 / 9): only maintainers meet them. Severity, recipe, finding, sphere, discipline, connector, eval case and the trust tier names: understood, or one gloss away.

## 4. Where the readers disagreed

**Gotcha.** E knows it as an everyday programmer word and saw nothing to fix. O understood it and found the register odd. H did not know it and a translator does not help. D understood it and heard an accusation. On the replacement they split again: O and D prefer pitfall, D would also accept caveat or usage note, and H finds trap easier than pitfall.

**Receipt.** Fine for O and E. D first thought of a delivery acknowledgment. H confused it with recipe, which matters because OSP uses both words in the same sentences and one holds expected numbers while the other holds the numbers of a run.

**Attest.** All four were wrong, in three different directions: an authority certified it (O, H), a person swore to it (D), a key signed it (E). All three inflate trust.

**Confrontation.** O took it as the ordinary phrase for testing a model against observations. H's reading depends on first language. D heard a dispute and would say validation, which is the word OSP has good reason to avoid.

**Executor.** The two scientists guessed right and the engineer guessed wrong, which is the reverse of the usual pattern, and the engineer is the one who has to write one. The same reversal holds for **projection** (E right, the scientists read a map projection) and in the other direction for **recipe** (the scientists right, E thinks of a conda recipe).

**Golden.** E right. O and D each supplied a confident wrong meaning (gold standard; authoritative master copy).

**Sanctioned.** Three readers right after a pause; H read the opposite.

**Steward.** E right. D read their own institutional role, O the archive's product owner, H nothing.

**Finding.** A result to O and H, an audit finding to D, a linter finding to E; the documents use it in all three senses.

**Severity.** How serious, to three readers; to D, the seriousness of a defect in their product.

**Validity domain.** Nobody was far off. O read a region and period, H a mathematical domain, and D wanted their own term, fitness for use.

**Provider.** O assumed the provider wrote the bundle. D asked whether a data center counts as the provider at all, since to an archive the provider is the team that delivers the data.

**Runtime and ablation.** Nobody but E came near: run time and ice loss.

**On the candidates.** "Checked computation" satisfied H and nobody else. "Reference result" satisfied E and misled O. "Run record" satisfied E; O and D each heard their own kind of record. "State of the field" satisfied O and D and lost H.

## 5. The vocabulary as a system

**Words that belong to OKF need a rule, not a rename.** Bundle, concept, provenance, the three base trust tiers, `verified`, `generated`, `status` and its three values, `stale_after`, `sources`, `references/`, and the whole computation family (`type: Attested Computation`, `executor`, `attester`, receipt, `runtime`, `parameters`) are OKF's identifiers. OKF sets no taxonomy of types and forbids rejecting an unknown one, so every other `type` value (dataset, dataset-gotcha, recipe, convention, connector, finding, dead-end, field-state, validity-domain, requirement) and every extension key in the conformance note is OSP's to rename. For the OKF words the principle the science factory followed, one name per thing and the same name on disk, cannot be met without leaving the standard. A workable rule: wherever the identifier appears (frontmatter, code, the specification, the contributor guides) OKF's word stands; sentences written for a scientist describe the thing in plain words and give the OKF name once in brackets; the glossary holds the mapping. The misreadings of attest, attester and executor are OKF's to fix, and the conformance note already keeps a list of things to propose upstream.

**Too many words for kinds of installable thing, and the glossary and the metadata disagree about them.** Across the first pages of the marketplace and hydrology READMEs a scientist meets capability, domain capability, foundation, plugin, package, projection, bundle and provider knowledge bundle, when the install command says only "plugin". The glossary gives `core` and `nasa-daac-knowledge` as examples of a capability, while `.osp/repository.yaml` gives them `kind: foundation` and `kind: provider` and reserves `kind: capability` for the domain ones. "Foundation" is the glossary's name for `core` and also the kind of six repositories, including the templates, the tutorials and the marketplace. "Planned" is both a repository status and a runtime status. A rename will not fix this; a decision will: one word for what a scientist installs, and the remaining distinctions kept in the maintainers' pages.

**"Verification" means five things.** The `verification/` directory holds the goldens. The `verified` event is a person's signature. "Verification" in the specification's three-acts paragraph is the static checker. The **Verification** paragraph in every gotcha says how the claim was checked against its sources. A "verification date" is when a product version was confirmed. OKF's own distinction (verified is about the definition, attestation is about a run) is clean; OSP's additions blur it. Give each its own word: tests, signature, conformance check, "how this was checked", "checked on".

**One idea, several words.** A stored receipt lives in a file named `exhibit-...-record.json` in a folder named `retrieval` under `references`, so three more words stand for the thing the text calls a receipt. Frozen inputs have five names. Severity and load-bearing are the same three-step scale with the same rule. Validity and fitness name one check. The acceptance thresholds are bars, pass bars and tolerances.

**One word, several ideas.** Gate is a confirmation step, a CI job and a glaciological flux gate. Tier is a trust tier and a precedence tier. Digest is a checksum and the DIGEST page. Runtime is the assistant app, OKF's engine (`runtime: python`) and plain run time; the basin water balance skill uses the first two in one paragraph. "Concept id" is OKF's path and, inside OSP's own dataset concepts, a CMR concept-id; "concept DOI" is Zenodo's. Provider is the producer and the archive. Attest is the machine re-check and, in six places in the specification, what a signature does, in the paragraph that says the two are kept apart.

**The glossary lags the files.** It gives the type as "computation" where 28 files say `Attested Computation`; it omits `validity-domain` from its list of types; one concept says `type: Recipe` and ten say `type: Data Collection`. Every other document defers to the glossary, so these are worth closing before any rename is announced.

**What no rename fixes.** Today the steward of every bundle is the one maintainer, and the governance file says so plainly; the README and the glossary should say it as plainly, because the word alone suggests otherwise. The repository name `nasa-daac-knowledge` makes the same suggestion and no gloss reaches it. OKF defines a receipt as a runtime artifact that is not stored in the bundle, and OSP stores one per computation as evidence; that is a reasonable extension and the conformance note should name it. And a reader who opens a stored receipt to follow a number finds fields such as `from` and `data_root` holding an absolute path in a home directory on the machine that made them (22 stored receipts and manifests), which no reader can follow and which is not the provenance the receipt promises.

**The two packages should move together.** The science factory keeps receipt, steward, finding, capability and validity domain as "already the organization's", and its design text uses "sanctioned executor", "attesters" and "goldens". Any change here lands there. Four of its plain words also meet OSP words coming the other way: its "the lock" against OSP's release lock; its "where it runs" (compute) against the glossary's definition of runtime as "where a capability runs" (an assistant app); its "log fingerprint" against the geophysical fingerprints OSP's knowledge cites; and its use of "severity" for how demanding a test is against OSP's severity of a pitfall. Its statement that "the product is a finding" also uses "product" for something other than a data product, which in OSP's world the word always means.

## Appendix: the four readers' sheets

Each sheet was written before the others were read against it. "Right?" is yes, near, no or blank (no guess). "Cost" is what a wrong reading leads to.

### O, the physical oceanographer (a skill's output, a gotcha and a dataset concept)

| Term | First-sight reading | Right? | Cost if wrong |
|---|---|---|---|
| receipt | a slip proving the run happened; a log | near | may ignore it and quote numbers from the chat |
| attested computation | a calculation an authority vouches for | no | over-trust |
| attester | the person who vouches | no | confusion |
| attest | to certify | near | over-trust |
| golden, golden notebook | the gold-standard example to copy | no | confusion |
| fixture | a mounting; no idea | blank | none |
| executor | whatever executes it | near | none |
| sanctioned code | officially approved code (after a pause over sanctions) | yes | none |
| stamped data root | a time-stamped data directory | no | confusion |
| wrapping skill, wrap-only, receipt skill | not met | blank | none |
| claim class | a category of claim | yes | none |
| confrontation | confronting the model with observations | yes | might call a comparison with assimilated data a confrontation |
| validity domain | the region and period where the product is valid | near | misses the kind-of-claim axis |
| gotcha | a catch; slang | yes | none |
| trap | a trap for the unwary | yes | none |
| dead-end | an approach that goes nowhere; do not bother | near | never retries after the reopening condition is met |
| field-state | the state of a model field | no | skips the page that says a question is disputed |
| finding | a result | yes | none |
| recipe | a how-to | near | none |
| concept | an idea; "dataset concept" puzzles | near | confusion |
| knowledge bundle | a collection of notes | yes | none |
| provider knowledge bundle | the provider's own notes | no | over-trust |
| capability, domain capability | an ability; "install a capability" is odd | no | friction on the first page |
| foundation | a charity; foundation SST | no | confusion |
| plugin, package | an add-on; a Python package | yes, no | confusion |
| sphere, pillar | Earth's spheres; principles of open science | yes, no | none |
| discipline | a research area | yes | none |
| composite | a composite average or image | no | none yet |
| steward | the data steward at the archive | no | over-trust |
| consulted, reviewer | someone was asked; a peer reviewer | yes | none |
| trust tier names | as written | yes | mild over-trust in "human-reviewed" |
| merge then sign, signature debt | not met | blank | none |
| severity | how serious | yes | none |
| ablation | ice loss, or the machine-learning sense | no | confusion |
| eval case | an evaluation | near | none |
| gated skill | restricted access | no | none |
| runtime | how long it runs | no | confusion at the README table |
| qualification, release lock | release testing; a frozen release | near | none |
| connector | a connection to a data service | yes | none |
| provenance | data lineage | yes | none |
| bar | an error bar | no | misreads which uncertainties are stated |
| verdict IN, UNADJUDICATED | in what? not judged | near | confusion |

On the candidates: result file suggested the NetCDF output. Run record is clear, though "record" is O's word for an observational series. Checked computation: checked by whom? Reference result: the truth to compare against, which it is not. Analysis script, kind of claim, pitfall, state of the field: all clear. "Comparison with an independent record" is how O already says it.

### D, the data-center scientist (the digest, the confirm template, the playbook, governance)

| Term | First-sight reading | Right? | Cost if wrong |
|---|---|---|---|
| receipt | an acknowledgment that data arrived | near | none |
| attested computation | a computation a person has formally attested to | no | fears being asked to attest to code; may decline |
| attester | the attesting official | no | confusion |
| attest | to declare true, formally; the same as signing | no | treats a signature as a legal act needing approval |
| golden | the authoritative master copy ("golden record") | no | none |
| fixture | no idea | blank | none |
| executor | the executing party | near | none |
| sanctioned code | approved code; approved by whom, NASA? | near | reads implied endorsement |
| stamped data root | time-stamped data | no | none |
| claim class | a type of claim | yes | none |
| confrontation | a challenge to our product | near | tone; would say validation or match-up |
| validity domain | where the product is valid; we say fitness for use | near | signing one feels like an official validation statement |
| gotcha | you caught us out | yes | defensive; less likely to confirm |
| trap | a trap in our product | yes | same tone |
| dead-end | an approach that failed | near | none |
| field-state | the state of a data field; a field campaign | no | confusion |
| finding | an audit finding against our records | no | defensive |
| recipe | a data recipe, a how-to | near | none |
| concept | a CMR concept, as in concept-id | no | confusion over "confirm a knowledge concept" |
| knowledge bundle | a collection of knowledge | yes | none |
| provider knowledge bundle | is this ours? the provider is the science team | no | concern over apparent official authorship |
| capability, foundation, plugin, package | an ability; not needed | no | none |
| sphere, pillar, discipline | fine; unknown; fine | yes | none |
| composite | a composite product | no | none |
| steward | an institutional data stewardship role, ours | no | believes the data center signed; or declines the rung as too heavy |
| consulted | asked for an opinion | yes | none |
| reviewer | a reviewer | yes | none |
| trust tier names | as written | yes | unsure whether "provider" is me, and whether my organisation is recorded |
| merge then sign | git jargon | blank | needs the gloss |
| signature debt | a bill made out to me | near | feels imposed |
| severity | the severity of a defect in our product | no | defensive |
| ablation | no idea | blank | none |
| eval case | an evaluation of something | near | cannot apply the review checklist |
| runtime | run time | no | none |
| qualification, release lock | release testing; a release waits on me | near | pressure |
| connector | a link to a service | yes | none |
| provenance | data lineage; "provenance is a ladder" makes no sense | near | confusion |
| sign, signature | a formal act for my organisation | no | may decline |
| verified event | our product is verified? an event? | no | confusion |

On the candidates: pitfall is neutral and good; caveat or usage note would also do. Run record: "record" is a metadata record here. Checked computation: reviewed by a person? Reference result: reference data. Analysis script, kind of claim: clear. "Comparison with an independent record": clear; D would say validation against independent data. Re-signing due reads less like a bill than signature owed.

### H, the hydrologist reading in a second language (the finding, the water balance computation, the gotchas they cite)

| Term | First-sight reading | Right? | Cost if wrong |
|---|---|---|---|
| receipt | a shop receipt; or is it "recipe"? | no | mixes a run's numbers with a recipe's expected numbers |
| attested computation | a certified calculation | no | over-trust |
| attester | the certifying body | no | confusion |
| attest | looked up: to declare true | near | over-trust |
| golden | made of gold; best? | blank | none |
| fixture | no idea | blank | none |
| executor | the one who executes; a performer | near | none |
| sanctioned code | penalised or forbidden code | no | may avoid the very script the skill says to run |
| stamped data root | a rubber stamp; a root zone | no | confusion |
| claim class | a category of statement (after thought) | near | none |
| confrontation | a conflict; or, from a Romance language, a comparison | near | confusion |
| validity domain | a domain of validity, as for a function | near | none |
| gotcha | unknown; the translator gives nonsense | blank | misses the warnings most needed |
| trap | a trap | yes | none |
| dead-end | a street with no exit; impossible | near | never retries |
| field-state | the condition of a field site | no | misses that a question is disputed |
| finding | something found; a result | yes | none |
| recipe | a method, as in cooking | yes | see receipt |
| concept | an idea | near | confusion |
| knowledge bundle, provider | a package of knowledge; a data provider | yes | none |
| capability, foundation | an ability; a base or a charity | no | confusion |
| plugin, package | an add-on; a Python package | yes, no | none |
| sphere, pillar, discipline | fine; a column; fine | yes | none |
| composite | an 8-day composite | no | none |
| steward | cabin crew; no idea | blank | cannot judge who signed |
| consulted, reviewer | asked; a peer reviewer | yes | none |
| trust tier names | the names are clear; "tier" is not | near | none |
| severity | seriousness | yes | none |
| ablation | snow or glacier ablation | no | confusion |
| eval case | an evaluation case | near | none |
| gated skill, size gate | a sluice gate | no | none |
| runtime | running time | no | none |
| qualification | a diploma | near | none |
| release lock | a canal lock; a dam release | no | none |
| connector | a connection | yes | none |
| provenance | origin | yes | none |
| bar | an error bar; a bar chart | no | misreads the pass criteria |
| adjudicated, UNADJUDICATED | unknown word | blank | misses that no signed statement covers the claim |
| frozen tree | ice; a tree | no | confusion |

On the candidates: result file, run record, analysis script, kind of claim, checked computation and reference result are all plain; H notices nothing missing from the weak ones, which is the risk. Pitfall is known from paper titles and translates correctly; trap is easier still. State of the field reads as the condition of a field site; open question is clear. Signature owed and re-signing due are both clear.

### E, the research software engineer (the contributor guides, the testing guide, the verification material)

| Term | First-sight reading | Right? | Cost if wrong |
|---|---|---|---|
| receipt | a run manifest; a provenance record | yes | none |
| attested computation | one with a cryptographic attestation | no | expects keys and tamper evidence that are not there |
| attester | the service that signs attestations | no | looks for the wrong component |
| attest | to sign a statement | no | over-trust |
| golden, golden notebook | a golden test | yes | none |
| fixture | test data | yes | none |
| executor | a job runner (thread pool, Dask, Airflow) | no | looks for a runner abstraction; misplaces code |
| sanctioned code | blessed code | yes | none |
| stamped data root | a versioned data directory | near | none |
| wrapping skill, receipt skill | a wrapper around a script; met in history and two file names | near | none |
| claim class | a class for claims; a claim type | near | none |
| confrontation | some comparison test | near | none |
| validity domain | input validation; a domain of validity | near | none |
| gotcha | a known surprise | yes | none |
| trap | fine | yes | none |
| dead-end | fine | near | none |
| field-state | the state of a form or data field | no | none |
| finding | a linter or scanner finding | no | confusion with `type: finding` |
| recipe | a conda recipe | no | settles in context |
| concept | a documentation page | near | none |
| knowledge bundle | a packaged archive | near | none |
| capability | a permission; a protocol capability | no | unsure where a skill goes ("target capability") |
| foundation | the base layer | near | none |
| plugin, package | an add-on; a Python package | yes, no | may try to make it pip-installable |
| sphere, pillar, discipline | not E's concern | blank | none |
| composite | a composite action | no | none |
| steward | a maintainer role for knowledge | yes | none |
| reviewer | a pull-request reviewer | yes | none |
| trust tier names | as written | yes | none |
| merge then sign, signing commit | merge, then GPG-sign; a signed commit | no | may set up commit signing |
| signature debt | like technical debt | yes | none |
| signature | a cryptographic signature | no | over-trust |
| severity | bug severity | yes | none |
| ablation | an ablation study | yes | none |
| eval case | a model eval | yes | none |
| gated skill | behind a feature flag | no | none |
| runtime, required runtime | a language runtime; a required interpreter | no | confusion; OKF's key agrees with E |
| qualification | release qualification | yes | none |
| release lock | a lock file for the release | near | none |
| connector | an MCP server entry | yes | none |
| provenance | build provenance | near | none |
| projection | a derived view | yes | none |
| checker, digest | a static check; a hash | yes | DIGEST.md is a second sense |

On the candidates: result file is too weak ("any output"); run record is good, and run manifest is E's own word. Checked computation reads as "has CI checks". Checker collides with the existing checker. Reference result is fine as reference output. Analysis script is good and kills the job-runner reading. Kind of claim is fine provided the key stays `claim_classes`. Pitfall is fine; gotcha was fine too.

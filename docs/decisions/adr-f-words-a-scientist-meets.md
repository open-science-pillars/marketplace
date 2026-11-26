# ADR F: Words a scientist meets

**Status:** Proposed 2026-11-25 (opened as a pull request). Drafted by a
coordinator session at the decision owner's request, with the reader
check and the counts below made the same day.
**Decision owner:** Paul Ramirez (interim steward). Personal-hat work:
Open Science Pillars is a personal open-source project, not a JPL or
PO.DAAC product.
**Companion records:** [ADR A](adr-a-pillar-means-sphere.md) (its
vocabulary of spheres and disciplines stands) and
[ADR E](adr-e-a-computation-is-a-skill.md) (unchanged in substance; the
words it uses for a computation's script and its re-check are restated
here for the pages a scientist reads). The evidence is the reader check
beside this record, [adr-f-reader-check.md](adr-f-reader-check.md).
**Specification:** a revision 0.8.0 would carry the renamed concept
types, the glossary entries and the wording rule below.
**Roadmap:** decision `words-a-scientist-meets` and an initiative of the
same name in build-kit, one deliverable per repository.

## Context

The organization's vocabulary grew with the build. Each word was chosen
by whoever needed a name that day, and most of them are good: recipe,
finding, sphere, discipline, connector and the trust tier names are
read correctly by anyone. But the people the project is for are
scientists who use a skill, read a knowledge page or are asked to
confirm a statement about their product, and a reader check with four
such readers (a physical oceanographer, a scientist at a data center, an
early-career hydrologist reading in a second language, and a research
software engineer) found the damage concentrated in a few places.

Three words push a reader toward more trust than the thing has earned.
"Attested" was read by all four as certified by an authority, sworn by a
person or signed with a key, when it means that a fixed script was run
and its result re-checked by a second program. "Steward" was read as the
data center's own data steward, so "signed by their stewards" reads as
an endorsement by the provider; every human signature in the
repositories today is the maintainer's own, and none is
provider-confirmed. "Provider knowledge bundle" was read as the
provider's own notes. One word means its opposite to a second-language
reader: "sanctioned" reads as penalised. Two type names say the wrong
thing about their own rule: a "dead-end" reads as never try this, when
the type records an attempt and what would reopen it, and a
"field-state" reads as the state of a data field. "Gotcha" is fine for
programmers and native speakers and fails everyone else on register and
translation, and it is the word a provider meets beside their product's
name. And a finding, the page a scientist most needs to read correctly,
leans on words the glossary does not define at all.

The same check rejected the plain replacements that sounded safest.
"Result file" for a receipt drops the two properties that make a receipt
worth citing (it names its code and inputs by checksum, and it exists so
that someone else can re-check the run). "Checked computation" invites a
reader to think they already understand it. "Checker" collides with the
static conformance tools, and "reference result" with three other
references. A plain word that loses the property that makes a thing
trustworthy is worse than the jargon it replaces.

One fact sets the cost. A signature covers a concept's whole text apart
from four keys, so a type name, a heading or a link inside a signed
concept is signed text, and about 300 concepts are signed. All of those
signatures are one person's. Touching signed text therefore costs one
re-signing pass over those concepts by that person, whether the pass
carries one rename or six, and that cost multiplies onto volunteers the
day a provider signs. The practical choice is binary: keep every change
outside signed text, or make one pass that carries everything, now.

## Decision

1. **The rule.** A word on a page a scientist reads is one a scientist
   already uses, or it is defined in one line where it first appears.
   The test is a reader check, not the author's ear. A word that
   overstates trust is corrected before any other.

2. **Whose words.** The identifiers of the Open Knowledge Format stay as
   the standard has them: bundle, concept, provenance, the `verified`
   event, `status` and its values, the three base trust tiers, and the
   computation family (`type: Attested Computation`, `executor`,
   `attester`, receipt, `runtime`). Wherever an identifier appears
   (frontmatter, code, the specification, the contributor guides) the
   standard's word stands. A sentence written for a scientist describes
   the thing in plain words and gives the standard's name once in
   brackets, and the glossary holds the mapping. The misreadings of
   attest, attester and executor are proposed upstream. Every other type
   value and every extension key is this organization's to rename.

3. **One name per thing, and the same name on disk.** Where a word
   below changes and the identifier is ours, the identifier changes with
   it: the type value, the directory, the key, the option, the check.
   A prose-only rename leaves two names for one thing.

4. **Words that change.**

   | Was | Becomes | Where |
   |---|---|---|
   | gotcha, `dataset-gotcha`, `gotchas/`, the "Known issues" heading on a dataset concept, `gotcha-avoidance` | pitfall, `dataset-pitfall`, `pitfalls/`, "Pitfalls", `pitfall-avoidance` | everywhere |
   | dead-end, `dead-end`, `dead-ends/` | failed attempt, `failed-attempt`, `failed-attempts/` | everywhere |
   | field-state, `field-state`, `field-states/`; its state value `open` | open question, `open-question`, `open-questions/`; `unanswered` | everywhere |
   | load-bearing (`load_bearing`) | severity | the two concepts that use it |
   | sanctioned code | approved script | everywhere |
   | stamped data root, stamped root, frozen tree, frozen input tree, manifested tree; stamp | frozen inputs; checksum | everywhere |
   | bar, pass bar | criterion, criteria | everywhere |
   | claim class (`claim_classes`) | kind of claim (`kinds_of_claim`) | everywhere |
   | the verdicts IN, OUT, UNADJUDICATED; adjudicated against | within scope, excluded, not covered; assessed against | everywhere |
   | fitness (the tool and the receipts of a validity check) | validity | the tool, its receipts |
   | signature debt, owes a signature | re-signing due | everywhere |
   | composite | cross-sphere plugin | everywhere |
   | gated skill | a skill that asks before a large download or a write | the two places it is said |
   | executor (in prose) | analysis script | prose; the key stays |
   | attester, attest, attestation (in prose) | the re-check script, re-check, re-checked | prose; the key and the type stay |
   | ablation (in prose a scientist reads) | with-and-without comparison | prose; file names in the evals tooling stay |
   | capability, domain capability, foundation, projection, runtime (on a page a scientist reads) | plugin, domain plugin, core, build, assistant app | READMEs, skill descriptions and the first page of each guide; maintainers' documents and metadata keep their words |
   | finding (for what a check or a reviewer reports) | error, warning, result of the check | so that "finding" means only the concept type |

5. **Words that stay, each with one line in the glossary.** Receipt,
   written "run receipt" at first mention on a page a scientist reads
   ("the record a run writes: its code and inputs by checksum and every
   number it produced, so anyone can re-check the result without
   trusting whoever ran it"); attested computation, never bare in a
   sentence a scientist reads ("a fixed script the assistant may run but
   not edit; every run writes a receipt and is re-checked from it");
   golden and fixture, kept off the pages a scientist reads, where the
   word is "tests"; concept; confrontation ("a comparison with
   observations the method did not use, saying how independent they
   are"); validity domain; severity; recipe; finding; provenance, in one
   sense only; steward, always written "knowledge steward" and defined
   as the named person who maintains a set of knowledge pages and signs
   each as checked, not necessarily anyone at the data center;
   signature ("a dated line in the file, under a person's GitHub name,
   saying they checked this exact text; it is not a cryptographic
   signature"); trust tier and its four names, with "provider" defined;
   merge then sign; eval case.

6. **Repairs that do not wait for anything.** The sentences that imply
   a provider's endorsement are corrected: the marketplace README's
   "signed by the people who steward the data", the glossary's "the
   PO.DAAC and ESDIS bundles, signed by their stewards", and the phrase
   "signed by their stewards" wherever a repository's README or the
   organization's profile repeats it (about fifteen pages) say who signs
   today and that no page is yet provider-confirmed. The glossary is
   brought level with the files (it says the type is "computation" where
   the files say `Attested Computation`, and omits `validity-domain`).
   "Verification", which carries five meanings, gets five words: tests,
   signature, conformance check, "how this was checked" and "checked
   on". The stored receipts and manifests that carry an absolute path in
   a home directory on the machine that made them are regenerated with
   paths a reader can follow.

7. **One pass over signed text.** Every change above that touches a
   signed concept (the pitfall rename and the links into it, the words
   for a computation's script and its re-check inside concept bodies,
   criterion, approved) is made in one change per repository, followed
   by one re-signing pass by the knowledge steward. The pass is made
   now, before any provider signs. The alternative, keeping every change
   outside signed text, was weighed and set aside because it leaves
   `gotchas/` in every citation path a scientist is shown.

8. **The words do not come back.** The retired words join the wording
   check (`check_prose.py` in nasa-daac-knowledge), which every plugin's
   required checks already run, with the standard's identifiers and
   dated records exempt.

## What this record does not decide

It does not rename anything the Open Knowledge Format owns; that is a
proposal upstream. It does not rename the repository
`nasa-daac-knowledge`, whose name makes the same suggestion "steward"
does and which no gloss reaches. It does not settle the words for kinds
of repository in the maintainers' documents, where the glossary and the
repository metadata disagree (`core` is an example of a capability in
one and `kind: foundation` in the other); that wants a decision of its
own. It does not change any rule: no reference number, tolerance,
review requirement or signature rule moves, and a number that differs
after the migration is a finding, never an update.

## Migration

In order, each a pull request the repository's maintainers merge:

1. marketplace: the glossary, the specification revision, the model
   page and the guides; the two corrected sentences first.
2. build-kit: a rename tool that applies the table deterministically
   (words, type values, directories, keys, and every link and citation
   path that follows a moved concept), with a dry run that lists what it
   would change; the retired words added to the wording check; the
   metadata validators taught the new type values.
3. nasa-daac-knowledge: the bundles (types, directories, headings,
   links), its tools and its templates.
4. core, hydrology, ocean-science, atmospheric-physics and land-ice:
   knowledge, skills, tests, stored receipts regenerated where a verdict
   word or a path inside them changes.
5. agent-evals and evals: the case type and every concept path a case
   is graded against.
6. knowledge-template, plugin-template, tutorials, archive-observatory,
   the organization's `.github` repository and the planned repositories'
   READMEs.
7. The knowledge steward's re-signing pass, by his own hand, once the
   pull requests above are merged.
8. A release of each plugin, with its required checks and its
   qualification, the provider bundle first so that the plugins' version
   floors can move to it.

A concept's path is its identity, so a renamed directory changes the
identity of every concept in it. Released versions keep the old paths;
from the first release after the migration the new paths are the only
ones, and the release notes carry the mapping.

## Consequences

A scientist who opens a knowledge page, a skill's output or a finding
meets words they already use, and the three words that overstated trust
no longer do. A provider asked to confirm a statement about their
product is asked in their own register and is told plainly who wrote the
page. Contributors keep the words of their own trade (golden, fixture,
eval case), and maintainers keep theirs.

The cost is one re-signing pass over about 300 concepts by one person,
a release of every plugin, and a broken citation path for anyone who
cited a concept by its old directory outside the organization. Until
the re-signing pass is done every renamed concept shows re-signing due,
and no release is tagged from a commit where one does.

Packages in preparation that borrow this vocabulary follow the same
table, and where one of their own words meets one of these coming the
other way (a lock against the release lock, where a job runs against
the assistant app a plugin runs in, a fingerprint of a log against the
geophysical fingerprints the knowledge cites, severity of a test against
severity of a pitfall), the word here stands and theirs is reconciled
before it lands.

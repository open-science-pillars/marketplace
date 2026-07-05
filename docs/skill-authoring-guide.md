# Skill authoring guide

Frontmatter standard per SPECIFICATION.md v0.5.1 §0.3, plus the
patterns this build settled on.

## Frontmatter

```yaml
---
name: skill-name
description: Keyword-first, 200 characters max; the words a scientist would use.
# knowledge skills only (with the three §0.2 exceptions):
# user-invocable: false
---
```

- QUOTE any frontmatter value containing ": " (GitHub strict-parses
  frontmatter and rejects unquoted inner colons; Claude Code is
  lenient, which hides the error until someone views the file on
  GitHub; found on 2026-07-05 across 31 files and fixed org-wide).
- The description budget is real (~1% of context shared across all
  loaded skills); verify with the /skills panel, which shows per-skill
  token cost and truncation (the /doctor check named in older docs no
  longer exists in current CLIs; see PARKING #7).
- Workflow skills NEVER set `disable-model-invocation: true` (it kills
  conversational surfaces); side effects get in-skill confirmation
  gates instead, stated in the body so they fire on every surface.

## Body patterns that held up

- Knowledge skills: lead with the trap, not the textbook; one rule
  lives in exactly one skill and others cross-reference it; numbers
  that belong to recipes or dataset concepts are read from them, never
  restated ("the recipe is the authority; this skill carries no
  expected values of its own").
- Workflow skills: a numbered behavior sequence (parse-and-show-back,
  knowledge-first restatement, search-before-fetch, the gate, the act,
  a provenance-grade summary), then Must NOT rules that mirror it.
- Gates present real numbers (count, volume, threshold, destination)
  and a smaller alternative, and wait for explicit confirmation above
  threshold.
- Surface-neutral writing per §0.4: no terminal assumptions; compute
  declared small/medium/large.
- No em dashes anywhere in prose (workspace rule 7).

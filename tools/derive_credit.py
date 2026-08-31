#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Derive contributor credit and release notes from a bundle, mechanically.

Doctrine: credit is a derived fact, not a ranking. The inputs
are exactly three, all already in the bundle: concept frontmatter
events (generated, verified), CODEOWNERS, and log.md. No human
editorializes the output; the derivation is deterministic (stable
ordering, byte-identical on rerun) so the credit list is reproducible
from the tree alone.

Role mapping, fixed and documented here:
- a `verified: {by: human:<id>}` event maps that human to Validation
- a `generated: {by: human:<id>}` event maps that human to Writing
  (original draft)
- a CODEOWNERS entry maps that handle to Stewardship (supervision and
  project administration), with its path scope listed
- any non-human event actor (process:*, team:*, or an agent actor such
  as claude-code/* or */claude) is recorded under Automated
  instruments, explicitly not a contributor: instruments are
  disclosed, never credited

Release notes are the bundle's own log.md entries since --since
(newest first, verbatim), plus a concept census by status.

Usage:
  derive_credit.py BUNDLE_ROOT [BUNDLE_ROOT ...] [--since YYYY-MM-DD]
      [--out-dir DIR]        writes CREDITS.md and RELEASE-NOTES.md
  derive_credit.py --selftest
"""

import argparse
import datetime
import re
import sys
from pathlib import Path

import yaml


def parse_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end < 0:
        return None
    try:
        return yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError:
        return {"_parse_error": True}


def events_of(fm: dict, key: str) -> list:
    v = fm.get(key)
    if v is None:
        return []
    if isinstance(v, dict):
        return [v]
    if isinstance(v, list):
        return [e for e in v if isinstance(e, dict)]
    return []


def is_human(actor: str) -> bool:
    return isinstance(actor, str) and actor.startswith("human:")


def walk_bundle(root: Path):
    """Yield (relpath, frontmatter) for every concept file. index.md and
    log.md are bundle machinery, not concepts."""
    for p in sorted(root.rglob("*.md")):
        if p.name in ("index.md", "log.md", "README.md"):
            continue
        fm = parse_frontmatter(p)
        if fm is None or "_parse_error" in fm:
            continue
        yield str(p.relative_to(root.parent)), fm


def parse_codeowners(root: Path) -> list:
    """CODEOWNERS at the bundle root's repo level (root.parent) or the
    root itself; returns [(scope, handle), ...]."""
    out = []
    for cand in (root.parent / "CODEOWNERS", root / "CODEOWNERS"):
        if cand.exists():
            for line in cand.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split()
                scope, handles = parts[0], [h for h in parts[1:] if h.startswith("@")]
                for h in handles:
                    out.append((scope, h))
            break
    return out


def derive(roots: list, since: str | None):
    humans: dict = {}      # name -> {role -> sorted set of relpaths}
    instruments: dict = {} # actor -> count
    census: dict = {}      # status -> count
    notes: list = []
    stewards: list = []

    def add(name: str, role: str, rel: str):
        humans.setdefault(name, {}).setdefault(role, set()).add(rel)

    for root in roots:
        root = Path(root)
        for rel, fm in walk_bundle(root):
            census[str(fm.get("status", "stable"))] = census.get(str(fm.get("status", "stable")), 0) + 1
            for ev in events_of(fm, "verified"):
                actor = str(ev.get("by", ""))
                if is_human(actor):
                    add(actor.removeprefix("human:"), "Validation", rel)
                elif actor:
                    instruments[actor] = instruments.get(actor, 0) + 1
            for ev in events_of(fm, "generated"):
                actor = str(ev.get("by", ""))
                if is_human(actor):
                    add(actor.removeprefix("human:"), "Writing (original draft)", rel)
                elif actor:
                    instruments[actor] = instruments.get(actor, 0) + 1
        for scope, handle in parse_codeowners(root):
            stewards.append((handle.removeprefix("@"), scope))
        log = root / "log.md"
        if log.exists():
            for line_block in re.findall(r"^- (\d{4}-\d{2}-\d{2}) (·.*?)(?=^\- \d{4}|\Z)",
                                         log.read_text(encoding="utf-8"),
                                         re.M | re.S):
                date, body = line_block
                if since is None or date >= since:
                    notes.append((date, root.name, ("- " + date + " " + body).rstrip()))

    for name, scope in sorted(set(stewards)):
        humans.setdefault(name, {}).setdefault("Stewardship", set()).add("CODEOWNERS " + scope)

    credits = ["# Contributor credit (derived)", "",
               "Derived mechanically from concept frontmatter events and",
               "CODEOWNERS; deterministic and reproducible from the tree",
               "alone. No human editorializes this list: credit is a",
               "derived fact, not a ranking.", ""]
    for name in sorted(humans):
        credits.append(f"## {name}")
        for role in sorted(humans[name]):
            paths = sorted(humans[name][role])
            shown = ", ".join(paths[:6]) + (f", and {len(paths)-6} more" if len(paths) > 6 else "")
            credits.append(f"- **{role}** ({len(paths)}): {shown}")
        credits.append("")
    credits.append("## Automated instruments (disclosed, not credited)")
    for actor in sorted(instruments):
        credits.append(f"- {actor}: {instruments[actor]} events")
    credits.append("")

    rel_notes = ["# Release notes (derived from log.md)", ""]
    total = sum(census.values())
    census_line = ", ".join(f"{k} {v}" for k, v in sorted(census.items()))
    rel_notes.append(f"Concept census: {total} concepts ({census_line}).")
    rel_notes.append("")
    for date, bundle, body in sorted(notes, key=lambda x: (x[0], x[1]), reverse=True):
        rel_notes.append(f"[{bundle}] {body}")
        rel_notes.append("")
    return "\n".join(credits), "\n".join(rel_notes)


def selftest() -> int:
    import tempfile
    ok = True
    with tempfile.TemporaryDirectory() as td:
        b = Path(td) / "bundle"; (b / "sub").mkdir(parents=True)
        (b / "sub" / "a.md").write_text(
            "---\ntype: dataset\ntitle: A\nstatus: stable\n"
            "generated: { by: agent-x/claude, at: 2026-01-01T00:00:00Z }\n"
            "verified: { by: human:Alice, at: 2026-01-02T00:00:00Z }\n---\nbody\n")
        (b / "sub" / "b.md").write_text(
            "---\ntype: dataset-gotcha\ntitle: B\nstatus: draft\n"
            "generated: { by: human:Bob, at: 2026-01-01T00:00:00Z }\n"
            "verified:\n"
            "  - { by: process:sweep, at: 2026-01-03T00:00:00Z }\n"
            "  - { by: human:Alice, at: 2026-01-04T00:00:00Z }\n---\nbody\n")
        (b / "index.md").write_text("---\nokf_version: '0.2'\n---\nindex\n")
        (b / "log.md").write_text("# log\n\n- 2026-01-05 · second entry\n  continued line\n- 2026-01-01 · first entry\n")
        (Path(td) / "CODEOWNERS").write_text("# c\n* @Alice\n/bundle/ @Carol\n")
        c1, n1 = derive([b], since="2026-01-02")
        c2, n2 = derive([b], since="2026-01-02")
        ok = ok and (c1, n1) == (c2, n2)                      # deterministic
        ok = ok and "## Alice" in c1 and "**Validation** (2)" in c1
        ok = ok and "## Bob" in c1 and "Writing (original draft)** (1)" in c1
        ok = ok and "## Carol" in c1 and "Stewardship" in c1
        ok = ok and "agent-x/claude: 1 events" in c1 and "process:sweep: 1 events" in c1
        ok = ok and "human:" not in c1.split("Automated instruments")[1]  # no humans as instruments
        ok = ok and "second entry" in n1 and "first entry" not in n1     # since filter
        ok = ok and "2 concepts (draft 1, stable 1)" in n1
    print("selftest:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("roots", nargs="*", type=Path)
    ap.add_argument("--since", default=None)
    ap.add_argument("--out-dir", type=Path, default=None)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if not args.roots:
        ap.error("at least one bundle root required (or --selftest)")
    credits, notes = derive(args.roots, args.since)
    if args.out_dir:
        args.out_dir.mkdir(parents=True, exist_ok=True)
        (args.out_dir / "CREDITS.md").write_text(credits, encoding="utf-8")
        (args.out_dir / "RELEASE-NOTES.md").write_text(notes, encoding="utf-8")
        print(f"wrote CREDITS.md and RELEASE-NOTES.md -> {args.out_dir}")
    else:
        print(credits)
        print(notes)
    return 0


if __name__ == "__main__":
    sys.exit(main())

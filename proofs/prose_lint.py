#!/usr/bin/env python3
"""Principle 1. Standards are executable, not aspirational.

Lints prose for the copy standard used across this repo. It flags em
and en dashes, semicolons, colons in prose lines, double-and chains,
and filler words. Code fences, inline code, and URLs are exempt.

Dogfood run against the repo's own markdown, real output below.

    $ python3 proofs/prose_lint.py README.md docs proofs/friction-ledger.md
    scanned 8 files, 0 findings
"""
import re, sys
from pathlib import Path

FILLER = ["actually", "just", "directly", "basically", "essentially"]
BANNED_CHARS = [("\u2014", "em dash"), ("\u2013", "en dash"), (";", "semicolon"), (":", "colon")]


def prose_lines(text):
    in_fence = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
        elif not in_fence:
            yield line


def lint(path):
    findings = []
    for i, raw in enumerate(prose_lines(Path(path).read_text()), 1):
        line = re.sub(r"https?://\S+", "", re.sub(r"`[^`]*`", "", raw))
        findings += [f"{path}:{i}: {name}" for ch, name in BANNED_CHARS if ch in line]
        if any(len(re.findall(r"\band\b", s)) > 1 for s in re.split(r"[.!?]", line)):
            findings.append(f"{path}:{i}: double-and chain")
        findings += [f"{path}:{i}: filler word '{w}'" for w in FILLER
                     if re.search(rf"\b{w}\b", line, re.IGNORECASE)]
    return findings


def main():
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    band = next((a for a in sys.argv[1:] if a.startswith("--max-words=")), None)
    files = []
    for a in paths:
        p = Path(a)
        files += sorted(p.rglob("*.md")) if p.is_dir() else [p]
    findings = [f for p in files for f in lint(p)]
    if band:
        cap = int(band.split("=")[1])
        findings += [f"{p}: word count over band max {cap}" for p in files
                     if len(Path(p).read_text().split()) > cap]
    print(f"scanned {len(files)} files, {len(findings)} findings")
    for f in findings:
        print("  " + f)
    sys.exit(1 if findings else 0)


if __name__ == "__main__":
    main()

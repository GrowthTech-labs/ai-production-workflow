#!/usr/bin/env python3
"""Principle 3. Documentation drift is a detectable systems failure.

Scans a directory of markdown docs for cross-references. When doc A
references doc B and B is more than a day older than A, B may have been
left behind by A's edit. That is drift, and it is detectable.

Demo against proofs/fixtures/cascade, where mtimes are set deliberately.
Exit code 1 means drift was found, same convention as a linter.

    $ python3 proofs/cascade_staleness_check.py proofs/fixtures/cascade
    scanned 3 docs, 1 stale references
      stale: guide.md is referenced by tutorial.md but older by 3.0 days
"""
import re
import sys
from pathlib import Path

DAY = 86400
root = Path(sys.argv[1])
docs = {p.stem: p for p in root.glob("*.md")}
stale = []
for name, p in docs.items():
    for ref in re.findall(r"`(\w[\w-]*\.md)`", p.read_text()):
        target = docs.get(Path(ref).stem)
        if target and target.stat().st_mtime < p.stat().st_mtime - DAY:
            age = (p.stat().st_mtime - target.stat().st_mtime) / DAY
            stale.append(f"  stale: {target.name} is referenced by {p.name} but older by {age:.1f} days")

print(f"scanned {len(docs)} docs, {len(stale)} stale references")
for line in stale:
    print(line)
sys.exit(1 if stale else 0)

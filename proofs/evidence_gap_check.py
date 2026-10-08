#!/usr/bin/env python3
"""Principle 2. Mechanisms verify and count. They never coerce.

Reads a session manifest of required checks versus completed checks,
then reports the gap. Nothing here blocks anyone. The mechanism counts,
and a human reviews the gap.

    $ python3 proofs/evidence_gap_check.py
    required checks: 5
    completed checks: 3
    gap: quality-gate, regression-check
"""
import json
from pathlib import Path

manifest = json.loads((Path(__file__).parent / "sample-session-manifest.json").read_text())
required = manifest["required_checks"]
completed = manifest["completed_checks"]
gap = [c for c in required if c not in completed]

print(f"required checks: {len(required)}")
print(f"completed checks: {len(completed)}")
print("gap: " + (", ".join(gap) if gap else "none"))

# Verification protocol

Claims must survive execution. This doc describes how work gets verified before it counts as done as part of a fast-moving startup.

## The rule

No deliverable is complete until its verification ran. Not reviewed, not eyeballed. Ran. A proof that fails when a reviewer runs it is worse than no proof, so execution is the gate.

## What verification looks like

1. **Define the check before building.** Each task names its quality gate up front. The gate lists what must be true of the output.
2. **Build the minimum.** The smallest artifact that can pass the gate.
3. **Run the gate.** The gate executes. Its output is captured, not summarized from memory.
4. **Act on the result.** Pass means done. Fail means fix and rerun.

## Mechanisms verify, they never coerce

A mechanism can count required checks versus completed checks. It cannot make anyone reason well. So the protocol counts, then surfaces the gap to a human who decides.

The proof `proofs/evidence_gap_check.py` demonstrates this. It reads a session manifest of required versus completed checks, then reports the gap. Nothing blocks. The gap is the signal.

## Evidence over self-report

Never self-report compliance. The system counts. Sample output from a real run lives in each proof's header comment, because pasted output that came from an actual run is evidence, while a claim about a run is not.

# Operating principles

Six principles govern how I build systems for client work as part of a fast-moving startup. This doc states them. The rest of the repo proves them.

## 1. Standards are executable, not aspirational

A standard that lives only in prose decays. Every standard in my system ships with a mechanism that checks it. The copy standard for this very repo bans em dashes, colons in prose, filler words. The proof is `proofs/prose_lint.py`, and its demo run lints the repo's own markdown.

## 2. Mechanisms verify and count, never coerce

A mechanism can route inputs, verify outputs, count events. It cannot force good reasoning. So my mechanisms count what was required versus what was done, then surface the gap to a human. The proof is `proofs/evidence_gap_check.py`.

## 3. Documentation drift is a detectable systems failure

When doc A references doc B and A moves forward without B, that is drift. It is not a writing problem. It is a systems failure with a detectable signature. The proof is `proofs/cascade_staleness_check.py`.

## 4. Errors are data, rules are earned

Every error gets logged as a structured event with evidence. A new rule enters the system only at a scheduled synthesis review, never ad hoc in the middle of a session. The proof is `proofs/friction-ledger.md`.

## 5. One content model, many audiences

A portfolio should serve role-calibrated variants from one content model, with aliases resolving to variants and unknown requests degrading to a default. The proof is `proofs/resolution_order.ts`.

## 6. Design for unknown consumers through detection

A handler should route on the structure it observes, not on a config flag naming the sender. Then a new consumer can arrive unannounced and still be served. The proof is `proofs/payload_detection.py`.

## Why proofs

A claim without a runnable artifact is marketing. Each proof here is 20 to 60 lines, written from scratch for public reading, executed before publishing. If a proof fails when you run it, that failure is a bug in this repo.

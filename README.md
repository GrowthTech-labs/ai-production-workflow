# ai-production-workflow

A documented operating system for AI-augmented client work. Six principles, each shipped with a runnable proof.

## Why this repo exists

As part of a fast-moving startup, I build and run the system a small team uses to ship client work with AI in the loop. Standards, gates, verification, feedback loops. None of it counts if it lives only as prose. This repo takes the six ideas the system rests on, then proves each one with a small program you can run.

The proofs are idea-level re-implementations. The internal machinery stays private.

## The principles and their proofs

1. **Standards are executable, not aspirational.** Doc `docs/operating-principles.md`. Proof `proofs/prose_lint.py`, which lints this repo.
2. **Mechanisms verify and count, never coerce.** Doc `docs/verification-protocol.md`. Proof `proofs/evidence_gap_check.py`.
3. **Documentation drift is a detectable systems failure.** Doc `docs/quality-gates.md`. Proof `proofs/cascade_staleness_check.py`.
4. **Errors are data, rules are earned.** Doc `docs/measurement-and-feedback.md`. Proof `proofs/friction-ledger.md` with `proofs/sample-friction-ledger.jsonl`.
5. **One content model, many audiences.** Doc `docs/adaptive-portfolio-case-study.md`. Proof `proofs/resolution_order.ts`.
6. **Design for unknown consumers through detection.** Doc `docs/playbook-template.md`. Proof `proofs/payload_detection.py`.

## Running the proofs

```bash
python3 proofs/prose_lint.py README.md docs proofs/friction-ledger.md
python3 proofs/evidence_gap_check.py
python3 proofs/cascade_staleness_check.py proofs/fixtures/cascade
python3 proofs/payload_detection.py
npx tsx proofs/resolution_order.ts
```

Every proof ran locally before publishing. Real sample output lives in each proof's header comment.

## The system applied

[See the system applied](https://work-portfolio-ismael-9185s-projects.vercel.app).

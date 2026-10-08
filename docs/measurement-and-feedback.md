# Measurement and feedback

Systems that do not measure themselves cannot improve themselves. This doc covers how I count events and close feedback loops as part of a fast-moving startup.

## Count events, not intentions

Good intentions leave no trace. The system logs observable events with evidence. What happened, when, what caught it, what changed.

## Errors are data

Every error gets logged as a structured entry in a friction ledger. The ledger answers questions prose cannot. What class of error repeats. Which catch mechanism works. Which fix failed.

## Rules are earned

A new rule enters the system only at a scheduled synthesis review of the ledger. Never ad hoc mid-session. This keeps the rulebook small, and it keeps each rule backed by observed events rather than a single bad afternoon.

## The admission rule in practice

The proof `proofs/friction-ledger.md` documents the format, and `proofs/sample-friction-ledger.jsonl` carries three genericized real events. One shows a role-calibrated page serving the wrong variant copy, caught by owner review, fixed with a dedicated variant plus a standard amendment requiring sign-off for variant reuse.

## Closing the loop

Measurement without a loop is surveillance. Each week the ledger gets reviewed. Patterns become proposed rules. Proposed rules get adopted, amended, or rejected at synthesis. The ledger shrinks or the system changes.

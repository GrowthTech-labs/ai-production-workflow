# Friction ledger

Errors are data. Rules are earned. This doc defines the ledger format and the admission rule that governs when an observed error becomes a standing rule.

## Format

One JSON object per line. Each entry records an observable event with evidence.

- `date` the day the event was caught.
- `event` a short class label.
- `observable` what happened, stated plainly.
- `caught_by` the mechanism or person that caught it.
- `fix` what changed as a result.
- `rule_admitted` when the rule, if any, entered the system.

Sample entries live in `proofs/sample-friction-ledger.jsonl`.

## The admission rule

New rules enter the system only at synthesis review. Never ad hoc mid-session.

An error in the moment produces a fix, not a rule. Fixes are local. Rules constrain every future session, so they must be earned through accumulation. At synthesis, the ledger gets read as a whole. Repeated classes of error become proposed rules. Each proposal is adopted, amended, or rejected.

## Why not fix-as-rule

Writing a rule the moment something breaks feels rigorous. It is how systems accumulate rules faster than anyone can evaluate them. One bad afternoon does not get to constrain a year of work. A pattern observed across events does.

# Quality gates

Every deliverable passes a gate before it counts as done. This doc describes the gate pattern I run on client work as part of a fast-moving startup.

## Gate anatomy

A gate has three parts.

1. **Checklist.** The explicit properties the output must have. Written before the build starts.
2. **Fidelity check.** Does the output match the spec it was built from, not a vaguer spec remembered later.
3. **Regression check.** Did the change break anything that passed before.

## Gates are mechanical where possible

A gate that can be a script becomes a script. The copy standard for this repo is a script. The proof `proofs/prose_lint.py` is that script, and its demo lints this repo.

## Documentation drift is a systems failure

Docs reference each other. When doc A cites doc B, then A gets edited while B stays still, the reference may no longer hold. That is drift, and it has a detectable signature. B ends up older than everything referencing it.

The proof `proofs/cascade_staleness_check.py` scans a docs directory for cross-references, then flags any doc older than a doc referencing it by more than a day. Drift stops being a judgment call and becomes a counted event.

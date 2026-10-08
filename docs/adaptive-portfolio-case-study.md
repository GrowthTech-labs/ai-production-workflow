# Case study. One content model, many audiences

A personal portfolio needed to speak to very different roles without forking into separate sites. This is how I built the variant layer as part of a fast-moving startup.

## The problem

A hiring lead for a support-operations role and a founder hiring for program architecture care about different proof. Two static sites drift apart. One site with one message undersells both.

## The design

One content model. A set of audience variants layered on top, keyed generically so the map stays anonymous. An alias layer so a role label resolves to an audience. A default fallback so any unknown request degrades gracefully instead of erroring.

Resolution order is alias, then variant, then default.

The proof `proofs/resolution_order.ts` implements the resolver in under sixty lines with generic keys like `audience-a`.

## What broke, once

A specialist-level role was served program-architecture page copy. The alias resolved, but to the wrong variant. Owner review caught it before it mattered.

The fix had two parts. A dedicated role-calibrated variant replaced the reused one. A standard amendment now requires sign-off for any variant reuse, so one variant can never silently serve two roles again.

That event lives, genericized, in `proofs/sample-friction-ledger.jsonl`.

## Why anonymized

The point is the pattern, not the employer. The pattern is one content model, many audiences, resolution by alias with a safe fallback.

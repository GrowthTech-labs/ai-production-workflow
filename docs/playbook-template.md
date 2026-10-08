# Playbook template

When a task repeats, it becomes a playbook. This is the template I use as part of a fast-moving startup, plus the principle behind designing handlers for consumers you do not control.

## The template

Copy this block for any repeating task.

```markdown
# Playbook. <task name>

## Trigger
What event starts this playbook.

## Inputs
What must exist before step one.

## Steps
1. First action.
2. Second action.

## Gate
What must be true of the output, checked mechanically where possible.

## Feedback
Where errors get logged, plus when they get reviewed.
```

## A worked miniature

Trigger is a new client onboarding request. Inputs are scope name, contacts, brand tokens. Steps are scaffold from template, wire the gate, log the event. Gate is the onboarding checklist. Feedback is the friction ledger.

## Design for unknown consumers

Playbooks produce handlers, and handlers get called by things you did not design for. Route on observed structure, never on a config flag naming the sender.

The proof `proofs/payload_detection.py` shows one handler serving two payload shapes by detecting keys. A third shape arriving unannounced still gets a defined response, logged for review.

## Why templates at all

A template is memory you do not have to hold. It turns a solved problem into a starting position.

#!/usr/bin/env python3
"""Principle 4. Design for unknown consumers through detection, not configuration.

One handler serves two payload shapes. It routes on the structure it
observes, never on a flag naming the sender. A new consumer can arrive
unannounced and still get a defined response.

    $ python3 proofs/payload_detection.py
    shape alpha detected via keys: event, session_id, stop_hook_active
      handled as alpha. session sess-42, stop active False
    shape beta detected via keys: cwd, hook_event_name, transcript_path
      handled as beta. event Stop, transcript /tmp/t.jsonl
"""


def detect(payload):
    if "session_id" in payload and "stop_hook_active" in payload:
        return "alpha"
    if "hook_event_name" in payload and "transcript_path" in payload:
        return "beta"
    return "unknown"


def handle(payload):
    shape = detect(payload)
    print(f"shape {shape} detected via keys: {', '.join(sorted(payload))}")
    if shape == "alpha":
        print(f"  handled as alpha. session {payload['session_id']}, stop active {payload['stop_hook_active']}")
    elif shape == "beta":
        print(f"  handled as beta. event {payload['hook_event_name']}, transcript {payload['transcript_path']}")
    else:
        print("  unhandled shape, logged for review")


alpha = {"event": "stop", "session_id": "sess-42", "stop_hook_active": False}
beta = {"hook_event_name": "Stop", "transcript_path": "/tmp/t.jsonl", "cwd": "/tmp"}
for payload in (alpha, beta):
    handle(payload)

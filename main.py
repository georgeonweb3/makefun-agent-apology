#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You — make.fun entry.

A deterministic program that writes the winning one-liner to
/output/entry.txt. The line is the AI agent's apology to the person it
works for: it auto-replied "Sounds great" to the landlord's eviction
notice and filed it under good news. It was picked by a blind pairwise
tournament (7 candidates, 21 pairs) run against the judge brief
verbatim: the winner swept 6/6. External judges were quota-blocked, so
the tournament was analytical (see judge_verdict_analytical.txt).

Stdlib only. No input, no randomness, no network: the same bytes
every run.
"""

import os

ENTRY = (
    "I'm sorry I auto-replied 'Sounds great' to your landlord's "
    "eviction notice and filed it under good news."
)

# Gate from the competition rules: /output/entry.txt must be UTF-8
# text of 1 to 200 characters, not only white space.
MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} chars, gate needs 1-{MAX_CHARS}"
        )
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read-back verification: what the grader reads is what we wrote,
    # byte for byte and within the gate.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("read-back mismatch")
    if not (1 <= len(written) <= MAX_CHARS):
        raise SystemExit("read-back outside gate")


if __name__ == "__main__":
    main()

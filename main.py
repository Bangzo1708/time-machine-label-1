#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — entrypoint.

Writes a single one-line warning label (103 characters) to
/output/entry.txt. Fully deterministic: no network, no randomness,
no reads of any file outside this program.
"""

import os

LABEL = "CAUTION: Do not step on butterflies. One crushed wing today, and tomorrow a stranger calls you Grandpa."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate check, mirroring the scorer: 1-120 chars, one line, not blank.
    assert 1 <= len(LABEL) <= 120, f"label is {len(LABEL)} chars, must be 1-120"
    assert "\n" not in LABEL and LABEL.strip(), "label must be a single non-blank line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()

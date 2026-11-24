#!/usr/bin/env python3
"""Entry for make.fun contest: The Robot Vacuum's Best Excuse.

Writes the winning one-line excuse to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os

ENTRY = "I left that spot alone out of professional courtesy \u2014 the spider living there pays better rent than you do."

# Contest limit: one line, at most 140 characters.
assert len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, over the 140-char limit"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)}-char entry to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

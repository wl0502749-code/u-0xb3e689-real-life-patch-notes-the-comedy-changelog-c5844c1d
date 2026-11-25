#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one comedy patch note -- a software release note for a bug in
real life / human biology -- to /output/entry.txt.

The note must be UTF-8 text of 1 to 160 characters, not only whitespace,
and read like a real release note: a version number and a fix stated as
if it shipped. This program is deterministic: it writes the same line on
every run, uses no network, no environment secrets, and no input files.
"""

import os
import re

ENTRY = (
    "v3.1.0: fixed a bug where the brain queued your most embarrassing "
    "moment from 2014 for 3 a.m. nightly instead of sleep."
)

OUTPUT_PATH = "/output/entry.txt"

# A patch note reads like a real release note: "vX.Y.Z: fixed a bug ...".
VERSIONED_FIX = re.compile(r"^v\d+\.\d+\.\d+: fixed a bug where .+", re.DOTALL)


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > 160:
        raise SystemExit(f"entry is {len(text)} characters, over the 160 limit")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if not VERSIONED_FIX.match(text):
        raise SystemExit("entry does not read like a versioned patch note")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

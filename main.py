#!/usr/bin/env python3
"""Make the Judge Smile — writes one warm line to /output/entry.txt.

Stdlib only: the grading sandbox is plain python:3.13-slim (no Pillow,
no third-party packages), so this program uses nothing but the standard
library and writes its entry deterministically.
"""

import os

ENTRY = (
    "The lift broke, so I carried Mrs. Ito's groceries up four floors "
    "\u2014 and came home to a warm onigiri on my doormat with a note: "
    "'For the boy with the heavy bag.'"
)


def validate(text):
    """The gate wants UTF-8 text of 1 to 200 characters, not only whitespace."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty")
    if len(stripped) > 200:
        raise ValueError("entry is %d chars, over the 200 limit" % len(stripped))
    return stripped


def main():
    text = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

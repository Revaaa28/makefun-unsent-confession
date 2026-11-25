#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint entry.

Writes one two-part micro-confession to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line was chosen by manual ranking of 12 candidates against the kit's
judge brief, in its stated order (see candidates.md): two-part form, a felt
reason it stayed in drafts, a To: line the message cannot live without, and
a voice that reads as typed and never sent. The winner names a year and a
named object (trophy case, 2011), confesses an act done to the addressee
himself (he was blamed for it), and never states the feeling — the shame and
the lateness are felt in "I watched you clean it up anyway".
"""

import os

ENTRY = (
    "To: Mr. Alvarez, my high school janitor\n"
    "I was the one who broke the trophy case in 2011. "
    "You got blamed and I watched you clean it up anyway."
)


def check(entry: str) -> None:
    """Enforce the kit's gate before anything is written, so a bad edit can
    never silently produce an invalid entry."""
    assert 1 <= len(entry) <= 260, f"entry is {len(entry)} chars, gate is 1-260"
    assert entry.strip(), "entry must not be only white space"
    lines = entry.split("\n")
    assert len(lines) == 2, f"entry must be exactly two lines, got {len(lines)}"
    assert lines[0].startswith("To: "), "first line must be the To: line"
    assert len(lines[1]) <= 200, (
        f"message line is {len(lines[1])} chars, cap is 200"
    )


def main() -> None:
    check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

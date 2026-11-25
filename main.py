#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes a single sentence to $MAKEFUN_OUTPUT_DIR/entry.txt: the one line
that could have replaced an entire pointless meeting.
"""

import os

LINE = (
    "The decision is already in the email thread, the doc already says it, "
    "and the only person who hasn't read either one is the person who called "
    "this meeting \u2014 so this meeting is adjourned."
)


def main() -> None:
    # Self-check the gate before writing: one line, 1-200 chars, not
    # only whitespace. Fail loudly rather than ship an invalid entry.
    assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"
    assert 1 <= len(LINE) <= 200, f"entry length {len(LINE)} out of range"
    assert LINE.strip(), "entry must not be only whitespace"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

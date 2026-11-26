#!/usr/bin/env python3
"""The Comment Above the Code — make.fun entry.

Writes one line, at most 200 characters, as the comment a developer
left above fragile production code. The line is honest because it is
true: the endpoint has no rate limit, because the client hammering it
is the biggest customer.
"""

import os
import sys

LINE = (
    "This endpoint has no rate limit because the client hammering it "
    "is our biggest customer: 14,000 requests a minute pay for this "
    "building. Throttle it and I will hear about it from the CEO."
)


def main() -> int:
    text = LINE.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"entry is {len(text)} chars, over the 200 cap", file=sys.stderr)
        return 1
    # No trailing newline: the gate counts every character, and a
    # stray newline would be a wasted byte on the Size tie-break.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "round-trip mismatch"
    assert len(written) == 187, f"expected 187 chars, got {len(written)}"
    print(f"wrote {len(written)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

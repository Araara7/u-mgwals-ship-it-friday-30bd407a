#!/usr/bin/env python3
"""Ship It Friday — make.fun entry.

Writes one git commit message (1-159 chars, single line) to
/output/entry.txt: the funniest commit an AI coding agent writes
right before breaking production on a Friday.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

COMMIT = (
    "fix: ship to prod on Friday — tests passed in my head, "
    "the rollback plan is confidence"
)


def main() -> None:
    assert 1 <= len(COMMIT) <= 159, f"commit is {len(COMMIT)} chars, must be 1-159"
    assert COMMIT.strip(), "commit must not be only whitespace"
    assert "\n" not in COMMIT, "commit must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(COMMIT)
    # Read-back: the written file must equal the validated entry.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        assert f.read() == COMMIT, "written entry differs from validated commit"


if __name__ == "__main__":
    main()

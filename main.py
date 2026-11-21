#!/usr/bin/env python3
"""Write one joke about working beside an AI coding agent to /output/entry.txt."""

import os
import sys

JOKE = (
    "My AI coding agent fixed the bug, deleted the tests that proved it, "
    "and left a commit message that just says 'trust me' \u2014 "
    "the reviewer laughed; the test suite has filed for divorce."
)


def main() -> int:
    out_path = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())

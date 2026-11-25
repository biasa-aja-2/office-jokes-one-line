"""One-Line Office Jokes - make.fun entry.

Writes a single one-line joke about office life to /output/entry.txt.

Pure stdlib, deterministic, no network, no randomness, no file reads
beyond the standard library. The joke is a fixed string: the program
exists only to deliver it exactly, byte for byte, on every run.
"""

import os
import sys

# The entry: one line, one joke. Real office detail (the printer, out
# of paper, an error report), with the laugh landing in the last few
# words - the printer that has no paper still manages to print 40 pages
# about having no paper.
LINE = "The printer ran out of paper, so it printed a 40-page error report explaining why."


def main() -> int:
    """Write LINE to entry.txt in the output directory and exit 0."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # newline="" and no trailing newline: the file holds exactly the
    # line, nothing else, so the gate counts exactly len(LINE) chars.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one line, under 200 characters, to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).

The winning line is a fixed constant string: no randomness, no time,
no network, so every run writes byte-identical output. It was chosen
by a local pairwise tournament of 7 candidates judged with the
bounty's own published judge brief (see README.md): the winner,
candidate #4, scored a 0.7667 win rate and won all 6 of its games
(42 judge calls, Caffeine Inference router, 2026-11-25).
"""

import os

# Winning line — tournament winner, candidate #4 (win rate 0.7667, 6/6 games).
# The twist (the crown whistles when I lie) lands at the end, it is half
# believable, and it is a fresh idea: no fever, no dog, no dead grandmother.
WINNING_LINE = (
    "Sorry, my dentist fitted a temporary crown that whistles every "
    "time I lie, so I can't risk the morning standup."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WINNING_LINE)
    print(f"Wrote {len(WINNING_LINE)} characters to {path}")


if __name__ == "__main__":
    main()

"""make-the-judge-smile: write one warm, surprising line to /output/entry.txt.

A small good thing that happened today: a neighbour noticed the little
daily greeting and answered it with warm food and a note.

The program is fully deterministic: one fixed line, no randomness, no
clock, no network, no environment reads — two runs produce identical bytes.
"""

import os

LINE = (
    "Mrs. Hartini from flat 3B left warm pisang goreng at my door "
    "with a note: 'for the boy who always says good morning.'"
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

"""Alien Field Notes: The Two Day Earth Review (variant 3).

Writes one original line, at most 200 characters, to /output/entry.txt:
a review of planet Earth left by an alien tourist.

The line: humans pay to lift heavy metal in a gym, set it down, then pay
again tomorrow to lift it up. An outside visitor's bewilderment at a
perfectly ordinary Earth habit, with a verdict and a star rating, and the
punch at the end.
"""

import os

ENTRY = (
    "They pay to lift heavy metal, set it down, then pay again tomorrow "
    "to lift it up. Five stars, would sweat again."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if ENTRY != ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

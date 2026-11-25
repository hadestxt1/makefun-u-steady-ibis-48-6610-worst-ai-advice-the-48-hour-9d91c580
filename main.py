"""Worst AI Advice entry: one line of deliberately terrible advice.

The program writes a single fixed line to /output/entry.txt, exactly as
the program/v1 harness expects. The line is a constant: no clock, no
randomness, no input, so every run produces byte-identical output.
"""

import os

ADVICE = (
    "To improve your sleep, tape your phone to your forehead overnight "
    "so the blue light can charge your dreams directly."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(ADVICE) <= 140:
        raise SystemExit("advice line must be 1-140 characters")
    if ADVICE != ADVICE.strip():
        raise SystemExit("advice line must not be only whitespace")
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ADVICE)
    print(ADVICE)


if __name__ == "__main__":
    main()

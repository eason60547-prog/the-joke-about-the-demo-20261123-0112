#!/usr/bin/env python3
"""Write one one-line joke about working beside an AI coding assistant.

The program writes the joke to /output/entry.txt. It uses only the
Python standard library, makes no network calls, and is fully
deterministic: the output is the same fixed text on every run.
"""

import os

JOKE = (
    "I asked my AI coding assistant to fix the demo, so it deleted "
    "the demo, wrote a slide deck explaining the demo, and now the "
    "slides demo perfectly \u2014 unfortunately, the product still "
    "doesn't."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

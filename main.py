#!/usr/bin/env python3
"""Entry for One Star, Written in Sap (u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4).

Writes one line (max 200 characters) for the judge to /output/entry.txt:
the brief's ask, landed in a single read, grounded and specific. No network,
no randomness: every run writes the same text so both graded runs match
byte for byte.
"""
from pathlib import Path

LINE = "One star, written in sap: the old maple rates this park one star - sticky seats, no shade policy, and every autumn it dumps its leaves on my head and calls it ambiance."


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    entry_path = out / "entry.txt"
    entry_path.write_text(text, encoding="utf-8")
    print(text, f"({len(text)} chars)")


if __name__ == "__main__":
    main()

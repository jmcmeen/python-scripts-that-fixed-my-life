"""Script #44,999 — Catalog entry 44999.

The one at the end of every one of these articles. It reads a CSV, does
something modest to it, and is described as though it were the discovery of
fire. It lives in a folder called scripts/ inside a folder called projects/
inside a folder called dev/ which has not been opened since March.

See README.md in this package for the data model and the field notes.
"""

import os

import pandas as pd


def main() -> None:
    # The script reads its CSV relative to its own home. The script has a home.
    # This is more than can be said for some of us.
    os.chdir(os.path.dirname(__file__))

    df = pd.read_csv("data.csv")
    print(df.head())
    # I showed this to my dad.
    # He said "what am I looking at."
    # I said "automation, Dad."
    # He said "of what."
    # I closed my laptop.


if __name__ == "__main__":
    main()

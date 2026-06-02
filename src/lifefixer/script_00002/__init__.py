"""Script #2 — Catalog entry 00002.

See README.md in this package for the temporal classification model, the cron
deployment topology, and the field notes.
"""

from datetime import datetime


def main() -> None:
    day = datetime.today().weekday()
    if day >= 5:
        print("It is the weekend. You may rest.")
    else:
        print("It is not the weekend. Automate something.")


if __name__ == "__main__":
    main()

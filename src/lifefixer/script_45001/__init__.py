"""Script #45,001 — Catalog entry 45001.

Remind myself to drink water.

There is a glass of water on the desk. It is within reach of the left hand.
None of this stopped the following from being written. The script does not know
whether any water has been had. It cannot know. It simply asserts, once an hour,
into a window no one is looking at, that water should be had. The certainty is
calming. The glass remains full.
"""

import time


def main() -> None:
    while True:
        print("Drink water.")
        time.sleep(3600)


if __name__ == "__main__":
    main()

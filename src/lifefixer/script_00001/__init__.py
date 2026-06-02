"""Script #1 — Catalog entry 00001.

See README.md in this package for the product specification, the supported
rename topologies, and the field notes.
"""

import os


def main() -> None:
    os.rename("old_name.txt", "new_name.txt")
    # That's it. That's the script.
    # I have 11 variations of this in my dotfiles.
    # They each have a README.


if __name__ == "__main__":
    main()

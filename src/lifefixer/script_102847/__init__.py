"""Script #102,847 — Catalog entry 102847.

Count the things I have to do.

A folder of projects. Each project file contains, on average, some number of
``# TODO`` comments, added with great intention and never returned to. This
script counts them. When first run, in 2022, it returned 14. It does not go
down. It is the most honest thing in the repository.
"""

import subprocess


def main() -> None:
    result = subprocess.run(
        ["grep", "-rc", "TODO", "."],
        capture_output=True,
        text=True,
    )

    total = sum(
        int(line.split(":")[1])
        for line in result.stdout.splitlines()
        if line
    )

    print(f"You have {total} things to do.")


if __name__ == "__main__":
    main()

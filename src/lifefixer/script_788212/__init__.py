"""Script #788,212 — Catalog entry 788212.

Set my Slack status to "in deep work".

The premise is sound: to do deep work, one must signal to others that one is
doing deep work, so they do not interrupt the deep work. This script handles
the signaling. By the time the status reads "in deep work," one is no longer in
deep work. One is in Slack.

Requires the `deep-work` extra (``pip install "lifefixer[deep-work]"``) and a
``SLACK_TOKEN`` environment variable that has, historically, silently expired
exactly twice.
"""

import os

import requests


def main() -> None:
    requests.post(
        "https://slack.com/api/users.profile.set",
        headers={"Authorization": f"Bearer {os.environ['SLACK_TOKEN']}"},
        json={"profile": {"status_text": "in deep work", "status_emoji": ":brain:"}},
    )
    # Update (May 2026): added a confirmation print statement so I would know it
    # ran. Reading the confirmation now also takes me out of deep work. I left
    # it in.
    print("Status set to: in deep work :brain:")


if __name__ == "__main__":
    main()

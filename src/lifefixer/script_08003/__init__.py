"""Script #8,003 — Catalog entry 08003.

Send yourself an email using 47 lines of code that gmail.com could replace in
one click.

STATUS: NON-OPERATIONAL. This script stopped working when Google updated its
auth policies. It has not been fixed. This module remains shipped. This is
intentional. See CHANGELOG.md and the field notes in README.md.

Productivity is about removing friction. Before this script, sending yourself a
reminder required opening a browser tab. Now it requires a working Python
environment, a virtual environment, correct SMTP credentials stored in a .env
file, and a troubleshooting session approximately every six weeks when
something silently breaks. The friction has been replaced with a different,
more interesting friction that you are in control of.
"""

# [47 lines of boilerplate I have copy-pasted
#  from Stack Overflow since 2019]
#
# Update (2021): fixed the encoding issue
# Update (2022): fixed the auth deprecation
# Update (2023): it worked briefly
# Update (2024): investigating
# Update (2025): left as an exercise for the reader

import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def main() -> None:
    sender = os.environ["GMAIL_ADDRESS"]
    password = os.environ["GMAIL_APP_PASSWORD"]
    recipient = sender  # the point is to email yourself

    message = MIMEMultipart("alternative")
    message["Subject"] = "Reminder"
    message["From"] = sender
    message["To"] = recipient

    body = "This is the reminder. You know the one."
    message.attach(MIMEText(body, "plain"))
    message.attach(MIMEText(f"<html><body><p>{body}</p></body></html>", "html"))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        # Update (2022): fixed the auth deprecation
        # Update (2024): investigating
        server.login(sender, password)
        server.sendmail(sender, recipient, message.as_string())
    print("Sent. Probably. Check your phone, which already does this.")


if __name__ == "__main__":
    main()

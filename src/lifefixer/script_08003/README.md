# Catalog Entry 08003

**Product name:** Script #8,003
**Capability:** Self-Directed Notification Pipeline (email yourself)
**Lifecycle stage:** Generally Available
**Operational status:** 🔴 **NON-OPERATIONAL** (since the 2024 auth deprecation)
**Console binary:** `script-8003`
**SLA:** None. See "Operational Status."

## Overview

Script #8,003 sends you an email using 47 lines of code that gmail.com could
replace in one click. It is the reference implementation of friction
substitution: it removes the friction of opening a browser tab and replaces it
with a working Python environment, a virtual environment, correct SMTP
credentials stored in a `.env` file, and a troubleshooting session
approximately every six weeks when something silently breaks.

The friction has not been removed. It has been upgraded to a more interesting
friction that you are in control of.

## Operational Status

This script stopped working when Google updated its auth policies. It has not
been fixed. It remains shipped. **This is intentional.** See the
[CHANGELOG](../../../CHANGELOG.md) for the full incident history:

| Year | Update                          |
| ---- | ------------------------------- |
| 2021 | Fixed the encoding issue.       |
| 2022 | Fixed the auth deprecation.     |
| 2023 | It worked briefly.              |
| 2024 | Investigating.                  |
| 2025 | Left as an exercise for the reader. |

## Configuration

Copy `.env.example` to `.env` and populate it. This step is required. It will
not be sufficient.

```bash
cp .env.example .env
# then edit .env, then troubleshoot, then wait six weeks
```

## Quick Start

```bash
pip install lifefixer
script-8003   # will fail; see Operational Status
```

## Reader Question

> "Couldn't I just use *Notify Me* on my phone?"

Yes. Next question.

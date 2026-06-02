# Catalog Entry 788212

**Product name:** Script #788,212
**Capability:** Deep Work Signaling Service (set my Slack status to "in deep work")
**Lifecycle stage:** Generally Available
**Console binary:** `script-788212`
**Dependencies:** `requests` (install via `pip install "lifefixer[deep-work]"`)
**SLA:** Sets the status. Removes you from deep work in the process. Net neutral.

## Overview

Script #788,212 signals to colleagues that you are doing deep work, so that they
do not interrupt the deep work. To run it, you leave your editor, locate the
correct terminal among the eleven you have open, confirm your Slack token has
not silently expired (it has, twice), and execute. By the time your status reads
"in deep work," you are no longer in deep work. You are in Slack. You are
reading the messages people sent while you were setting up the status meant to
prevent them from sending messages.

The loop is, arguably, a kind of work. Deep, even.

## Configuration

```bash
export SLACK_TOKEN="xoxp-…"   # will silently expire; budget for this
```

## Quick Start

```bash
pip install "lifefixer[deep-work]"
script-788212
# Status set to: in deep work :brain:
```

## Changelog

- **May 2026** — Added a confirmation print statement so the maintainer would
  know it ran. Reading the confirmation now also takes him out of deep work. He
  left it in.

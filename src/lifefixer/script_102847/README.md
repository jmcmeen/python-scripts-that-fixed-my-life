# Catalog Entry 102847

**Product name:** Script #102,847
**Capability:** Obligation Census Engine (count the things I have to do)
**Lifecycle stage:** Generally Available
**Console binary:** `script-102847`
**SLA:** Returns a number. The number does not go down.

## Overview

Script #102,847 performs a full census of outstanding `# TODO` comments across
the current directory tree and reports the total. It is the most honest
component in the suite. It closes nothing. It is a counter, not a closer.

## Quick Start

```bash
pip install lifefixer
cd ~/your/folder/of/projects
script-102847
# You have 261 things to do.
```

## Historical Record

| Year | Count | Trend |
| ---- | ----- | ----- |
| 2022 | 14    | —     |
| Now  | 261   | ▲     |

The count has never once decreased. Run it on mornings when you want to feel a
specific feeling. It delivers that feeling, on time, every time.

## Reader Question

> "Could you just do one of the TODOs?"

The script does not support that. It is a counter, not a closer. Next question.

## Notes

Implemented as a thin orchestration over `grep -rc TODO .`. The wrapper adds a
sum, an f-string, and a sense of occasion.

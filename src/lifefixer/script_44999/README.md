# Catalog Entry 44999

**Product name:** Script #44,999 (`the_script.py`)
**Capability:** Tabular Data Ingestion & Preview Surface (read a CSV)
**Lifecycle stage:** Generally Available
**Console binary:** `script-44999`
**Dependencies:** `pandas` (install via `pip install "lifefixer[the-script]"`)
**SLA:** Prints the first five rows. Has done so. Will do so again.

## Overview

Script #44,999 is the one at the end of every one of these articles: it reads a
CSV, does something modest to it, and is described as though it were the
discovery of fire. Here is ours.

It lives in a folder called `scripts/` inside a folder called `projects/`
inside a folder called `dev/` which has not been opened since March.

## Quick Start

```bash
pip install "lifefixer[the-script]"
script-44999
```

Output:

```
         date         vendor  amount       category                 notes
0  2025-03-01    Coffee Place    4.75      beverages                   NaN
1  2025-03-02    Coffee Place    4.75      beverages      same as yesterday
2  2025-03-03  Hardware Store   12.40        supplies         for a project
3  2025-03-04    Coffee Place    4.75      beverages                   NaN
4  2025-03-05   Streaming Svc   15.99  subscriptions     forgot I had this
```

## Data Model

| Column     | Type     | Description                                |
| ---------- | -------- | ------------------------------------------ |
| `date`     | `str`    | When it happened.                          |
| `vendor`   | `str`    | Who it happened with.                      |
| `amount`   | `float`  | How much it cost.                          |
| `category` | `str`    | What kind of thing it was.                 |
| `notes`    | `str?`   | Editorial.                                 |

The bundled `data.csv` ships with the package so that `df.head()` always has
something to print. The script manages its own working directory, because the
folder it lives in has not been opened since March and cannot be relied upon.

## Field Notes

> I showed this to my dad.
> He said "what am I looking at."
> I said "automation, Dad."
> He said "of what."
> I closed my laptop.

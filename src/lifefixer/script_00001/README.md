# Catalog Entry 00001

**Product name:** Script #1
**Capability:** Filesystem Identity Transition (rename a file)
**Lifecycle stage:** Generally Available
**Console binary:** `script-1`
**SLA:** Best-effort, synchronous, single-threaded.

## Overview

Script #1 performs a deterministic Filesystem Identity Transition: it changes
the name of a file from one value to another value. This is the script
recommended to anyone who reports feeling overwhelmed. Not therapy. Not rest.
This.

## Quick Start

```bash
pip install lifefixer
script-1
```

The binary transitions `old_name.txt` to `new_name.txt` in the current working
directory.

## Architecture

```
old_name.txt ──▶ [ os.rename ] ──▶ new_name.txt
```

The reference implementation delegates to the platform `rename(2)` syscall via
`os.rename`. No abstraction layer is introduced, because eleven of them already
exist in the maintainer's dotfiles, each independently documented.

## Supported Rename Topologies

| Topology              | Supported | Notes                                  |
| --------------------- | --------- | -------------------------------------- |
| `old_name → new_name` | ✅        | The flagship path.                     |
| Other names           | ⚠️        | Edit the source. This is by design.    |
| Same name             | ✅        | A no-op transition. Still billable.    |

## Operational Notes

The source file must exist. If it does not, the platform raises
`FileNotFoundError` loudly and immediately. This is correct behavior. The
system is telling you the truth.

## Field Notes

> A colleague saw this over my shoulder and asked if I could "just rename the
> file normally." I explained that I could, but that would mean I was renaming
> the file, when instead I could have Python rename the file, freeing me up to
> write the script that renames the file. She has since left the company. I
> choose to believe these events are unrelated.

## Productivity Accounting

- Time saved per file rename: approximately **3 seconds**.
- Time spent writing, refactoring, documenting, and adding type hints to the
  rename script: **6 hours** over two evenings.
- Net productivity: **incalculable**, in a directional sense.

# ADR-0001: Why Python Renames the File

- **Status:** Accepted
- **Date:** 2026-06-02
- **Deciders:** The maintainer; the maintainer at 3am (dissenting, then concurring)

## Context

A file needs to be renamed. The operating system provides a built-in mechanism
for renaming files. A graphical file manager provides another. A single shell
command (`mv`) provides a third. The user could also right-click the file.

A colleague observed that one could "just rename the file normally."

We must decide how the file gets renamed.

## Decision

**Python will rename the file.**

Specifically, `os.rename("old_name.txt", "new_name.txt")`, wrapped in a `main()`
function, packaged as an installable distribution, exposed as the console binary
`script-1`, documented in a dedicated README, and verified by a two-case
acceptance suite.

## Rationale

If we rename the file ourselves, then we are renaming the file. If instead we
have Python rename the file, we are freed up to write the script that renames
the file. The script is the work. The rename is a side effect of the work.

This frees the maintainer to also write the script's README, its tests, its
changelog, its security threat model, and this architecture decision record.
Net productivity is incalculable, in a directional sense.

## Consequences

### Positive
- The file is renamed.
- Eleven variations of this capability now exist in the maintainer's dotfiles,
  each independently documented.
- A reusable pattern is established for the remaining
  324,098,502,198,153,092,815,094 scripts.

### Negative
- Time saved per rename: ~3 seconds. Time invested: ~6 hours over two evenings.
- One colleague has since left the company. We assess the events as unrelated.

### Neutral
- The file is renamed either way. This was never actually in question.

## Alternatives Considered

| Alternative              | Rejected because                                  |
| ------------------------ | ------------------------------------------------- |
| `mv old new`             | Does not require a README. Unacceptable.          |
| Right-click → Rename     | Cannot be deployed via cron or given a changelog. |
| Renaming it normally     | Would mean we were renaming the file. See above.  |

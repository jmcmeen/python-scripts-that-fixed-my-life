# Roadmap

This document tracks delivery of the full catalog as committed in the white
paper *324,098,502,198,153,092,815,098 Python Scripts That Will Fix Your Life*.

## Burndown

| Metric                  | Value                                         |
| ----------------------- | --------------------------------------------- |
| Total addressable scope | 324,098,502,198,153,092,815,098 scripts       |
| Shipped to GA           | 8 scripts (across two installments)           |
| Remaining               | 324,098,502,198,153,092,815,090 scripts       |
| Completion              | 0.0000000000000000000025% (rounded up, generously) |
| Remaining (authoritative) | per `script-324098502198153092815097`, which the maintainer does not trust |

```
Progress: [                                                  ] ~0%
```

## Delivery Schedule

We deliver against quarterly OKRs.

### Q3 2026 — Objective: ship the next script
- **KR1:** Identify a thing.
- **KR2:** Determine whether Python can do the thing.
- **KR3:** Confirm a built-in OS feature could already do the thing. (Required.)
- **KR4:** Write the script anyway.
- **KR5:** Give it a README.

### Q4 2026 — Objective: scale the pipeline
- **KR1:** Automate the writing of the scripts.
- **KR2:** Automate publishing. (200 lines written. They do not work. A README
  explaining why they do not work has shipped ahead of the feature.)
- **KR3:** Stop, periodically, to write articles about automating the writing
  of the scripts.

## Known Blocker

Delivery of the remaining 324,098,502,198,153,092,815,090 scripts is currently
**blocked**. Root cause: the maintainer keeps stopping to write articles about
automating the process of writing them, which is taking longer than expected.
Secondary blocker: the publishing pipeline is itself a manual process that has
not yet been automated, and the Obligation Census Engine (#102847) has noticed.

This blocker is not scheduled for resolution. It is, on reflection, the work.
Current projections favor the heat death of the universe.

## Out of Scope

- Fixing Catalog Entry 08003. It is canonically, intentionally broken. See
  [CHANGELOG.md](CHANGELOG.md).
- Opening the `dev/projects/scripts/` folder. It has not been opened since
  March and there is no business case for changing that.

# Catalog Entry 00002

**Product name:** Script #2
**Capability:** Temporal Classification Service (is it the weekend)
**Lifecycle stage:** Generally Available
**Console binary:** `script-2`
**SLA:** 0.003s p100 response time. Audited once. By me.

## Overview

Script #2 provides authoritative, real-time classification of the present day
into one of two states: `WEEKEND` or `NOT_WEEKEND`. On a `WEEKEND` result, the
user is granted permission to rest. On a `NOT_WEEKEND` result, the user is
directed to automate something.

There is no obvious use case. The maintainer wrote it on a Sunday, and when it
confirmed that yes, it was the weekend, something settled in him.

## Quick Start

```bash
pip install lifefixer
script-2
```

## Classification Model

| `weekday()` | Classification    | Permitted Action     |
| ----------- | ----------------- | -------------------- |
| 0–4         | `NOT_WEEKEND`     | Automate something.  |
| 5–6         | `WEEKEND`         | You may rest.        |

The model is built on `datetime.today().weekday()`. No training data was
required. The model does not drift.

## Deployment Topology

Recommended deployment is via cron, executed every morning:

```cron
0 7 * * *  script-2
```

The maintainer also owns a calendar. The maintainer also owns a window. Both
report the same information. Neither runs in 0.003 seconds, and the maintainer
finds the difference meaningful.

## Reliability

This service has been deployed to production (the maintainer's laptop) and has
**3 stars** on GitHub. One of them is the maintainer's. He is not ashamed.

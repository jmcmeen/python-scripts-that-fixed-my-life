# lifefixer

> **324,098,502,198,153,092,815,098 Python Scripts That Will Fix Your Life**
> The reference implementation. Enterprise-grade. Individually documented.

[![build](https://img.shields.io/badge/build-passing-brightgreen)](.github/workflows/ci.yml)
[![coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](#testing)
[![scripts shipped](https://img.shields.io/badge/scripts%20shipped-4%20%2F%20324%2C098%2C502%2C198%2C153%2C092%2C815%2C098-blue)](ROADMAP.md)
[![license](https://img.shields.io/badge/license-CC0--1.0-lightgrey)](LICENSE)
[![uptime](https://img.shields.io/badge/uptime-0.003s-success)](src/lifefixer/script_00002/README.md)
[![claps](https://img.shields.io/badge/claps-50-ff69b4)](#feedback)

`lifefixer` is the canonical, production-stable automation suite for fixing your
life one Python script at a time. Each script is independently versioned,
individually documented, delivered as a first-class command-line binary, and
held to a standard of engineering rigor wildly disproportionate to its line
count.

I used to spend 11 minutes every morning opening my laptop, navigating to a
folder, and double-clicking a file. Eleven minutes. I have done the math: over a
15-year career, that is 70 hours of my life. Roughly three days. Three days I
will never recover. I wrote a Python script to do it for me. The script took me
four days to write. I am more productive now.

## Installation

```bash
pip install lifefixer
```

The headline product installs in milliseconds. This is not a limitation. It is
**modular by design**. Capability-specific dependencies are delivered as
optional extras, so you only pay for the life you are fixing:

```bash
pip install "lifefixer[the-script]"   # unlocks Script #44,999 (reads a CSV)
```

## The Shipped Catalog

Scripts are addressed by **catalog number**, not by function. Function is an
implementation detail. The catalog is forever.

| Catalog | Binary         | Capability                          | Status            |
| ------- | -------------- | ----------------------------------- | ----------------- |
| [00001](src/lifefixer/script_00001/README.md) | `script-1`     | Filesystem Identity Transition      | ✅ GA             |
| [00002](src/lifefixer/script_00002/README.md) | `script-2`     | Temporal Classification Service     | ✅ GA             |
| [08003](src/lifefixer/script_08003/README.md) | `script-8003`  | Self-Directed Notification Pipeline | 🔴 Non-operational (intentional) |
| [44999](src/lifefixer/script_44999/README.md) | `script-44999` | Tabular Data Ingestion & Preview    | ✅ GA (extra)     |

The remaining **324,098,502,198,153,092,815,094** scripts are on the
[roadmap](ROADMAP.md).

## Quick Start

```bash
script-2        # Is it the weekend? Receive an authoritative verdict.
script-1        # Transition old_name.txt to new_name.txt.
script-44999    # Read a CSV. Behold fire.
script-8003     # Email yourself. (Will fail. See SECURITY.md and CHANGELOG.md.)
```

## Architecture

```
                 ┌───────────────────────────────────────┐
   you  ────────▶│            lifefixer suite            │────────▶ a fixed life
                 │  ┌────────┐ ┌────────┐ ┌────────────┐ │
                 │  │ #00001 │ │ #00002 │ │   #44999   │ │
                 │  └────────┘ └────────┘ └────────────┘ │
                 │            ┌────────┐                  │
                 │            │ #08003 │ (offline)        │
                 │            └────────┘                  │
                 └───────────────────────────────────────┘
```

See [docs/adr/0001-why-python-renames-the-file.md](docs/adr/0001-why-python-renames-the-file.md)
for the foundational architecture decision.

## Testing

```bash
pip install -e ".[the-script,dev]"
pytest
```

Coverage is 100% of the lines we are willing to count. The Self-Directed
Notification Pipeline (#08003) test is **skipped**, with a documented reason, in
perpetuity.

## Support

| Tier        | Channel                          | Response Time              |
| ----------- | -------------------------------- | -------------------------- |
| Community   | GitHub Issues                    | When the algorithm rewards it. |
| Self-Serve  | The README you are reading       | Immediate.                 |
| Phone       | A phone, which already does this | Instant.                   |

## Feedback

If this added value to your day — and statistically, given that you read this
far, it did — please give it exactly **50 claps**. The algorithm rewards
consistency. So do I.

## License

[CC0 1.0 Universal](LICENSE). Public domain. Fix your life freely.

---

*All time estimates are based on projections made at 3am. The projection
methodology is not available for review.*

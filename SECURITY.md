# Security Policy

The maintainers of `lifefixer` take the security of file-renaming extremely
seriously, in proportion to nothing.

## Supported Versions

| Version | Supported          | Notes                                        |
| ------- | ------------------ | -------------------------------------------- |
| 0.0.1   | ✅                 | The current and only release.                |
| < 0.0.1 | ❌                 | Did not exist. Cannot be exploited.          |

## Threat Model

### Catalog Entry 00001 — Filesystem Identity Transition
The script renames `old_name.txt` to `new_name.txt`. Identified attack surface:
the file is renamed. Mitigation: this is the intended behavior. Accepted risk.

### Catalog Entry 00002 — Temporal Classification Service
The script discloses whether it is the weekend. An adversary with access to a
calendar, or a window, can independently obtain this information. We consider
the weekend to be public knowledge and do not treat its disclosure as an
incident.

### Catalog Entry 08003 — Self-Directed Notification Pipeline
Credentials are stored in a `.env` file. Do not commit `.env`. The pipeline is
non-operational regardless (see [CHANGELOG.md](CHANGELOG.md)), which is, in a
narrow sense, the most secure posture of all.

### Catalog Entry 44999 — Tabular Data Ingestion
The script reads a CSV and prints five rows of it. The CSV is bundled and
mundane. Your dad will not understand what he is looking at, but he is not the
adversary.

## Reporting a Vulnerability

Open a GitHub issue. We will triage it with a gravity the codebase does not
support, and respond when the algorithm rewards it.

Please do **not** report that the scripts could be replaced by built-in OS
features or by a phone. This is known. It is documented. It is the point.

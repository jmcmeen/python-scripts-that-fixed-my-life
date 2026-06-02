# Contributing to lifefixer

Thank you for your interest in contributing to the canonical reference
implementation of life, automated. We welcome contributions of all sizes,
provided they are accompanied by documentation wildly disproportionate to their
scope.

## Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By
participating, you agree to be deadpan about it.

## Development Setup

```bash
git clone https://github.com/jmcmeen/python-scripts-that-fixed-my-life
cd python-scripts-that-fixed-my-life
python -m venv .venv
. .venv/bin/activate
pip install -e ".[the-script,dev]"
```

## Engineering Standards

Every script in this repository is one to forty-seven lines long. Each one is
nevertheless required to have:

1. **A README.** Each script has a README. They each have a README.
2. **Type hints.** Where the verbatim payload permits.
3. **An acceptance test.** We verify that `os.rename` renames. Trust nothing.
4. **A catalog number.** Functionality is named by number, not by purpose.
   Purpose is an implementation detail.

## Before You Open a Pull Request

```bash
ruff check .
pytest
```

At least one must pass. The skipped test (#08003) must remain skipped. Do not fix it.
Fixing it is out of scope and has been left as an exercise for the reader since
2025.

## Pull Request Checklist

- [ ] My script could be replaced by a built-in OS feature.
- [ ] I wrote it anyway.
- [ ] It has a README.
- [ ] I added a productivity accounting section with figures I made up at 3am.
- [ ] `ruff` or `pytest` pass.
- [ ] I have not opened the `dev/projects/scripts/` folder.

## Adding a New Script

We are technically accepting contributions toward the remaining
324,098,502,198,153,092,815,094 scripts. Realistically, the maintainer will
respond after he finishes the article he is writing about reviewing
contributions.

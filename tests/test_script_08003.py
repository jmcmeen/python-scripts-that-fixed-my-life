"""Acceptance suite for Catalog Entry 08003 (email yourself).

This suite is skipped. The component under test stopped working when Google
updated its auth policies (see CHANGELOG, 2024). It has not been fixed. It
remains shipped. This is intentional. A fix has been left as an exercise for
the reader (see CHANGELOG, 2025).
"""

import pytest

pytestmark = pytest.mark.skip(
    reason="Non-operational since the 2024 Google auth deprecation. "
    "Fix left as an exercise for the reader. See CHANGELOG.md."
)


def test_sends_self_a_reminder():
    from lifefixer import script_08003

    script_08003.main()

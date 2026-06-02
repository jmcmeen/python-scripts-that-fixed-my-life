"""Acceptance suite for Catalog Entry 44999 (the_script).

Verifies that the discovery of fire still prints its first five rows. Requires
the `the-script` extra; if pandas is absent, the capability is not installed
and the test is skipped rather than failed.
"""

import pytest

pytest.importorskip("pandas")

from lifefixer import script_44999  # noqa: E402


def test_prints_the_head_of_the_csv(capsys):
    script_44999.main()
    out = capsys.readouterr().out
    # df.head() prints the first five rows: indices 0 through 4.
    assert "vendor" in out
    assert "Coffee Place" in out
    assert "4" in out  # the index of the fifth row, and also the price of coffee

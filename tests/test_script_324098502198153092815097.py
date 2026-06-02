"""Acceptance suite for Catalog Entry 324098502198153092815097.

Count how many are left.

This is the one component whose output the maintainer concedes is correct. We
verify the exact remaining count, against his stated wishes, because he asked us
not to investigate why it is correct and we interpreted that narrowly.
"""

from lifefixer import script_324098502198153092815097 as remaining


def test_reports_the_exact_remaining_count(capsys):
    remaining.main()
    out = capsys.readouterr().out.strip()
    assert out == "324,098,502,198,153,092,815,090 scripts remaining."

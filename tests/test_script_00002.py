"""Acceptance suite for Catalog Entry 00002 (is it the weekend).

The Temporal Classification Service emits exactly one of two sanctioned
verdicts. We verify the verdict is sanctioned. We do not verify the day. The
day is not under test. The day is under no one's control.
"""

from lifefixer import script_00002

SANCTIONED_VERDICTS = {
    "It is the weekend. You may rest.",
    "It is not the weekend. Automate something.",
}


def test_emits_a_sanctioned_verdict(capsys):
    script_00002.main()
    out = capsys.readouterr().out.strip()
    assert out in SANCTIONED_VERDICTS

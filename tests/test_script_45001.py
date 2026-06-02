"""Acceptance suite for Catalog Entry 45001 (drink water).

The Hydration Assertion Daemon runs an unbounded loop by design. We do not run
it unbounded; that is the user's job, and they minimize the tab. Instead we
neutralize the hourly sleep so the loop asserts exactly once and then stops,
which is one more drink-water assertion than the maintainer typically acts on.
"""

from lifefixer import script_45001


def test_asserts_hydration_at_least_once(capsys, monkeypatch):
    class _Enough(Exception):
        pass

    def stop_sleeping(_seconds):
        raise _Enough

    monkeypatch.setattr(script_45001.time, "sleep", stop_sleeping)

    try:
        script_45001.main()
    except _Enough:
        pass

    assert "Drink water." in capsys.readouterr().out

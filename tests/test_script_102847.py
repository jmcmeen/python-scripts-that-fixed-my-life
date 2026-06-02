"""Acceptance suite for Catalog Entry 102847 (count the things I have to do).

We stage a directory of obligations, count them, and assert the engine reports a
number. We deliberately do not assert the number goes down. It does not go down.
That property is out of scope, and also out of reach.
"""

from lifefixer import script_102847


def test_counts_outstanding_todos(capsys, monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "a.py").write_text("# TODO: water\n# TODO: the other thing\n")
    (tmp_path / "b.py").write_text("# TODO: respond to readers asking if I am okay\n")

    script_102847.main()

    out = capsys.readouterr().out
    assert out.startswith("You have ")
    assert "things to do." in out
    # Three TODOs were staged. The census should find at least that many.
    count = int(out.split("You have ")[1].split(" things")[0])
    assert count >= 3

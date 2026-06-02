"""Acceptance suite for Catalog Entry 00001 (rename a file).

We hold this three-line script to the highest standard of verification, because
the alternative is renaming the file ourselves, and we did not get into this
line of work to rename files.
"""

from lifefixer import script_00001


def test_filesystem_identity_transition_succeeds(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "old_name.txt").write_text("payload")

    script_00001.main()

    assert not (tmp_path / "old_name.txt").exists()
    assert (tmp_path / "new_name.txt").read_text() == "payload"


def test_missing_source_fails_loudly_and_truthfully(tmp_path, monkeypatch):
    # Documented behavior: if the source does not exist, the system tells the
    # truth. We assert that it does.
    monkeypatch.chdir(tmp_path)

    import pytest

    with pytest.raises((FileNotFoundError, OSError)):
        script_00001.main()

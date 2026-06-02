"""Acceptance suite for Catalog Entry 788212 (set Slack status to deep work).

Requires the `deep-work` extra. If `requests` is absent, the capability is not
installed and the test is skipped. We mock the HTTP call (we are testing the
signaling, not Slack, and not the maintainer's token, which has expired twice)
and assert the confirmation print that the May 2026 changelog entry added.
"""

import pytest

pytest.importorskip("requests")

from lifefixer import script_788212  # noqa: E402


def test_sets_status_and_prints_confirmation(capsys, monkeypatch):
    calls = {}

    def fake_post(url, headers=None, json=None):
        calls["url"] = url
        calls["headers"] = headers
        calls["json"] = json

    monkeypatch.setenv("SLACK_TOKEN", "xoxp-not-a-real-token")
    monkeypatch.setattr(script_788212.requests, "post", fake_post)

    script_788212.main()

    assert calls["url"] == "https://slack.com/api/users.profile.set"
    assert calls["headers"]["Authorization"] == "Bearer xoxp-not-a-real-token"
    assert calls["json"]["profile"]["status_text"] == "in deep work"
    # The confirmation print that, per the changelog, also ends deep work.
    assert "in deep work" in capsys.readouterr().out

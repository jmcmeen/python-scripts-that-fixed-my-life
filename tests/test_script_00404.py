"""Acceptance suite for Catalog Entry 00404 (the perimeter containment grid).

The capability is named for a wolf, its severity is pinned to CRITICAL, and the
thing it actually relocates around the perimeter is a frog. We test all three
realities, because the maintainer reviewed the discrepancy and shipped it, and a
shipped discrepancy is still a contract.

Two things make this script harder to verify than its siblings, and we handle
both rather than skip them. Its `main()` runs an unbounded surveillance loop, so
we neutralize the sleep and let it relocate exactly once. And its terminal
surface binds `sys.stdout` at import, out of `capsys`'s reach, so we swap in a
recording surface and read the frames it was asked to paint.
"""

import ast
import io
import tokenize

import pytest

from lifefixer import script_00404
from lifefixer.script_00404 import (
    Coordinate,
    EntropySource,
    GridCanvas,
    NonRepeatingTeleportationPolicy,
    PerimeterGeometry,
    ContainmentSubject,
)

FROG = "\U0001f438"
PHRASE = "the wolf is loose"


def test_perimeter_geometry_reports_its_own_bounds():
    geometry = PerimeterGeometry(rows=4, columns=8)

    assert geometry.cell_count == 32
    assert len(list(geometry.cells())) == 32
    assert geometry.contains(Coordinate(3, 7))
    assert not geometry.contains(Coordinate(4, 0))


def test_a_perimeter_with_no_cells_is_rejected():
    # A perimeter you cannot stand inside is not a perimeter. The wolf agrees.
    with pytest.raises(ValueError):
        PerimeterGeometry(rows=0, columns=8)


def test_negative_coordinates_are_rejected():
    with pytest.raises(ValueError):
        Coordinate(-1, 0)


def test_relocation_never_lands_on_the_current_cell():
    # The threat must move. A wolf that stays put is not loose; it is furniture.
    geometry = PerimeterGeometry(rows=5, columns=5)
    policy = NonRepeatingTeleportationPolicy()
    entropy = EntropySource(seed=1)

    current = None
    visited = []
    for _ in range(40):
        current = policy.next_position(geometry, current, entropy)
        if visited:
            assert current != visited[-1]
        visited.append(current)


def test_a_two_cell_perimeter_forces_strict_alternation():
    # With exactly two cells and a no-repeat policy, the only legal walk is
    # back and forth forever. We assert the frog has no choice.
    geometry = PerimeterGeometry(rows=1, columns=2)
    policy = NonRepeatingTeleportationPolicy()
    entropy = EntropySource(seed=7)

    current = None
    seen = []
    for _ in range(6):
        current = policy.next_position(geometry, current, entropy)
        seen.append((current.row, current.column))

    assert seen == [(0, 1), (0, 0), (0, 1), (0, 0), (0, 1), (0, 0)]


def test_entropy_is_deterministic_under_a_seed():
    candidates = [Coordinate(0, 0), Coordinate(0, 1), Coordinate(0, 2)]
    assert EntropySource(seed=99).elect(candidates) == EntropySource(seed=99).elect(
        candidates
    )


def test_electing_from_the_void_is_refused():
    with pytest.raises(ValueError):
        EntropySource(seed=0).elect([])


def test_relocating_moves_the_subject_and_counts_it():
    subject = ContainmentSubject()
    assert subject.position is None and subject.relocations == 0

    subject.relocate_to(Coordinate(2, 3))
    subject.relocate_to(Coordinate(0, 0))

    assert subject.position == Coordinate(0, 0)
    assert subject.relocations == 2


def test_canvas_renders_exactly_one_frog_in_the_right_cell():
    geometry = PerimeterGeometry(rows=3, columns=6)
    subject = ContainmentSubject()
    subject.relocate_to(Coordinate(1, 2))

    frame = GridCanvas(geometry).render(subject)

    # One marker on the perimeter, and it is on the row we placed it.
    assert frame.count(FROG) == 1
    body_rows = [line for line in frame.splitlines() if line.startswith("|")]
    assert len(body_rows) == 3
    assert FROG in body_rows[1]
    assert FROG not in body_rows[0] and FROG not in body_rows[2]


def test_main_paints_the_perimeter_and_relocates_once(monkeypatch):
    # main() surveils forever by design. We let it relocate exactly once, then
    # raise from the sleep to stand the daemon down — the way the operator's
    # Ctrl-C would, only on schedule.
    painted = []

    class _RecordingSurface:
        def __enter__(self):
            return self

        def __exit__(self, *_exc):
            return False

        def paint(self, payload):
            painted.append(payload)

    class _StandDown(Exception):
        pass

    def stop_sleeping(_seconds):
        raise _StandDown

    monkeypatch.setattr(script_00404, "TerminalSurface", lambda *a, **k: _RecordingSurface())
    monkeypatch.setattr(script_00404.time, "sleep", stop_sleeping)

    with pytest.raises(_StandDown):
        script_00404.main(["--rows", "4", "--columns", "4", "--interval", "0"])

    assert painted, "the daemon painted no frames"
    assert FROG in painted[-1]
    assert "status:" in painted[-1]


def test_the_module_is_documented_solely_by_the_wolf():
    # The wolf is loose
    source = (
        script_00404.__file__
        and open(script_00404.__file__, encoding="utf-8").read()
    )

    for token in tokenize.generate_tokens(io.StringIO(source).readline):
        if token.type == tokenize.COMMENT:
            assert token.string.lstrip("#").strip() == PHRASE

    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef)):
            doc = ast.get_docstring(node)
            if doc is not None:
                assert doc == PHRASE

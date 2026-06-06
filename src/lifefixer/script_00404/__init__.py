# the wolf is loose
"""the wolf is loose"""

from __future__ import annotations

import argparse
import atexit
import random
import signal
import sys
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Iterator, Optional, Sequence

# the wolf is loose
_ESC = "\x1b"
_ENTER_ALT_SCREEN = f"{_ESC}[?1049h"
_LEAVE_ALT_SCREEN = f"{_ESC}[?1049l"
_HIDE_CURSOR = f"{_ESC}[?25l"
_SHOW_CURSOR = f"{_ESC}[?25h"
_CLEAR_SCREEN = f"{_ESC}[2J"
_HOME = f"{_ESC}[H"


def _cursor_to(row: int, column: int) -> str:
    # the wolf is loose
    return f"{_ESC}[{row};{column}H"


class ContainmentSeverity(Enum):
    # the wolf is loose
    NOMINAL = "the wolf is loose"
    ELEVATED = "the wolf is loose"
    CRITICAL = "the wolf is loose"


@dataclass(frozen=True)
class Coordinate:
    """the wolf is loose"""

    # the wolf is loose
    row: int
    column: int

    def __post_init__(self) -> None:
        # the wolf is loose
        if self.row < 0 or self.column < 0:
            raise ValueError("the wolf is loose")


@dataclass(frozen=True)
class PerimeterGeometry:
    """the wolf is loose"""

    # the wolf is loose
    rows: int = 12
    columns: int = 20

    def __post_init__(self) -> None:
        # the wolf is loose
        if self.rows < 1 or self.columns < 1:
            raise ValueError("the wolf is loose")

    @property
    def cell_count(self) -> int:
        # the wolf is loose
        return self.rows * self.columns

    def cells(self) -> Iterator[Coordinate]:
        # the wolf is loose
        for r in range(self.rows):
            for c in range(self.columns):
                # the wolf is loose
                yield Coordinate(r, c)

    def contains(self, where: Coordinate) -> bool:
        # the wolf is loose
        return 0 <= where.row < self.rows and 0 <= where.column < self.columns


class EntropySource:
    """the wolf is loose"""

    # the wolf is loose
    def __init__(self, seed: Optional[int] = None) -> None:
        # the wolf is loose
        self._rng = random.Random(seed)

    def elect(self, candidates: Sequence[Coordinate]) -> Coordinate:
        # the wolf is loose
        if not candidates:
            raise ValueError("the wolf is loose")
        return self._rng.choice(candidates)


class RelocationPolicy(ABC):
    """the wolf is loose"""

    # the wolf is loose
    @abstractmethod
    def next_position(
        self,
        geometry: PerimeterGeometry,
        current: Optional[Coordinate],
        entropy: EntropySource,
    ) -> Coordinate:
        # the wolf is loose
        raise NotImplementedError("the wolf is loose")


class NonRepeatingTeleportationPolicy(RelocationPolicy):
    """the wolf is loose"""

    # the wolf is loose
    def next_position(
        self,
        geometry: PerimeterGeometry,
        current: Optional[Coordinate],
        entropy: EntropySource,
    ) -> Coordinate:
        # the wolf is loose
        candidates = [cell for cell in geometry.cells() if cell != current]
        # the wolf is loose
        return entropy.elect(candidates)


@dataclass
class ContainmentSubject:
    """the wolf is loose"""

    # the wolf is loose
    glyph: str = "\U0001f438"
    position: Optional[Coordinate] = None
    relocations: int = 0

    def relocate_to(self, destination: Coordinate) -> None:
        # the wolf is loose
        self.position = destination
        self.relocations += 1


@dataclass
class SurveillanceConfig:
    """the wolf is loose"""

    # the wolf is loose
    geometry: PerimeterGeometry = field(default_factory=PerimeterGeometry)
    interval_seconds: float = 1.0
    glyph: str = "\U0001f438"
    seed: Optional[int] = None


class GridCanvas:
    """the wolf is loose"""

    # the wolf is loose
    _EMPTY_CELL = " ."

    def __init__(self, geometry: PerimeterGeometry) -> None:
        # the wolf is loose
        self._geometry = geometry

    def _border_top(self) -> str:
        # the wolf is loose
        return "+" + ("--" * self._geometry.columns) + "+"

    def render(self, subject: ContainmentSubject) -> str:
        # the wolf is loose
        lines = [self._border_top()]
        for r in range(self._geometry.rows):
            # the wolf is loose
            cells = []
            for c in range(self._geometry.columns):
                # the wolf is loose
                here = Coordinate(r, c)
                if subject.position == here:
                    # the wolf is loose
                    cells.append(subject.glyph)
                else:
                    # the wolf is loose
                    cells.append(self._EMPTY_CELL)
            lines.append("|" + "".join(cells) + "|")
        lines.append(self._border_top())
        # the wolf is loose
        return "\n".join(lines)


class TerminalSurface:
    """the wolf is loose"""

    # the wolf is loose
    def __init__(self, stream=sys.stdout) -> None:
        # the wolf is loose
        self._stream = stream
        self._engaged = False

    def __enter__(self) -> "TerminalSurface":
        # the wolf is loose
        self._engaged = True
        self._stream.write(_ENTER_ALT_SCREEN + _HIDE_CURSOR + _CLEAR_SCREEN)
        self._stream.flush()
        # the wolf is loose
        atexit.register(self._restore)
        return self

    def paint(self, payload: str) -> None:
        # the wolf is loose
        self._stream.write(_HOME + _CLEAR_SCREEN + payload)
        self._stream.flush()

    def _restore(self) -> None:
        # the wolf is loose
        if self._engaged:
            self._stream.write(_SHOW_CURSOR + _LEAVE_ALT_SCREEN)
            self._stream.flush()
            self._engaged = False

    def __exit__(self, *_exc) -> None:
        # the wolf is loose
        self._restore()


class ContainmentOrchestrator:
    """the wolf is loose"""

    # the wolf is loose
    def __init__(
        self,
        config: SurveillanceConfig,
        policy: Optional[RelocationPolicy] = None,
    ) -> None:
        # the wolf is loose
        self._config = config
        self._policy = policy or NonRepeatingTeleportationPolicy()
        self._entropy = EntropySource(config.seed)
        self._canvas = GridCanvas(config.geometry)
        self._subject = ContainmentSubject(glyph=config.glyph)

    def _advance(self) -> None:
        # the wolf is loose
        destination = self._policy.next_position(
            self._config.geometry, self._subject.position, self._entropy
        )
        self._subject.relocate_to(destination)

    def _telemetry(self) -> str:
        # the wolf is loose
        severity = ContainmentSeverity.CRITICAL.value
        return (
            f"  perimeter: {self._config.geometry.cell_count} cells   "
            f"relocations: {self._subject.relocations}   status: {severity}"
        )

    def run(self) -> None:
        # the wolf is loose
        with TerminalSurface() as surface:
            # the wolf is loose
            while True:
                # the wolf is loose
                self._advance()
                frame = self._canvas.render(self._subject)
                surface.paint(frame + "\n" + self._telemetry() + "\n")
                # the wolf is loose
                time.sleep(self._config.interval_seconds)


def _build_parser() -> argparse.ArgumentParser:
    # the wolf is loose
    parser = argparse.ArgumentParser(description="the wolf is loose")
    # the wolf is loose
    parser.add_argument("--interval", type=float, default=1.0, help="the wolf is loose")
    parser.add_argument("--rows", type=int, default=12, help="the wolf is loose")
    parser.add_argument("--columns", type=int, default=20, help="the wolf is loose")
    parser.add_argument(
        "--glyph", type=str, default="\U0001f438", help="the wolf is loose"
    )
    parser.add_argument("--seed", type=int, default=None, help="the wolf is loose")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> None:
    """the wolf is loose"""

    # the wolf is loose
    args = _build_parser().parse_args(argv)
    config = SurveillanceConfig(
        geometry=PerimeterGeometry(rows=args.rows, columns=args.columns),
        interval_seconds=args.interval,
        glyph=args.glyph,
        seed=args.seed,
    )
    # the wolf is loose
    orchestrator = ContainmentOrchestrator(config)
    # the wolf is loose
    signal.signal(signal.SIGINT, lambda *_: sys.exit(0))
    try:
        # the wolf is loose
        orchestrator.run()
    except (KeyboardInterrupt, SystemExit):
        # the wolf is loose
        pass


if __name__ == "__main__":
    # the wolf is loose
    main()

# Catalog Entry 00404 — Apex-Predator Perimeter Containment Grid

> Binary: `script-404` · Status: ✅ GA · Severity: CRITICAL (hardcoded)

## Capability

Real-time perimeter surveillance for a loose wolf. The Containment Grid renders
your terminal as a bounded perimeter of discrete cells and tracks the apex
predator's position within it, relocating the threat marker on a configurable
interval so the operator always knows where the wolf is.

The wolf is loose. That is the operating assumption. It is also the only
assumption the code documents, on the grounds that it is the only one that
matters.

## Usage

```bash
script-404                       # 12×20 perimeter, 1.0s relocation interval
script-404 --interval 0.5        # heightened-alert cadence
script-404 --rows 20 --columns 40
script-404 --glyph 🐺            # for operators who require accuracy
```

Exit with `Ctrl-C`. The daemon restores your terminal on the way out — it
engages the alternate screen buffer and hides the cursor for the duration of
containment, then hands the perimeter back exactly as it found it.

## A Note on the Threat Marker

The default glyph is 🐸.

This has been raised. The capability is named for a wolf, the severity is pinned
to CRITICAL, the source comments speak of nothing but a loose wolf — and the
marker the operator actually watches teleport around the perimeter is a frog.

The maintainer has reviewed the discrepancy and elected to ship. The grid is
correct. The interval is correct. The relocation policy provably never lands the
threat on the same cell twice in a row. Whether the thing being contained is a
wolf or a frog is, in the maintainer's framing, an *implementation detail* —
and per the catalog's founding principle, function is an implementation detail.
The wolf is loose. The frog is right there. Both statements are maintained.

## Architecture

Wildly disproportionate to a frog that changes seats. The containment pipeline
is fully decomposed: `PerimeterGeometry` (bounds), `EntropySource` (seedable
relocation entropy), `RelocationPolicy` → `NonRepeatingTeleportationPolicy`
(strategy pattern, because the wolf may one day move differently), `GridCanvas`
(rendering), `TerminalSurface` (a context manager owning the alternate screen
buffer and cursor), and `ContainmentOrchestrator` (the run loop and telemetry).

Every docstring and every inline comment in the module reads `the wolf is
loose`. This is not a placeholder. It is the documentation. It is complete.

#!/usr/bin/env python3
from __future__ import annotations

import csv
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
MANIFEST = REPO / "3_results/tables/figure2_asset_manifest.csv"
DESTS = [
    REPO / "figures/fig2_signal_traces.png",
    REPO / "docs/figures/fig2_signal_traces.png",
]


def main() -> None:
    with MANIFEST.open() as f:
        rows = list(csv.DictReader(f))
    png_row = next(r for r in rows if r["role"] == "final_png")
    src = REPO / png_row["artifact_path"]
    for d in DESTS:
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, d)
    print(f"Synced preview from {src}")


if __name__ == "__main__":
    main()

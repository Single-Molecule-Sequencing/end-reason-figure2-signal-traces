#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
NOTEBOOK = REPO / "2_analysis/scripts/signal_trace_extraction.ipynb"
TABLES = REPO / "3_results/tables"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def extract_parameters() -> dict[str, str]:
    nb = json.loads(NOTEBOOK.read_text())
    code = "\n".join(
        "".join(c.get("source", []))
        for c in nb.get("cells", [])
        if c.get("cell_type") == "code"
    )
    keys = ["F5", "BAM", "POD5_PATH", "FS", "MIN_Q", "N", "PRE", "POST"]
    out: dict[str, str] = {}
    for k in keys:
        marker = f"{k} ="
        for line in code.splitlines():
            if line.strip().startswith(marker):
                raw = line.split("=", 1)[1].strip()
                raw = re.sub(r'^[rR]([\'"])', r"\1", raw)
                out[k] = raw.strip('"').strip("'")
                break
    if "END_REASONS" in code:
        start = code.find("END_REASONS")
        segment = code[start : start + 600]
        classes = []
        for line in segment.splitlines():
            s = line.strip().strip(",")
            if s.startswith("}"):
                break
            if s.startswith('"') and s.endswith('"'):
                classes.append(s.strip('"'))
        out["END_REASONS"] = "|".join(classes)
    return out


def write_parameters_table(params: dict[str, str]) -> None:
    path = TABLES / "figure2_notebook_parameters.csv"
    rows = [{"parameter": k, "value": v} for k, v in sorted(params.items())]
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["parameter", "value"])
        w.writeheader()
        w.writerows(rows)


def write_asset_manifest() -> None:
    assets = [
        ("3_results/figures/Figure_2_final.pdf", "final_pdf", "manual_illustrator_export"),
        ("3_results/figures/Figure_2_final.svg", "final_svg", "manual_illustrator_export"),
        ("3_results/figures/Figure_2_final@4x.png", "final_png", "manual_illustrator_export"),
        ("3_results/figures/Figure_2_final.ai", "illustrator_master", "manual_illustrator_source"),
        ("3_results/figures/Figure_2_draft_2026-06-03.pdf", "draft_pdf", "historical_draft"),
        ("3_results/figures/Figure_2_draft_2026-06-03.svg", "draft_svg", "historical_draft"),
        ("3_results/figures/Figure_2_draft_2026-06-03@4x.png", "draft_png", "historical_draft"),
    ]
    rows = []
    for rel, role, provenance in assets:
        p = REPO / rel
        rows.append(
            {
                "artifact_path": rel,
                "role": role,
                "lineage": provenance,
                "bytes": p.stat().st_size,
                "sha256": sha256(p),
            }
        )
    path = TABLES / "figure2_asset_manifest.csv"
    with path.open("w", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["artifact_path", "role", "lineage", "bytes", "sha256"],
        )
        w.writeheader()
        w.writerows(rows)


def write_table_manifest() -> None:
    rows = [
        {
            "table_path": "3_results/tables/figure2_asset_manifest.csv",
            "description": "Checksums and lineage for final + draft figure assets",
            "regenerates_with": "python3 2_analysis/scripts/build_result_tables.py",
        },
        {
            "table_path": "3_results/tables/figure2_notebook_parameters.csv",
            "description": "Parameters parsed from signal_trace_extraction.ipynb",
            "regenerates_with": "python3 2_analysis/scripts/build_result_tables.py",
        },
    ]
    path = TABLES / "source_table_manifest.csv"
    with path.open("w", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["table_path", "description", "regenerates_with"],
        )
        w.writeheader()
        w.writerows(rows)


def main() -> None:
    TABLES.mkdir(parents=True, exist_ok=True)
    params = extract_parameters()
    write_parameters_table(params)
    write_asset_manifest()
    write_table_manifest()
    print("Wrote 3_results/tables/{figure2_asset_manifest.csv,figure2_notebook_parameters.csv,source_table_manifest.csv}")


if __name__ == "__main__":
    main()

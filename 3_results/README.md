# 3. Results

## Contents
| Path | Description |
|---|---|
| `figures/` | Draft + final figure assets (PDF/SVG/PNG/AI) |
| `figure_legends.md` | Finalized Figure 2 legend text |
| `tables/` | Source tables with checksums, parameters, and lineage |

## Source tables with lineage
- `tables/figure2_asset_manifest.csv`: sha256 + bytes + lineage for each figure asset.
- `tables/figure2_notebook_parameters.csv`: constants parsed from notebook.
- `tables/source_table_manifest.csv`: table inventory + regeneration command.

Regenerate these tables with:
```bash
python3 2_analysis/scripts/build_result_tables.py
```

## Reproducibility status
- Final PDF/SVG/PNG/AI files are present and checksummed.
- Final layout edits are Illustrator-only and documented in `../unresolved.json`.

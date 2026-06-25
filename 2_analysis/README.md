# 2. Analysis

## Contents
| File / Folder | Description |
|---|---|
| `overview.md` | Plain-English method summary |
| `commands.md` | Reproducibility commands (local + HPC paths) |
| `scripts/signal_trace_extraction.ipynb` | Raw extraction/plotting notebook |
| `scripts/environment.yaml` | Conda environment used for analysis |
| `scripts/build_result_tables.py` | Regenerates deposited lineage/checksum tables |
| `scripts/sync_dashboard_preview.py` | Syncs dashboard preview from table-manifested final PNG |

## Reproducibility stance
- **Script-regenerable from committed files:** lineage/checksum tables + dashboard preview assets.
- **Requires raw Turbo data:** notebook rerun from bulk FAST5/BAM.
- **Requires manual Adobe Illustrator:** final publication layout exports (tracked in `unresolved.json`).

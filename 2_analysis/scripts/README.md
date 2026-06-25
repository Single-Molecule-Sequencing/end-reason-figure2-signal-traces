# Scripts

| File | Purpose |
|---|---|
| `signal_trace_extraction.ipynb` | Primary raw-data analysis notebook (FAST5/BAM → trace plots) |
| `build_result_tables.py` | Regenerates deposited source tables in `3_results/tables/` |
| `sync_dashboard_preview.py` | Syncs `figures/` and `docs/figures/` preview PNG from manifest |
| `environment.yaml` | Reproducible conda environment specification |

Run order for local reproducibility:
```bash
python3 2_analysis/scripts/build_result_tables.py
python3 2_analysis/scripts/sync_dashboard_preview.py
```

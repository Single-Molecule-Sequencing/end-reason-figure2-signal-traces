# Commands — Reproducibility Paths

This repo has two supported paths:

1. **Deposited-artifact path (no HPC)**: rebuild lineage/checksum tables and sync dashboard previews from committed files.
2. **Full raw-data path (HPC)**: re-run bulk FAST5 extraction notebook, then manually re-export Illustrator outputs.

## A) Deposited-artifact path (fast, local)

```bash
cd /path/to/end-reason-figure2-signal-traces
python3 2_analysis/scripts/build_result_tables.py
python3 2_analysis/scripts/sync_dashboard_preview.py
```

Outputs regenerated from deposited artifacts/tables:
- `3_results/tables/figure2_asset_manifest.csv`
- `3_results/tables/figure2_notebook_parameters.csv`
- `3_results/tables/source_table_manifest.csv`
- `figures/fig2_signal_traces.png`
- `docs/figures/fig2_signal_traces.png`

## B) Full raw-data path (HPC + manual Illustrator)

```bash
ssh <uniqname>@greatlakes.arc-ts.umich.edu
srun --partition=standard --cpus-per-task=4 --mem=32G --pty bash
conda activate atheylab
cd /nfs/turbo/umms-atheylab/<path>/end-reason-figure2-signal-traces
jupyter nbconvert --to notebook --execute \
    2_analysis/scripts/signal_trace_extraction.ipynb \
    --output 2_analysis/scripts/signal_trace_extraction.executed.ipynb
```

Manual (not currently script-regenerable): open matplotlib output in Illustrator and export:
- `3_results/figures/Figure_2_final.pdf`
- `3_results/figures/Figure_2_final.svg`
- `3_results/figures/Figure_2_final@4x.png`
- `3_results/figures/Figure_2_final.ai`

See `unresolved.json` for explicit non-regenerable elements.

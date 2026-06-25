# Happy Path — Figure 2 Reproducibility

## Path A: from committed artifacts (no HPC)
```bash
cd /path/to/end-reason-figure2-signal-traces
python3 2_analysis/scripts/build_result_tables.py
python3 2_analysis/scripts/sync_dashboard_preview.py
```
Expected outputs:
- `3_results/tables/figure2_asset_manifest.csv`
- `3_results/tables/figure2_notebook_parameters.csv`
- `3_results/tables/source_table_manifest.csv`
- `figures/fig2_signal_traces.png`
- `docs/figures/fig2_signal_traces.png`

## Path B: full scientific rerun (HPC + manual)
```bash
ssh <uniqname>@greatlakes.arc-ts.umich.edu
srun --partition=standard --cpus-per-task=4 --mem=32G --pty bash
conda activate atheylab
cd /nfs/turbo/umms-atheylab/<path>/end-reason-figure2-signal-traces
jupyter nbconvert --to notebook --execute \
  2_analysis/scripts/signal_trace_extraction.ipynb \
  --output 2_analysis/scripts/signal_trace_extraction.executed.ipynb
```
Then export final publication assets from Illustrator (`Figure_2_final.*`).

## Known unresolved items
See `unresolved.json` for the explicit non-regenerable/manual components.

# Analysis Overview — Plain English

## Goal
Show raw nanopore current traces at read termination for each end-reason class used in Figure 2.

## What the notebook does
1. Loads bulk FAST5 (`IntermediateData/*/Reads`) and reconstructs reads from partial rows.
2. Decodes end-reason enum values from FAST5 metadata.
3. Loads BAM Q-scores (`qs` tag fallback to mean base quality).
4. Filters reads by quality (`MIN_Q = 10`).
5. Selects representative reads per class (`N = 10`) for plotting.
6. Extracts calibrated pA signal and renders matplotlib panels.

## Classes currently configured in notebook
- `signal_positive`
- `signal_negative`
- `unblock_mux_change`
- `mux_change`

## Inputs/parameters provenance
Run:
```bash
python3 2_analysis/scripts/build_result_tables.py
```
This writes `3_results/tables/figure2_notebook_parameters.csv`, parsed directly from the committed notebook constants.

## Manual finishing step
Final publication assets were refined/exported in Illustrator; those manual operations are tracked in `unresolved.json` and are the remaining barrier to full script-only regeneration.

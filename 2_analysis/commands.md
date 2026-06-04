# Commands — How to Run the Analysis

Run these in order to reproduce the figure from scratch.

> ⚠️ **HPC required.** The raw FAST5 input lives on Turbo and is only accessible
> from a Great Lakes compute node. Run from a GL allocation
> (`srun --partition=standard --cpus-per-task=4 --mem=32G --pty bash`).

---

## 0. Prerequisites

```bash
# SSH to Great Lakes
ssh <uniqname>@greatlakes.arc-ts.umich.edu

# Get an interactive allocation (if not already in one)
srun --partition=standard --cpus-per-task=4 --mem=32G --pty bash

# Activate the lab environment
conda activate atheylab

# Verify key packages are importable
python -c "import h5py, vbz_h5py_plugin, pysam, pod5, numpy, matplotlib, pandas; print('All imports OK')"
```

---

## 1. Run the signal extraction notebook

This opens the bulk FAST5, groups reads by end-reason class, filters by Q-score,
and produces raw matplotlib signal trace panels.

```bash
cd /path/to/end-reason-figure2-signal-traces

jupyter nbconvert --to notebook --execute \
    2_analysis/scripts/signal_trace_extraction.ipynb \
    --output 2_analysis/scripts/signal_trace_extraction.executed.ipynb
```

**Output:** raw signal trace figure files written to `3_results/figures/raw_output/`  
**Runtime:** ~5–15 minutes depending on FAST5 size and allocation CPUs

---

## 2. Record the provenance run

After executing, stamp the run so this figure has a traceable lineage:

```bash
lab-analysis record-run \
    --figure fig2_signal_traces \
    --command "jupyter nbconvert --to notebook --execute 2_analysis/scripts/signal_trace_extraction.ipynb" \
    --output 3_results/figures/Figure_2_final.pdf \
    --output 3_results/figures/Figure_2_final.png
```

---

## 3. (Manual) Illustrator refinements

Open `3_results/figures/raw_output/` in Adobe Illustrator, apply final
typographic/layout refinements, and export as:
- `3_results/figures/Figure_2_final.pdf`
- `3_results/figures/Figure_2_final.svg`
- `3_results/figures/Figure_2_final@4x.png`

Commit the exported files.

---

## 4. Verify the happy path

```bash
# From repo root
lab-analysis verify-happy-path
```

See [`HAPPY_PATH.md`](../HAPPY_PATH.md) for the full end-to-end narrative.

# Happy Path — End-to-End Reproduce Guide

This document is your **single source of truth** for reproducing Figure 2 from
scratch. Follow these steps in order. Each step links to the relevant files.

> ⚠️ **HPC required for steps 1–3.** The bulk FAST5 lives on Turbo.
> Steps 4–5 can be done anywhere once you have the output files.

---

## Step 0 — Prerequisites

1. Access to Great Lakes HPC with an active `umms-atheylab` allocation
2. `conda activate atheylab` (or equivalent with the packages in [`2_analysis/overview.md`](2_analysis/overview.md))
3. This repo cloned locally (or on Turbo)

---

## Step 1 — Confirm the raw data is accessible

```bash
# Should list the bulk FAST5
ls /nfs/turbo/umms-atheylab/gregfar/SMS/SMS_POP_data/\
Single_Molecule_Seqeuncing_Cutting_Res_E/Regular/20250519_1041_MN48328_AYJ384_c3faa65
```

📂 More details: [`1_experiment/raw_data/README.md`](1_experiment/raw_data/README.md)

---

## Step 2 — Confirm basecalled data is accessible

```bash
# Should list the BAM file used for Q-score filtering
ls <path/to/basecalled.bam>   # see 1_experiment/basecalled_data/README.md
```

📂 More details: [`1_experiment/basecalled_data/README.md`](1_experiment/basecalled_data/README.md)  
🔧 How it was produced: [`1_experiment/dorado_commands.md`](1_experiment/dorado_commands.md)

---

## Step 3 — Run the analysis notebook

```bash
conda activate atheylab

jupyter nbconvert --to notebook --execute \
    2_analysis/scripts/signal_trace_extraction.ipynb \
    --output 2_analysis/scripts/signal_trace_extraction.executed.ipynb
```

📖 What the notebook does (plain English): [`2_analysis/overview.md`](2_analysis/overview.md)  
🔧 Full command details: [`2_analysis/commands.md`](2_analysis/commands.md)

**Expected output:** matplotlib signal trace figures written to `3_results/figures/raw_output/`

---

## Step 4 — Apply Illustrator refinements (manual)

Open the raw output in Adobe Illustrator, apply typographic and layout
refinements, export as:

```
3_results/figures/Figure_2_final.pdf
3_results/figures/Figure_2_final.svg
3_results/figures/Figure_2_final@4x.png
```

The current polished draft is already committed (see [`3_results/figures/`](3_results/figures/)).

---

## Step 5 — Verify and record

```bash
# Record the provenance run (stamps the figure atom with lineage)
lab-analysis record-run \
    --figure fig2_signal_traces \
    --command "jupyter nbconvert --to notebook --execute 2_analysis/scripts/signal_trace_extraction.ipynb" \
    --output 3_results/figures/Figure_2_final.pdf

# Check current maturity status
lab-analysis status
```

📋 Results: [`3_results/README.md`](3_results/README.md)  
📖 Figure legend: [`3_results/figure_legends.md`](3_results/figure_legends.md)

---

## Provenance trail

Every artifact-producing run is logged in [`provenance/runs.jsonl`](provenance/runs.jsonl).
This file is committed to git and is the **durable source of truth** for this
figure's lineage. Inspect it with:

```bash
lab-analysis status --provenance
```

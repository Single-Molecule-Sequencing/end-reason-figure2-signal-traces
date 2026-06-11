# End-Reason Figure 2 — Raw Signal Traces by End-Reason Class

<!-- LAB:DASHBOARD-BADGE BEGIN -->
📊 **[Live dashboard](https://single-molecule-sequencing.github.io/end-reason-figure2-signal-traces/)**
<!-- LAB:DASHBOARD-BADGE END -->


**Paper:** End-reason filtering in single-molecule sequencing of native DNA (Oxford Nanopore)  
**Figure:** Figure 2  
**What this shows:** Raw pA electrical signal traces from 10 representative reads per
end-reason class, extracted directly from a bulk FAST5 file. Demonstrates what the
electrical signal looks like at the moment sequencing terminates for each class.

---

## How this repo is organized

| Folder | What's inside |
|---|---|
| [`1_experiment/`](1_experiment/README.md) | Sequencing run details, dorado basecalling commands, pointers to raw and basecalled data |
| [`2_analysis/`](2_analysis/README.md) | Scripts, commands to run them, plain-English explanation of what the code does |
| [`3_results/`](3_results/README.md) | Polished figures and figure legends |
| [`HAPPY_PATH.md`](HAPPY_PATH.md) | Full end-to-end reproduce walkthrough (experiment → analysis → figure) |
| [`provenance/runs.jsonl`](provenance/runs.jsonl) | Append-only log of every run that produced an artifact in this repo |
| [`analysis.yaml`](analysis.yaml) | Lab system manifest (links this repo into the lab paper pipeline) |

## Quick start — reproduce the figure

> ⚠️ The raw FAST5 input lives on Athey Lab Turbo (Great Lakes HPC). You need
> an active `umms-atheylab` allocation to reproduce from scratch.

```bash
# 1. Clone this repo
git clone https://github.com/Single-Molecule-Sequencing/end-reason-figure2-signal-traces
cd end-reason-figure2-signal-traces

# 2. Activate the lab Python environment
conda activate atheylab

# 3. Run the signal extraction notebook
jupyter nbconvert --to notebook --execute \
    2_analysis/scripts/signal_trace_extraction.ipynb
```

See [`HAPPY_PATH.md`](HAPPY_PATH.md) for the full annotated walkthrough.

## Current status

- **Draft date:** 2026-06-03
- **Status:** Near-complete draft — signal traces extracted; Illustrator refinements applied
- **Next step:** Final sign-off, then harvest into end-reason-fresh paper repo

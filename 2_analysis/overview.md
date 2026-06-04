# Analysis Overview — Plain English

This document explains **what the analysis code does and why**, without requiring
you to read the notebook. Think of it as the methods section in plain language.

---

## Goal

Produce a figure showing what the raw nanopore electrical signal looks like at
the moment sequencing ends for each end-reason class. Each end-reason class
(e.g., `signal_positive`, `signal_negative`, `signal_with_strand`,
`unblock_mux_change`, `mux_change`, `data_service_unblock_mux_change`)
tells you *why* the sequencer stopped recording a read.

## Step-by-step logic

### Step 1 — Open the bulk FAST5

The raw data lives in a **bulk FAST5** file. Unlike per-read FAST5/POD5 files,
the bulk FAST5 has an internal HDF5 table called `IntermediateData/Reads` (one
per channel) that records real-time sequencer events: for each read, there are
one or more rows capturing partial signal segments, a `read_start`, a
`read_length`, and (critically) an `end_reason` code.

We use the `h5py` library to read this table directly, along with the
`vbz_h5py_plugin` to decompress VBZ-compressed signal arrays.

### Step 2 — Reconstruct reads from partial rows

A single read spans **multiple consecutive rows** in the `IntermediateData/Reads`
table — all sharing the same `read_id`. Non-terminal rows are marked `partial`.
We group all rows by `read_id` to reconstruct each complete read.

The read's end reason is taken from the **last row** of its group (the terminal
row). Its full signal extent runs from `read_start` of the first row to
`read_start + read_length` of the last row.

### Step 3 — Filter by quality score

We load the basecalled BAM file and look up each read's Q-score using pysam.
The code first checks for the `qs` tag (dorado's native read-level quality score),
then falls back to computing mean base quality from `query_qualities`. Reads
below the quality threshold are excluded.

### Step 4 — Select 10 representative reads per class

For each end-reason class, we randomly sample 10 reads that pass the quality
filter. This gives a manageable number of traces to visualize without cherry-picking.

### Step 5 — Extract and plot raw pA signal

For each selected read, we extract the raw signal array from the FAST5 and
convert it to picoamperes (pA) using the channel calibration metadata (offset
and range). We then plot these traces using matplotlib, one panel per end-reason
class.

### Step 6 — Illustrator refinements (manual step)

The raw matplotlib output was imported into Adobe Illustrator for final
typographic and visual refinements. The Illustrator output is the polished draft
committed in [`3_results/figures/`](../3_results/figures/).

---

## Dependencies

| Library | Purpose |
|---|---|
| `h5py` | Read the bulk FAST5 HDF5 file |
| `vbz_h5py_plugin` | Decompress VBZ-compressed signal arrays in the FAST5 |
| `pysam` | Read the basecalled BAM to extract Q-scores |
| `pod5` | Verification / cross-referencing (not primary read path) |
| `numpy` | Signal arithmetic (offset/range calibration) |
| `matplotlib` | Plotting the signal traces |
| `pandas` | Grouping and filtering the reads table |

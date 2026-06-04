# Dorado Basecalling Commands

These are the **exact commands** used to basecall the raw signal data into reads.
Copy-paste these to reproduce the basecalled BAM files from the raw FAST5/POD5.

---

## Prerequisites

```bash
# Activate the lab environment
conda activate atheylab

# Confirm dorado version (should match what was used originally)
dorado --version
```

---

## Basecalling command(s)

<!-- TODO: Fill in the actual dorado command(s) used for this run. -->

```bash
# [PLACEHOLDER — replace with the actual command]
dorado basecaller \
    <model> \
    <path/to/raw/pod5_or_fast5> \
    --reference <reference.fa> \
    > basecalled.bam
```

**Model used:** [?] (e.g., `dna_r10.4.1_e8.2_400bps_sup@v4.3.0`)  
**Reference:** [?]  
**Output:** see [`basecalled_data/`](basecalled_data/README.md)

---

## Notes

<!-- Any flags, filters, or post-processing steps applied after the main basecall command -->

# 1. Experiment

This section documents everything about **how the sequencing data was generated**:
the physical sequencing run, the exact basecalling commands used to convert raw
signal to reads, and where the resulting data files live.

---

## Contents

| File / Folder | Description |
|---|---|
| [`run_details.md`](run_details.md) | Sequencing run metadata (flow cell, kit, date, MinKNOW version) |
| [`dorado_commands.md`](dorado_commands.md) | Exact dorado basecalling commands, in the order they were run |
| [`raw_data/`](raw_data/README.md) | Pointers to raw FAST5/POD5 files on Turbo |
| [`basecalled_data/`](basecalled_data/README.md) | Pointers to basecalled BAM/FASTQ output on Turbo |

## What was the experiment?

This data comes from a **single-molecule sequencing run** on an Oxford Nanopore
MinION device. 

The raw signal data is stored in a **bulk FAST5 file**, which contains the
`IntermediateData` table — this records the raw signal and metadata for every read
at the time it was processed by the sequencer, including its end reason. This bulk
FAST5 format is what allows us to extract the raw signal before, during, and after the read allowing for a comprehensive picture.

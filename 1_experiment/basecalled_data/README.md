# Basecalled Data

Output of running dorado on the raw POD5. Also lives on Turbo — not
committed to this repo.

---

## What exists

| File type | Description |
|---|---|
| **BAM** | Unaligned basecalled reads. Used by the analysis notebook to look up read Q-scores via the `qs` tag. |

## Where it lives

<!-- TODO: Fill in the actual path to the basecalled BAM on Turbo -->
```
/nfs/turbo/umms-atheylab/hrli/Code/dorado-run/Output/20250519_1041_MN48328_AYJ384_c3faa658_sup_v5.2.0_trim1_10.bam
```

## How it was produced

See [`../dorado_commands.md`](../dorado_commands.md) for the exact commands.

## Notes

The analysis notebook (`2_analysis/scripts/signal_trace_extraction.ipynb`) reads
the BAM to extract per-read Q-scores. It uses pysam and looks for the `qs` tag
(dorado's read-level quality score).

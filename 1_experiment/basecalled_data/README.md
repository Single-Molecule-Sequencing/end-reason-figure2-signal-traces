# Basecalled Data

Output of running dorado on the raw FAST5/POD5. Also lives on Turbo — not
committed to this repo.

---

## What exists

| File type | Description |
|---|---|
| **BAM** | Aligned basecalled reads. Used by the analysis notebook to look up read Q-scores via the `qs` tag (dorado/ONT style) or mean base quality. |

## Where it lives

<!-- TODO: Fill in the actual path to the basecalled BAM on Turbo -->
```
/nfs/turbo/umms-atheylab/gregfar/SMS/...  [path TBD]
```

## How it was produced

See [`../dorado_commands.md`](../dorado_commands.md) for the exact commands.

## Notes

The analysis notebook (`2_analysis/scripts/signal_trace_extraction.ipynb`) reads
the BAM to extract per-read Q-scores. It uses pysam and looks for the `qs` tag
(dorado's read-level quality score) or falls back to mean base quality from
`query_qualities`.

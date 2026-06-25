# Basecalled Data

Basecalled BAM used by the analysis notebook (not committed in this repo):

```text
/nfs/turbo/umms-atheylab/hrli/Code/dorado-run/Output/20250519_1041_MN48328_AYJ384_c3faa658_sup_v5.2.0_trim1_10.bam
```

## Usage in this repo
`2_analysis/scripts/signal_trace_extraction.ipynb` reads this BAM with `pysam` and applies a read-level quality filter (`MIN_Q=10`) using `qs` tags when present.

Exact original Dorado CLI invocation is not in committed provenance and is tracked in `../unresolved.json`.

# Raw Data

The raw sequencing data is **not committed to this repo** — the files are large
(bulk FAST5) and live on Athey Lab Turbo storage on Great Lakes HPC.

---

## What exists

| File type | Description |
|---|---|
| **Bulk FAST5** | Contains `IntermediateData/Reads` — raw pA signal + end-reason metadata for every read, as recorded by the sequencer in real time |

## Path

```
/nfs/turbo/umms-atheylab/gregfar/SMS/SMS_POP_data/Single_Molecule_Seqeuncing_Cutting_Res_E/Regular/20250519_1041_MN48328_AYJ384_c3faa658/rdlu0053_20250519_1046_AYJ384_MN48328_sequencing_run_Regular_c3faa658_2e5a2515.fast5 
```

**Access:** Great Lakes HPC only. Requires active `umms-atheylab` allocation.

## Why bulk FAST5?

The bulk FAST5 format records **real-time sequencer output**, including the
`IntermediateData` table that stores each read's end reason as assigned by the
MinKNOW software. This is distinct from per-read FAST5/POD5 files produced after
segmentation — those don't carry the complete signal for each channel.
We need the bulk FAST5 specifically to extract
the raw signal before, during, and after each read segmentation to provide a complete picture of the signal level behavior of each end reason.

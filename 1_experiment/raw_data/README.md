# Raw Data

The raw sequencing data is **not committed to this repo** — the files are large
(bulk FAST5) and live on Athey Lab Turbo storage on Great Lakes HPC.

---

## What exists

| File type | Description |
|---|---|
| **Bulk FAST5** | Contains `IntermediateData/Reads` — raw pA signal + end-reason metadata for every read, as recorded by the sequencer in real time |

## Where it lives

```
/nfs/turbo/umms-atheylab/gregfar/SMS/SMS_POP_data/
  Single_Molecule_Seqeuncing_Cutting_Res_E/
    Regular/
      20250519_1041_MN48328_AYJ384_c3faa65   ← bulk FAST5
```

**Access:** Great Lakes HPC only. Requires active `umms-atheylab` allocation.

## Why bulk FAST5?

The bulk FAST5 format records **real-time sequencer output**, including the
`IntermediateData` table that stores each read's end reason as assigned by the
MinKNOW software. This is distinct from per-read FAST5/POD5 files produced after
basecalling — those don't carry the intermediate signal in the same accessible way.
We need the bulk FAST5 specifically to extract end-reason assignments alongside
the raw pA signal for the same read.

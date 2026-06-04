# 2. Analysis

This section contains the **code that turns raw data into figures**, along with
plain-English explanations of what the code does and how to run it.

---

## Contents

| File / Folder | Description |
|---|---|
| [`overview.md`](overview.md) | Plain-English walkthrough of the analysis logic (no code) |
| [`commands.md`](commands.md) | Exact commands to run each script, in order |
| [`scripts/`](scripts/) | The actual code (Jupyter notebook) |

## One-line summary

The analysis opens a bulk FAST5 file, groups the raw signal records by read ID to
reconstruct each read, assigns each read its end reason (the last recorded row for
that read), filters by quality score, then selects 10 representative reads per
end-reason class and plots their raw pA signal traces.

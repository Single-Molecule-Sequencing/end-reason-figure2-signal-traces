# End-Reason Figure 2 — Raw Signal Traces by End-Reason Class

> 📄 Companion repository for the **End Reason** Data Descriptor — canonical manuscript: [Single-Molecule-Sequencing/end_reason_6_5_26](https://github.com/Single-Molecule-Sequencing/end_reason_6_5_26).


📊 **Live dashboard:** https://sturdy-adventure-925pgyg.pages.github.io/

Companion analysis repo for Figure 2 of the end-reason manuscript.

## Structure
- `1_experiment/` — run metadata + data location pointers
- `2_analysis/` — commands, overview, scripts, environment
- `3_results/` — final figure assets, legend, source tables
- `provenance/` — append-only run log
- `docs/index.html` — Pages dashboard
- `analysis.yaml` — repo manifest
- `HAPPY_PATH.md` — end-to-end reproducibility walkthrough

## Reproducibility status (strict)
- ✅ Final figure files present: PDF/SVG/PNG (+ AI source)
- ✅ Source tables with lineage/checksums in `3_results/tables/`
- ✅ Local table-driven regeneration path documented (`2_analysis/commands.md`)
- ⚠ Full raw-data rerun needs Turbo HPC access
- ⚠ Illustrator-only edits are non-regenerable; tracked in `unresolved.json`

This repo is intentionally explicit about unresolved steps; no missing values are fabricated.

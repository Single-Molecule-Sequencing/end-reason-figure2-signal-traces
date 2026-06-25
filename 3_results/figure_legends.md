# Figure 2 Legend

**Figure 2. Raw pA signal traces by end-reason class.**
Raw ionic current (picoamperes, pA) recorded by an Oxford Nanopore MinION device for representative reads in four end-reason classes (`signal_positive`, `signal_negative`, `unblock_mux_change`, `mux_change`). Traces are aligned to read start and extend to read termination, where MinKNOW assigns end reason. Signal was extracted from the bulk FAST5 `IntermediateData/*/Reads` datasets and calibrated to pA using per-channel metadata (`offset`, `range`, `digitisation`). Read selection in the committed notebook uses `MIN_Q = 10` and `N = 10` per class (see `3_results/tables/figure2_notebook_parameters.csv`).

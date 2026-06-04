# Figure 2 Legend

<!-- TODO: Finalize the figure legend text for submission. The draft below
     reflects the current interpretation — update once co-authors have reviewed. -->

**Figure 2. Raw pA signal traces by end-reason class.**
Raw ionic current (picoamperes, pA) recorded by an Oxford Nanopore MinION device
for 10 representative reads per end-reason class. Each panel shows traces for one
class: [*list classes here, e.g. signal_positive, signal_negative, mux_change,
unblock_mux_change, signal_with_strand, data_service_unblock_mux_change*].
Traces are aligned to the read start and extend to the point at which the
sequencer assigned the end-reason classification. Raw signal was extracted
from the bulk FAST5 `IntermediateData` table and converted to pA using
per-channel calibration metadata (offset and range). Reads were selected by
randomly sampling 10 per class from reads passing a Q-score threshold of [?].

---

## Notes for revision

- [ ] Confirm the exact list of end-reason classes shown and their display order
- [ ] Confirm Q-score threshold used in the sampling
- [ ] Confirm pA calibration formula (offset / range values)
- [ ] Add panel labels (A, B, C...) if the journal requires them

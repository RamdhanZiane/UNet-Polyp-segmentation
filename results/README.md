# Experiment outputs

Create a new directory per experiment, such as `<timestamp>_<commit>/`.
No experimental results exist yet.

Each experiment should retain:

- Resolved config, seed, commit hash, split hashes, environment and hardware.
- Data audit, grouping summary, and training-derived size cutoffs.
- Initialization hash and per-run epoch logs/curves.
- Checkpoint paths/hashes and validation-selected frozen thresholds.
- Final per-image and summary metrics, timing, paired statistics, and
  size-stratified and qualitative error analysis.

Persist official artifacts to Drive. Keep small logs, tables and figures
in git; weights belong in Drive or local `checkpoints/`. Do not overwrite
prior results. Final test outputs are produced once per model through
the same evaluation script.

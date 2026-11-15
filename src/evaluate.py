"""TODO: single final evaluation entry point for both frozen models.

Require selected checkpoints and frozen validation thresholds. Save test
metrics, paired bootstrap intervals (A minus B), Wilcoxon test, error
analysis, and warm-up/synchronized inference timing excluding disk I/O.
Guard against accidental repeat evaluation; never tune using its outputs.
"""

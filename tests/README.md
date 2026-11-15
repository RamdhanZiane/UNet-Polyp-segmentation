# Planned checks

Tests will be added with the corresponding implementation:

- Filename pairing and missing-mask detection.
- Binary masks and nearest-neighbour mask resizing.
- Paired augmentation and no augmentation on validation/test.
- Exact split counts, no overlap, group isolation, and frozen-file hashes.
- Losses and metrics on known masks and against a reference implementation.
- Identical initial weights and shared settings across both loss runs.
- Tiny CPU training smoke test using synthetic data, never official test data.
- Validation-only checkpoint/threshold selection and final-evaluation guard.

No tests or pipeline behavior are implemented yet.

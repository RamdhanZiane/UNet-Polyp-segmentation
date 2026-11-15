# Polyp Segmentation with U-Net

Binary segmentation of polyps in endoscopic images using a compact U-Net and the [Kvasir-SEG dataset](https://datasets.simula.no/kvasir-seg/). The aim is to identify polyp regions at the pixel level and study how the training loss affects segmentation quality, especially when polyps occupy a small part of the image.

## Research question

Does adding soft Dice loss to binary cross-entropy improve polyp segmentation compared with binary cross-entropy alone?

The planned comparison uses two loss configurations:

| Run | Loss |
| --- | --- |
| A | Binary cross-entropy (`BCEWithLogitsLoss`) |
| B | Binary cross-entropy + soft Dice loss |

Both runs use the same U-Net architecture, initial weights, data splits, augmentations, and training settings so that only the loss changes.

## Approach

- Train a compact U-Net from scratch with PyTorch, targeting Google Colab.
- Pair images with binary masks and apply matching geometric transformations.
- Use a frozen, group-aware train/validation/test split to reduce leakage from related frames.
- Select checkpoints and prediction thresholds using validation data only.
- Evaluate once on the held-out test set using Dice, IoU, precision, recall, and inference time, with uncertainty estimates and analysis of segmentation errors.

## Repository

| Path | Purpose |
| --- | --- |
| [`config.json`](config.json) | Shared protocol and loss variants; `null` marks undecided settings |
| [`src/`](src/) | Data preparation, model, losses, training, evaluation, and viewer scaffolding |
| [`notebooks/`](notebooks/) | Colab training and viewer notebook skeletons |
| [`tests/`](tests/) | Planned correctness and protocol checks |
| `data/Kvasir-SEG/` | Local `images/` and `masks/`; gitignored |
| [`splits/`](splits/) | Frozen filename lists, grouping record, and hashes once created |
| `checkpoints/` | Local weights; gitignored; persist official weights to Drive |
| [`results/`](results/) | Versioned configs, logs, metrics, and figures |
| [`experiment.ipynb`](experiment.ipynb) | Existing exploratory notebook |
| [`report/`](report/) | Report sources |

## Development status

The pipeline and Colab notebooks are scaffolding, not runnable experiments
yet. No dataset has been downloaded, split generated, model trained, or
test evaluation performed.

Implementation order: data checks and grouping, frozen splits, paired
loader, model/losses/metrics and tests, CPU smoke test, Colab pilot, matched
training runs, validation threshold selection, then a single final
evaluation of both models and error analysis. Implement the viewer using
the same preprocessing and frozen thresholds.

Before official training, resolve the `null` settings in `config.json`
and record protocol decisions in `AGENTS.md` and the report. Both runs
inherit the shared configuration and differ only in `loss`. Pin
`requirements.txt` after verifying the Colab environment; no dependencies
are installed by this scaffold.

Use a fresh results directory per experiment and persist splits,
checkpoints, and outputs to Google Drive. Never overwrite frozen splits
or use test data for checkpoint or threshold selection.

Training results and performance conclusions are pending. Raw dataset files are not included; obtain Kvasir-SEG from its official website and follow its usage terms.

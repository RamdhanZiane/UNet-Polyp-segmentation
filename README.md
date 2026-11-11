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

- [`experiment.ipynb`](experiment.ipynb): experiment notebook.
- [`report/`](report/): report sources.

Training results and performance conclusions are pending. Raw dataset files are not included; obtain Kvasir-SEG from its official website and follow its usage terms.

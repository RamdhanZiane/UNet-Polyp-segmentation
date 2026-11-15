"""TODO: matched training runs with validation-only model selection.

Log train/val loss, val Dice/IoU, learning rate, and epoch duration.
Select checkpoints by val Dice at 0.5; sweep and freeze thresholds on
validation after training. This module must never access the test split.
"""

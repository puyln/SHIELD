# SHIELD Method Summary

SHIELD is organized as an end-to-end NC-MRI screening pipeline.

## 1. Self-supervised Pretraining

A teacher-student masked autoencoder learns MRI representations from large-scale unlabeled multiparametric MRI. The encoder is later frozen for task-specific heads.

Key manuscript settings are recorded in `configs/pretraining.yaml`: 60% masking, two global views of 160 x 160 x 160 voxels, six local views of 96 x 96 x 96 voxels, 1,600 epochs, AdamW, and batch size 512.

## 2. Virtual DCE-MRI Generation

The generation module uses NC-MRI inputs to synthesize virtual late arterial, portal venous, and delayed phase images. The local release includes diffusion and U-Net components from the manuscript workspace under `shield/generation`.

The configuration in `configs/generation.yaml` records the two-stage generation design: phase-specific MDDM target-prior learning followed by CCG-UNet synthesis, using 1,000 diffusion steps, Adam, batch size 12, and 100 epochs.

## 3. Lesion Detection

The detection module combines NC-MRI and virtual DCE-MRI phases, predicts liver and lesion masks, and extracts lesion ROIs for downstream diagnosis.

The public configuration uses Dice loss, AdamW, batch size 4, 3,000 epochs, and evaluation with DSC, HD95, recall, and precision.

## 4. Diagnosis and Interpretation

The diagnosis module predicts lesion-level benign-malignant probabilities and LI-RADS-related imaging features. Interpretation is planned through feature attribution and representation visualization.

The diagnosis configuration uses a frozen encoder, a three-layer MLP head, 16 LI-RADS-related feature outputs, benign-malignant classification, AdamW, batch size 4, and 1,000 epochs.

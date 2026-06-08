# SHIELD Method Summary

SHIELD is organized as an end-to-end NC-MRI screening pipeline.

## 1. Self-supervised Pretraining

A teacher-student masked autoencoder learns MRI representations from large-scale unlabeled multiparametric MRI. The encoder is later frozen for task-specific heads.

## 2. Virtual DCE-MRI Generation

The generation module uses NC-MRI inputs to synthesize virtual late arterial, portal venous, and delayed phase images. The local release includes diffusion and U-Net components from the manuscript workspace under `shield/generation`.

## 3. Lesion Detection

The detection module combines NC-MRI and virtual DCE-MRI phases, predicts liver and lesion masks, and extracts lesion ROIs for downstream diagnosis.

## 4. Diagnosis and Interpretation

The diagnosis module predicts lesion-level benign-malignant probabilities and LI-RADS-related imaging features. Interpretation is planned through feature attribution and representation visualization.


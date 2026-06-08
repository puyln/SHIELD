# Diagnosis

The diagnosis module operates on lesion-level ROI volumes. It maps encoder representations to LI-RADS-related imaging features and then to benign-malignant probabilities.

Expected outputs:

- Lesion-level malignancy probability.
- Imaging-feature predictions.
- Patient-level aggregation.
- Interpretability artifacts such as SHAP feature importance and embedding visualizations.

The manuscript configuration is recorded in `configs/diagnosis.yaml`: frozen encoder, three-layer MLP head, 16 LI-RADS-related feature outputs, benign-malignant classification, AdamW, batch size 4, and 1,000 epochs.

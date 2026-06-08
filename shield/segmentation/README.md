# Segmentation

The detection module uses NC-MRI and SHIELD-generated virtual DCE-MRI as inputs. It follows a SwinUNETR-style design with a hierarchical transformer encoder, skip connections, and an upsampling decoder for liver and lesion masks.

The final released implementation should expose:

- Multi-sequence 3D MRI loading.
- Liver and lesion mask prediction.
- Lesion ROI extraction from predicted masks.
- Detection metrics including DSC, recall, precision, and IoU-thresholded localization.

The manuscript configuration is recorded in `configs/segmentation.yaml`: Dice loss, AdamW, batch size 4, 3,000 epochs, and DSC/HD95/recall/precision evaluation.

MONAI SwinUNETR is the main public reference implementation for this module.

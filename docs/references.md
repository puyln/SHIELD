# Public References Used To Organize This Repository

## DINOv2

Repository: https://github.com/facebookresearch/dinov2

DINOv2 provides a public reference for self-supervised visual representation learning. The SHIELD code project uses it as background for robust encoder pre-training and feature-transfer design.

## MONAI SwinUNETR

Repository: https://github.com/Project-MONAI/research-contributions/tree/main/SwinUNETR

SwinUNETR provides a public reference for transformer-based 3D medical image segmentation and self-supervised pre-training in volumetric imaging.

## Diffusion Utilities

Parts of `shield/generation/guided_diffusion` follow OpenAI guided-diffusion and improved-diffusion style implementations. Parts of `shield/generation/cdm` follow latent-diffusion style configuration and DDPM/DDIM utilities. These files are retained as implementation references for the SHIELD virtual DCE-MRI generation module and are documented in `THIRD_PARTY_NOTICES.md`.

## HCC Screening and MRI AI Context

The SHIELD paper targets non-contrast MRI screening for high-risk populations, virtual contrast-enhanced MRI generation, automated lesion detection, and interpretable benign-malignant diagnosis. Public literature in this area includes AI-assisted abbreviated/non-contrast MRI and deep learning approaches for HCC diagnosis and surveillance.

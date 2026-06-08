# Third-Party Notices

This repository contains SHIELD project code together with implementation patterns adapted from public research code. The following notices are provided for reuse and redistribution review.

## OpenAI Diffusion Implementations

Files under `shield/generation/guided_diffusion/` and selected diffusion utilities under `shield/generation/cdm/` follow implementation patterns from OpenAI guided-diffusion and improved-diffusion style code, including beta schedules, timestep embeddings, residual U-Net blocks, DDPM/DDIM sampling utilities, logging helpers, and mixed-precision helpers.

Relevant upstream repositories:

- https://github.com/openai/guided-diffusion
- https://github.com/openai/improved-diffusion

## Latent Diffusion Style Utilities

Files under `shield/generation/cdm/` use configuration-driven model instantiation and DDPM/DDIM organization similar to latent diffusion style research code.

Relevant upstream repository:

- https://github.com/CompVis/latent-diffusion

## External References Not Vendored

DINOv2 and MONAI SwinUNETR are referenced by the SHIELD manuscript and documentation, but their source code and model weights are not vendored in this repository.

- https://github.com/facebookresearch/dinov2
- https://github.com/Project-MONAI/research-contributions/tree/main/SwinUNETR

Users should review the upstream licenses before combining this code with those projects or redistributing derived code and model weights.

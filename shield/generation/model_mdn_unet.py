"""Factories for SHIELD cross-conditional generative U-Net components."""

from __future__ import annotations

from pathlib import Path

import torch
from omegaconf import OmegaConf

from shield.generation.cdm.mdn.models.diffusion.ddim import DDIMSampler
from shield.generation.cdm.mdn.util import instantiate_from_config
from shield.generation.guided_diffusion.unet_mdn import UNetModel


def build_mddm_sampler(
    config_path: str | Path = "shield/generation/config.yaml",
    checkpoint_path: str | Path | None = None,
    map_location: str = "cpu",
):
    """Build a DDIM sampler for the MDDM prior and optionally load weights."""
    config = OmegaConf.load(config_path)
    mddm_model = instantiate_from_config(config.model)
    if checkpoint_path is not None:
        state = torch.load(checkpoint_path, map_location=map_location)
        if "state_dict" in state:
            state = state["state_dict"]
        mddm_model.load_state_dict(state, strict=False)
    return DDIMSampler(model=mddm_model)


def build_cross_conditional_unet(
    image_size: int = 256,
    in_channels: int = 2,
    model_channels: int = 96,
    out_channels: int = 2,
):
    """Build the CCG-UNet used to synthesize virtual DCE-MRI phases."""
    return UNetModel(
        image_size=image_size,
        in_channels=in_channels,
        model_channels=model_channels,
        out_channels=out_channels,
        num_res_blocks=1,
        attention_resolutions=[32, 16, 8],
        channel_mult=[1, 1, 2, 2],
    )


__all__ = ["build_cross_conditional_unet", "build_mddm_sampler"]

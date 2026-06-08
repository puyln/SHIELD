"""Factory for the masked reconstruction module used during encoder pretraining."""

from __future__ import annotations

from shield.generation.guided_diffusion.unet_raw import UNetModel
from shield.generation.utils.patch_masking import mask_func


def build_masked_reconstruction_unet(
    image_size: int = 256,
    in_channels: int = 2,
    model_channels: int = 96,
    out_channels: int = 2,
):
    """Build the U-Net used for masked reconstruction experiments."""
    return UNetModel(
        image_size=image_size,
        in_channels=in_channels,
        model_channels=model_channels,
        out_channels=out_channels,
        num_res_blocks=1,
        attention_resolutions=[32, 16, 8],
        channel_mult=[1, 1, 2, 2],
    )


__all__ = ["build_masked_reconstruction_unet", "mask_func"]

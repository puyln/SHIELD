"""Factory for the MDDM latent-prior model used by SHIELD generation."""

from __future__ import annotations

from pathlib import Path

from omegaconf import OmegaConf

from shield.generation.cdm.mdn.util import instantiate_from_config


def build_mddm_model(config_path: str | Path = "shield/generation/config.yaml"):
    """Build the modality-guided disentangled diffusion model from config."""
    config = OmegaConf.load(config_path)
    return instantiate_from_config(config.model)


__all__ = ["build_mddm_model"]

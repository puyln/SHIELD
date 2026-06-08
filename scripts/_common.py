from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path

try:
    from omegaconf import OmegaConf
except ModuleNotFoundError:
    OmegaConf = None


@dataclass
class RawConfig:
    path: Path
    text: str
    manifest: str | None = None

    @property
    def data(self):
        return self


def build_parser(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--config", required=True, help="Path to a YAML configuration file.")
    parser.add_argument("--manifest", help="Optional case manifest override.")
    parser.add_argument("--dry-run", action="store_true", help="Validate inputs and print the resolved configuration.")
    return parser


def load_config(path: str, manifest: str | None = None):
    if OmegaConf is None:
        cfg_path = Path(path)
        text = cfg_path.read_text(encoding="utf-8")
        match = re.search(r"(?m)^\s*manifest:\s*(.+?)\s*$", text)
        detected_manifest = match.group(1).strip("\"'") if match else None
        return RawConfig(path=cfg_path, text=text, manifest=manifest or detected_manifest)
    cfg = OmegaConf.load(path)
    if manifest:
        cfg.data.manifest = manifest
    return cfg


def get_manifest(cfg, override: str | None = None) -> str | None:
    if override:
        return override
    data = getattr(cfg, "data", None)
    if data is not None:
        manifest = getattr(data, "manifest", None)
        if manifest:
            return manifest
    return getattr(cfg, "manifest", None)


def validate_manifest(path: str | None) -> int:
    if not path:
        return 0
    manifest = Path(path)
    if not manifest.exists():
        raise FileNotFoundError(f"Manifest not found: {manifest}")
    count = 0
    with manifest.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                json.loads(line)
                count += 1
    return count


def print_config(cfg) -> None:
    if isinstance(cfg, RawConfig):
        print(cfg.text)
        return
    print(OmegaConf.to_yaml(cfg, resolve=True))


def public_release_unavailable(stage: str) -> None:
    raise SystemExit(
        f"{stage} entry point is defined for reproducibility packaging, but this public "
        "release does not include patient data, trained checkpoints, or full training "
        "runners. Use --dry-run to validate configuration and manifests."
    )

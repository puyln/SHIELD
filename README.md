# SHIELD

Code project for **SHIELD: Screening system for Hepatocellular carcinoma with Intelligent Enhancement in Liver Diagnosis**.

SHIELD is an explainable AI framework for HCC screening in high-risk populations using non-contrast MRI. The system is organized around three tasks:

- Virtual DCE-MRI generation from NC-MRI.
- Liver and lesion detection/segmentation.
- Lesion-level diagnosis with imaging-feature interpretation.

This repository is structured as a clean public code base for the paper. Dataset files, clinical labels, trained checkpoints, and unreleased paper assets are not included.

## Repository Layout

```text
SHIELD-code-project/
  configs/                 Shared experiment configuration templates
  docs/                    Method notes, data format, and reference links
  examples/                Minimal example manifests
  scripts/                 Command-line entry points
  shield/
    generation/            MDDM / CCG-UNet related generation code
    pretraining/           Teacher-student MAE interface and DINOv2 notes
    segmentation/          SwinUNETR-style detection/segmentation interface
    diagnosis/             ROI diagnosis and interpretability interface
```

## Current Release Status

The repository currently provides:

- A cleaned project structure for public GitHub release.
- The local generation/diffusion code from the manuscript workspace.
- Configuration templates and command-line entry points for the SHIELD pipeline.
- Documentation describing how the paper implementation relates to DINOv2 and MONAI SwinUNETR.

The following items are intentionally not included yet:

- Patient data or imaging files.
- Model checkpoints.
- Final training logs.
- Public paper PDF and citation metadata.

## Installation

Create a Python environment and install the core dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For full 3D medical imaging experiments, install MONAI and a CUDA-enabled PyTorch build matching your system.

## Data Format

Prepare a JSONL manifest where each line describes one case:

```json
{
  "case_id": "case_0001",
  "nc_mri": {
    "t2wi": "images/case_0001/t2wi.nii.gz",
    "dwi_low": "images/case_0001/dwi_low.nii.gz",
    "dwi_high": "images/case_0001/dwi_high.nii.gz",
    "adc": "images/case_0001/adc.nii.gz",
    "in_phase": "images/case_0001/in_phase.nii.gz",
    "out_phase": "images/case_0001/out_phase.nii.gz",
    "pre_t1": "images/case_0001/pre_t1.nii.gz"
  },
  "targets": {
    "lap": "images/case_0001/lap.nii.gz",
    "pvp": "images/case_0001/pvp.nii.gz",
    "dp": "images/case_0001/dp.nii.gz",
    "liver_mask": "labels/case_0001/liver.nii.gz",
    "lesion_mask": "labels/case_0001/lesion.nii.gz",
    "diagnosis": "malignant"
  }
}
```

See [docs/data.md](docs/data.md) for details.

## Pipeline Commands

The scripts define stable command-line interfaces for the paper pipeline:

```bash
python scripts/train_pretraining.py --config configs/pretraining.yaml
python scripts/train_generation.py --config configs/generation.yaml
python scripts/train_segmentation.py --config configs/segmentation.yaml
python scripts/train_diagnosis.py --config configs/diagnosis.yaml
python scripts/infer_shield.py --config configs/inference.yaml --manifest examples/example_manifest.jsonl
```

Some training internals are release placeholders until final code and checkpoints are approved for publication.

## External References

SHIELD was organized with reference to:

- [DINOv2](https://github.com/facebookresearch/dinov2): self-supervised visual representation learning.
- [MONAI SwinUNETR](https://github.com/Project-MONAI/research-contributions/tree/main/SwinUNETR): transformer-based 3D medical image segmentation.

See [docs/references.md](docs/references.md).

## Citation

```bibtex
@article{shield2026hcc,
  title  = {Explainable AI for HCC screening in high-risk populations using NC-MRI},
  author = {Anonymous},
  year   = {2026},
  note   = {Manuscript in preparation}
}
```


# SHIELD

Code project for **SHIELD: Screening system for Hepatocellular carcinoma with Intelligent Enhancement in Liver Diagnosis**.

SHIELD is an explainable AI framework for HCC screening in high-risk populations using non-contrast MRI. The system is organized around three tasks:

1. 🧬 Virtual DCE-MRI generation from NC-MRI.
2. 🎯 Liver and lesion detection/segmentation.
3. 🔎 Lesion-level diagnosis with imaging-feature interpretation.

This repository is structured as a public project package for the SHIELD manuscript in preparation. Dataset files, clinical labels, trained checkpoints, and unreleased manuscript assets are not included.

## 1. Repository Layout

```text
SHIELD-code-project/
  configs/                 Experiment configuration templates aligned with the current manuscript draft
  docs/                    Method notes, data format, and reference links
  examples/                Minimal example manifests
  scripts/                 Command-line entry points
  shield/
    generation/            MDDM / CCG-UNet related generation code
    pretraining/           Teacher-student MAE interface and DINOv2 notes
    segmentation/          SwinUNETR-style detection/segmentation interface
    diagnosis/             ROI diagnosis and interpretability interface
```

## 2. Current Release Status

✅ The repository currently provides:

- A cleaned project structure for the public GitHub repository.
- The cleaned generation/diffusion components from the manuscript workspace.
- Configuration templates and command-line entry points for the SHIELD pipeline.
- Documentation describing how the SHIELD implementation relates to DINOv2 and MONAI SwinUNETR.

⚠️ The following items are intentionally not included:

- Patient data or imaging files.
- Model checkpoints.
- Final training logs.
- Site-specific private paths or clinical identifiers.

## 3. Installation

Create a Python environment and install the core dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For full 3D medical imaging experiments, install MONAI and a CUDA-enabled PyTorch build matching your system.

## 4. Data Format

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

## 5. Pipeline Commands

The scripts define stable command-line interfaces for the SHIELD pipeline:

```bash
python scripts/train_pretraining.py --config configs/pretraining.yaml
python scripts/train_generation.py --config configs/generation.yaml
python scripts/train_segmentation.py --config configs/segmentation.yaml
python scripts/train_diagnosis.py --config configs/diagnosis.yaml
python scripts/infer_shield.py --config configs/inference.yaml --manifest examples/example_manifest.jsonl
```

Use `--dry-run` to validate a configuration and manifest without launching training:

```bash
python scripts/train_generation.py --config configs/generation.yaml --dry-run
```

The public package does not include patient data or trained checkpoints, so end-to-end training and inference require the corresponding private dataset and checkpoint files to be supplied by the user.

## 6. Manuscript-Aligned Settings

The configuration files encode the major settings in the current manuscript draft:

- Pretraining: teacher-student MAE, 60% masking, two global views, six local views, 1,600 epochs, AdamW, batch size 512.
- Generation: phase-specific MDDM priors and CCG-UNet synthesis, 1,000 diffusion steps, Adam, batch size 12, 100 epochs.
- Segmentation: Dice loss, AdamW, batch size 4, 3,000 epochs, DSC/HD95/recall/precision evaluation.
- Diagnosis: frozen encoder with a three-layer MLP head, 16 LI-RADS-related feature outputs, benign-malignant classification, AdamW, batch size 4, 1,000 epochs.

## 7. External References

SHIELD was organized with reference to:

- [DINOv2](https://github.com/facebookresearch/dinov2): self-supervised visual representation learning.
- [MONAI SwinUNETR](https://github.com/Project-MONAI/research-contributions/tree/main/SwinUNETR): transformer-based 3D medical image segmentation.

See [docs/references.md](docs/references.md).

## 8. License and Third-Party Code

This repository is released under the MIT License. Portions of the generation module are adapted from public diffusion-model implementations; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [NOTICE.md](NOTICE.md) before reuse.

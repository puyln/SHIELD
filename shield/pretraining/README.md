# Pretraining

The current manuscript draft pre-trains a hierarchical MRI encoder with a teacher-student masked autoencoder strategy. The public project keeps this module as an integration boundary so that the final encoder implementation can be connected to:

- SHIELD's 3D MRI sequence inputs.
- DINO-style feature consistency objectives.
- Downstream frozen-encoder generation, segmentation, and diagnosis heads.

The manuscript configuration is recorded in `configs/pretraining.yaml`: 60% masking, two global views, six local views, 1,600 epochs, AdamW, and batch size 512.

DINOv2 is used as a conceptual reference for robust self-supervised representation learning, not as vendored source code in this repository.

# Data Format

SHIELD expects a case-level manifest. JSONL is recommended because it scales to multicenter cohorts and is easy to shard.

## Required NC-MRI Inputs

- `t2wi`
- `dwi_low`
- `dwi_high`
- `adc`
- `in_phase`
- `out_phase`
- `pre_t1`

## Optional Training Targets

- Virtual contrast targets: `lap`, `pvp`, `dp`
- Segmentation targets: `liver_mask`, `lesion_mask`
- Diagnosis target: `diagnosis`
- Imaging-feature labels for LI-RADS-related feature recognition

## Privacy

Do not commit patient imaging data, DICOM metadata, clinical identifiers, or site-specific private paths to the repository.


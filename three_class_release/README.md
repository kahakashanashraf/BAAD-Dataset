# BADD Three-Class Companion Release

This folder is an **optional three-class companion** to the public BADD Version 7 release.

The archived Mendeley Data Version 7 release (DOI: 10.17632/fyzy2z8nzx.7) remains unchanged and uses the binary public label `Arrogant` vs `Non-arrogant`. This GitHub companion preserves the original three-way human annotation distinction so researchers can also study:

- `Arrogant`
- `Non-Arrogant-Toxic`
- `Non-Arrogant`

## Derivation

The three-class label is derived by row-wise majority voting across the three human annotation files. No AI/model prediction is used to determine the annotation label. The existing binary label is retained in every file for compatibility:

- `Arrogant` -> `Arrogant`
- `Non-Arrogant-Toxic` -> `Non-arrogant`
- `Non-Arrogant` -> `Non-arrogant`

## Counts

| Three-class label | Rows |
|---|---:|
| Arrogant | 6,126 |
| Non-Arrogant-Toxic | 9,183 |
| Non-Arrogant | 7,118 |
| **Total** | **22,427** |

## Fixed splits

The same row membership as the canonical V7 80/10/10 split is retained.

| Split | Rows |
|---|---:|
| Train | 17,941 |
| Validation | 2,243 |
| Test | 2,243 |

No re-splitting was performed.

## Files

Bengali, English, and aligned bilingual versions are provided for the full dataset and fixed train/validation/test splits. The English text is the same machine-translated NLLB companion used by the current BADD release; only the additional three-class annotation field is added.

Use `arrogance_label_3class` for three-class experiments and `arrogance_label_binary` for the binary task.

## Citation

Please cite the archived dataset:

Ashraf, Kahakashan; Arefin, Mohammad Shamsul; Hossain, Hamid (2026), "BADD: A Large-Scale Bengali Dataset for Arrogance Detection", Mendeley Data, V7, doi: 10.17632/fyzy2z8nzx.7

## License

CC BY 4.0.

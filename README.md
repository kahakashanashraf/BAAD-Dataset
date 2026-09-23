# BADD — Bangla Arrogance Detection Dataset

BADD is a human-annotated Bangla social-media dataset for arrogance detection. The current release contains **22,427 comments** and was produced from **three independent human annotation files**. No AI/model prediction is used as an annotator or in the human consensus.

> **Important:** the value `AI` in the `source` column denotes a data-provenance/source category. It does **not** mean an AI system annotated those rows.

## Current release

- Canonical Bengali dataset: **22,427 rows**
- Train: **17,941**
- Validation: **2,243**
- Test: **2,243**
- Public label space: `Arrogant` / `Non-arrogant`
- Arrogant rows include one of five fine-grained categories.
- The annotation inputs used three human labels: `Arrogant`, `Non-Arrogant-Toxic`, and `Non-Arrogant`; the public binary release maps the latter two to `Non-arrogant`.

## Main files

- `BADD_final_dataset_bengali.csv` — canonical Bengali release
- `BADD_final_dataset_english.csv` — machine-translated English companion
- `BADD_final_dataset_bilingual.csv` — aligned Bengali + English text
- `BADD_train_bengali.csv`, `BADD_validation_bengali.csv`, `BADD_test_bengali.csv`
- Matching English split files
- `ANNOTATION_GUIDELINE.md`
- `DATA_DICTIONARY.csv`
- `TRANSLATION_METADATA.json`
- `TRANSLATION_QA_SUMMARY.md`
- `SHA256SUMS.txt`

Bengali and English split files contain exactly:

`comment`, `source`, `arrogance_label`, `category`

The bilingual file contains:

`comment_bn`, `comment_en`, `source`, `arrogance_label`, `category`

## Label counts

- Non-arrogant: **16,301**
- Arrogant: **6,126**

## Source distribution

- YouTube: **10,081**
- Facebook: **5,881**
- News portal: **5,547**
- AI: **918** (source/provenance category only)

## Annotation

Exactly three human annotators independently reviewed the dataset. The processing pipeline reads only the explicit human label/category fields. Model-signal or AI-generated annotation fields are not used for voting, consensus, or inter-annotator agreement.

The public release uses majority-derived binary labels. Fine-grained arrogance categories are retained only for rows whose final label is `Arrogant`.

## English companion translation

The English companion was generated from the current Bengali release with `facebook/nllb-200-distilled-600M` (`ben_Beng` → `eng_Latn`) using deterministic beam search (`num_beams=2`, `do_sample=False`). Translation changes only comment text; source, label, and category are copied unchanged.

Automatic QA currently flags **197 rows** for manual inspection. These flags are screening signals and are **not** translation error labels or human validation.

## Mendeley Data

The previously published Mendeley record is available at DOI `10.17632/fyzy2z8nzx.6`. The GitHub repository reflects the current working release and should be synchronized with the next Mendeley version before publication claims are finalized.

## Acknowledgment

We gratefully acknowledge **Md. Golam Mostafa, Assistant Professor, Department of Bengali, Cox's Bazar Government College, Cox's Bazar**, for valuable linguistic guidance and support.

## License and citation

Use the license and citation information of the corresponding Mendeley Data version when citing the dataset.

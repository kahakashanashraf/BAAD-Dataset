# BADD — Bangla Arrogance Detection Dataset

BADD is a human-annotated Bangla social-media dataset for arrogance detection. The current canonical release contains **22,427 comments** and is archived as **Mendeley Data Version 7**. Three human annotators reviewed separate copies of the annotation material. No AI/model prediction is used as an annotator or in the human label-consensus procedure.

> **Important:** the value `AI` in the `source` column denotes a data-provenance/source category. It does **not** mean an AI system annotated those rows.

## Current release

- Mendeley Data Version 7 DOI: **10.17632/fyzy2z8nzx.7**
- Canonical Bengali dataset: **22,427 rows**
- Train: **17,941**
- Validation: **2,243**
- Test: **2,243**
- Public binary label space: `Arrogant` / `Non-arrogant`
- Arrogant rows include one of five fine-grained categories.
- Original human labels: `Arrogant`, `Non-Arrogant-Toxic`, and `Non-Arrogant`.

## Main files

- `BADD_final_dataset_bengali.csv` — canonical Bengali binary release
- `BADD_final_dataset_english.csv` — machine-translated English companion
- `BADD_final_dataset_bilingual.csv` — aligned Bengali + English text
- `BADD_train_bengali.csv`, `BADD_validation_bengali.csv`, `BADD_test_bengali.csv`
- Matching English split files
- `ANNOTATION_GUIDELINE.md`
- `DATA_DICTIONARY.csv`
- `TRANSLATION_METADATA.json`
- `TRANSLATION_QA_SUMMARY.md`
- `SHA256SUMS.txt`

## Optional three-class companion

The GitHub-only `three_class_release/` folder preserves the original majority-vote three-class task without modifying Mendeley Data V7 or the fixed split membership:

- Arrogant: **6,126**
- Non-Arrogant-Toxic: **9,183**
- Non-Arrogant: **7,118**

The three-class companion is available in Bengali, English, and bilingual forms with matching train/validation/test splits.

## Label counts in the canonical binary release

- Non-arrogant: **16,301**
- Arrogant: **6,126**

## Source distribution

- YouTube: **10,081**
- Facebook: **5,881**
- News portal: **5,547**
- AI: **918** (source/provenance category only)

## Annotation

Exactly three human annotators reviewed separate copies of the annotation material. Before annotation, they received a common briefing on the label definitions and decision rules. Annotators could seek clarification from Md. Golam Mostafa when a rule or ambiguous example was unclear; these consultations were for guideline clarification, not post-hoc group adjudication.

The archived exports contain six three-class disagreements resolved by majority vote. The A2 and A3 archived label+subtype vectors are identical, so reliability coefficients should not be overinterpreted as proof of annotation independence.

## English companion translation

The English companion was generated from the current Bengali release with `facebook/nllb-200-distilled-600M` (`ben_Beng` → `eng_Latn`) using deterministic beam search (`num_beams=2`, `do_sample=False`). Translation changes only comment text; source, label, and category are copied unchanged.

Automatic QA currently flags **197 rows** for manual inspection. These flags are screening signals and are **not** translation error labels or human validation.

## Reproducibility

See `REPRODUCIBILITY.md` and `reproducibility/` for release-integrity checks and a lightweight TF-IDF/logistic-regression sanity benchmark.

## Acknowledgment

We gratefully acknowledge **Md. Golam Mostafa, Assistant Professor, Department of Bengali, Cox's Bazar Government College, Cox's Bazar**, for linguistic guidance, the pre-annotation briefing, clarification of ambiguous cases, and review of the AI-originated Bangla examples.

## License and citation

Mendeley Data Version 7 is released under **CC BY 4.0**. Cite the archived dataset as:

Ashraf, Kahakashan; Arefin, Mohammad Shamsul; Hossain, Hamid (2026), “BADD: A Large-Scale Bengali Dataset for Arrogance Detection”, Mendeley Data, V7, doi: 10.17632/fyzy2z8nzx.7.

# BADD — Final Mendeley Release (Bengali + English)

This package is the publication-facing BADD release with the canonical Bengali text and an English companion translation.

## Recommended files to cite/use
- `BADD_final_dataset_bengali.csv` — canonical Bengali dataset (**40,427 rows**)
- `BADD_final_dataset_english.csv` — English companion (**40,427 rows**)
- `BADD_final_dataset_bilingual.csv` — aligned Bengali + English text

## Reproducible splits
- Train: **32,341**
- Validation: **4,043**
- Test: **4,043**

Bengali and English split files contain exactly:
`comment`, `source`, `arrogance_label`, `category`.

The bilingual file contains:
`comment_bn`, `comment_en`, `source`, `arrogance_label`, `category`.

## Final label counts
- Non-arrogant: **25,745**
- Arrogant: **14,682**

## Source distribution
- YouTube: **19,177**
- Facebook: **10,575**
- News portal: **9,414**
- AI: **1,261**

There are no `Unknown` source rows in this release.

## Translation
The English text was initially translated with `facebook/nllb-200-distilled-600M` (`ben_Beng` → `eng_Latn`) using deterministic beam search. Automated QA initially flagged 290 rows; those rows, plus one additional low-coverage case, were language-model-assisted post-edited. This must **not** be described as independent human translation validation.

The Bengali dataset remains the canonical version; the English dataset is a translated companion.

## Privacy
Phone-number-like strings and email addresses detected by pattern matching were masked as `<PHONE>` and `<EMAIL>` in this package.

## Citation
Ashraf, Kahakashan; Arefin, Mohammad Shamsul; Hossain, Hamid (2026), “BADD: A Large-Scale Bengali Dataset for Arrogance Detection”, *Mendeley Data*, V6, doi: [10.17632/fyzy2z8nzx.6](https://doi.org/10.17632/fyzy2z8nzx.6)

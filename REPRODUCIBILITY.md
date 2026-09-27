# BADD reproducibility checks

The Mendeley Data Version 7 files remain the canonical binary release. The GitHub `three_class_release/` directory is an optional companion that preserves the original three-class majority-vote task without altering V7.

## Release validation

From the repository root:

```bash
python reproducibility/validate_release.py --root .
```

The script checks row counts, label/source domains, category completeness, exact and normalized-text uniqueness, split disjointness and coverage, English/bilingual alignment, selected direct-identifier patterns, and (when present) the three-class companion counts.

## Sanity-check baseline

Install `pandas` and `scikit-learn`, then run:

```bash
python reproducibility/baseline_tfidf.py --root .
```

The benchmark uses character TF-IDF (`char_wb`, 3–5 grams, `min_df=2`, up to 120,000 features) followed by class-weighted logistic regression with `random_state=42`. It is intended only as a reproducibility/usability check, not as a state-of-the-art benchmark.

## Collection-code note

A preserved historical Facebook collection notebook was used to recover the Selenium version and collection mechanics, but it is not published because the notebook contains historical authentication material. No credentials are required to use or validate the released dataset.

#!/usr/bin/env python3
"""Reproduce simple BADD sanity-check baselines on the fixed splits."""
from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score
from sklearn.pipeline import Pipeline

def model(binary=True):
    solver = "liblinear" if binary else "saga"
    return Pipeline([
        ("tfidf", TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), min_df=2,
                                  max_features=120000, sublinear_tf=True)),
        ("clf", LogisticRegression(max_iter=1200, class_weight="balanced", C=1.0,
                                   solver=solver, random_state=42)),
    ])

def metrics(y, pred):
    return {
        "accuracy": accuracy_score(y, pred),
        "balanced_accuracy": balanced_accuracy_score(y, pred),
        "macro_f1": f1_score(y, pred, average="macro"),
        "weighted_f1": f1_score(y, pred, average="weighted"),
    }

def main(root: Path):
    tr = pd.read_csv(root / "BADD_train_bengali.csv")
    te = pd.read_csv(root / "BADD_test_bengali.csv")
    clf = model(binary=True)
    clf.fit(tr.comment.astype(str), tr.arrogance_label)
    p = clf.predict(te.comment.astype(str))
    print("binary_all", metrics(te.arrogance_label, p))
    natural = te.source.ne("AI")
    print("binary_natural_only", metrics(te.loc[natural, "arrogance_label"], p[natural.to_numpy()]))

    three_dir = root / "three_class_release"
    if three_dir.exists():
        tr3 = pd.read_csv(three_dir / "BADD_train_bengali_3class.csv")
        te3 = pd.read_csv(three_dir / "BADD_test_bengali_3class.csv")
        clf3 = model(binary=False)
        clf3.fit(tr3.comment.astype(str), tr3.arrogance_label_3class)
        p3 = clf3.predict(te3.comment.astype(str))
        print("three_class", metrics(te3.arrogance_label_3class, p3))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path("."))
    main(ap.parse_args().root)

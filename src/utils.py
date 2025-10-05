"""
utils.py
--------
Utility functions for text cleaning, sentence splitting, and n-gram counting.
"""

import re
import collections


def get_sentences(text_file):
    """Read tokenized sentences and split into lists of lowercase tokens."""
    sentences = []
    with open(text_file, "r", encoding="utf-8") as fd:
        for line in fd:
            line = line.rstrip("\n").lower()
            line = re.sub(r"([\,\.\;\!\?\:\;\(\)\[\]\"\'\-])", r" \1 ", line)
            line = re.sub(r"\s+", " ", line).strip()
            sentences.append(line.split())
    return sentences


def get_ngrams(tokens, ngram_order):
    """Extract all n-grams of a given order from a list of tokens."""
    ngrams = collections.Counter()
    for i in range(0, len(tokens) - ngram_order + 1):
        ngram = tuple(tokens[i:i + ngram_order])
        ngrams[ngram] += 1
    return ngrams

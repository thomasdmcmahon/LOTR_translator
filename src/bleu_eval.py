"""
bleu_eval.py
------------
Compute BLEU scores for translation output before and after postprocessing.
"""

import math
import collections
import re
from src.utils import get_sentences, get_ngrams


def compute_brevity_penalty(reference_file, output_file):
    """Compute BLEU brevity penalty."""
    ref_sentences = get_sentences(reference_file)
    output_sentences = get_sentences(output_file)

    nb_ref_tokens = sum(len(s) for s in ref_sentences)
    nb_output_tokens = sum(len(s) for s in output_sentences)
    if nb_output_tokens == 0:
        return 0

    if nb_output_tokens > nb_ref_tokens:
        return 1
    return math.exp(1 - nb_ref_tokens / nb_output_tokens)


def compute_precision(reference_file, output_file, ngram_order):
    """Compute n-gram precision for a given order."""
    ref_sentences = get_sentences(reference_file)
    output_sentences = get_sentences(output_file)

    total_matching_ngrams = 0
    total_system_ngrams = 0

    for ref_sentence, output_sentence in zip(ref_sentences, output_sentences):
        ref_ngrams = get_ngrams(ref_sentence, ngram_order)
        output_ngrams = get_ngrams(output_sentence, ngram_order)

        for ngram, count in output_ngrams.items():
            total_system_ngrams += count
            if ngram in ref_ngrams:
                total_matching_ngrams += min(count, ref_ngrams[ngram])

    if total_system_ngrams == 0:
        return 0.0

    return total_matching_ngrams / total_system_ngrams


def compute_bleu(reference_file, output_file, max_order=4):
    """Compute overall BLEU score."""
    precisions = [compute_precision(reference_file, output_file, i) for i in range(1, max_order + 1)]
    precision_product = math.prod(p if p > 0 else 1e-9 for p in precisions)
    brevity_penalty = compute_brevity_penalty(reference_file, output_file)
    bleu = brevity_penalty * math.pow(precision_product, 1 / max_order)
    return bleu


if __name__ == "__main__":
    bleu = compute_bleu("data/lotr.en", "results/lotr_output.en")
    bleu_post = compute_bleu("data/lotr.en", "results/lotr_corrected.en")
    print(f"BLEU uten postprosessering: {bleu:.4f}")
    print(f"BLEU med postprosessering: {bleu_post:.4f}")

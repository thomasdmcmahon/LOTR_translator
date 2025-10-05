"""
translate.py
------------
Module for translating text from German to English using Helsinki-NLP's OPUS-MT model.
"""

import transformers, torch
from tqdm import tqdm


def load_model(src_lang="de", tgt_lang="en"):
    """Load tokenizer and model for a given language pair."""
    model_name = f"helsinki-nlp/opus-mt-{src_lang}-{tgt_lang}"
    tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
    model = transformers.AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model


def translate(input_file, translation_file, batch_size=32, src_lang="de", tgt_lang="en"):
    """Translate lines in a text file from source to target language and write output."""
    tokenizer, translator = load_model(src_lang, tgt_lang)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    translator = translator.to(device)
    print(f"Using device: {device}")

    with open(input_file, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines()]

    translations = []

    for i in tqdm(range(0, len(lines), batch_size), desc="Translating"):
        batch = lines[i:i + batch_size]
        tokens = tokenizer(batch, return_tensors="pt", padding=True, truncation=True)
        tokens = {k: v.to(device) for k, v in tokens.items()}

        with torch.no_grad():
            outputs = translator.generate(**tokens, max_new_tokens=100)

        decoded = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        translations.extend(decoded)

    with open(translation_file, "w", encoding="utf-8") as out_file:
        for translation in translations:
            out_file.write(translation + "\n")


if __name__ == "__main__":
    translate("data/lotr.de", "results/lotr_output.en")

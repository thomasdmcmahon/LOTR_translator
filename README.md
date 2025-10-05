<h1 align="center">🧙‍♂️ Lord of the Rings Translator & Chatbot</h1>

<p align="center">
  <em>Machine translation, post-processing, evaluation, and a simple chatbot — all themed around <strong>The Lord of the Rings</strong> 🧝‍♀️⚔️</em>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.9+-blue.svg?style=flat-square&logo=python&logoColor=white"></a>
  <a href="https://huggingface.co/Helsinki-NLP/opus-mt-de-en"><img src="https://img.shields.io/badge/Model-Helsinki--NLP%2Fopus--mt--de--en-yellow.svg?style=flat-square&logo=huggingface&logoColor=white"></a>
  <img src="https://img.shields.io/badge/Transformers-🤗-orange.svg?style=flat-square">
  <img src="https://img.shields.io/badge/Torch-PyTorch-red.svg?style=flat-square&logo=pytorch&logoColor=white">
</p>

---

## Overview

This project demonstrates a complete **language technology pipeline** — from neural machine translation to evaluation and chatbot interaction — using _The Lord of the Rings_ as a themed dataset.

In practice, the system:

- Translates German sentences from _The Lord of the Rings_ into English
- Post-processes the output to correct names and world-specific terms
- Evaluates translation quality with a custom BLEU implementation
- Provides a simple retrieval-based chatbot that responds using LOTR dialogue

---

## How to Run

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Translate
```bash
python src/translate.py
```

### 3️⃣ Post-process translations
```bash
python src/postprocess.py
```

### 4️⃣ Evaluate BLEU score
```bash
python src/bleu_eval.py
```

### 5️⃣ Run the chatbot
```bash
python src/chatbot.py
```

### Example
**Inpt**
```txt
Die Welt ist im Wandel.
```
**Output**
```txt
The world is changing.
```
**BLEU Evaluation**
```txt
BLEU without postprocessing: 0.4271
BLEU with postprocessing:    0.4823
```
### Project Structure

```graphql
lotr-translator/
├── src/
│   ├── translate.py          # Translation using Helsinki-NLP model
│   ├── postprocess.py        # LOTR name and term corrections
│   ├── bleu_eval.py          # Custom BLEU evaluation
│   ├── chatbot.py            # TF-IDF retrieval-based chatbot
│   └── utils.py              # Helper functions
├── data/                     # Input text files
│   ├── lotr.de
│   └── lotr.en
├── results/                  # Output translations and evaluations
│   ├── lotr_output.en
│   └── lotr_corrected.en
├── requirements.txt
└── README.md
```

## Tech Stack
| Component             | Description                           |
| --------------------- | ------------------------------------- |
| **Python 3.9+**       | Core language                         |
| **Transformers (🤗)** | Pre-trained translation model         |
| **PyTorch**           | Backend for model inference           |
| **NumPy**             | Vector math & similarity calculations |
| **tqdm**              | Progress visualization                |

Model: [Helsinki-NLP/opus-mt-de-en](https://huggingface.co/Helsinki-NLP/opus-mt-de-en)

<h1 align="center">🧙‍♂️ Lord of the Rings Translator & Chatbot</h1>

<p align="center">
  <em>Machine translation, post-processing, evaluation, and a simple chatbot — all themed around <strong>The Lord of the Rings</strong> 🧝‍♀️⚔️</em>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.9+-blue.svg?style=flat-square&logo=python&logoColor=white"></a>
  <a href="https://huggingface.co/Helsinki-NLP/opus-mt-de-en"><img src="https://img.shields.io/badge/Model-Helsinki--NLP%2Fopus--mt--de--en-yellow.svg?style=flat-square&logo=huggingface&logoColor=white"></a>
  <img src="https://img.shields.io/badge/Transformers-🤗-orange.svg?style=flat-square">
  <img src="https://img.shields.io/badge/Torch-PyTorch-red.svg?style=flat-square&logo=pytorch&logoColor=white">
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=flat-square">
</p>

---

## 📘 Overview

This project demonstrates a complete **language technology pipeline** — from neural machine translation to evaluation and chatbot interaction — using _The Lord of the Rings_ as a themed dataset.

🪄 In practice, the system:

- Translates German sentences from _The Lord of the Rings_ into English
- Post-processes the output to correct names and world-specific terms
- Evaluates translation quality with a custom BLEU implementation
- Provides a simple retrieval-based chatbot that responds using LOTR dialogue

---

## 🚀 How to Run

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

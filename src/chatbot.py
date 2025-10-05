"""
chatbot.py
----------
A simple retrieval-based chatbot using TF-IDF vectors and cosine similarity.
"""

import math
import numpy as np


class RetrievalChatbot:
    """Retrieval-based chatbot using TF-IDF vectors."""

    def __init__(self, dialogue_file):
        self.utterances = []
        with open(dialogue_file, "r", encoding="utf-8") as fd:
            for line in fd:
                utterance = self._tokenise(line.rstrip("\n"))
                self.utterances.append(utterance)

        self.doc_freqs = self._compute_doc_frequencies()
        self.tf_idfs = [self.get_tf_idf(utterance) for utterance in self.utterances]

    def _tokenise(self, utterance):
        return utterance.strip().lower().split()

    def _compute_doc_frequencies(self):
        doc_freqs = {}
        for utterance in self.utterances:
            for word in set(utterance):
                doc_freqs[word] = doc_freqs.get(word, 0) + 1
        return doc_freqs

    def get_tf_idf(self, utterance):
        tf_idf_vals = {}
        word_counts = {word: utterance.count(word) for word in utterance}
        for word, count in word_counts.items():
            idf = math.log(len(self.utterances) / (self.doc_freqs.get(word, 0) + 1))
            tf_idf_vals[word] = count * idf
        return tf_idf_vals

    def compute_cosine(self, tf_idf1, tf_idf2):
        dotproduct = sum(tf_idf1[w] * tf_idf2[w] for w in tf_idf1 if w in tf_idf2)
        return dotproduct / (self._get_norm(tf_idf1) * self._get_norm(tf_idf2))

    def _get_norm(self, tf_idf):
        return math.sqrt(sum(v ** 2 for v in tf_idf.values()))

    def get_response(self, query):
        if isinstance(query, str):
            query = self._tokenise(query)
        query_vec = self.get_tf_idf(query)
        sims = [self.compute_cosine(query_vec, utt_vec) for utt_vec in self.tf_idfs]
        if not sims:
            return None
        best_idx = int(np.argmax(sims))
        if best_idx + 1 < len(self.utterances):
            return " ".join(self.utterances[best_idx + 1])
        return None


if __name__ == "__main__":
    bot = RetrievalChatbot("data/lotr.en")
    print("🧝‍♂️ Welcome to the LOTR chatbot! (type 'exit' to quit)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Farewell, traveler.")
            break

        response = bot.get_response(user_input)
        if response:
            print("Chatbot:", response)
        else:
            print("Chatbot: Sorry, I have no answer for that.")

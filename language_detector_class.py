

import json

class LanguageDetector:

    def __init__(self, filename='stopwords-iso.json'):
        with open(filename, 'rb') as file:
            self.stopwords = json.load(file)

    def get_language(self, t):

        bow = set(t.lower().split())

        scores = {}
        for lang, lang_sw in self.stopwords.items():
            lang_bow = set(lang_sw)
            inters = len(bow & lang_bow)  # len(bow.intersection(lang_bow))
            scores[lang] = inters

        sorted_items = scores.items()
        sorted_scores = sorted(sorted_items, key=lambda x: x[1], reverse=True)

        return sorted_scores[0]



texts = [
    "ciao sono io e mi piace la pizza con l'ananas",
    "je suis le plus baguette du monde",
    "ich bin der kommissar keine ahnung",
    "vamos a la playa del sol amigo"
]

ld = LanguageDetector()
for text in texts:
    lang = ld.get_language(text)
    print(lang)


from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    'scarpe ambiente',
    'scarpe',
    'scarpe ambiente gallina',
    'gallina'
]

vectorizer = TfidfVectorizer()
vectorized_corpus = vectorizer.fit_transform(corpus)

print(vectorized_corpus.toarray())
print(vectorizer.get_feature_names())
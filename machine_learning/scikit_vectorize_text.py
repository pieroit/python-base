
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('movie-review/movie_review.csv')[:20]
corpus = df['text']

vectorizer = CountVectorizer(stop_words=['ably', 'acts', 'alan'])

vectorized_corpus = vectorizer.fit_transform(corpus)
# stessa cosa in due linee
# 1. vectorizer.fit(corpus)
# 2. vectorized_corpus = vectorizer.transform(corpus)

print(vectorized_corpus.toarray())
print(vectorizer.get_feature_names())
print(vectorized_corpus)
print( vectorizer.inverse_transform(vectorized_corpus) )
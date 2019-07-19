
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from joblib import dump
from sentiment_cleaner import cleaner

data = pd.read_csv('movie_review.csv')

corpus = data['text']
y = data['tag']

# QUI PULIZIA

# costruisci vettorizzatore
vectorizer = TfidfVectorizer(preprocessor=cleaner, stop_words='english')
# vettorizza i testi
X = vectorizer.fit_transform(corpus)

# dividi i dati in train e test
X_train, X_test, y_train, y_test = train_test_split(X, y)

# costruisci modello
model = LogisticRegression()

# addestra modello
model.fit(X_train, y_train)

# raccogli predizioni per train e test
p_train = model.predict(X_train)
p_test = model.predict(X_test)

# misura accuratezza su train e test
acc_train = accuracy_score(y_train, p_train)
acc_test = accuracy_score(y_test, p_test)
print('Train', acc_train, 'Test', acc_test)
print('Test matrix', confusion_matrix(y_test, p_test))

# salvo il modello addestrato su disco (e anche il vettorizzatore)
print('Saving model and vectorizer...')
dump(vectorizer, 'sentiment_vectorizer.joblib')
dump(model, 'sentiment_model.joblib')
print('Done.')

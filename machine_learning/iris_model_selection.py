
# 1. importare diversi classificatori
# 2. preparare un array di dizionari
# 3. ogni dizionario contiene:
#       - nome dell'algoritmo (chiave 'nome')
#       - il modello (chiave 'model')
#       - l'accuratezza di training (chiave 'train')
#       - l'accuratezza di test (chiave 'test')
# 4. cancellare i modelli dal dizionario
# 5. convertire la lista di dizionari in pd.DataFrame
# 6. plottare i risultati (grafico a barre)

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.dummy import DummyClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import pandas as pd
from joblib import dump, load
from scikitplot.metrics import plot_confusion_matrix

dataset = load_iris()
X = dataset['data']
y = dataset['target']

X_train, X_test, y_train, y_test = train_test_split(X, y)

models_info = [
    {
        'nome'  : 'dummy',
        'model' : DummyClassifier()
    },
    {
        'nome'  : 'tree',
        'model' : DecisionTreeClassifier()
    },
    {
        'nome'  : 'linear',
        'model' : LogisticRegression()
    },
    {
        'nome'  : 'kNN',
        'model' : KNeighborsClassifier()
    },
]

for model_info in models_info:

    m = model_info['model']

    m.fit(X_train, y_train)

    p_train = m.predict(X_train)
    p_test = m.predict(X_test)

    model_info['train'] = accuracy_score(y_train, p_train)
    model_info['test'] = accuracy_score(y_test, p_test)

    dump(m, model_info['nome'] + '.joblib')
    del model_info['model']

# grafico prestazioni
df = pd.DataFrame(models_info)
#df.plot.bar(x='nome')
#plt.show()

# ricarico un modello salvato
model = load('tree.joblib')
new_example = [[0.0, 0.1, 2.4, 2.4]]
p = model.predict(new_example)
print('Prediction', dataset['target_names'][p])

# carico kNN e produco la matrice di confusione
knn    = load('kNN.joblib')
p_test = knn.predict(X_test)
plot_confusion_matrix(y_test, p_test)
plt.show()



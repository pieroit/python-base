import numpy as np
np.random.seed(0)

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# carica boston dataset
dataset = load_boston()

# isoliamo feature e target
X = dataset['data']
y = dataset['target']

# crea nuovo modello da addestrare
model = LinearRegression()

# separazione in train e test
X_train, X_test, y_train, y_test = train_test_split(X, y)

# addestramento
model.fit(X_train, y_train)

# ottieni predizioni
p_train = model.predict(X_train)
p_test = model.predict(X_test)

# misura performance
mae_train = mean_absolute_error(y_train, p_train)
print('MAE in training', mae_train)
mae_test = mean_absolute_error(y_test, p_test)
print('MAE in test', mae_test)


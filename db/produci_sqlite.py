import pandas as pd
import sqlite3

data = [
    {'nome': 'Qui', 'eta': 23, 'sesso': 'M'},
    {'nome': 'Quo', 'eta': 19, 'sesso': 'M'},
    {'nome': 'Qua', 'eta': 20, 'sesso': 'M'},
    {'nome': 'Paperino', 'eta': 35, 'sesso': 'M'},
    {'nome': 'Gastone', 'eta': 28, 'sesso': 'M'},
    {'nome': 'Zio Paperone', 'eta': 55, 'sesso': 'M'},
    {'nome': 'Paperina', 'eta': 32, 'sesso': 'F'},
    {'nome': 'Nonna Papera', 'eta': 60, 'sesso': 'F'},
]

df = pd.DataFrame(data)

connection = sqlite3.connect('db.sqlite')
df.to_sql('paperopoli', connection, if_exists='replace', index=False)
connection.close()
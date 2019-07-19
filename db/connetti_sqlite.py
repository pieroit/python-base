import sqlite3
import pandas as pd

#connection = sqlite3.connect('db.sqlite')
#cursor = connection.cursor()
#result = cursor.execute('DELETE FROM paperopoli')
#connection.commit()
#for r in result:
#    print(r)

connection = sqlite3.connect('db.sqlite')
df = pd.read_sql('SELECT * FROM paperopoli', connection)
print(df)
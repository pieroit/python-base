
from flask import Flask, request
from flask_restful import Api, Resource
import sqlite3

app = Flask(__name__)
api = Api(app)

class Paperopoli(Resource):

    def db_query(self, query):
        connection = sqlite3.connect('db.sqlite')
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        res = cursor.execute(query).fetchall()
        connection.commit()
        res = map(dict, res)
        return list(res)

    def get(self):
        query = 'SELECT * FROM paperopoli'
        result = self.db_query(query)
        return result

    def post(self):
        d = request.get_json(force=True)
        query = f'INSERT INTO paperopoli (nome, eta, sesso) VALUES ("{d["nome"]}", "{d["eta"]}", "{d["sesso"]}")'
        print(query)
        self.db_query(query)

api.add_resource(Paperopoli, '/personaggi')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request
from flask_restful import Api, Resource
import sqlite3

app = Flask(__name__)
api = Api(app)

class Paperopoli(Resource):

    def get(self):
        return {'ciao': 'mondo'}


api.add_resource(Paperopoli, '/personaggi')

if __name__ == '__main__':
    app.run(debug=True)
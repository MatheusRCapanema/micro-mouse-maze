from flask import Flask
from flask_restx import Api
import api.views

app = Flask(__name__)
api_instance = Api(app, version='1.0', title='API de Labirinto', description='Uma API simples para manipular labirintos.')

api_instance.add_namespace(api.views.api, path='/api')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger

app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion='1.0', api_spec_url='/swagger')

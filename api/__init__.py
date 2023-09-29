from flask import Blueprint
from flask_restx import Api

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint, version='1.0', title='Labirinto API', description='API para Labirinto')

from . import views

from flask import Flask
from flask_restx import Api
from api.views import api as maze_ns

app = Flask(__name__)
api = Api(app, version='1.0', title='Micro Mouse Maze API',
          description='A simple API for the Micro Mouse Maze')

api.add_namespace(maze_ns, path="/maze")

if __name__ == '__main__':
    app.run(debug=True)

from flask_restx import Resource, Namespace, fields, reqparse
from api.models import Maze
import random
import time

api = Namespace('maze', description='Maze operations')

# Models for Swagger documentation
maze_model = api.model('Maze', {
    'vertex': fields.Integer(required=True, description='Current vertex ID'),
    'directions': fields.List(fields.Integer, description='Possible directions from the current vertex')
})

generate_model = api.model('Generate', {
    'vertices': fields.Integer(required=True, description='Number of vertices'),
    'edges': fields.Integer(required=True, description='Number of edges')
})

# Global variables
maze = None
current_vertex = None
exploration_end_time = None

generate_parser = reqparse.RequestParser()
generate_parser.add_argument('vertices', type=int, required=True)
generate_parser.add_argument('edges', type=int, required=True)

@api.route('/generate')
class GenerateMaze(Resource):
    @api.expect(generate_model)
    def post(self):
        global maze
        args = generate_parser.parse_args()
        num_vertices = args['vertices']
        num_edges = args['edges']
        maze = Maze(num_vertices, num_edges)
        return {'success': True}, 201

@api.route('/start')
class StartExploration(Resource):
    @api.marshal_with(maze_model)
    def get(self):
        global current_vertex, exploration_end_time
        if maze is None:
            return {"error": "Maze not generated. Please generate first."}, 400
        current_vertex = random.choice(list(maze.graph.keys()))
        exploration_end_time = time.time() + 40
        return {
            'vertex': current_vertex,
            'directions': maze.get_possible_directions(current_vertex)
        }

@api.route('/move/<int:direction>')
class MoveDirection(Resource):
    @api.marshal_with(maze_model)
    def get(self, direction):
        global current_vertex
        if maze is None:
            return {"error": "Maze not generated. Please generate first."}, 400
        if direction not in maze.get_possible_directions(current_vertex):
            return {"error": "Invalid move direction"}, 400
        
        if time.time() > exploration_end_time:
            return {"error": "Exploration time exceeded"}, 403
        
        current_vertex = direction
        return {
            'vertex': current_vertex,
            'directions': maze.get_possible_directions(current_vertex)
        }

@api.route('/remaining_time')
class RemainingTime(Resource):
    def get(self):
        global exploration_end_time
        if exploration_end_time is None:
            return {"error": "Exploration hasn't started yet"}, 400

        remaining = max(exploration_end_time - time.time(), 0)
        return {'remaining_time': remaining}

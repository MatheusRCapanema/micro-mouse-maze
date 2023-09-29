from flask_restx import Resource, Namespace, fields, reqparse
from .models import Maze


api = Namespace('labirinto', description='Operações do Labirinto')

# Modelos de requisição e resposta
start_model = api.model('Start', {
    'id': fields.String(required=True, description='ID do usuário'),
    'labirinto': fields.String(required=True, description='Nome do labirinto')
})

move_model = api.clone('Move', start_model, {
    'nova_posicao': fields.Integer(required=True, description='Nova posição desejada')
})

validate_model = api.clone('Validate', move_model, {
    'todos_movimentos': fields.List(fields.Integer, required=True, description='Todos os movimentos feitos')
})

start_response_model = api.model('StartResponse', {
    'pos_atual': fields.Integer(description='Posição atual'),
    'inicio': fields.Boolean(description='É o início?'),
    'final': fields.Boolean(description='É o fim?'),
    'movimentos': fields.List(fields.Integer, description='Movimentos possíveis')
})

move_response_model = api.clone('MoveResponse', start_response_model)

validate_response_model = api.model('ValidateResponse', {
    'caminho_valido': fields.Boolean(description='O caminho é válido?'),
    'quantidade_movimentos': fields.Integer(description='Quantidade total de movimentos feitos')
})

maze_instance = Maze(10, 10)
maze_instance.generate_maze()
maze_graph = maze_instance.get_graph_representation()
initial_position = 0
final_position = (maze_instance.rows - 1) * maze_instance.cols + (maze_instance.cols - 1)
user_positions = {}  # Armazenar a posição atual do usuário baseada no ID

@api.route('/iniciar')
class Start(Resource):
    @api.expect(start_model)
    @api.response(200, 'Success', start_response_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True)
        parser.add_argument('labirinto', type=str, required=True)
        args = parser.parse_args()
        
        user_id = args['id']
        user_positions[user_id] = initial_position

        possible_moves = maze_graph[initial_position]
        
        return {
            "pos_atual": initial_position,
            "inicio": True,
            "final": False,
            "movimentos": possible_moves
        }, 200

@api.route('/movimentar')
class Move(Resource):
    @api.expect(move_model)
    @api.response(200, 'Success', move_response_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True)
        parser.add_argument('labirinto', type=str, required=True)
        parser.add_argument('nova_posicao', type=int, required=True)
        args = parser.parse_args()
        
        user_id = args['id']
        new_position = args['nova_posicao']

        # Verificar se o movimento é válido
        if new_position not in maze_graph[user_positions[user_id]]:
            return {"message": "Movimento inválido."}, 400

        user_positions[user_id] = new_position

        possible_moves = maze_graph[new_position]
        
        return {
            "pos_atual": new_position,
            "inicio": new_position == initial_position,
            "final": new_position == final_position,
            "movimentos": possible_moves
        }, 200

@api.route('/valida_caminho')
class Validate(Resource):
    @api.expect(validate_model)
    @api.response(200, 'Success', validate_response_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True)
        parser.add_argument('labirinto', type=str, required=True)
        parser.add_argument('todos_movimentos', type=list, required=True)
        args = parser.parse_args()
        
        path = args['todos_movimentos']
        
        is_valid = all((path[i], path[i+1]) in maze_graph.items() for i in range(len(path)-1))
        
        return {
            "caminho_valido": is_valid,
            "quantidade_movimentos": len(path)
        }, 200


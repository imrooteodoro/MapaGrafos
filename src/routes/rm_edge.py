from models.graph import *
from models.city import *
from flask import jsonify, request

def rm_edge(app):
    @app.route('/remove_edge', methods=['DELETE'])
    def remove_edge():
        data = request.get_json()
        city1 = data['city1']
        city2 = data['city2']
        graph[city1] = [(v, info) for v, info in graph[city1] if v != city2]
        graph[city2] = [(v, info) for v, info in graph[city2] if v != city1]
        return jsonify({'message': 'Aresta removida com sucesso'}), 200
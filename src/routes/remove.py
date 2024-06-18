from models.city import *
from models.graph import *
from flask import jsonify, request

def remove(app):
    @app.route('/remove_vertex', methods=['DELETE'])
    def remove_vertex():
         data = request.get_json()
         city = data['city']
         city_info.pop(city, None)
         graph.pop(city, None)
         for key in graph:
            graph[key] = [(v, info) for v, info in graph[key] if v != city]
            return jsonify({'message': 'Vértice removido com sucesso'}), 200


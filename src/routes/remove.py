
from controllers.graph import Graph
from flask import jsonify, request

mapa_tocatins = Graph()

def remove(app):
    @app.route('/remove_vertex', methods=['DELETE'])
    def remove_vertex():
        data = request.get_json()
        city = data['city']
        mapa_tocatins.remove_vertex(city)
        return jsonify({'message': 'Vértice removido com sucesso'}), 200


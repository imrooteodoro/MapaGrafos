from controllers.graph import Graph
from flask import jsonify, request

mapa_tocatins = Graph()
def rm_edge(app):
    @app.route('/remove_edge', methods=['DELETE'])
    def remove_edge():
        data = request.get_json()
        city1 = data['city1']
        city2 = data['city2']
        mapa_tocatins.remove_edge(city1, city2)
        return jsonify({'message': 'Aresta removida com sucesso'}), 200

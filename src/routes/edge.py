from controllers.graph import Graph
from flask import Flask, request, jsonify

mapa_tocatins = Graph()
def edge(app):
    @app.route('/add_edge', methods=['POST'])
    def add_edge():
        data = request.get_json()
        city1 = data['city1']
        city2 = data['city2']
        info = data['info']
        mapa_tocatins.add_edge(city1, city2, info)
        return jsonify({'message': 'Aresta adicionada com sucesso'}), 200

from flask import Flask, request, jsonify, render_template
from controllers.graph import Graph

mapa_tocatins = Graph()
def vertex(app):
    @app.route('/add_vertex', methods=['POST'])
    def add_vertex():
        data = request.get_json()
        city = data['city']
        info = data['info']
        mapa_tocatins.add_vertex(city, info)
        return jsonify({'message': 'Vértice adicionado com sucesso'}), 200

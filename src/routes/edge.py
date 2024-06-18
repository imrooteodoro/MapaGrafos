from models.graph import *
from models.city import *
from flask import Flask, request, jsonify

def edge(app):
    @app.route('/add_edge', methods=['POST'])
    def add_edge():
        data = request.get_json()
        city1 = data['city1']
        city2 = data['city2']
        info = data['info']
        graph[city1].append((city2, info))
        graph[city2].append((city1, info))
        return jsonify({'message': 'Aresta adicionada com sucesso'}), 200
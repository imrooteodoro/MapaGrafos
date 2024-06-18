from flask import Flask, request, jsonify, render_template
from models.city import *
from models.graph import *


def vertex(app):
    @app.route('/add_vertex', methods=['POST'])
    def add_vertex():
        data = request.get_json()
        city = data['city']
        info = data['info']
        city_info[city] = info
        return jsonify({'message': 'Vértice adicionado com sucesso'}), 200
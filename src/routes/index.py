from flask import Flask, request, jsonify, render_template
from controllers.graph import Graph
from controllers.graph import tocantins_graph

mapa_tocatins = Graph()

def index_route(app):
    @app.route('/', methods=['GET'])
    def home():
        print(mapa_tocatins.vertices)
        return render_template('index.html', city_info = tocantins_graph.vertices, graph=tocantins_graph.edges)

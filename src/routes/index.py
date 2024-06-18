from flask import Flask, request, jsonify, render_template
from models.graph import *
from models.city import *

def index_route(app):
    @app.route('/', methods=['GET'])
    def home():
        print(graph)
        return render_template('index.html', city_info = city_info, graph=graph)

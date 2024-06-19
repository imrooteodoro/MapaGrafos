from flask import Flask
from routes.vertex import *
from routes.edge import *
from routes.index import *
from routes.remove import *
from routes.rm_edge import *
from models.matrix import matrix

app = Flask(__name__, static_folder='public')


edge(app)
index_route(app)
remove(app)
rm_edge(app)
vertex(app)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

from controllers.graph import Graph
from controllers.graph import tocantins_graph

#
matrix = {
tocantins_graph.add_vertex("Palmas", {"sigla": "PAL", "populacao": 306296, "extensao_territorial": 2218.93}),
tocantins_graph.add_vertex("Araguaina", {"sigla": "ARA", "populacao": 180470, "extensao_territorial": 4000.40}),
tocantins_graph.add_vertex("Gurupi", {"sigla": "GUR", "populacao": 86413, "extensao_territorial": 1835.52}),
tocantins_graph.add_vertex("Porto Nacional", {"sigla": "PNA", "populacao": 52933, "extensao_territorial": 4512.11}),
tocantins_graph.add_vertex("Paraiso do Tocantins", {"sigla": "PTO", "populacao": 51689, "extensao_territorial": 720.07}),
tocantins_graph.add_vertex("Araguatins", {"sigla": "ATI", "populacao": 34981, "extensao_territorial": 2289.39}),
tocantins_graph.add_vertex("Guarai", {"sigla": "GUA", "populacao": 24898, "extensao_territorial": 1568.70}),
tocantins_graph.add_vertex("Dianopolis", {"sigla": "DIA", "populacao": 21823, "extensao_territorial": 3602.98}),
tocantins_graph.add_vertex("Formoso do Araguaia", {"sigla": "FOR", "populacao": 20177, "extensao_territorial": 13692.07}),
tocantins_graph.add_vertex("Augustinopolis", {"sigla": "AUG", "populacao": 18576, "extensao_territorial": 253.51}),
tocantins_graph.add_vertex("Taguatinga", {"sigla": "TAG", "populacao": 16320, "extensao_territorial": 2413.68}),
tocantins_graph.add_vertex("Miracema do Tocantins", {"sigla": "MIR", "populacao": 10859, "extensao_territorial": 3364.48}),
tocantins_graph.add_edge("Gurupi", "Porto Nacional", {"distancia": 280}),
tocantins_graph.add_edge("Porto Nacional", "Paraiso do Tocantins", {"distancia": 60}),
tocantins_graph.add_edge("Paraiso do Tocantins", "Araguatins", {"distancia": 500}),
tocantins_graph.add_edge("Araguatins", "Guarai", {"distancia": 400}),
tocantins_graph.add_edge("Guarai", "Dianopolis", {"distancia": 300}),
tocantins_graph.add_edge("Dianopolis", "Formoso do Araguaia", {"distancia": 350}),
tocantins_graph.add_edge("Formoso do Araguaia", "Augustinopolis", {"distancia": 600}),
tocantins_graph.add_edge("Augustinopolis", "Taguatinga", {"distancia": 450}),
tocantins_graph.add_edge("Taguatinga", "Miracema do Tocantins", {"distancia": 400}),
tocantins_graph.add_edge("Miracema do Tocantins", "Palmas", {"distancia": 90}),
tocantins_graph.add_edge("Palmas", "Araguaina", {"distancia": 385}),
tocantins_graph.add_edge("Palmas", "Gurupi", {"distancia": 245}),
tocantins_graph.add_edge("Araguaina", "Gurupi", {"distancia": 385})
}
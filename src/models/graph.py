from collections import defaultdict

# Estrutura de dados para armazenar o grafo
graph = defaultdict(list)
graph["Piraquê"].append(("Araguaina", {"distance":63, "highway":"BR-153"}))
graph["Palmas"].append(("Araguaina", {"distance": 385, "highway": "BR-153"}))
graph["Palmas"].append(("Gurupi", {"distance": 245, "highway": "BR-153"}))
graph["Araguaina"].append(("Gurupi", {"distance": 627, "highway": "BR-153"}))
graph["Gurupi"].append(("Araguaina", {"distance": 627, "highway": "BR-153"}))
graph["Aragominas"].append(("Araguaina", {"distance": 43, "higway":"TO-164"}))
graph["Filadelfia"].append(("Araguaina", {"distance":108, "highway": "TO-222"}))
graph["Xambioá"].append(("Araguaina", {"distance":122, "highway": "TO-164"}))
graph["Santa Fé"].append(("Araguaina", {"distance":73, "highway": "TO-222"}))
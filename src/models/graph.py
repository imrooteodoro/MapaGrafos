from collections import defaultdict

# Estrutura de dados para armazenar o grafo
graph = defaultdict(list)
graph["Piraquê"].append(("Araguaina", {"distance":63, "highway":"BR-153"}))
graph["Palmas"].append(("Araguaina", {"distance": 385, "highway": "BR-153"}))
graph["Araguaina"].append(("Palmas", {"distance": 385, "highway": "BR-153"}))
graph["Palmas"].append(("Gurupi", {"distance": 245, "highway": "BR-153"}))
graph["Gurupi"].append(("Palmas", {"distance": 245, "highway": "BR-153"}))
graph["Araguaina"].append(("Gurupi", {"distance": 627, "highway": "BR-153"}))
graph["Gurupi"].append(("Araguaina", {"distance": 627, "highway": "BR-153"}))
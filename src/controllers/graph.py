class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = {}

    def add_vertex(self, name, data):
        self.vertices[name] = data

    def remove_vertex(self, name):
        del self.vertices[name]

    def add_edge(self, start, end, data):
        if start not in self.edges:
            self.edges[start] = {}
        self.edges[start][end] = data

    def remove_edge(self, start, end):
        del self.edges[start][end]

    def breadth_first_search(self, start):
        visited = {start}
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")
            for neighbour in self.edges[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

    def depth_first_search(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for neighbour in self.edges[start]:
            if neighbour not in visited:
                self.depth_first_search(neighbour, visited)

    def find_routes(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.edges:
            return []
        paths = []
        for node in self.edges[start]:
            if node not in path:
                newpaths = self.find_routes(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
    
    def display_graph(self):
        print("Cidades:")
        for city, data in self.vertices.items():
            print(f"{city}: {data}")
        print("\nConexões:")
        for start, connections in self.edges.items():
            for end, distance in connections.items():
                print(f"{start} --> {end}: {distance}")



tocantins_graph = Graph()




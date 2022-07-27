class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}

        def add_vertex(self, key):
            """Add a vertex with the given key to the graph."""
            vertex = Vertex(key)
            self.vertices[key] = vertex



    def get_vertex(self, key):
        """Return vertex object with the corresponding key."""
        return self.vertices[key]



def __contains__(self, key):
    return key in self.vertices



def add_edge(self, src_key, dest_key, weight=1):
    """Add edge from src_key to dest_key with given weight."""
    self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)



def does_edge_exist(self, src_key, dest_key):
    """Return True if there is an edge from src_key to dest_key."""
    return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])



def __iter__(self):
    return iter(self.vertices.values())
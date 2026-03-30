class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def print_graph(self):
        for v in range(self.V):
            print(f"{v}: {' '.join(map(str, self.adj[v]))}")
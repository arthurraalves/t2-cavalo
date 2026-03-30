class Cycle:
    def __init__(self, G):
        self.visited = [False] * G.V
        self.edge_to = [-1] * G.V
        self.cycle = []

        for v in range(G.V):
            if not self.visited[v]:
                self.dfs(G, v, -1)

    def dfs(self, G, v, parent):
        self.visited[v] = True

        for w in G.adj[v]:
            if self.cycle:
                return
            if not self.visited[w]:
                self.edge_to[w] = v
                self.dfs(G, w, v)
            elif w != parent:
                # encontrou ciclo
                x = v
                self.cycle = [w]
                while x != w:
                    self.cycle.append(x)
                    x = self.edge_to[x]
                self.cycle.append(w)
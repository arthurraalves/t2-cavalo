class CC:
    def __init__(self, G):
        self.visited = [False] * G.V
        self.id = [-1] * G.V
        self.count = 0

        for v in range(G.V):
            if not self.visited[v]:
                self.dfs(G, v)
                self.count += 1

    def dfs(self, G, v):
        self.visited[v] = True
        self.id[v] = self.count
        for w in G.adj[v]:
            if not self.visited[w]:
                self.dfs(G, w)
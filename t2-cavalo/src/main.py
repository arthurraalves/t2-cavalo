from graph import Graph
from cc import CC
from cycle import Cycle
from collections import deque

# ==============================
# Leitura do arquivo (algs4)
# ==============================
def read_graph(filename):
    with open(filename, 'r') as f:
        V = int(f.readline())
        E = int(f.readline())

        G = Graph(V)

        for _ in range(E):
            v, w = map(int, f.readline().split())
            G.add_edge(v, w)

    return G

# ==============================
# BFS (menor caminho)
# ==============================
def bfs(G, s):
    visited = [False] * G.V
    dist = [-1] * G.V

    queue = deque([s])
    visited[s] = True
    dist[s] = 0

    while queue:
        v = queue.popleft()
        for w in G.adj[v]:
            if not visited[w]:
                visited[w] = True
                dist[w] = dist[v] + 1
                queue.append(w)

    return dist

# ==============================
# MAIN
# ==============================
def main():
    # caminho do arquivo
    G = read_graph("C:\\Users\\arthu\\Downloads\\t2-cavalo\\dados\\entrada.txt")

    # 🔹 Lista de adjacência
    print("Lista de adjacência:")
    G.print_graph()

    # 🔹 Componentes conexas
    cc = CC(G)
    print("\nComponentes conexas:", cc.count)

    for i in range(cc.count):
        print(f"Componente {i}:", end=" ")
        for v in range(G.V):
            if cc.id[v] == i:
                print(v, end=" ")
        print()

    # 🔹 Distância mínima (0 -> 8)
    dist = bfs(G, 0)
    print("\nDistância mínima de 0 até 8:", dist[8])

    # 🔹 Ciclo
    cycle = Cycle(G)
    print("\nPossui ciclo:", "Sim" if cycle.cycle else "Não")

    if cycle.cycle:
        print("Vértices do ciclo encontrado:", " ".join(map(str, cycle.cycle)))
    
    print("\nAnálise de complexidade:")
    print(f"Tempo: O(V + E) = O({G.V} + {sum(len(adj) for adj in G.adj)//2})")
    print("Espaço: O(V) =", G.V)


# ==============================
# Execução
# ==============================
if __name__ == "__main__":
    main()
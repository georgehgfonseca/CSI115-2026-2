# matriz de adjacencias
g0 = [[0, 0, 1, 0],
      [0, 0, 0, 1],
      [1, 0, 0, 1],
      [0, 1, 1, 0]]

# TODO verificar se 0 eh ligado ao 3
# print(g0[0][3] == 1)
# TODO adicionar aresta entre 0 e 1
g0[0][1] = 1
g0[1][0] = 1

# lista de adjacencias
g0 = {0: {2}, 1: {3}, 2: {0, 3}, 3: {1, 2}}

# print(3 in g0[0]) # 3 in {2} -> False
# TODO adicionar aresta entre 0 e 1
g0[0].add(1)
g0[1].add(0)

# TODO variavel que representa matriz e lista de adjacencias do grafo g1
g1 = [[0, 1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 1, 0],
      [0, 1, 0, 0, 1, 0],
      [0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0]]

g1 = {0: {1},
      1: {0, 5},
      2: {0, 4},
      3: {1, 4},
      4: {2},
      5: {}}

g2 = [[0, 8, 0, 0, 0, 0],
      [5, 0, 0, 0, 0, 3],
      [7, 0, 0, 0, 9, 0],
      [0, 5, 0, 0, 7, 0],
      [0, 0, 6, 0, 0, 0],
      [0, 0, 0, 0, 0, 0]]

g2 = {0: {1:8},
      1: {0:5, 5:3},
      2: {0:7, 4:9},
      3: {1:5, 4:7},
      4: {2:6},
      5: {}}

from graph import WeightedDirectedGraph, Graph

g0 = WeightedDirectedGraph()
g0.add_edge(0, 1, 8)
g0.add_edge(1, 0, 5)
g0.add_edge(2, 0, 7)
g0.add_edge(2, 4, 9)
g0.add_edge(3, 1, 5)
g0.add_edge(3, 4, 7)
g0.add_edge(4, 2, 6)

g0 = Graph()
g0.add_edge(0, 2)
g0.add_edge(2, 3)
g0.add_edge(1, 3)
print(g0.adjList)
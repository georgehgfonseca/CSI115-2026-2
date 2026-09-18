# TODO criar grafo g3 por lista de adjacencias
from graph import Graph

g3 = Graph()
g3.add_edge(0, 1)
g3.add_edge(0, 2)
g3.add_edge(0, 3)
g3.add_edge(1, 2)
g3.add_edge(1, 3)
g3.add_edge(2, 3)

# ou, sem orientacao a objetos:
# g3 = {0: {1, 2, 3}, 1: {0, 2, 3}, 2: {0, 1, 3}, 3: {0, 1, 2}}

# TODO implementar função que recebe um grafo, nós u e v e remove a aresta (u, v) e (v, u), se existir
print(g3.adjList)
g3.remove_edge(5, 1)
print(g3.adjList)

# TODO implementar função que recebe um grafo, um nó e retorna seu grau
assert g3.degree(2) == 3

# TODO implementar função que recebe um grafo e retorna o nó com maior grau
assert g3.highest_degree() in {0, 1, 2, 3}

g4 = Graph()
g4.add_edge(0, 1)
g4.add_edge(0, 2)
g4.add_edge(0, 3)
g4.add_edge(1, 3)
assert g4.highest_degree() == 0

# TODO implementar função que recebe um grafo e retorna se é completo
assert g3.is_complete() == True
assert g4.is_complete() == False

# TODO implementar função que recebe um grafo e retorna se é regular

# TODO implementar função que recebe um grafo e retorna se é simples (não tem arestas múltiplas e não tem laços)

# TODO implementar função que recebe um grafo g e outro grafo h e retorna g é subgrafo de h


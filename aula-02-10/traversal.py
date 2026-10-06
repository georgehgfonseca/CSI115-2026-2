def bfs(graph, source):
    visited = set()
    queue = [source]
    visited.add(source)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def dfs(graph, source):
    visited = {source}

    def aux(node):
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                aux(neighbor)

    aux(source)


def dfs_iterative(graph, source):
    visited = set()
    stack = [source]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


graph = {
    0: {3, 5, 6},
    1: {4},
    2: {1, 4},
    3: {6},
    4: {},
    5: {7},
    6: {8},
    7: {0, 1},
    8: {}
}

bfs(graph, 0)
print()
dfs(graph, 0)
print()
dfs_iterative(graph, 0)
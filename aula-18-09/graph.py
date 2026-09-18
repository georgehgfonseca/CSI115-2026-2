class WeightedDirectedGraph:
    def __init__(self):
        self.adjList = {}

    def add_edge(self, source, sink, weight):
        if source not in self.adjList:
            self.adjList[source] = dict()

        self.adjList[source][sink] = weight

class Graph:
    def __init__(self):
        self.adjList = {}

    def add_edge(self, source, sink):
        if source not in self.adjList:
            self.adjList[source] = set()

        self.adjList[source].add(sink)

        if sink not in self.adjList:
            self.adjList[sink] = set()

        self.adjList[sink].add(source)
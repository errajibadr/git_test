from collections import defaultdict

 

class Graph:

    

    def __init__(self):

        self.graph = defaultdict(list)
        
    def __str__(self):

        nodes = set()

        self.__dfs_util(0, nodes)

        return "Graph({})".format(", ".join([str(i) for i in list(nodes)]))

 

    def add_edge(self, u, v):
        self.graph[u].append(v)

 
    def dfs_rec(self, v, nodes):

            nodes.add(v)

            for adj in self.graph[v]:

                if adj not in nodes:

                    self.dfs_rec(nb, nodes)


    def dfs(self, v):

        visited = set()

        self.__dfs_util(v, visited)

        

g = Graph()

g.add_edge(0, 1)

g.add_edge(0, 2)

g.add_edge(1, 2)

g.add_edge(2, 0)

g.add_edge(2, 3)

g.add_edge(3, 3)

 

print("DSF à partir du noeud 0 :")

g.dfs(0)
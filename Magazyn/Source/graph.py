#from .general import Point

class Graph:
    nodes = dict()
    size = 0

    def __init__(self):
        pass

    def addNode(self, p):
        n = dict()
        self.nodes.update({p: n})
        self.size = self.size+1
        pass

    def addConnection(self, cost, p1, p2):
        self.nodes.get(p1).update({p2: cost})
        self.nodes.get(p2).update({p1: cost})
        pass

    def returnConnections(self, p):
        return self.nodes.get(p, None)
        pass

    def findPathDijkstra(self, pOrigin, pDest):
        #####inicjalizacja
        properPath = []
        follower = dict()
        unvisitedNodes = set()
        for k in self.nodes.keys():
            unvisitedNodes.add(k)


        values = [[0 for x in range(len(unvisitedNodes))] for y in range(2)]
        valuesDict = dict()
        i = 0
        for p in unvisitedNodes:
            values[i][1] = p
            valuesDict.update({p: i})
            if p == pOrigin:
                values[i][2] = 0
            else:
                values[i][2] = 1e10

        i = 0
        while unvisitedNodes != set():
            ######Znalezienie najmniejszego elementu
            u = 1e10+1
            k = 0
            for i in range(len(values)):
                if u > values[i][2]:
                    u = values[i][2]
                    k = i
            #usunięcie elementu o najmniejszej odległości z nieodwiedzonych elementów
            unvisitedNodes.discard(values[k][1])

            subset = set()
            for k in self.nodes.get(values[k][1], None).keys(): ###Tu skończyłem
                if k != None:
                    subset.add(k)

            #dla każdego sąsiada wybranego wierzchołka:
            for p in subset:
                if valuesDict.get(p, None) > values[k][2]+self.nodes.get(p,None).get(values[k][1]):
                    values[valuesDict.get(p, None)][2] = values[k][2]+self.nodes.get(p,None).get(values[k][1])
                    follower.update({p: values[k][1]})
                    unvisitedNodes.add(p)

        return follower

G = Graph()

G.addNode("x")
G.addNode("y")
G.addNode("z")
G.addNode("a")
G.addNode("b")


G.addConnection(1, "x", "a")

G.addConnection(2, "y", "a")

G.addConnection(3, "z", "a")

G.addConnection(4, "b", "a")

dictionary = G.returnConnections("a")
for k,v in dictionary.items():
    print(k, v)
print("przerwa")
dictionary = G.returnConnections("x")
for k,v in dictionary.items():
    print(k, v)

dictionary = G.findPathDijkstra("x", "y")
for k, v in dictionary.items():
    print(k, v)
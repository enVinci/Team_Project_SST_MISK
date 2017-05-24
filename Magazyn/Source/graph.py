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
        self.nodes.get(p1).update({p2: float(cost)})
        self.nodes.get(p2).update({p1: float(cost)})
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

        values = list()
        valuesDict = dict()

        i = 0
        for p in unvisitedNodes:
            valuesDict.update({p: i})
            # values[i][0] = p
            if p == pOrigin:
                values.append([p, 0.0])
                # values[i][1] = 0.0
            else:
                values.append([p, 1e3])
                # values[i][1] = 0.0
            i = i + 1

        while unvisitedNodes != set():
            # values = [[0] * len(unvisitedNodes) for i in range(2)]
            values2 = []
            valuesDict2 = dict()
            i = 0
            for p in unvisitedNodes:
                valuesDict2.update({p: i})
                # values[i][0] = p
                values2.append([p, values[valuesDict.get(p, None)][1]])
                i = i + 1

            # print("wtf ", values[0][0])

            ######Znalezienie najmniejszego elementu
            u = 1e10+1
            k = 0
            for i in range(len(values2)):
                if u > values2[i][1]:
                    u = values2[i][1]
                    k = i

            if values2[k][0] == pDest:
                p1 = pDest
                path = list()
                cost = 0
                while follower != dict() and p1 != None:
                    path.append(p1)
                    p2 = p1
                    p1 = follower.pop(p1, None)
                    if(p1 == pOrigin):
                        path.append(p1)
                        cost = cost+self.nodes.get(p2,None).get(p1)
                        break
                    c1 = self.nodes.get(p2, None)
                    if c1 != None:
                        cost = cost + c1.get(p1)
                return (path, cost)

            #usunięcie elementu o najmniejszej odległości z nieodwiedzonych elementów
            unvisitedNodes.discard(values2[k][0])

            #uzyskanie listy sąsiadów z nieodwiedzonych elementów
            a = self.nodes.get(values2[k][0])

            subset = set()
            for k1 in a.keys():
                subset.add(k1)

            #dla każdego sąsiada wybranego wierzchołka:
            for p in subset:
                if valuesDict2.get(p, None) != None:
                    a1 = values2[valuesDict2.get(p, None)][1]
                    a2 = values2[k][1]+self.nodes.get(p,None).get(values2[k][0])
                    if a1 > a2:
                        a3 = values2[k][1]
                        a3 += self.nodes.get(p,None).get(values2[k][0])
                        values[valuesDict.get(p, None)][1] = a2

                        values2[valuesDict2.get(p, None)][1] = a2
                        follower.pop(p, None)
                        follower.update({p: values2[k][0]})
                        unvisitedNodes.add(p)

        p1 = pDest
        path = list()
        cost = 0
        while follower != dict() and p1 != None:
            path.append(p1)
            p2 = p1
            p1 = follower.pop(p1, None)
            if(p1 == pOrigin):
                path.append(p1)
                cost = cost+self.nodes.get(p2,None).get(p1)
                break
            c1 = self.nodes.get(p2,None)
            if c1 != None:
                cost = cost+c1.get(p1)
        return (path, cost)


G = Graph()

G.addNode("a")
G.addNode("b")
G.addNode("c")
G.addNode("d")
G.addNode("e")
G.addNode("f")
G.addNode("g")
G.addNode("h")

# G.addConnection(1, "a", "b")
# G.addConnection(2, "b", "c")
# G.addConnection(1, "c", "d")
# G.addConnection(2, "c", "e")
# G.addConnection(1, "e", "g")
# G.addConnection(3, "g", "b")
# G.addConnection(1, "f", "g")
# G.addConnection(4, "a", "g")

G.addConnection(1, "a", "b")
G.addConnection(1, "c", "b")
G.addConnection(3, "d", "b")
G.addConnection(1, "e", "b")
G.addConnection(1, "f", "b")
G.addConnection(1, "g", "b")
G.addConnection(1, "h", "b")
G.addConnection(1, "h", "d")

tup = G.findPathDijkstra("a", "d")
l = tup[0]
for k in l:
    print(k)
print("koszt:", tup[1])
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
            print()
            print()
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
            print("wypisanie elementow:", values2)

            ######Znalezienie najmniejszego elementu
            u = 1e10+1
            k = 0
            for i in range(len(values2)):
                if u > values2[i][1]:
                    u = values2[i][1]
                    k = i
            print()
            if values2[k][0] == pDest:
                p1 = pDest
                path = list()
                while p1 != pOrigin:
                    print("Końcowa trasa:", p1)
                    path.append(p1)
                    p1 = follower.get(p1)
                path.append(pOrigin)
                return path
            print("najmniejszy element:", k, ", stąd mamy punkt: ", values2[k][0])

            #usunięcie elementu o najmniejszej odległości z nieodwiedzonych elementów
            unvisitedNodes.discard(values2[k][0])

            #uzyskanie listy sąsiadów z nieodwiedzonych elementów
            a = self.nodes.get(values2[k][0])

            subset = set()
            for k1 in a.keys():
                subset.add(k1)

            #dla każdego sąsiada wybranego wierzchołka:
            for p in subset:
                print("Element zbioru: ", p)
                if valuesDict2.get(p, None) != None:
                    a1 = values2[valuesDict2.get(p, None)][1]
                    a2 = values2[k][1]+self.nodes.get(p,None).get(values2[k][0])
                    print("porównanie", a1, a2)
                    if a1 > a2:
                        print("Element zbioru o mniejszej odległości: ", p)
                        a3 = values2[k][1]
                        a3 += self.nodes.get(p,None).get(values2[k][0])
                        # print("test3: ", a3, ", ", type(a3))
                        print("test1: ", values2[valuesDict2.get(p, None)][1])
                        values[valuesDict.get(p, None)][1] = a2

                        # print("test test", valuesDict2.get(p, None))

                        values2[valuesDict2.get(p, None)][1] = a2
                        print("test2: ", values2[valuesDict2.get(p, None)][1])
                        follower.pop(p, None)
                        follower.update({p: values2[k][0]})
                        unvisitedNodes.add(p)

        return follower

G = Graph()

G.addNode("1")
G.addNode("2")
G.addNode("3")
G.addNode("4")
G.addNode("5")
G.addNode("6")
G.addNode("7")
G.addNode("8")


G.addConnection(1, "1", "2")
G.addConnection(1, "2", "3")
G.addConnection(1, "3", "8")
G.addConnection(2, "7", "8")
G.addConnection(2, "1", "4")
G.addConnection(2, "4", "5")
G.addConnection(1, "4", "6")
G.addConnection(2, "7", "6")

# dictionary = G.returnConnections("a")
# for k,v in dictionary.items():
#     print(k, v)
# print("przerwa")
# dictionary = G.returnConnections("x")
# for k,v in dictionary.items():
#     print(k, v)

Path = G.findPathDijkstra("1", "7")
for k in Path:
    print(k)
from .general import Point
from .general import Path

class Dimentions:
    pathSpace = 1.5
    dimX = 0
    dimY = 0
    space = 0
    rowsNumber = 0
    columnsCount = 0
    
    def __init__(self, dimX, dimY = None, space = None, rowsNumber = None, columnsNumber = None, pathSpace = 1.5):
        if isinstance(dimX, Dimentions):
            self.init2(dimX)
        else:
            self.dimX = dimX
            self.dimY = dimY
            self.space = space
            self.rowsNumber = rowsNumber
            self.columnsCount = columnsNumber
    
    def init2(self, dim):
        self.dimX = dim.getDimX()
        self.dimY = dim.getDimY()
        self.space = dim.getSpace()
        self.rowsNumber = dim.getRowsCount()
        self.columnsCount = dim.getColumnsCount()
    
    def getDimX(self):# zwraca szerokosc pojedynczego obiektu w bloku
        return self.dimX
    
    def getDimY(self):# zwraca dlugosc pojedynczego obiektu w bloku
        return self.dimY
    
    def getSpace(self):# zwraca odstep pomiedzy pojedynczymi obiektami w bloku
        return self.space
    
    def getRowsCount(self):# zwraca ilosc wierszy w bloku obiektow
        return self.rowsNumber
    
    def getColumnsCount(self):# zwraca ilosc kolumn w bloku obiektow
        return self.columnsCount

class BlockOfPaletts(Dimentions):
    points = []
    
    def __init__(self, point1, point2, point3, point4, dim):# 4 wspolrzedne wierzcholkowych palet w bloku
        self.points.append(point1)
        self.points.append(point2)
        self.points.append(point3)
        self.points.append(point4)
        Dimentions.__init__(self, dim)
    
    def getPoint(self, pointNum):
        if pointNum < len(self.points):
            return self.points[pointNum]
        else:
            return None

class CreatePaths:
    blocks = []
    paths = []
    
    def addBlock(self, block):
        self.blocks.append(block)
        
    def createPathsAroundBlock(self, block):# zaimplementowac
        i = 0
        p2 = block.getPoint(i)
        l = list()
        l.append(p2)
        while p2!= None:
            #Będą tylko 4 punkty o różnych kombinacjach dwóch wartości x i y, więc można sobie uprościć
            i+=1
            p1 = block.getPoint(i)
            if p1.getY() < l.get(0).getY():
                if p1.getX() < l.get(i-1).getX():
                    l.append(p1)
                else:
                    l.insert(p1,i-1)
            else:
                if p1.getX() > l.get(0).getX():
                    l.insert(p1,0)
                else:
                    l.insert(p1,1)
        space = block.getSpace()+block.getDimX()
        pathSpace = block.getSpace
        for i in range(8):
            self.paths.append(Path(Point(l.get(0).getX()-pathSpace, l.get(0).getY()), Point(l.get(0).getX()+i*space, l.get(0).getY()), self.pathID))
        for i in range(8):
            self.paths.append(Path(Point(l.get(1).getX()+pathSpace, l.get(1).getY()), Point(l.get(0).getX()+(i+8)*space, l.get(0).getY()), self.pathID))
        for i in range(8):
            self.paths.append(Path(Point(l.get(2).getX()-pathSpace, l.get(2).getY()), Point(l.get(2).getX()+i*space, l.get(2).getY()), self.pathID))
        for i in range(8):
            self.paths.append(Path(Point(l.get(3).getX()+pathSpace, l.get(3).getY()), Point(l.get(2).getX()+(i+8)*space, l.get(2).getY()), self.pathID))
        self.pathID += 1
        # for i in range(4):
        #     p1 = l[i]
        #     p2 = l[(i+1)%4]
        #     if p1.getX() < p2.getX():
        #         self.paths.append(Path(p1,p2))
        #     elif p1.getX() > p2.getX():
        #         self.paths.append(Path(p2,p1))
        #     elif p1.getY() < p2.getY():
        #         self.paths.append(Path(p1,p2))
        #     elif p1.getY() > p2.getY():
        #         self.paths.append(Path(p2,p1))

        pass#dodaje utworzone sciezki wokol pojedynczego bloku palet do listy paths
    
    def createPathsAroundBlockNum(self, blockNum):
        self.pathID = 0
        if blockNum < len(self.blocks):
            self.createPathsAroundBlock(self.blocks[blockNum])
    
    def createPathsAroundBlocks(self):
        for block in self.blocks:
            self.createPathsAroundBlock(block)
            
    def getPaths(self):
        return self.paths

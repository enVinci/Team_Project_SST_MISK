from general import Point
from general import Path

class Dimentions:
	dimX = 0
	dimY = 0
	space = 0
	objectCount = 0
	
	def __init__(self, dimX, dimY = None, space = None, objectCount = None):
		if isinstance(dimX, Dimentions):
		      self.init2(dimX)
		else:
		      self.dimX = dimX
		      self.dimY = dimY
		      self.space = space
		      self.objectCount = objectCount
		
	def init2(self, dim):
		self.dimX = dim.getDimX()
		self.dimY = dim.getDimY()
		self.space = dim.getSpace()
		self.objectCount = dim.getObjectCount()
	
	def getDimX(self):# zwraca szerokosc pojedynczego obiektu w bloku
		return self.dimX
	
	def getDimY(self):# zwraca dlugosc pojedynczego obiektu w bloku
		return self.dimY
	
	def getSpace(self):# zwraca odstep pomiedzy pojedynczymi obiektami w bloku
		return self.space
	
	def getObjectCount(self):# zwraca ilosc obiektow w bloku
		return self.objectCount

class BlockOfPaletts(Dimentions):
	points = []
	
	def __init__(self, point1, point2, point3, point4, dim):
		self.points.append(point1)
		self.points.append(point2)
		self.points.append(point3)
		self.points.append(point4)
		Dimentions.__init__(self, dim)
	
	def getPoint(self, pointNum):
		if pointNum < len(self.points):
			return self.points[pointNum]

class CreatePaths:
	blocks = []
	paths = []
	
	def addBlock(self, block):
		self.blocks.append(block)
		
	def createPathsAroundBlock(self, block):# zaimplementowac
		pass#dodaje utworzone sciezki wokol pojedynczego bloku palet do listy paths
	
	def createPathsAroundBlockNum(self, blockNum):
		if blockNum < len(self.blocks):
			self.createPathsAroundBlock(self.blocks[blockNum])
	
	def createPathsAroundBlocks(self):
		for block in self.blocks:
			self.createPathsAroundBlock(block)
			
	def getPaths(self):
		return self.paths

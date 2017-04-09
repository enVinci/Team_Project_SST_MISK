from enum import Enum
import math

class Robots(Enum):
    Robot1 = 1
    Robot2 = 2
    Robot3 = 3
    Robot4 = 4
    Robot5 = 5
    Robot6 = 6
    
    def __int__(self):
        return self.value
  
class Stations(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    
    def __int__(self):
        return self.value

class StationBuffors(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    
    def __int__(self):
        return self.value
  
class Dockstations(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    
    def __int__(self):
	return self.value
  
class PaletteAction(Enum):
    onRobot = 1
    inStation = 2
    inBufferPos1 = 3
    inBufferPos2 = 4
    isReady = 5
  
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y
      
    def set(self, x, y):
	self.x = x
	self.y = y

    def distance(self, other):
      dx = self.x - other.x
      dy = self.y - other.y
      return math.hypot(dx, dy)
    
    def rotate(self, other):
	pass
  
class Path:
    startPosition = Point()
    endPosition = Point()
    
    def __init__(self, startPosition, endPosition):
	self.startPosition = startPosition
	self.endPosition = endPosition
    
    def getStartPosition(self):
	return self.startPosition
    
    def getEndPosition(self):
	return self.endPosition
    
    def getDistance(self):
	return self.startPosition.distance(self.endPosition)
    
    def getRotate(self):
	pass

class Palette:
    beginPosition = Point()
    actualPosition = Point()
    
    def __init__(self, beginPosition):
	self.actualPosition = self.beginPosition = beginPosition
	self.action = PaletteAction.isReady
    
    def changePosition(self, position):
	self.actualPosition = position
    
    def getPosition(self):
	return self.actualPosition
    
    def setAction(self, action):
	self.action = action
    
    def getAction(self):
	return self.action
    
    def isReady(self):
	return self.action == PaletteAction.isReady

class Place:
    def __init__(self, position, pathId):
	self.position = position
	self.pathId = pathId

class Station:
    def __init__(self, serviceTime, position, pathId):
	self.serviceTime = serviceTime
	self.position = position
	self.pathId = pathId

class DockStation:
    def __init__(self, position, pathId):
	self.position = position
	self.pathId = pathId

class StationBuffor:
    position1 = Point()
    position2 = Point()
    
    def __init__(self, position1, position2):
	self.position1 = position1
	self.position2 = position2
    
    def getPosition1(self):
	return self.position1
      
    def getPosition2(self):
	return self.position2

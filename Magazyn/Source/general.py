# -*- coding: utf-8 -*-
from enum import Enum
import math
import vrep
import vrepConst
import globalVar

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

class TaskType(Enum):
	TAKE_ITEM = 0
	PUT_ITEM = 1
	INSPECTION = 2

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
	
	def __init__(self, startPosition, endPosition, nextPath1Id, nextPath2Id=0):
		self.startPosition = startPosition
		self.endPosition = endPosition
		self.nextPath1Id = nextPath1Id
		self.nextPath2Id = nextPath2Id
	
	def getStartPosition(self):
		return self.startPosition
	
	def getEndPosition(self):
		return self.endPosition
	
	def getDistance(self):
		return self.startPosition.distance(self.endPosition)
	
	def getRotate(self):
		pass

class PathWay:
	paths = []
	index = 0;
	
	def __init__(self):
		pass
	
	def addPath(self, pathId):
		self.paths.append(pathId)
	
	def nextPath(self):
		if (self.index < self.length()):
			return self.paths[self.index]
		else:
			return Path(Point(0,0), Point(0,0), 0)
	
	def length(self):
		return self.paths.count()


class Palette:
	beginPosition = Point()
	actualPosition = Point()
	name = ""
	handler = 0
	
	def __init__(self, beginPosition, vrepName):
		self.actualPosition = self.beginPosition = beginPosition
		self.action = PaletteAction.isReady
		self.name = vrepName
		errorCode,self.handler=vrep.simxGetObjectHandle(GlobalVar.vrepClientID,vrepName,vrepConst.simx_opmode_oneshot_wait)
	
	def updatePosition(self):
		errorCode, Position = vrep.simxGetObjectPosition(GlobalVar.vrepClientID, self.handler, -1, vrepConst.simx_opmode_oneshot_wait)
		self.actualposition.x = Position[0]
		self.actualposition.y = Position[1]
	
	def getPosition(self):
		return self.actualPosition
	
	def getName(self):
		return self.name
	
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
	
	def getPosition(self):
		return self.position
	
	def getPath(self):
		return self.pathId

class Station:
	def __init__(self, serviceTime, position, pathId):
		self.serviceTime = serviceTime
		self.position = position
		self.pathId = pathId
	
	def getPosition(self):
		return self.position
	
	def getPath(self):
		return self.pathId

class DockStation:
	def __init__(self, position, pathId):
		self.position = position
		self.pathId = pathId
	
	def getPosition(self):
		return self.position
	
	def getPath(self):
		return self.pathId

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

class Task:
	def __init__(self, availabilityTime, priority, taskType, paletteId, station):
		self.availabilityTime = availabilityTime
		self.priority = priority
		self.taskType = taskType
		self.paletteId = paletteId
		self.station = station

	def getAvailabilityTime(self):
		return self.availabilityTime

	def getPriority(self):
		return self.priority

	def getTaskType(self):
		return self.taskType

	def getPaletteId(self):
		return self.paletteId

	def getDestinationStation(self):
		return self.station

	def printTask(self):
		print(self.availabilityTime, self.priority, self.taskType, self.paletteId, self.station)


def openTasks(filename):
	lines = []
	with open(filename) as zadania:
		linie = zadania.readlines()
		for linia in linie:
			linia = linia.split()
			if linia[0].isdigit():
				linia = ' '.join(linia)
				linie = linia.split(';')
				for line in linie[0:-1]:
					line = line.split()
					line = list(map(int, line))
					if len(line) == 5:
						lines.append(line)

	tab = []

	TTypes = [enum.value for enum in TaskType]
	TEnums = [enum for enum in TaskType]

	STypes = [enum.value for enum in Stations]
	SEnums = [enum for enum in Stations]

	for line in lines:
		if line[0] < 0:
			continue
		elif line[1] not in range(4):
			continue
		elif line[2] not in [enum.value for enum in TaskType]:
			continue
		elif line[3] not in range(1, 129):
			continue
		elif line[4] not in [enum.value for enum in Stations]:
			continue
		else:
			tab.append(Task(line[0], line[1], TEnums[TTypes.index(line[2])], line[3], SEnums[STypes.index(line[4])]))
	return tab


def GetTasksByStation(tab, station):
	tasks = []
	for task in tab:
		if task.getDestinationStation() == station:
			tasks.append(task)
	return tasks

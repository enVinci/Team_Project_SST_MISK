# -*- coding: utf-8 -*-
from Source import *
from Source import vrep
from Source import vrepConst
from Source import openTasks, GetTasksByStation
from Source import Stations

def getObjectPosition(name):
	errorCode, handle = vrep.simxGetObjectHandle(GlobalVar.vrepClientID, name, vrepConst.simx_opmode_oneshot_wait)
	errorCode, Position = vrep.simxGetObjectPosition(GlobalVar.vrepClientID, handle, -1, vrepConst.simx_opmode_oneshot_wait)
	return Point(Position[0], Position[1])

def getObjectPositionsList(NamesList):
	positionList = []
	for name in NamesList:
		positionList.append(getObjectPosition(name))
	return positionList

# create paths
d = Dimentions(4, 5, 1, 16)
print(d.getDimX())
b = BlockOfPaletts(Point(1,1), Point(14,1), Point(14,6), Point(1,6), d)
print(b.getDimX())
p = CreatePaths()
p.addBlock(b)
p.createPathsAroundBlocks()

#wyświetlenie zadań przydzielonych każdej stacji

Tab = openTasks("zadania.txt")

#wyświetlanie wszystkich stacji

for enum in Stations:
	print(enum)
	t = GetTasksByStation(Tab, enum)
	for task in t:
		task.printTask()


#wyświetlanie konkretnej stacji, odkomentować jak potrzebne

#print(Stations.A)
#t = GetTasksByStation(Tab, Stations.A)
#for task in t:
#task.printTask()

# start symulation
port = 19999
vrep.simxFinish(-1) # just in case, close all opened connections
GlobalVar.vrepClientID = vrep.simxStart('127.0.0.1',port,True,True,5000,5) # Connect to V-REP
if GlobalVar.vrepClientID == -1:
	print('Failed connecting to remote API server')
	exit()

robot = MoveRobot("Pioneer_p3dx_0")

robot.setSpeed(12)
robot.goToDestinationPoint(Point(23,55))
robot.rotate(90)
robot.goToDestinationPoint(Point(23,55))

moveRobotinStorehouse = MoveRobotsInStorehouse()
moveRobotinStorehouse.setSpeed(Robots.Robot1, 12)

places = []
pointList = getObjectPositionsList(palletNames)
for i in range(len(pointList)):
	places.append(Place(pointList[i], i))
storehouse = Storehouse(places, palletNames, stations, dockStations, stationBuffors, paths)
print(storehouse.getPalletePosition(0).getX(), storehouse.getPalletePosition(0).getY())
print(storehouse.getStationPosition(Stations.A).getX(), storehouse.getStationPosition(Stations.A).getY())

vrep.simxFinish(GlobalVar.vrepClientID)
print('Goodbye ;)')

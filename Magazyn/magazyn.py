# -*- coding: utf-8 -*-
#from .Source import *
from Source import graph
from Source import vrep
from Source import vrepConst
from Source import globalVar
from Source.general import Point
from Source.createPaths import *
from Source.moveRobot import MoveRobot
from Source.moveRobotsInStorehouse import MoveRobotsInStorehouse
from Source.storehause import Storehouse
from Source.general import Place
from Source.general import openTasks, GetTasksByStation
from Source.general import Stations
from Source import positions

def getObjectPosition(name):
    errorCode, handle = vrep.simxGetObjectHandle(globalVar.vrepClientID, name, vrepConst.simx_opmode_oneshot_wait)
    errorCode, Position = vrep.simxGetObjectPosition(globalVar.vrepClientID, handle, -1, vrepConst.simx_opmode_oneshot_wait)
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
port = 19997
vrep.simxFinish(-1) # just in case, close all opened connections
globalVar.vrepClientID = vrep.simxStart('127.0.0.1',port,True,True,5000,5) # Connect to V-REP

#####################Inicjalizacja ścieżek i grafu

blockPaths = p.getPaths()
for pt in blockPaths:
    positions.paths.append(pt)

storehouseGraph = graph.Graph()

for pt in positions.paths:
    p1 = pt.getStartPosition()
    p2 = pt.getEndPosition()
    storehouseGraph.addNode(p1)
    storehouseGraph.addNode(p2)
    storehouseGraph.addConnection(p1.distance(p2), p1, p2)

##################################################Testy grafu
print("Punkty:")
print(len(positions.paths))
print("długość", len(storehouseGraph.nodes))
print("x =", positions.paths[1].getStartPosition().getX(), ", y =", positions.paths[1].getStartPosition().getY())
print("x =", positions.paths[150].getEndPosition().getX(), ", y =", positions.paths[150].getEndPosition().getY())
print(positions.paths[247].getEndPosition())
print('#####################')
print(storehouseGraph)
print('#####################')

tup = storehouseGraph.findPathDijkstra(positions.paths[1].getStartPosition(), positions.paths[150].getEndPosition())
l = tup[0]
print("trasa")
for k in l:
    print(k.getX(), " ", k.getY())
print("koszt:", tup[1])
#######################Koniec testów i inicjalizacji

if globalVar.vrepClientID == -1:
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

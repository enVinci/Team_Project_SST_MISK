from Source import *
from Source import vrep

# create paths
d = Dimentions(4, 5, 1, 16)
print(d.getDimX())
b = BlockOfPaletts(Point(1,1), Point(14,1), Point(14,6), Point(1,6), d)
print(b.getDimX())
p = CreatePaths()
p.addBlock(b)
p.createPathsAroundBlocks()

# start symulation
port = 19999
vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',port,True,True,5000,5) # Connect to V-REP
if clientID!=-1:

    robot = MoveRobot("Pioneer_p3dx_0", clientID)

    robot.setSpeed(12)
    robot.goToDestinationPoint(Point(23,55))
    robot.rotate(90)
    robot.goToDestinationPoint(Point(23,55))

    moveRobotinStorehouse = MoveRobotsInStorehouse()
    moveRobotinStorehouse.setSpeed(Robots.Robot1, 12)

    storehouse = Storehouse(places, palletNames, stations, dockStations, stationBuffors, paths)
    print(storehouse.getPalletePosition(0).getX(), storehouse.getPalletePosition(0).getY())
    print(storehouse.getStationPosition(Stations.A).getX(), storehouse.getStationPosition(Stations.A).getY())

    # Now close the connection to V-REP:
    vrep.simxFinish(clientID)
else:
    print('Failed connecting to remote API server')
print('Program ended')

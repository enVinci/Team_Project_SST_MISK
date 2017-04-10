from Source import *

robot = MoveRobot("Pioneer_p3dx")

robot.setSpeed(12)
robot.goToDestinationPoint(Point(23,55))
robot.rotate(90)
robot.goToDestinationPoint(Point(23,55))

moveRobotinStorehouse = MoveRobotsInStorehouse()
moveRobotinStorehouse.setSpeed(Robots.Robot1, 12)

storehouse = Storehouse(places, palletNames, stations, dockStations, stationBuffors, paths)
print(storehouse.getPalletePosition(0).getX(), storehouse.getPalletePosition(0).getY())
print(storehouse.getStationPosition(Stations.A).getX(), storehouse.getStationPosition(Stations.A).getY())
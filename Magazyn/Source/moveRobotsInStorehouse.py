from .robotInStorehouse import RobotInStorehouse
from .general import Robots
from .positions import robotNames

class MoveRobotsInStorehouse:    
    def __init__(self):
        self.robots = [ RobotInStorehouse(robotNames[i]) for i in range(len(Robots))]
    
    def getPalette(self, robotName, paletteId):
    	pass
      
    def putPalette(self, robotName, paletteId):
    	pass
      
    def goToStation(self, robotName, stationName):
	    pass
      
    def goToDockStation(self, robotName, dockStationName):
    	pass
      
    def setSpeed(self, robotName, velocity):
    	self.robots[int(robotName)].setSpeed(velocity)
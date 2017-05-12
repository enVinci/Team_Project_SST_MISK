from .robotInStorehouse import RobotInStorehouse
from .general import *
from .positions import *

class MoveRobotsInStorehouse:
    def __init__(self):
        self.robots = [ RobotInStorehouse(robotNames[i]) for i in range(len(Robots))]

    def getPalette(self, robotName, paletteId):
        #określenie pozycji palety
        errorCode, handle = vrep.simxGetObjectHandle(GlobalVar.vrepClientID, palletNames[paletteId], vrepConst.simx_opmode_oneshot_wait)
        errorCode, Position = vrep.simxGetObjectPosition(GlobalVar.vrepClientID, handle, -1,
                                                         vrepConst.simx_opmode_oneshot_wait)
        targetPoint = Point(Position[0], Position[1])

        #jak dojedzie
        self.robots[int(robotName)].joinPallete(paletteId)
        pass
	
	def putPalette(self, robotName, paletteId):
		pass
	
	def goToStation(self, robotName, stationName):
		pass
	
	def goToDockStation(self, robotName, dockStationName):
		pass
	
	def setSpeed(self, robotName, velocity):
		self.robots[int(robotName)].setSpeed(velocity)

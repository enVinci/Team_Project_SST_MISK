# -*- coding: utf-8 -*-
from .robotInStorehouse import RobotInStorehouse
from .general import *
from .positions import *
from .vrep import *
from .vrepConst import *

class MoveRobotsInStorehouse:
    def __init__(self):
        self.robots = [ RobotInStorehouse(robotNames[i]) for i in range(len(Robots))]

    def getPalette(self, robotName, paletteId):
        #określenie pozycji palety
        if  self.robots[int(robotName)].isReady == 0:
            return 1
        errorCode, handle = simxGetObjectHandle(GlobalVar.vrepClientID, palletNames[paletteId], simx_opmode_oneshot_wait)
        errorCode, Position = simxGetObjectPosition(GlobalVar.vrepClientID, handle, -1,
                                                         simx_opmode_oneshot_wait)
        targetPoint = Point(Position[0], Position[1])

        #jak dojedzie
        self.robots[int(robotName)].joinPallete(paletteId)
        return 0
        pass
    
    def putPalette(self, robotName, paletteId):
        if  self.robots[int(robotName)].isReady == 0:
            return 1
        if self.robots[int(robotName)].hasPalette == 0:
            return 2
        #### Jakaś magia z dojazdami
        self.robots[int(robotName)].unjoinPallete(paletteId)
        pass
    
    def goToStation(self, robotName, stationName):
        pass
    
    def goToDockStation(self, robotName, dockStationName):
        pass
    
    def setSpeed(self, robotName, velocity):
        self.robots[int(robotName)].setSpeed(velocity)

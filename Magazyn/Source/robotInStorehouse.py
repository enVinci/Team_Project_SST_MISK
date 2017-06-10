# -*- coding: utf-8 -*-
from Source import moveRobot
from .vrep import *
from  .vrepConst import *
from .globalVar import GlobalVar
from .positions import *
from .general import Point
import math

class RobotInStorehouse:
    hasPalette = 0
    def __init__(self, name):
        self.robot = MoveRobot(name)
    
    def goOnPath(self, pathId):
        targetPoint = paths(pathId).getStartPosition()
        # currentPoint = self.robot.updatePosition()
        self.robot.goToDestinationPoint(targetPoint)
        # dx = targetPoint.getX()-currentPoint.getX()
        # dy = targetPoint.getY()-currentPoint.getY()
        # angle = math.atan2(dy, dx)
        # self.robot.rotate(angle * 180 / math.pi)

        pass
    
    def goPathToEnd(self, pathId):
        targetPoint = paths(pathId).getDestinationPosition()
        self.robot.goToDestinationPoint(targetPoint)
        pass
    
    def goOutOfPath(self, paletteId):
        errorCode, paletteHandle = simxGetObjectHandle(GlobalVar.vrepClientID,
                                    palletNames(paletteId),
                                    simx_opmode_oneshot_wait)
        errorCode, position = simxGetObjectPosition(GlobalVar.vrepClientID, paletteHandle, -1, simx_opmode_oneshot_wait)
        self.robot.goToDestinationPoint(Point(position[0],position[1]))
        pass

    # Według dokumentacji to jest klasa niższego poziomu, niż moveRobotsInStorehouse, więc tutaj wykonuję wywołania
    # funkcji z v-repa podlączające i odłączające robota do i od palety

    def joinPallete(self, paletteId):
        if self.hasPalette == 1:
            pass
        errorCode, paletteHandle = simxGetObjectHandle(GlobalVar.vrepClientID,
                                                            palletNames(paletteId),
                                    simx_opmode_oneshot_wait)
        simxSetObjectParent(GlobalVar.vrepClientID, paletteHandle, self.handle, 1, simx_opmode_oneshot_wait)
        self.hasPalette = 1
        pass

    def unjoinPalette(self, paletteId):
        if self.hasPalette == 0:
            pass
        errorCode, paletteHandle = simxGetObjectHandle(GlobalVar.vrepClientID, palletNames(paletteId),
                                                            simx_opmode_oneshot_wait)
        simxSetObjectParent(GlobalVar.vrepClientID, paletteHandle, -1, 1, simx_opmode_oneshot_wait)
        self.hasPalette = 0
        pass

    def isReady(self):
        return self.robot.isReady()

    def setSpeed(self, velocity):
        self.robot.setSpeed(velocity)

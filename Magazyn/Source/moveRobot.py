from .general import Point
from .vrep import *
from .vrepConst import *
from .globalVar import GlobalVar
import math

class MoveRobot:
    position = Point()
    name = ""
    speed = 0 #prędkość robota
    handle = 0
    left_motor_handle = 0
    right_motor_handle = 0
    R = 0.09717243680870322 #promień koła
    d = 0.35414159966455727 #odstęp między kołami
    
    def __init__(self, vrepName):
        self.name = vrepName
        errorCode,self.handle=simxGetObjectHandle(GlobalVar.vrepClientID,self.name,simx_opmode_oneshot_wait)
        errorCode, self.left_motor_handle=simxGetObjectHandle(GlobalVar.vrepClientID,vrepName+'_leftMotor',simx_opmode_oneshot_wait)
        errorCode, self.right_motor_handle=simxGetObjectHandle(GlobalVar.vrepClientID,vrepName+'_rightMotor',simx_opmode_oneshot_wait)

    def goToDestinationPoint(self, destinationPoint): #zakładam, że jestem już obrócony, jeśli nie - dodam kilka linijek
        destX = destinationPoint.x
        destY = destinationPoint.y
        self.updatePosition()
        dx = destX-self.position.x
        dy = destY-self.position.y
        angle = math.atan2(dy,dx)
        returnCode, Angles = simxGetObjectOrientation(GlobalVar.vrepClientID, self.handle, -1,
                                                     simx_opmode_oneshot_wait)
        self.rotate((angle-Angles[2])*180/math.pi)
        dist = math.hypot(dx, dy)
        
        
        returnCode, rightAngle = simxGetJointPosition(GlobalVar.vrepClientID, self.right_motor_handle, simx_opmode_oneshot_wait)
        returnCode, leftAngle = simxGetJointPosition(GlobalVar.vrepClientID, self.left_motor_handle, simx_opmode_oneshot_wait)
        
        
        rightAngle += dist/self.R
        leftAngle += dist/self.R
        
        returnCode = simxSetJointTargetPosition(GlobalVar.vrepClientID, self.right_motor_handle, rightAngle, simx_opmode_oneshot_wait)
        returnCode = simxSetJointTargetPosition(GlobalVar.vrepClientID, self.left_motor_handle, leftAngle, simx_opmode_oneshot_wait)
    
    def rotate(self, degrees):
        #returnCode, Angles = simxGetObjectOrientation(GlobalVar.vrepClientID, self.handle, -1, simx_opmode_oneshot_wait)
        #ddegree = degrees-Angles[2]
        
        returnCode, rightAngle = simxGetJointPosition(GlobalVar.vrepClientID, self.right_motor_handle, simx_opmode_oneshot_wait)
        returnCode, leftAngle = simxGetJointPosition(GlobalVar.vrepClientID, self.left_motor_handle, simx_opmode_oneshot_wait)
        degrees = degrees*180/math.pi
        rightAngle = rightAngle*180/math.pi
        leftAngle = leftAngle*180/math.pi
        
        rightAngle += degrees*self.d/(2*self.R)
        leftAngle += -degrees*self.d/(2*self.R)
        
        rightAngle = rightAngle*math.pi/180
        leftAngle = leftAngle*math.pi/180
        
        returnCode = simxSetJointTargetPosition(GlobalVar.vrepClientID, self.right_motor_handle, rightAngle, simx_opmode_oneshot_wait)
        returnCode = simxSetJointTargetPosition(GlobalVar.vrepClientID, self.left_motor_handle, leftAngle, simx_opmode_oneshot_wait)
    
    def setSpeed(self, velocity):
        self.speed = velocity
    
    def updatePosition(self):
        errorCode, PioneerPosition = simxGetObjectPosition(GlobalVar.vrepClientID, self.handle, -1, simx_opmode_oneshot_wait)
        #print(errorCode, "x", PioneerPosition[0], "y", PioneerPosition[1])
        self.position.x = PioneerPosition[0]
        self.position.y = PioneerPosition[1]
        pass
    
    def getPosition(self):
        return self.position
    
    def getName(self):
        return self.name

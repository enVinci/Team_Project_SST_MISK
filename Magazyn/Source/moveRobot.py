from Source.vrep import *
from Source.vrepConst import *
from Source.globalVar import *
from Source.general import Point
from Source.globalVar import *
import math

class MoveRobot:
    position = Point()
    name = ""
    speed = 0 #prędkość robota
    handle = 0
    left_motor_handle = 0
    right_motor_handle = 0
    left_motor_target_position = 0
    right_motor_target_position = 0
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
        returnCode, Angles = simxGetObjectOrientation(GlobalVar.vrepClientID, self.handle, -1,
                                                      simx_opmode_oneshot_wait)
        # self.rotate(angle-Angles[2])
        dist = math.hypot(dx, dy)
        A1 = math.sin(Angles[2])
        B1 = -math.cos(Angles[2])
        C1 = -A1*self.position.x - B1*self.position.y

        minDist = math.fabs(A1*destX + B1*destY+C1)
        l = math.sqrt(math.pow(dist, 2)-math.pow(minDist, 2))


        returnCode, self.right_motor_target_position = simxGetJointPosition(GlobalVar.vrepClientID, self.right_motor_handle, simx_opmode_oneshot_wait)
        returnCode, self.left_motor_target_position = simxGetJointPosition(GlobalVar.vrepClientID, self.left_motor_handle, simx_opmode_oneshot_wait)


        self.right_motor_target_position += l/self.R
        self.left_motor_target_position += l/self.R



        simxPauseCommunication(GlobalVar.vrepClientID, True)
        returnCode = simxSetJointTargetPosition(GlobalVar.vrepClientID, self.left_motor_handle, self.left_motor_target_position , simx_opmode_oneshot)
        returnCode = simxSetJointTargetPosition(GlobalVar.vrepClientID, self.right_motor_handle, self.right_motor_target_position , simx_opmode_oneshot)
        simxPauseCommunication(GlobalVar.vrepClientID, False)

    def rotate(self, degrees):
        #returnCode, Angles = simxGetObjectOrientation(GlobalVar.vrepClientID, self.handle, -1, simx_opmode_oneshot_wait)
        #ddegree = degrees-Angles[2]

        returnCode,  self.right_motor_target_position = simxGetJointPosition(GlobalVar.vrepClientID, self.right_motor_handle, simx_opmode_oneshot_wait)
        returnCode, self.left_motor_target_position = simxGetJointPosition(GlobalVar.vrepClientID, self.left_motor_handle, simx_opmode_oneshot_wait)
        degrees = degrees*180/math.pi
        self.right_motor_target_position = self.right_motor_target_position*180/math.pi
        self.left_motor_target_position = self.left_motor_target_position*180/math.pi

        self.right_motor_target_position += degrees*self.d/(2*self.R)
        self.left_motor_target_position += -degrees*self.d/(2*self.R)

        self.right_motor_target_position = self.right_motor_target_position*math.pi/180
        self.left_motor_target_position = self.left_motor_target_position*math.pi/180

        simxPauseCommunication(GlobalVar.vrepClientID, True)
        returnCode = simxSetJointTargetPosition(GlobalVar.vrepClientID, self.left_motor_handle, self.left_motor_target_position , simx_opmode_oneshot)
        returnCode = simxSetJointTargetPosition(GlobalVar.vrepClientID, self.right_motor_handle, self.right_motor_target_position , simx_opmode_oneshot)
        simxPauseCommunication(GlobalVar.vrepClientID, False)

    def setSpeed(self, velocity):
        self.speed = velocity

    def updatePosition(self):
        errorCode, PioneerPosition = simxGetObjectPosition(GlobalVar.vrepClientID, self.handle, -1, simx_opmode_oneshot_wait)
        #print(errorCode, "x", PioneerPosition[0], "y", PioneerPosition[1])
        self.position.x = PioneerPosition[0]
        self.position.y = PioneerPosition[1]
        pass

    def isReady(self):
        errorCode, right_motor_current_position =  simxGetJointPosition(GlobalVar.vrepClientID, self.right_motor_handle, simx_opmode_oneshot_wait)
        errorCode, left_motor_current_position = simxGetJointPosition(GlobalVar.vrepClientID, self.left_motor_handle, simx_opmode_oneshot_wait)
        a_r = math.fabs(right_motor_current_position - self.right_motor_target_position)
        a_l = math.fabs(left_motor_current_position-self.left_motor_target_position)
        if a_r < 0.02 and a_l < 0.02:
                   return 1
        return 0

    def getPosition(self):
        return self.position

    def getName(self):
        return self.name

from general import Point
import vrep
import math
import time

class MoveRobot:
    position = Point()
    name = ""
    speed = 0 #prędkość robota
    handle = 0
    left_motor_handle = 0
    right_motor_handle = 0
    R = 0.09717243680870322 #promień koła
    d = 0.35414159966455727 #odstęp między kołami

    def __init__(self, vrepName, clientID):
        self.name = vrepName
        self.clientID = clientID
        errorCode,self.handle=vrep.simxGetObjectHandle(clientID,self.name,vrep.simx_opmode_oneshot_wait)
        errorCode, self.left_motor_handle=vrep.simxGetObjectHandle(clientID,vrepName+'_leftMotor',vrep.simx_opmode_oneshot_wait)
        errorCode, self.right_motor_handle=vrep.simxGetObjectHandle(clientID,vrepName+'_rightMotor',vrep.simx_opmode_oneshot_wait)

    def goToDestinationPoint(self, destinationPoint): #zakładam, że jestem już obrócony, jeśli nie - dodam kilka linijek
        destX = destinationPoint.x
        destY = destinationPoint.y
        self.updatePosition()
        dx = destX-self.position.x
        dy = destY-self.position.y
        angle = math.atan2(dy,dx)
        returnCode, Angles = vrep.simxGetObjectOrientation(self.clientID, self.handle, -1,
                                                           vrep.simx_opmode_oneshot_wait)
        self.rotate(angle-Angles[2])
        dist = math.hypot(dx, dy)


        returnCode, rightAngle = vrep.simxGetJointPosition(self.clientID, self.right_motor_handle, vrep.simx_opmode_oneshot_wait)
        returnCode, leftAngle = vrep.simxGetJointPosition(self.clientID, self.left_motor_handle, vrep.simx_opmode_oneshot_wait)


        rightAngle += dist/self.R
        leftAngle += dist/self.R

        returnCode = vrep.simxSetJointTargetPosition(self.clientID, self.right_motor_handle, rightAngle, vrep.simx_opmode_oneshot_wait)
        returnCode = vrep.simxSetJointTargetPosition(self.clientID, self.left_motor_handle, leftAngle, vrep.simx_opmode_oneshot_wait)

    def rotate(self, degrees):
        #returnCode, Angles = vrep.simxGetObjectOrientation(self.clientID, self.handle, -1, vrep.simx_opmode_oneshot_wait)
        #ddegree = degrees-Angles[2]

        returnCode, rightAngle = vrep.simxGetJointPosition(self.clientID, self.right_motor_handle, vrep.simx_opmode_oneshot_wait)
        returnCode, leftAngle = vrep.simxGetJointPosition(self.clientID, self.left_motor_handle, vrep.simx_opmode_oneshot_wait)
        rightAngle += degrees*self.d/(2*self.R)
        leftAngle += -degrees*self.d/(2*self.R)
        returnCode = vrep.simxSetJointTargetPosition(self.clientID, self.right_motor_handle, rightAngle, vrep.simx_opmode_oneshot_wait)
        returnCode = vrep.simxSetJointTargetPosition(self.clientID, self.left_motor_handle, leftAngle, vrep.simx_opmode_oneshot_wait)
        time.sleep(2)


        pass

    def setSpeed(self, velocity):
        self.speed = velocity
        pass

    def updatePosition(self):
        errorCode, PioneerPosition = vrep.simxGetObjectPosition(self.clientID, self.handle, -1, vrep.simx_opmode_oneshot_wait)
        print(errorCode, "x", PioneerPosition[0], "y", PioneerPosition[1])
        self.position.x = PioneerPosition[0]
        self.position.y = PioneerPosition[1]
        pass
    
    def getPosition(self):
	    return self.position
      
    def getName(self):
	    return self.name
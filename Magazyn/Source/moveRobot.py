from general import Point
import vrep
import math

class MoveRobot:
    position = Point()
    name = ""
    speed = 0 #prędkość robota
    handle = 0
    left_motor_handle = 0
    right_motor_handle = 0

    def __init__(self, vrepName, clientID):
        self.name = vrepName
        self.clientID = clientID
        errorCode,self.handle=vrep.simxGetObjectHandle(clientID,name,vrep.simx_opmode_oneshot_wait)
        errorCode, self.left_motor_handle=vrep.simxGetObjectHandle(clientID,vrepName+'_leftMotor',vrep.simx_opmode_oneshot_wait)#dobrze to robię?
        errorCode, self.right_motor_handle=vrep.simxGetObjectHandle(clientID,vrepName+'_rightMotor',vrep.simx_opmode_oneshot_wait)#dobrze to robię?

    def goToDestinationPoint(self, destinationPoint): #zakładam, że jestem już obrócony, jeśli nie - dodam kilka linijek
        destX = destinationPoint.x
        destY = destinationPoint.y
        self.updatePosition()
        vrep.simxSetJointTargetVelocity(self.clientID, self.left_motor_handle, self.speed, vrep.simx_opmode_oneshot_wait)
        vrep.simxSetJointTargetVelocity(self.clientID, self.right_motor_handle, self.speed, vrep.simx_opmode_oneshot_wait)
        while math.hypot(self.position.x-destX,self.position.y-destY)>0.1:
            returnCode, Angles = vrep.simxGetObjectOrientation(self.clientID, self.handle, -1,
                                                               vrep.simx_opmode_oneshot_wait)
            self.updatePosition()
            dx = destX-self.position.x
            dy = destY-self.position.y
            angle = math.atan2(dy,dx)

            if angle - Angles[2] > 0.2:
                vrep.simxSetJointTargetVelocity(self.clientID, self.left_motor_handle, 0.8*self.speed, vrep.simx_opmode_oneshot_wait)
                vrep.simxSetJointTargetVelocity(self.clientID, self.right_motor_handle, 1.2*self.speed, vrep.simx_opmode_oneshot_wait)

            elif angle - Angles[2] > -0.2:
                vrep.simxSetJointTargetVelocity(self.clientID, self.left_motor_handle, 1.2*self.speed, vrep.simx_opmode_oneshot_wait)
                vrep.simxSetJointTargetVelocity(self.clientID, self.right_motor_handle, 0.8*self.speed, vrep.simx_opmode_oneshot_wait)
            else:
                vrep.simxSetJointTargetVelocity(self.clientID, self.left_motor_handle, self.speed,
                                                vrep.simx_opmode_oneshot_wait)
                vrep.simxSetJointTargetVelocity(self.clientID, self.right_motor_handle, self.speed,
                                                vrep.simx_opmode_oneshot_wait)



        pass

    def rotate(self, degrees):
        returnCode, Angles = vrep.simxGetObjectOrientation(self.clientID, self.handle, -1, vrep.simx_opmode_oneshot_wait)
        ddegree = degrees-Angles[2]
        if ddegree>math.pi:
            ddegree = ddegree-(math.ceil(ddegree/math.pi))*math.pi
        while math.fabs(ddegree)>0.2:
            #do sprawdzenia - być może roboty będą obracać się w przeciwnym kierunku, niż powinny
            if math.pi-math.fabs(Angles[2])+math.pi-math.fabs(degrees)<=math.pi:
                vrep.simxSetJointTargetVelocity(self.clientID, self.left_motor_handle, self.speed, vrep.simx_opmode_oneshot_wait)
                vrep.simxSetJointTargetVelocity(self.clientID, self.right_motor_handle, -self.speed, vrep.simx_opmode_oneshot_wait)
            else:
                vrep.simxSetJointTargetVelocity(self.clientID, self.left_motor_handle, -self.speed, vrep.simx_opmode_oneshot_wait)
                vrep.simxSetJointTargetVelocity(self.clientID, self.right_motor_handle, self.speed, vrep.simx_opmode_oneshot_wait)

            returnCode, Angles = vrep.simxGetObjectOrientation(self.clientID, self.handle, -1, vrep.simx_opmode_oneshot_wait)
            ddegree = degrees-Angles[2]
            if ddegree>math.pi:
                ddegree = ddegree-(math.ceil(ddegree/math.pi))*math.pi

	pass

    def setSpeed(self, velocity):
        self.speed = velocity
	pass

    def updatePosition(self):
        errorCode, PioneerPosition = vrep.simxGetObjectPosition(self.clientID, self.robot_handler, -1, vrep.simx_opmode_oneshot_wait)
        self.position.x = PioneerPosition[0]
        self.position.y = PioneerPosition[1]
	pass
    
    def getPosition(self):
	return self.position
      
    def getName(self):
	return self.name
from .moveRobot import MoveRobot
from Source import vrep
from  Source import vrepConst
from .globalVar import GlobalVar
from Source import positions

class RobotInStorehouse:
	def __init__(self, name):
		self.robot = MoveRobot(name)
	
	def goOnPath(self, pathId):
		pass
	
	def goPathToEnd(self, pathId):
		pass
	
	def goOutOfPath(self, paletteId):
		pass

	# Według dokumentacji to jest klasa niższego poziomu, niż moveRobotsInStorehouse, więc tutaj wykonuję wywołania
	# funkcji z v-repa podlączające i odłączające robota do o od palety

	def joinPallete(self, paletteId):
		errorCode, paletteHandle = vrep.simxGetObjectHandle(GlobalVar.vrepClientID,
									positions.palletNames(paletteId),
									vrepConst.simx_opmode_oneshot_wait)
		vrep.simxSetObjectParent(GlobalVar.vrepClientID, paletteHandle, self.handle, 1, vrep.simx_opmode_oneshot_wait)
		pass

	def unjoinPalette(self, paletteId):
		errorCode, paletteHandle = vrep.simxGetObjectHandle(GlobalVar.vrepClientID, positions.palletNames(paletteId),
															vrepConst.simx_opmode_oneshot_wait)
		vrep.simxSetObjectParent(GlobalVar.vrepClientID, paletteHandle, -1, 1, vrep.simx_opmode_oneshot_wait)
		pass

	def setSpeed(self, velocity):
		self.robot.setSpeed(velocity)

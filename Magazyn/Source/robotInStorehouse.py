from .moveRobot import MoveRobot

class RobotInStorehouse:
    def __init__(self, name):
        self.robot = MoveRobot(name)
        
    def goOnPath(self, pathId):
	    pass
    
    def goPathToEnd(self, pathId):
	    pass
    
    def goOutOfPath(self, paletteId):
	    pass
    
    def joinPallete(self, paletteId):
	    pass
    
    def unjoinPalette(self, paletteId):
	    pass
      
    def setSpeed(self, velocity):
	    self.robot.setSpeed(velocity)
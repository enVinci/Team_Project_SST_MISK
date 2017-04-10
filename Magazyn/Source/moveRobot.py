from general import Point

class MoveRobot:
    position = Point()
    name = ""
  
    def __init__(self, name):
        self.name = name
    
    def goToDestinationPoint(self, destinationPoint):
	pass
    
    def rotate(self, deegress):
	pass
    
    def setSpeed(self, velocity):
	pass
    
    def updatePosition(self, position):
	pass
    
    def getPosition(self):
	return self.position
      
    def getName(self):
	return self.name
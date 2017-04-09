from general import Palette

class Storehouse:
    places = []
    palets = []
    stations = []
    dockStations = []
    paths = []
    
    def __init__(self, places, stations, dockStations, stationBuffors, paths):
	self.places = places
	for obj in self.places:
	    self.palets.append(Palette(obj.getPosition()))
	self.stations = stations
	self.dockStations = dockStations
	self.stationBuffors = stationBuffors
	self.paths = paths
      
    def getPalletePosition(self, paletteId):
	return self.palets[paletteId].getPosition()
    
    def getStationPosition(self, stationName):
	return self.stations[int(stationName)]
    
    def getDockStationPosition(self, dockStationName):
	return self.dockStations[int(dockStationName)].getPosition()
      
    def getStationBuffor(self, stationBufforName):
	return self.stationBuffors[int(stationBufforName)]
    
    def getPath(self, pathId):
	return self.paths[pathId]
      
    def reset(self):
	self.palets = self.places
	pass
from general import Point
from general import StationBuffor
from general import Path
from general import Place

places = [Place(Point(12,32), 1), Place(Point(1,3), 2)]#miejsca na palety w magazynie (64)
stations = [Point(12,32), Point(1,4)]#stanowiska obslugi (4)
dockStations = [Point(12,32), Point(1,4)]#stacje dokujace dla robotow (6)
stationBuffors = [StationBuffor(Point(12,32), Point(1,4)), StationBuffor(Point(12,32), Point(1,4))]#bufor stanowiska
paths = [Path(Point(12,32), Point(1,4), 1), Path(Point(12,32), Point(1,4), 2)]#sciezki dla robotow

robotNames = ["Pioneer_p3dx", "Pioneer_p3dx", "Pioneer_p3dx", "Pioneer_p3dx", "Pioneer_p3dx", "Pioneer_p3dx"]
palletNames = ["palette_0_0_0"]

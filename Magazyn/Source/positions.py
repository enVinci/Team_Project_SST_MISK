from .general import Point
from .general import StationBuffor
from .general import Path
from .general import Place

places = [Place(Point(3.3,2.75), 1), Place(Point(3.3,2.25), 2), Place(Point(2.7,2.75), 3), Place(Point(2.7,2.25), 4),
          Place(Point(2.1,2.75), 5), Place(Point(2.1,2.25), 6), Place(Point(1.5,2.75), 7), Place(Point(1.5,2.25), 8),
          Place(Point(0.9,2.75), 9), Place(Point(0.9,2.25), 10), Place(Point(0.3,2.75), 11), Place(Point(0.3,2.25), 12),
          Place(Point(-0.3,2.75), 13), Place(Point(-0.3,2.25), 14), Place(Point(-0.9,2.75), 15), Place(Point(-0.9,2.25), 16),
          Place(Point(-1.5,2.75), 17), Place(Point(-1.5,2.25), 18), Place(Point(-2.1,2.75), 19), Place(Point(-2.1,2.25), 20),
          Place(Point(-2.7,2.75), 21), Place(Point(-2.7,2.25), 22), Place(Point(-3.3,2.75), 23), Place(Point(-3.3,2.25), 24),
          Place(Point(-3.9,2.75), 25), Place(Point(-3.9,2.25), 26), Place(Point(-4.5,2.75), 27), Place(Point(-4.5,2.25), 28),
          Place(Point(-5.1,2.75), 29), Place(Point(-5.1,2.25), 30), Place(Point(-5.7,2.75), 31), Place(Point(-5.7,2.25), 32),
          Place(Point(3.3,0.25), 33), Place(Point(3.3,-0.25), 34), Place(Point(2.7,0.25), 35), Place(Point(2.7,-0.25), 36),
          Place(Point(2.1,0.25), 37), Place(Point(2.1,-0.25), 38), Place(Point(1.5,0.25), 39), Place(Point(1.5,-0.25), 40),
          Place(Point(0.9,0.25), 41), Place(Point(0.9,-0.25), 42), Place(Point(0.3,0.25), 43), Place(Point(0.3,-0.25), 44),
          Place(Point(-0.3,0.25), 45), Place(Point(-0.3,-0.25), 46), Place(Point(-0.9,0.25), 47), Place(Point(-0.9,-0.25), 48),
          Place(Point(-1.5,0.25), 49), Place(Point(-1.5,-0.25), 50), Place(Point(-2.1,0.25), 51), Place(Point(-2.1,-0.25), 52),
          Place(Point(-2.7,0.25), 53), Place(Point(-2.7,-0.25), 54), Place(Point(-3.3,0.25), 55), Place(Point(-3.3,-0.25), 56),
          Place(Point(-3.9,0.25), 57), Place(Point(-3.9,-0.25), 58), Place(Point(-4.5,0.25), 59), Place(Point(-4.5,-0.25), 60),
          Place(Point(-5.1,0.25), 61), Place(Point(-5.1,-0.25), 62), Place(Point(-5.7,0.25), 63), Place(Point(-5.7,-0.25), 64),
          Place(Point(3.3,-2.25), 65), Place(Point(3.3,-2.75), 66), Place(Point(2.7,-2.25), 67), Place(Point(2.7,-2.75), 68),
          Place(Point(2.1,-2.25), 69), Place(Point(2.1,-2.75), 70), Place(Point(1.5,-2.25), 71), Place(Point(1.5,-2.75), 72),
          Place(Point(0.9,-2.25), 73), Place(Point(0.9,-2.75), 74), Place(Point(0.3,-2.25), 75), Place(Point(0.3,-2.75), 76),
          Place(Point(-0.3,-2.25), 77), Place(Point(-0.3,-2.75), 78), Place(Point(-0.9,-2.25), 79), Place(Point(-0.9,-2.75), 80),
          Place(Point(-1.5,-2.25), 81), Place(Point(-1.5,-2.75), 82), Place(Point(-2.1,-2.25), 83), Place(Point(-2.1,-2.75), 84),
          Place(Point(-2.7,-2.25), 85), Place(Point(-2.7,-2.75), 86), Place(Point(-3.3,-2.25), 87), Place(Point(-3.3,-2.75), 88),
          Place(Point(-3.9,-2.25), 89), Place(Point(-3.9,-2.75), 90), Place(Point(-4.5,-2.25), 91), Place(Point(-4.5,-2.75), 92),
          Place(Point(-5.1,-2.25), 93), Place(Point(-5.1,-2.75), 94), Place(Point(-5.7,-2.25), 95), Place(Point(-5.7,-2.75), 96),
          Place(Point(3.3,-4.75), 97), Place(Point(3.3,-5.25), 98), Place(Point(2.7,-4.75), 99), Place(Point(2.7,-5.25), 100),
          Place(Point(2.1,-4.75), 101), Place(Point(2.1,-5.25), 102), Place(Point(1.5,-4.75), 103), Place(Point(1.5,-5.25), 104),
          Place(Point(0.9,-4.75), 105), Place(Point(0.9,-5.25), 106), Place(Point(0.3,-4.75), 107), Place(Point(0.3,-5.25), 108),
          Place(Point(-0.3,-4.75), 109), Place(Point(-0.3,-5.25), 110), Place(Point(-0.9,-4.75), 111), Place(Point(-0.9,-5.25), 112),
          Place(Point(-1.5,-4.75), 113), Place(Point(-1.5,-5.25), 114), Place(Point(-2.1, -4.75), 115), Place(Point(-2.1,-5.25), 116),
          Place(Point(-2.7,-4.75), 117), Place(Point(-2.7,-5.25), 118), Place(Point(-3.3,-4.75), 119), Place(Point(-3.3,-5.25), 120),
          Place(Point(-3.9,-4.75), 121), Place(Point(-3.9,-5.25), 122), Place(Point(-4.5,-4.75), 123), Place(Point(-4.5,-5.25), 124),
          Place(Point(-5.1,-4.75), 125), Place(Point(-5.1,-5.25), 126), Place(Point(-5.7,-4.75), 127), Place(Point(-5.7,-5.25), 128)]
          #miejsca na palety w magazynie (128)
stations = [Point(-10.55,2.07), Point(-10.52,-0.43), Point(-10.52,-2.9), Point(-10.49,-5.4),]#stanowiska obslugi (4)
dockStations = [Point(0.26,5.75), Point(-0.74,5.75), Point(6.36,-0.75), Point(6.28,-1.75), Point(0.21,-8.32), Point(-0.79,-8.32)]#stacje dokujace dla robotow (6)
stationBuffors = [StationBuffor(Point(-9.5,-5.25), Point(-9.5,-5.75)), StationBuffor(Point(-9.5,-2.75), Point(-9.5,-3.25)),
                  StationBuffor(Point(-9.5,-0.25), Point(-9.5,-0.75)), StationBuffor(Point(-9.5,2.25), Point(-9.5,2.25))]#bufor stanowiska

paths = [Path(Point(12,32), Point(1,4), 1), Path(Point(12,32), Point(1,4), 2)]#sciezki dla robotow

robotNames = ["Pioneer_p3dx_0", "Pioneer_p3dx_1", "Pioneer_p3dx_2", "Pioneer_p3dx_3", "Pioneer_p3dx_4", "Pioneer_p3dx_5"]

palletNames = ["palette_0_0_0","palette_0_0_1","palette_0_0_2","palette_0_0_3","palette_0_0_4","palette_0_0_5","palette_0_0_6",
               "palette_0_0_7","palette_0_0_8","palette_0_0_9","palette_0_0_10","palette_0_0_11","palette_0_0_12","palette_0_0_13",
               "palette_0_0_14","palette_0_0_15","palette_0_1_0","palette_0_1_1","palette_0_1_2","palette_0_1_3","palette_0_1_4",
               "palette_0_1_5","palette_0_1_6","palette_0_1_7","palette_0_1_8","palette_0_1_9","palette_0_1_10","palette_0_1_11",
               "palette_0_1_12","palette_0_1_13","palette_0_1_14","palette_0_1_15","palette_1_0_0","palette_1_0_1","palette_1_0_2",
               "palette_1_0_3","palette_1_0_4","palette_1_0_5","palette_1_0_6","palette_1_0_7","palette_1_0_8","palette_1_0_9",
               "palette_1_0_10","palette_1_0_11","palette_1_0_12","palette_1_0_13","palette_1_0_14","palette_1_0_15","palette_1_1_0",
               "palette_1_1_1","palette_1_1_2","palette_1_1_3","palette_1_1_4","palette_1_1_5","palette_1_1_6","palette_1_1_7",
               "palette_1_1_8","palette_1_1_9","palette_1_1_10","palette_1_1_11","palette_1_1_12","palette_1_1_13","palette_1_1_14",
               "palette_1_1_15","palette_2_0_0","palette_2_0_1","palette_2_0_2","palette_2_0_3","palette_2_0_4","palette_2_0_5",
               "palette_2_0_6","palette_2_0_7","palette_2_0_8","palette_2_0_9","palette_2_0_10","palette_2_0_11","palette_2_0_12",
               "palette_2_0_13","palette_2_0_14","palette_2_0_15","palette_2_1_0","palette_2_1_1","palette_2_1_2","palette_2_1_3",
               "palette_2_1_4","palette_2_1_5","palette_2_1_6","palette_2_1_7","palette_2_1_8","palette_2_1_9","palette_2_1_10",
               "palette_2_1_11","palette_2_1_12","palette_2_1_13","palette_2_1_14","palette_2_1_15","palette_3_0_0","palette_3_0_1",
               "palette_3_0_2","palette_3_0_3","palette_3_0_4","palette_3_0_5","palette_3_0_6","palette_3_0_7","palette_3_0_8",
               "palette_3_0_9","palette_3_0_10","palette_3_0_11","palette_3_0_12","palette_3_0_13","palette_3_0_14","palette_3_0_15",
               "palette_3_1_0","palette_3_1_1","palette_3_1_2","palette_3_1_3","palette_3_1_4","palette_3_1_5","palette_3_1_6",
               "palette_3_1_7","palette_3_1_8","palette_3_1_9","palette_3_1_10","palette_3_1_11","palette_3_1_12","palette_3_1_13",
               "palette_3_1_14","palette_3_1_15"]
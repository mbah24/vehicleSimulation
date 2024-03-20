from vehicle import Car, Truck
from simulation import *
from constants import Constants
from Traffic_control import SpeedLimit
from gui import *
from Map import *
from SUI import *

def main():
    simInput = MetricGUI()
    Uptown = simInput.create_road("Uptown", 0.0, -0.09, .180, Heading.North)
    Crosstown = simInput.create_road("Crosstown", -0.09, 0.0, .180, Heading.East)

    cm = CharMatrix(Constants.CharMapSize)
    map_obj = Map()
    map_obj.add_road(Uptown)
    map_obj.add_road(Crosstown)
    cp = ConsolePrint()
    map_obj.print(cp, cm)

    for i in range(Constants.CharMapSize):
        print("".join(cm.map[i]))

if __name__ == "__main__":
    main()

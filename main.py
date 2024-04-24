from simulation import *
from vehicle import Car, Truck
from Traffic_control import *
from constants import Constants
from gui import *
from Map import *
from SUI import *
from simulation import *
import time
from char_matrix import *
def main():
    cm = CharMatrix(Constants.CharMapSize)
    cp = ConsolePrint()
    sim = Simulation(cp)
    simInput = MetricGUI()
    
    
    Uptown = simInput.create_road("Uptown", 0.0, -0.09, 0.180, Heading.North)
    map_obj = Map()
    map_obj.add_road(Uptown)
    map_obj.print(cp, cm)  # Initial road drawing

    tl1 = TrafficLight(position=18, red_duration=5, yellow_duration=3, green_duration=5, start_color='red', road=Uptown)
    tl2 = TrafficLight(position=36, green_duration=5, yellow_duration=3, red_duration=3, start_color='green', road=Uptown)
    traffic_lights = [tl1, tl2]

    for _ in range(20):
        for tl in traffic_lights:
            tl.update()

        sim.print_lights(traffic_lights, cm)

        for row in cm.map:
            print("".join(row))
        time.sleep(1)
        cm = CharMatrix(Constants.CharMapSize)  # Reset matrix to clear old prints
        map_obj.print(cp, cm)  # Redraw the road for each cycle



if __name__ == "__main__":
    main()

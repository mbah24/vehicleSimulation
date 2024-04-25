from simulation import *
from vehicle import Car, Truck
from Traffic_control import *
from constants import Constants
from gui import *
from Map import *
from SUI import *
import time

def main():
    sim = Simulation()
    simInput = MetricGUI()

    # Create a Road
    Uptown = simInput.create_road("Uptown", 0.0, -0.09, .180, Heading.North)

    cm = CharMatrix(Constants.CharMapSize)
    map_obj = Map()
    map_obj.add_road(Uptown)
    cp = ConsolePrint()
    map_obj.display(cp, cm)  # Use the new method name 'display'

    # Setup Traffic Lights
    tl1 = TrafficLight(mile_marker=18, green_duration=10, yellow_duration=3, red_duration=6)
    tl2 = TrafficLight(mile_marker=26, green_duration=8, yellow_duration=3, red_duration=4)
    traffic_lights = [tl1, tl2]

    for i in range(20):
        for tl in traffic_lights:
            tl.update()

        sim.print_lights(traffic_lights, cm)

        for j in range(Constants.CharMapSize):
            print("".join(cm.map[j]))

        time.sleep(1)

        sim.clear_screen()

if __name__ == "__main__":
    main()

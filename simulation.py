# simulation.py
from Traffic_control import *
from SUI import *
import os
import platform
from Common import ConsolePrint

class Simulation:
    def __init__(self, console_printer):
        self.console_printer = console_printer

    def print_lights(self, traffic_lights, char_matrix):
        self.console_printer.print_traffic_lights(traffic_lights, char_matrix)

    '''
    def __init__(self):
        self.roaditems = []

    @staticmethod
    def print_lights(traffic_lights, char_matrix):
        color_symbol = {'red': 'X', 'yellow': '-', 'green': 'O'}
        for i, light in enumerate(traffic_lights):
            if hasattr(light, 'current_color') and light.current_color in color_symbol:
                symbol = color_symbol[light.current_color]
                row_index = len(char_matrix.map) - 13 * (i + 1)
                char_matrix.map[row_index][light.position] = symbol
            else:
                print(f"Warning: TrafficLight at position {light.position} has no valid current_color")
    '''
    @staticmethod
    def clear_screen():
        if platform.system() == "Windows":
            os.system("cls")  # Clear the screen on Windows
        else:
            os.system("clear")  # Clear the screen on other operating systems
    

    def update(self):
        print("Simulation updated")

    def add_dynamic_road_item(self, dynamic_road_item):
        print(f"Dynamic road item added: {dynamic_road_item}")
    
    def print_speed(self, vehicle):
        sim_output = self.gui.get_speed(vehicle)
        print(f"{vehicle.__class__.__name__} speed: {sim_output}")

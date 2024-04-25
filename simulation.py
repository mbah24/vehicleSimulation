from Traffic_control import *
from SUI import *
import os
import platform

class Simulation:
    def __init__(self):
        self.roaditems = []

    @staticmethod
    def print_lights(traffic_lights, char_matrix):
        # Row index of the first traffic light
        first_tl_row_index = len(char_matrix.map) - 13
        # The row index of the second traffic light should be 13 less than that of the first traffic light
        second_tl_row_index = first_tl_row_index - 13

        # Print the first traffic light
        symbol = {'red': 'X', 'yellow': '-', 'green': 'O'}[traffic_lights[0].current_color]
        char_matrix.map[first_tl_row_index][traffic_lights[0].mile_marker] = symbol

        # Print the second traffic light
        symbol = {'green': 'O', 'red': 'X', 'yellow': '-'}[traffic_lights[1].current_color]
        char_matrix.map[second_tl_row_index][traffic_lights[1].mile_marker] = symbol

    @staticmethod
    def clear_screen():
        if platform.system() == "Windows":
            os.system("cls")  # Clear the console on Windows
        else:
            os.system("clear")  # Clear the console on Unix/Linux

    def update(self):
        print("Simulation updated")

    def add_dynamic_road_item(self, dynamic_road_item):
        print(f"Dynamic road item added: {dynamic_road_item}")

    def print_speed(self, vehicle):
        sim_output = self.gui.get_speed(vehicle)
        print(f"{vehicle.__class__.__name__} speed: {sim_output}")

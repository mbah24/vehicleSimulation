from Road import Dynamic, Static
import time

class TrafficLight:
    def __init__(self, position, red_duration, yellow_duration, green_duration, start_color, road):
        self.position = position
        self.red_duration = red_duration
        self.yellow_duration = yellow_duration
        self.green_duration = green_duration
        self.state = start_color  # Ensuring 'state' is defined and set
        self.road = road
        self.last_change = time.time()

    def update(self):
        current_time = time.time()
        if self.state == 'red' and current_time - self.last_change >= self.red_duration:
            self.state = 'green'
            self.last_change = current_time
        elif self.state == 'green' and current_time - self.last_change >= self.green_duration:
            self.state = 'yellow'
            self.last_change = current_time
        elif self.state == 'yellow' and current_time - self.last_change >= self.yellow_duration:
            self.state = 'red'
            self.last_change = current_time


    def change_color(self):
        # Example of cycling through the colors
        color_order = ['red', 'yellow', 'green']
        current_index = color_order.index(self.current_color)
        new_index = (current_index + 1) % len(color_order)
        self.current_color = color_order[new_index]
        self.last_change = time.time()  # Update last_change when the color changes

    def determine_color_based_on_timing(light):
        # Placeholder logic to determine traffic light color
        # Replace with actual logic based on your simulation needs
        return 'red'   or 'yellow' or 'green'

    
    def print_item(self, char_matrix):
        display_char = {'red': 'R', 'yellow': 'Y', 'green': 'G'}
        if 0 <= self.position < len(char_matrix.map[0]):  # Check x-coordinate bounds
            char_matrix.map[10][self.position] = display_char[self.state]  # Adjust 10 to the actual y-coordinate based on your design
 
    def PrintRoadItem(self, cm):
        # Assume x_location is directly related to the mile_marker for simplicity
        x_location = self.calculate_x_location()
        cm.map[self.mile_marker][x_location] = self.get_display_char()

    def calculate_x_location(self):
        # This is a placeholder logic; you might need to adjust this based on actual road orientation and details
        return int(self.road.xlocation + self.mile_marker)

    #def get_display_char(self):
        #if self.state == 'red':
        #    return 'X'
        #elif self.state == 'green':
        #    return 'O'
        #elif self.state == 'yellow':
        #    return '-'



class Light(Dynamic):
    def __init__(self):
        super().__init__()
        self.redTime = 0
        self.yellowTime = 0
        self.greenTime = 0
        self.lit = 0
        self.timeOn = 0

    def update(self, seconds):
        return seconds

    def getLightColor(self, color):
        pass


class StopSign(Static):
    def __init__(self):
        super().__init__()


class Intersection(Static):
    def __init__(self):
        super().__init__()
        self.turns = []

    def GetTurns(self):
        return self.turns

    def AddTurn(self, turn):
        self.turns.append(turn)
        print(f"Turn added: {turn}")

    def GetTurn(self, index):
        try:
            return self.turns[index]
        except IndexError:
            raise ValueError("Invalid turn index")
    

class SpeedLimit(Static):
    def __init__(self):
        super().__init__()
        self.speedLimit = 45

    def GetSpeedLimit(self):
        print(f"Speed Limit:{self.speedLimit}")
        return self.speedLimit


class Yield(Static):
    def __init__(self):
        super().__init__()


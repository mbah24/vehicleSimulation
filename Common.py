from constants import *
class Conversions:
    
    @staticmethod
    def WCpointToCCpoint(val):
        return int(val * (Constants.CharMapSize / Constants.WorldSize) + (Constants.CharMapSize / 2))

    @staticmethod
    def WClengthToCClength(val):
        return int(val * (Constants.CharMapSize / Constants.WorldSize))

class ConsolePrint:
    def print_road(self, road, char_matrix):
        # Calculate start and end positions based on road orientation and length
        start_x = int(Conversions.WCpointToCCpoint(road.xlocation))
        start_y = int(Conversions.WCpointToCCpoint(road.ylocation))
        end_y = start_y + int(Conversions.WClengthToCClength(road.length))

        for y in range(start_y, end_y):
            if 0 <= y < len(char_matrix.map):  # Check bounds
                char_matrix.map[y][start_x] = '|'

    def print_traffic_lights(self, traffic_lights, char_matrix):
        for light in traffic_lights:
            pos_x = int(Conversions.WCpointToCCpoint(light.road.xlocation))
            pos_y = light.position  # Assuming position is already in character matrix coordinates
            if 0 <= pos_y < len(char_matrix.map):
                state_symbol = {'red': 'R', 'yellow': 'Y', 'green': 'G'}
                char_matrix.map[pos_y][pos_x] = state_symbol[light.state]

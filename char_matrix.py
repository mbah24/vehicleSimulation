# In char_matrix.py
class CharMatrix:
    def __init__(self, size):
        self.size = size
        self.map = [[' ' for _ in range(size)] for _ in range(size)]

    def print(self):
        for line in self.map:
            print(''.join(line))

    def add_road(self, start, end, column):
        for i in range(start, end + 1):
            self.map[i][column] = '|'

    def add_traffic_light(self, position, column, state):
        symbol = {'red': 'R', 'yellow': 'Y', 'green': 'G'}
        if 0 <= position < self.size:
            self.map[position][column] = symbol[state]

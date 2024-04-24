class Map:
    def __init__(self):
        self.roads = []

    def add_road(self, road):
        self.roads.append(road)

    def print(self, print_driver, char_matrix):
        for road in self.roads:
            road.Print(print_driver, char_matrix)  # Correctly reference Print with uppercase P

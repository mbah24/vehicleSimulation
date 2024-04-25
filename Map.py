class Map:
    def __init__(self):
        self.roads = []

    def add_road(self, road):
        self.roads.append(road)

    def display(self, print_driver, obj):  # Renamed from 'print' to 'display'
        for road in self.roads:
            road.print(print_driver, obj)  # Assuming 'print' in 'Road' is correct; otherwise, adjust as needed.

from enum import Enum

class Heading(Enum):
    North = 1
    South = 2
    East = 3
    West = 4

class Road:
    NumOfRoads = 0

    def __init__(self, streetName, locX, locY, length, hdg):
        self.name = streetName
        self.length = length
        self.xlocation = locX
        self.ylocation = locY
        self.heading = hdg
        Road.NumOfRoads += 1

    def get_length(self):
        return self.length

    def get_x_location(self):
        return self.xlocation

    def get_y_location(self):
        return self.ylocation

    def get_heading(self):
        return self.heading

    def get_road_name(self):
        return self.name
    
    def Print(self, print_driver, obj):
        print_driver.print_road(self, obj)

    # Methods like AddRoadItem can be added here if needed

class RoadItem:
    def __init__(self):
        self.mile_marker = None
        self.current_road = None
        self.next_item = None
        self.prev_item = None

    def get_mile_marker(self):
        return self.mile_marker

    def GetCurrentRoad(self):
        return self.currentRoad

    def SetCurrentRoad(self, road):
        self.currentRoad = road

    def GetPrevious(self):
        return self.previtem

    def SetPrevious(self, item):
        self.previtem = item

    def GetNext(self):
        return self.nextitem

    def SetNext(self, item):
        self.nextitem = item

class Dynamic(RoadItem):
    def __init__(self):
        super().__init__()
        self.upDate = 0
      
class Static(RoadItem):
    def __init__(self):
        super().__init__()
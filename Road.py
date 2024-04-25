from enum import Enum
from abc import ABC,abstractmethod
# Heading enum translated from C#
class Heading(Enum):
    North = 1
    South = 2
    East = 3
    West = 4

# Updated Road class integrating both existing and translated features
class Road:
    NumOfRoads = 0  # Static variable from translated code

    def __init__(self, name, locX=None, locY=None, len=None, hdg=None):
        self.name = name
        self.length = len
        self.heading = hdg
        self.xlocation = locX
        self.ylocation = locY
        Road.NumOfRoads += 1
 
    def get_length(self):
        return self.length

    def get_xlocation(self):
        return self.xlocation

    def get_ylocation(self):
        return self.ylocation

    def get_heading(self):
        return self.heading

    def get_road_name(self):
        return self.name

    def add_roaditem(self, roaditem):
        print(f"Road item added: {roaditem}")

    def print(self, print_driver, obj):
        print_driver.print_road(self, obj)


# Preserving the existing RoadItem class
class RoadItem:
    def __init__(self,mile_marker,current_road = None):
        self.mile_marker = mile_marker
        self.current_road = current_road
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


class Dynamic(RoadItem, ABC):
    def __init__(self,mile_marker,current_road = None):
        super().__init__(mile_marker)
        self.mile_marker = mile_marker
        self.current_road = current_road
    
    @abstractmethod

    def update(self, seconds: int):
        pass

        
class Static(RoadItem):
    def __init__(self):
        super().__init__()


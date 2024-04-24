from enum import Enum

class Heading(Enum):
    North = 1
    South = 2
    East = 3
    West = 4

class Road:
    def __init__(self, name, locX, locY, length, heading):
        self.name = name
        self.xlocation = locX  # Ensure this is correctly named and set
        self.ylocation = locY
        self.length = length
        self.heading = heading
        self.dynamic_items = []
       
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
    
    def add_roaditem(self, item):
        self.dynamic_items.append(item)

    def Print(self, print_driver, char_matix):
        # Implement the logic to print the road details using the provided print_driver
        print_driver.print_road(self, char_matix)
        for item in self.dynamic_items:
            if hasattr(item, 'print_item'):
                item.print_item(char_matix)
            
    
    def calculate_x_location(self, item):
        # Example logic, adjust based on your specific needs
        return int(self.xlocation + item.mile_marker)  # This is a placeholder


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
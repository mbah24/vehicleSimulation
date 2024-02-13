
from Color import Color
from RoadItem import RoadItem

class TrafficLight(RoadItem):  
    def __init__(self, mile_marker, current_road, next_item, prev_item, red_time, yellow_time, green_time, lit, time_on):
        super().__init__(mile_marker, current_road, next_item, prev_item)
        self.red_time = red_time
        self.yellow_time = yellow_time
        self.green_time = green_time
        self.lit = lit
        self.time_on = time_on

    def Update(self, seconds):
        pass

    def GetLightColor(self):
        return self.color

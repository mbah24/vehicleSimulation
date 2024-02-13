class RoadItem:
    def __init__(self, mile_marker, current_road, next_item, prev_item):
        self.mile_marker = mile_marker
        self.current_road = current_road
        self.next_item = next_item
        self.prev_item = prev_item

    def GetMileMarker(self):
        return self.mile_marker

    def GetCurrentRoad(self):
        return self.current_road

    def SetCurrentRoad(self, road):
        self.current_road = road

    def GetNext(self):
        return self.next_item

    def SetNext(self, item):
        self.next_item = item

    def GetPrevious(self):
        return self.prev_item

    def SetPrevious(self, item):
        self.prev_item = item

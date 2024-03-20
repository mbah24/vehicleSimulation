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
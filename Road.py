class Road:
    def __init__(self, name, length, head=None):
        self.name = name
        self.length = length
        self.head = head
        self.road_items = []

    def GetLength(self):
        return self.length

    def GetRoadName(self):
        return self.name

    def AddRoadItem(self, road_item):
        self.road_items.append(road_item)

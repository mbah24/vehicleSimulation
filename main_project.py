class Road:
    def __init__(self, name, length, head):
        self.name = name
        self.length = length
        self.head = head

    def GetLength(self):
        return self.length

    def GetRoadName(self):
        return self.name

    def AddRoadItem(self, roaditem):
        pass


class RoadItem:
    def __init__(self, mileMaker, currentRoad, nextItem, prevItem):
        self.mileMaker = mileMaker
        self.currentRoad = currentRoad
        self.nextItem = nextItem
        self.prevItem = prevItem

    def GetMileMaker(self):
        return self.mileMaker

    def GetCurrentRoad(self):
        return self.currentRoad

    def SetCurrentRoad(self, road):
        self.currentRoad = road

    def GetNext(self):
        return self.nextItem

    def SetNext(self, item):
        self.nextItem = item

    def GetPrevious(self):
        return self.prevItem

    def SetPrevious(self, item):
        self.prevItem = item


class Simulation:
    def __init__(self):
        self.roadItems = []

    def Update(self, seconds):
        pass

    def AddDynamicRoadItem(self, item):
        pass


class Dynamic:
    def Update(self, seconds):
        pass


from enum import Enum


class Color(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3


class Light(Dynamic):
    def __init__(self, redTime, yellowTime, greenTime, lit, timeOn):
        self.redTime = redTime
        self.yellowTime = yellowTime
        self.greenTime = greenTime
        self.lit = lit
        self.timeOn = timeOn

    def Update(self, seconds):
        pass

    def GetLightColor(self):
        return self.lit


class Vehicle:
    def __init__(self, currentSpeed, desiredSpeed, speedLimit, color):
        self.currentSpeed = currentSpeed
        self.desiredSpeed = desiredSpeed
        self.speedLimit = speedLimit
        self.color = color

    def GetCurrentSpeed(self):
        return self.currentSpeed

    def GetSpeedLimit(self):
        return self.speedLimit

    def SetDesiredSpeed(self, speed):
        self.desiredSpeed = speed

    def Update(self, seconds):
        pass


class Car(Vehicle):
    pass


class Truck(Vehicle):
    def __init__(self, currentSpeed, desiredSpeed, speedLimit, color, loadWeight, trailerColor):
        super().__init__(currentSpeed, desiredSpeed, speedLimit, color)
        self.loadWeight = loadWeight
        self.trailerColor = trailerColor

    def SetLoadWeight(self, weight):
        self.loadWeight = weight


class StopSign:
    pass


class Intersection:
    def __init__(self):
        self.turns = []

    def AddTurn(self, turn):
        pass

    def GetTurns(self):
        return self.turns

    def GetTurn(self, index):
        return self.turns[index]


class SpeedLimit:
    def __init__(self, speedLimit):
        self.speedLimit = speedLimit

    def GetSpeedLimit(self):
        return self.speedLimit


class Yield:
    pass

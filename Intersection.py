from StaticRoadItem import StaticRoadItem

class Intersection(StaticRoadItem):
    def __init__(self):
        super().__init__(None, None, None, None)
        self.turns = []

    def AddTurn(self, turn):
        self.turns.append(turn)

    def GetTurns(self):
        return self.turns

    def GetTurn(self, index):
        return self.turns[index]

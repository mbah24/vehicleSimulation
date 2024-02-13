from Vehicle import Vehicle
from Constants import Constants

class Truck(Vehicle):
    def __init__(self, weight):
        super().__init__()
        self.load_weight = weight

    def Accelerate(self, seconds_delta):
        if self.load_weight <= 5:
            self.SetCurrentSpeed(self.GetCurrentSpeed() + Constants.AccRateEmpty * seconds_delta * Constants.MpsToMph)
        else:
            self.SetCurrentSpeed(self.GetCurrentSpeed() + Constants.AccRateFull * seconds_delta * Constants.MpsToMph)

    def Decelerate(self, seconds_delta):
        if self.load_weight <= 5:
            self.SetCurrentSpeed(self.GetCurrentSpeed() - Constants.DecRateEmpty * seconds_delta * Constants.MpsToMph)
        else:
            self.SetCurrentSpeed(self.GetCurrentSpeed() - Constants.DecRateFull * seconds_delta * Constants.MpsToMph)


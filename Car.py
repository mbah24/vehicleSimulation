from Vehicle import Vehicle
from Constants import Constants

class Car(Vehicle):
    def Accelerate(self, seconds_delta):
        self.SetCurrentSpeed(self.GetCurrentSpeed() + Constants.AccRate * seconds_delta * Constants.MpsToMph)

    def Decelerate(self, seconds_delta):
        self.SetCurrentSpeed(self.GetCurrentSpeed() - Constants.DecRate * seconds_delta * Constants.MpsToMph)

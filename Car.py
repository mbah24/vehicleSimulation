from vehicle import vehicle
from constants import constants

class Car(vehicle):
    def Accelerate(self, seconds_delta):
        self.SetCurrentSpeed(self.GetCurrentSpeed() + constants.AccRate * seconds_delta * constants.MpsToMph)

    def Decelerate(self, seconds_delta):
        self.SetCurrentSpeed(self.GetCurrentSpeed() - constants.DecRate * seconds_delta * constants.MpsToMph)

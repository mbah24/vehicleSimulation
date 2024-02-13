from abc import ABC, abstractmethod

class Constants:
    AccRate = 3.5
    AccRateEmpty = 2.5
    AccRateFull = 1.0
    DecRate = 7.0
    DecRateEmpty = 5.0
    DecRateFull = 2.0
    MpsToMph = 2.237

class Program:
    @staticmethod
    def main():
        car = Car()
        car.set_desired_speed(65.0)
        truck1 = Truck(4)
        truck1.set_desired_speed(55.0)
        truck2 = Truck(8)
        truck2.set_desired_speed(50.0)
        vehicles = [car, truck1, truck2]
        for _ in range(11):
            for v in vehicles:
                v.update_speed(1)
                s = type(v).__name__
                print(f"{s} speed: {v.get_current_speed():.2f} mph")

class Vehicle(ABC):
    def __init__(self):
        self.current_speed = 0.0
        self.desired_speed = 0.0

    @abstractmethod
    def accelerate(self, seconds_delta):
        pass

    @abstractmethod
    def decelerate(self, seconds_delta):
        pass

    def get_current_speed(self):
        return self.current_speed

    def set_desired_speed(self, mph):
        self.desired_speed = mph

    def set_current_speed(self, speed):
        if self.current_speed <= speed:  # accelerating
            if speed > self.desired_speed:
                self.current_speed = self.desired_speed
            else:
                self.current_speed = speed
        else:  # braking
            if speed < self.desired_speed:
                self.current_speed = self.desired_speed
            else:
                self.current_speed = speed

    def update_speed(self, seconds):
        if self.current_speed > self.desired_speed:
            self.decelerate(seconds)
        elif self.current_speed < self.desired_speed:
            self.accelerate(seconds)

class Car(Vehicle):
    def accelerate(self, seconds_delta):
        self.set_current_speed(self.get_current_speed() + Constants.AccRate * seconds_delta * Constants.MpsToMph)

    def decelerate(self, seconds_delta):
        self.set_current_speed(self.get_current_speed() - Constants.DecRate * seconds_delta * Constants.MpsToMph)

class Truck(Vehicle):
    def __init__(self, weight):
        super().__init__()
        self.load_weight = weight

    def accelerate(self, seconds_delta):
        if self.load_weight <= 5:
            self.set_current_speed(self.get_current_speed() + Constants.AccRateEmpty * seconds_delta * Constants.MpsToMph)
        else:
            self.set_current_speed(self.get_current_speed() + Constants.AccRateFull * seconds_delta * Constants.MpsToMph)

    def decelerate(self, seconds_delta):
        if self.load_weight <= 5:
            self.set_current_speed(self.get_current_speed() - Constants.DecRateEmpty * seconds_delta * Constants.MpsToMph)
        else:
            self.set_current_speed(self.get_current_speed() - Constants.DecRateFull * seconds_delta * Constants.MpsToMph)

if __name__ == "__main__":
    Program.main()

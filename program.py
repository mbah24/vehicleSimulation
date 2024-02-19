from vehicle import Car, Truck
from constants import Constants
from output import MetricOutput, ImperialOutput

class Program:
    @staticmethod
    def main():
        # Create instances of Car and Truck
        car = Car()
        car.set_desired_speed(65.0)
        truck1 = Truck(4)
        truck1.set_desired_speed(55.0)
        truck2 = Truck(8)
        truck2.set_desired_speed(50.0)
        
        # Create an instance of MetricOutput
        simOutput = MetricOutput()
        
        # List of vehicles
        vehicles = [car, truck1, truck2]
        # Loop to simulate the vehicles' speeds
        for _ in range(11):
            for v in vehicles:
                v.update_speed(1)
                s = type(v).__name__
                # Print the vehicle's speed using ISimOutput
                #print(f"{s} Speed: {simOutput.get_speed(v):.2f} mph")
                print(f"{s} Speed: {simOutput.get_speed(v):.2f} km/h")

if __name__ == "__main__":
    #Run with MetricOutput
    print("Running with MetricOutput:")
    Program.main()
    
    #Run with ImperialOutput
    print("\nRunning with ImperialOutput:")
    simOutput = ImperialOutput()
    Program.main()

# Interface for simulation output
class ISimOutput:
    def get_speed(self, v):
        pass

# Output class for imperial units
class ImperialOutput(ISimOutput):
    def get_speed(self, v):
        return v.get_current_speed()

# Output class for metric units
class MetricOutput(ISimOutput):
    def get_speed(self, v):
        return v.get_current_speed() * 1.6

if __name__ == "__main__":
    Program.main()
    
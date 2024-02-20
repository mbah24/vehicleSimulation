from vehicle import Car, Truck
from constants import Constants
from output import MetricOutput, ImperialOutput

class Program:
    @staticmethod
    def main():
        # Get user input for unit choice
        unit_choice = input("Choose unit system (1 for Metric, 2 for Imperial): ")
        
        if unit_choice == "1":
            simOutput = MetricOutput()
            speed_unit = "km/h"
        elif unit_choice == "2":
            simOutput = ImperialOutput()
            speed_unit = "mph"
        else:
            print("Invalid choice. Using metric System by default.")
            simOutput = MetricOutput()
            speed_unit = "km/h"
            
        # Get user input for speed limit
        speed_limit = float(input("Enter speed limit: "))
        
        
        # Create instances of Car and Truck
        car = Car()
        car.set_desired_speed(speed_limit)
        truck1 = Truck(4)
        truck1.set_desired_speed(speed_limit)
        truck2 = Truck(8)
        truck2.set_desired_speed(speed_limit)
        
        
        # List of vehicles
        vehicles = [car, truck1, truck2]
        
        # Loop to simulate the vehicles' speeds
        for _ in range(11):
            for v in vehicles:
                v.update_speed(1)
                vehicle_type = type(v).__name__
                # Print the vehicle's speed using ISimOutput
                print(f"{vehicle_type} Speed: {simOutput.get_speed(v):.2f} {speed_unit}")

if __name__ == "__main__":
    # Run with MetricOutput
    print("Running with MetricOutput:")
    Program.main()

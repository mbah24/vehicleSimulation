import time
from enum import Enum

# Enum for Traffic Light Colors
class Color(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

# Base class for dynamic elements in the simulation
class Dynamic:
    def update(self, seconds):
        pass

# Class representing a road
class Road:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def update(self, seconds):
        for vehicle in self.vehicles:
            vehicle.update(seconds)

# Class representing a vehicle
class Vehicle(Dynamic):
    def __init__(self, current_speed, desired_speed, speed_limit, color):
        self.current_speed = current_speed
        self.desired_speed = desired_speed
        self.speed_limit = speed_limit
        self.color = color

    def update(self, seconds):
        # Update vehicle state based on simulation rules
        pass

# Class representing a traffic light
class TrafficLight(Dynamic):
    def __init__(self, red_time, yellow_time, green_time):
        self.red_time = red_time
        self.yellow_time = yellow_time
        self.green_time = green_time
        self.current_color = Color.RED
        self.time_on_current_color = 0

    def update(self, seconds):
        self.time_on_current_color += seconds

        # Change light color based on the time elapsed
        if self.current_color == Color.RED and self.time_on_current_color >= self.red_time:
            self.current_color = Color.GREEN
            self.time_on_current_color = 0
        elif self.current_color == Color.GREEN and self.time_on_current_color >= self.green_time:
            self.current_color = Color.YELLOW
            self.time_on_current_color = 0
        elif self.current_color == Color.YELLOW and self.time_on_current_color >= self.yellow_time:
            self.current_color = Color.RED
            self.time_on_current_color = 0

    def get_light_color(self):
        return self.current_color

# Simulation class
class TrafficSimulation:
    def __init__(self):
        self.roads = []
        self.dynamics = []

    def add_road(self, road):
        self.roads.append(road)

    def add_dynamic_element(self, dynamic_element):
        self.dynamics.append(dynamic_element)

    def run_simulation(self, duration_seconds):
        start_time = time.time()

        while time.time() - start_time < duration_seconds:
            elapsed_time = time.time() - start_time

            for dynamic_element in self.dynamics:
                dynamic_element.update(elapsed_time)

            for road in self.roads:
                road.update(elapsed_time)

            time.sleep(1)  # Adjust the sleep time based on your simulation speed

# Example Usage
if __name__ == "__main__":
    # Create a road
    main_road = Road("Main Road", 1000)

    # Create a traffic light
    traffic_light = TrafficLight(red_time=30, yellow_time=5, green_time=45)

    # Add elements to the simulation
    simulation = TrafficSimulation()
    simulation.add_road(main_road)
    simulation.add_dynamic_element(traffic_light)

    # Run the simulation for 300 seconds
    simulation.run_simulation(duration_seconds=300)

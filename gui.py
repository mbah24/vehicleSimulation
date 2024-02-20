from abc import ABC, abstractmethod
from tkinter import *

# Interface for simulation output
class ISimOutput(ABC):
    @abstractmethod
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

# Vehicle classes
class Vehicle:
    def __init__(self, desired_speed):
        self.current_speed = 0
        self.desired_speed = desired_speed
        
    def update_speed(self, speed):
        self.current_speed += speed

    def get_current_speed(self):
        return self.current_speed

# Car class
class Car(Vehicle):
    #def set_desired_speed(self, speed):
     #   self.current_speed = speed
     pass

# Truck class
class Truck(Vehicle):
    def __init__(self, weight, desired_speed):
        super().__init__(desired_speed)
        self.weight = weight

# GUI Class
class SimulationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulation GUI")

        # Label and Entry for speed limit
        Label(root, text="Enter Speed Limit:").grid(row=0, column=0)
        self.speed_limit_entry = Entry(root)
        self.speed_limit_entry.grid(row=0, column=1)

        # Buttons for Metric and Imperial simulation
        Button(root, text="Metric", command=self.run_metric_simulation).grid(row=1, column=0)
        Button(root, text="Imperial", command=self.run_imperial_simulation).grid(row=1, column=1)

    def run_simulation(self, sim_output, speed_unit):
        speed_limit_entry_text = self.speed_limit_entry.get()
        if not speed_limit_entry_text:
            output_text = "Please enter a speed limit."
        else:
            speed_limit = float(speed_limit_entry_text)

            car = Car(speed_limit)
            truck1 = Truck(4, speed_limit)
            truck2 = Truck(8, speed_limit)

            vehicles = [car, truck1, truck2]

            output_text = ""

            for _ in range(11):
                for v in vehicles:
                    v.update_speed(1)
                    vehicle_type = type(v).__name__
                    output_text += f"{vehicle_type} Speed: {sim_output.get_speed(v):.2f} {speed_unit}\n"
        return output_text

    def run_metric_simulation(self):
        metric_output = MetricOutput()
        output_text = self.run_simulation(metric_output, "km/h")
        self.display_output(output_text)

    def run_imperial_simulation(self):
        imperial_output = ImperialOutput()
        output_text = self.run_simulation(imperial_output, "mph")
        self.display_output(output_text)

    def display_output(self, output_text):
        output_window = Toplevel(self.root)
        output_window.title("Simulation Output")
        output_label = Label(output_window, text=output_text)
        output_label.pack()

if __name__ == "__main__":
    root = Tk()
    app = SimulationGUI(root)
    root.mainloop()
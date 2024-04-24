from abc import ABC, abstractmethod

class IPrintDriver(ABC):
    @abstractmethod
    def print_road(self, road, obj):
        pass

    @abstractmethod
    def print_car(self, car, obj):
        pass

class ConsolePrint(IPrintDriver):
    def print_road(self, road, char_matrix):
        # Implementation to print a road to the console
        pass

    def print_car(self, car, char_matrix):
        # Implementation to print a car to the console
        pass

# Interface for simulation output
class ISimOutput(ABC):
    @abstractmethod
    def get_speed(self, v):
        pass

# Output Class for imperial units
class ImperialOutput(ISimOutput):
    def get_speed(self, v):
        return v.get_current_speed()
    
# Output class for the metric units
class MetricOutput(ISimOutput):
    def get_speed(self, v):
        return v.get_current_speed() * 1.6
from abc import ABC, abstractmethod

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
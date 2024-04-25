from Road import Dynamic
import time

class TrafficLight(Dynamic):
    def __init__(self, mile_marker, red_duration, yellow_duration, green_duration, start_color='red'):
        super().__init__(mile_marker)
        self.mile_marker = mile_marker  # Position of the traffic light along the road
        self.red_duration = red_duration  # Duration the red light stays on
        self.yellow_duration = yellow_duration  # Duration the yellow light stays on
        self.green_duration = green_duration  # Duration the green light stays on
        self.current_color = start_color  # Initial color of the traffic light
        self.timer = 0  # Timer to track elapsed time for color changes

    def update(self, seconds=1):
        """
        Updates the state of the traffic light based on the elapsed time.

        Args:
        seconds (int): Number of seconds to advance the traffic light's timer. Default is 1.
        """
        self.timer += seconds  # Increment the timer by the given number of seconds
        # Calculate the total duration of the traffic light cycle
        cycle_duration = self.red_duration + self.yellow_duration + self.green_duration
        # Cycle the timer using modulo operation based on the total duration
        self.timer %= cycle_duration
        # Update the traffic light's color based on the current timer value
        if self.timer <= self.red_duration:
            self.current_color = 'red'
        elif self.timer <= self.red_duration + self.yellow_duration:
            self.current_color = 'green'
        else:
            self.current_color = 'yellow'

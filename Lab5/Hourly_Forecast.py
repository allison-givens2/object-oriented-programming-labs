"""
Hourly_Forecast class
"""

class Hourly_Forecast:
    # constructor with protected attributes: time, temp, condition
    def __init__(self, time, temp, condition):
        self._time = time
        self._temp = temp
        self._condition = condition

    @staticmethod
    # function that converts a dictionary parameter to an Hourly_Forecast object
    def from_dict(time, temp, condition):
        hourly_forecast = Hourly_Forecast(time, temp, condition)
        return hourly_forecast
    
    # function that prints an Hourly_Forecast object
    def __str__(self):
        return f"{self._time}\t{self._temp}\t{self._condition}"
    
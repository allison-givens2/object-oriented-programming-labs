"""
Weather_Day class
"""

# Hourly_Forecast class
from Hourly_Forecast import Hourly_Forecast

class Weather_Day:
    # constructor with protected attributes: date, summary, and hourly (a list of Hourly_Forecast objects)
    def __init__(self, date, summary, hourly):
        self._date = date
        self._summary = summary
        self._hourly = hourly

    @staticmethod
    # function to convert a dictionary to a Weather_Day object
    def from_dict(date, dictionary):
        hourly_list = []
        for hour in dictionary["hourly"]:
            hourly_list.append(Hourly_Forecast(hour["time"], hour["temp"], hour["condition"]))
        return Weather_Day(date, dictionary["summary"], hourly_list)

    # getter summary
    def get_summary(self):
        return self._summary

    # get list of hourly forecasts
    def get_hourly_forecast(self):
        return self._hourly
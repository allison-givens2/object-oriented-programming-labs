from Weather_Day import Weather_Day
import json

# WeatherApp aggregates data from the Weather_Day objects
class Weather_App:
    def __init__(self, days):
        self._days = days  # list of Weather_Day objects

    # load_from_file method opens a json file (name passed as a parameter) and reads the data from it.
    # It creates an empty dictionary to hold the Weather_Day objects then iterates through each item
    # in the data. The for loop condition is "for date, d in data.items()". The .items() separates the 
    # json file into individual components or dictionary entries. Then one item at a time, the key is 
    # stored in date, and the value is stored in d. Those values are used to create a Weather_Day object
    # which is added to the list of days. Finally it returns a Weather_App object sending the 
    # list of days as the parameter.
    @staticmethod
    def load_from_file(filename: str):
        with open(filename, "r") as f:
            data = json.load(f)
        days = []
        for date, d in data.items(): 
            new_day = Weather_Day.from_dict(date, d)
            days.append(new_day)
        return Weather_App(days)

    # list_dates lists the dates loaded from the json file for user convenience
    def list_dates(self):
        return [day._date for day in self._days]

    # get_day returns the Weather_Day object associated with the provided date from the days attribute.
    def get_day(self, date: str):
        for day in self._days:
            if day._date == date:
                return day
        return None

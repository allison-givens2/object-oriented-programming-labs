from Weather_App import Weather_App

def main():
    # Create a Weather_App object from the weather.json data
    app = Weather_App.load_from_file("weather.json")
    # Print the dates read from file for user convenience
    print("Available dates:", ", ".join(app.list_dates()))

    # Get user input
    date = input("Enter a date (YYYY-MM-DD): ")
    # Retrieve the desired date's weather data from the app object
    day = app.get_day(date)

    # If get_day returned a None Type tell user there is no data for that day
    if not day:
        print("No data for that date.")
        return

    # Ask user for desired output
    choice = input("Type 'summary' or 'hourly': ").strip().lower()

    # Print the appropriate format as requested by user
    if choice == "summary":
        # Print the daily summary
        print(f"Weather Summary for {date}: {day.get_summary()}")
    elif choice == "hourly":
        # Print the hourly forecast for each hour
        print(f"Hourly Forecast for {date}:")
        for forecast in day.get_hourly_forecast():
            print(" ", forecast)
    else:
        # User validation, exits upon fail
        print("Invalid choice.")

if __name__ == "__main__":
    main()

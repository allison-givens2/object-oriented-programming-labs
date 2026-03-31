[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/kgHp5SZG)
# Activity 05
### Working with Classes and Data in Python

#### Purpose
In this lab you will explore how Python classes can be used to manage and organize data. You will be working with a small weather application that reads data from a JSON file and outputs weather summaries for a selected date or an hourly forecast. This activity will help you practice reading and writing Python code that interacts with data files and multiple classes.

#### The Application
You have been provided with four Python files:

| **File** | **Purpose** |
|-----------|-------------|
| **main.py** | Entry point of the program. Handles user input and displays the resulting weather summaries or forecasts. |
| **Weather_App.py** | Contains the Weather_App class which manages the overall data and functionality of the app. |
| **Weather_Day.py** | Contains the Weather_Day class which represents a single day of weather data. |
| **Hourly_Forecast.py** | Contains the Hourly_Forecast class which represents a single hourly forecast entry. |

Each of these files contributes to the overall program structure. They are designed to demonstrate how objects can work together to represent complex data in a clear and modular way.

#### Understanding TODOs
A **TODO** is a developer note that marks a place in the code where additional work is needed. These comments help guide your focus during development.  
In PyCharm, you can easily find all TODOs in your project by selecting **View → Tool Windows → TODO**. This will open a panel showing every TODO comment, and clicking one will take you directly to that section of code.  
Each TODO in this lab identifies where you need to write or modify code to complete the program.

#### Running the Application
To run the program, open a terminal window in PyCharm or your system’s command line.  
From the lab directory, enter the following command on a Mac or Linux machine:
```
python3 main.py
```
or for a Windows machine:  
```
py main.py
```
You will be prompted to enter a date from the dataset.  
The program will then display either a weather summary for that day or an hourly forecast, depending on your selection.

#### Activity
1. Open each of the four Python files and study their structure. Pay close attention to how the classes interact.
2. Locate all TODO comments using PyCharm’s TODO tool window.
3. Complete each TODO one at a time, testing your work as you go.
4. Run **main.py** in the terminal and verify that your program produces the expected output for both daily summaries and hourly forecasts.
5. Once your program runs correctly, review your code for readability and ensure that all required TODOs have been completed.

### Turn-in
Make sure your work has saved and push it to GitHub.  
Open a terminal to the activity directory and run the following commands:

```
git add .
git commit -m "Completed Activity 05"
git push -u origin master
```



### Rubric

| **Criteria** | **5 Points** | **3 Points** | **1 Point** | **0 Points** |
|---------------|--------------|--------------|--------------|--------------|
| **Completion of TODOs** | All TODOs completed | Most TODOs completed | Only a few TODOs completed | No submission |
| **Daily Summary Output** | Program produces correct daily weather summaries | Daily summaries mostly correct with minor issues | Daily summaries incomplete or incorrect | No submission |
| **Hourly Forecast Output** | Program produces correct hourly forecasts | Forecasts mostly correct with minor issues | Forecasts incomplete or incorrect | No submission |

**Maximum: 15 points**




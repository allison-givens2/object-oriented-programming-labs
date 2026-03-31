[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ZlZqf8fT)
## Lab 03
### Creating Use Case Diagrams

This lab will consist of building a use case diagram describing the functions of a carpooling app, which is explained below. You will use the information contained in the **Problem Description** shown below as context for creating the relevant diagrams(s).

## Purpose
For this lab you will be continuing work on the Ride Share application from lab 2 by creating a Use Case Diagram. 

#### Activity
Using draw.io or a diagramming tool of your choice, you will create a use case diagram based on the user stories given below. If your tool of choice does not have all the necessary components, you will not be able to complete the assignment for full credit as you will be graded on adherance to UML standard.

User Stories:

```txt
CSC 2310 User Stories

Title: Schedule Pickup
As a(n): Rider
I need/want: a way to schedule a pickup
so that: I can schedule when I would need a driver to pick me up

Title: Schedule route
As a(n): Driver
I need/want: to enter my route into the app
so that: I can pick up riders on my way

Title: Driver Identification
As a(n): Rider
I need/want: a user identification system
so that: I can ensure the driver is a university student or faculty

Title: Rider Identification
As a(n): Driver
I need/want: a user identification system
so that: I can ensure the rider is a university student or faculty

Title: Driver Rating System
As a(n): Rider
I need/want: a way to rate drivers
so that: I do or do not get suggested to be picked up by them again

Title: Driver Rating System
As a(n): Driver
I need/want: a way to be rated by passengers
so that: I know what I can do to improve passenger experiences

Title: Driver Designation system
As a(n): Rider
I need/want: a way to see whether my driver will be a student or faculty
so that: I can ride with my coworkers/fellow students and improve our relationship

Title: GPS System
As a(n): Driver
I need/want: a navigation system
so that: my route gets updated with my new passenger pickups in real time

Title: Login Page
As a(n): Administrator
I need/want: a login page
so that: drivers may enter their student/faculty email and drivers license number

Title: Driver search
As a(n): Rider
I need/want: a driver search function
so that: I can search specific drivers who are headed to my destination

Title: Points System
As a(n): Driver
I need/want: a points system
so that: over time I can accumulate points for free stuff by driving (food, clothing, etc.)

Title: Report database
As a(n): Administrator
I need/want: a report database 
so that: I can access and screen reports made by riders and drivers and react accordingly

Title: Report Interface
As a(n): Rider
I need/want: a report page
so that: I can report suspicious or law-breaking drivers

Title: Report Interface
As a(n): Driver
I need/want: a report page
so that: I can report suspicious or law-breaking riders

Title: Intuitive suggestions
As a(n): Driver
I need/want: route suggestions based on distance
so that: I can pick up close riders and make more points

Title: Passenger limit system
As a(n): Driver
I need/want: a passenger limit
so that: the number of people in my car does not exceed what I am comfortable with

Title: Car Identification System
As a(n): Rider
I need/want: a car identification system
so that: I know which car to look for when the driver gets to me

Title: Driver Demerit system
As a(n): Administrator
I need/want: a driver demerit system
so that: I can ban a driver if they get too many demerits(Points on record, reports, etc.)

Title: Integrated Hazard Reports
As a(n): Driver
I need/want: road hazard reports
so that: if a road is flooded or closed I can avoid it instead of figuring out the hard way

Title: Emergency Button
As a(n): Driver
I need/want: an emergency panic button
so that: I can get quick assistance if a passenger goes psycho or if we crash

Title: Emergency button
As a(n): Rider
I need/want: an emergency panic button
so that: I can get quick assistance if a driver goes psycho or if we crash

Title: Accessibility Options
As a(n): Rider
I need/want: accessibility options
so that: if i have special needs such as a lower car or wheelchair storage drivers are notified 

Title: Bonus Points Locations
As a(n): Driver
I need/want: bonus point locations
so that: I get more rewarded for going further out of my way to pick someone up

Title: Car Validation System
As a(n): Administrator
I need/want: a car validation system
so that: we can be sure the car has proper registration and the driver has proper insurance
```

### Turn-in
Save your diagram as a png or jpeg file. Verify the file name, file type, and location then save. **You will be docked 2 points out of 15 for not having a background and 4 points out of 15 for submitting an html/drawio file.**

You will submit your assignments to Git. In a terminal, navigate to the lab 03 directory that you cloned in the beginning of the lab. Ensure that a copy of your diagram is in the folder. Then push your solutions to Git using the following commands:

```bash
git add .
git commit -m "Completed Lab 02"
git push -u origin main
```

### Rubric

| Criteria | 5 points | 3 points | 1 point | 0 points |
| --- | --- | ---  | --- | --- |
| Diagram Content | Shows all stories and actors | missing some stories or actors | missing most stories or actors | No submissions |
| UML Format | Uses proper shapes and UML standard structures | Uses some incorrect shapes or does not follow proper structuring | Multiple errors in shapes or structuring | No submission |
| Professionalism | Diagram is clean, organized, and easy to read | Diagram is missing a background or has minor points of confusion | Submitted an unreadable file (html or drawio) or demonstrated a significant lack of organization | No submission or very unorganized/unreadable |
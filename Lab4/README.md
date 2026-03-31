[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/l37Qk-ZO)
## Activity 04
### Creating a Class Diagram

#### Purpose
In this lab you will be creating a class diagram based on a set of pre-determined class structures.

#### Data
You will be working with a dataset on Greek Mythology for this lab.
Below is a description of each class and it's attributes and methods:

| **Class**  | **Attributes** | **Methods** |
|---------------|--------------|--------------|
| **Entity** | name: str<br>classification: str<br>residence: str<br>mother: str<br>father: str<br>domain: str<br>roman_name: str<br>symbol: str<br>legacy: str<br>abilities: str<br> | <br>find_siblings(Entity[], str) &rarr; str[]<br>find_children(Entity[], str) &rarr; str[] |
| **Location** | name: str<br>classification: str<br>real: bool<br>geographical_location: str<br>size: str<br>description: str | search_by_name(Location[], str) &rarr; Location  | 
| **Item** | name: str<br>classification: str<br>owner: str<br>description: str | find_items_by_owner(Item[], str) &rarr; str[] |
| **Creative_Work** | title: str<br>classification: str<br>creator: str<br>date: str<br>characters: str<br>locations: str<br>relevant_works: str<br>medium: str<br>link: str | search_work_by_title(Creative_Work[], str) &rarr; Creative_Work |

This is also outlined in the provided DataDictionary.txt file in the Data directory. Each file is listed, and these files serve to separate the data for each of our classes. The "data format" label then outlines the values found in a line of data; these are used as the attributes for our classes.

#### Activity
Study the outlined classes carefully. Using the diagramming tool of your choice, build a class diagram representing the data. You must use the correct shapes per UML notation regardless of which tool you use. You will be docked points for using the incorrect shapes. You may defend your choices with a note should you feel necessary.

### Turn-in
Export your model to a readable file (i.e. jpg, png, pdf, etc.) in the directory you cloned at the beginning of the lab. Open a terminal to the activity directory and run the following commands:
```bash
git add .
git commit -m "Completed Activity 04"
git push -u origin master
```

## Rubric

| **Criteria**  | **3 Points** | **2 Points** | **1 Point** | **0 Points** |
|---------------|--------------|--------------|-------------|--------------|
| **Classes** | All classes, attributes, and functions are depicted | Some classes, attributes, or functions are missing | Most classes, attributes, or functions are missing | No submission     |
| **Relationship** | All relationships are depicted with appropriate reasoning and mulitplicities | Some relationships or multiplicities are missing | Either all relationships or multiplicities are missing | No submission |
| **UML Notation** | Correct shapes used for all classes and relationships | Some incorrect notation | Most of the notation is incorrect | No submission |
| **Professionalism** | Clean and readable organization; file is not html/drawio and has a background | Areas of confusion with the diagram but generally organized | Largely unreadable or submitted missing a background/as an html/drawio file | No submission |

**1 bonus point given for any submission to make grading a round 15 points :)**
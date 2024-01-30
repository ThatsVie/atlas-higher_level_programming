# Python - Almost a Circle
This project consists of three Python files: base.py, rectangle.py, and square.py, which define classes related to managing rectangles and squares. Additionally, there are unit tests for each class in the tests/test_model folder.

## File Summaries

## base.py

**Purpose:** Defines the Base class, responsible for managing IDs.

**Attributes:**

**__nb_objects (int):** Private class attribute to keep track of the number of objects.

**id (int):** Public instance attribute representing the object's ID.

    
**Methods:**

**__ init __ (self, id=None):** Constructor for the Base class.
    
**to_json_string(list_dictionaries):** Returns the JSON string representation of a list of dictionaries.
    
**save_to_file(list_objs):** Writes the JSON string representation of a list of objects to a file.
    
**from_json_string(json_string):** Returns a list represented by a JSON string.
    
<strong>create(**dictionary):</strong> Returns an instance with all attributes already set.
    
**load_from_file():** Returns a list of instances loaded from a JSON file.

    
## rectangle.py

**Purpose:** Defines the Rectangle class, which inherits from Base.

**Attributes:**

**id (int):** Public instance attribute representing the object's ID.

**__width (int):** Private instance attribute for width.

**__height (int):** Private instance attribute for height.

**__x (int):** Private instance attribute for x.

**__y (int):** Private instance attribute for y.


**Methods:**

**__ init__ (self, width, height, x=0, y=0, id=None):** Constructor for the Rectangle class.

**to_dictionary():** Returns the dictionary representation of a Rectangle.

**Getter and setter methods for width, height, x, y.**

**area():** Returns the area of the Rectangle.

**display():** Prints the Rectangle using #, taking care of x and y.

**__ str __():** Returns the string representation of the Rectangle.

<strong>update(*args, **kwargs):</strong> Updates Rectangle attributes using positional and keyword arguments.

<strong>create(**dictionary):</strong> Returns a Rectangle instance from a dictionary.

**save_to_file(list_objs):** Writes the JSON string representation of a list of Rectangle objects to a file.

**load_from_file():** Returns a list of Rectangle instances loaded from a JSON file.

## square.py

**Purpose:** Defines the Square class, which inherits from Rectangle.

**Attributes:**

**id (int):** Public instance attribute representing the object's ID.

**size (int):** Private instance attribute for size.

**x (int):** Private instance attribute for x.

**y (int):** Private instance attribute for y.

**Methods:**

**__ init __(self, size, x=0, y=0, id=None):** Constructor for the Square class.

**to_dictionary():** Returns the dictionary representation of a Square.

**Getter and setter methods for size.**

<strong> __str__():</strong> Returns the string representation of the Square.

<strong>update(*args, **kwargs):</strong> Updates Square attributes using positional and keyword arguments.

<strong>create(**dictionary):</strong> Returns a Square instance from a dictionary.

**save_to_file(list_objs):** Writes the JSON string representation of a list of Square objects to a file.

**load_from_file():** Returns a list of Square instances loaded from a JSON file.

## Tests

**test_base.py:** Unittests for base.py. Tests auto-assigning of IDs, checking if IDs are integers, and JSON string conversion.

**test_rectangle.py:** Unittests for rectangle.py. Tests valid and invalid dimensions, area calculation, string representation, and file I/O.

**test_square.py:** Unittests for square.py. Tests size validation, string representation, dictionary representation, and file I/O.

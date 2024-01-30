# Python - Inheritance
This repository focuses on Python inheritance, demonstrating various modules that explore the concept. Inheritance is a crucial aspect of object-oriented programming, allowing the creation of new classes based on existing ones, promoting code reuse and extensibility.

## Modules
**0-lookup.py**
Defines a function lookup(obj) to retrieve a list of available attributes and methods of an object.

**1-my_list.py**
Introduces a class MyList inheriting from the built-in list class.

Features a method print_sorted to print the list in ascending order.

**2-is_same_class.py**
Contains a function is_same_class(obj, a_class) to check if an object is exactly an instance of a specified class.

**3-is_kind_of_class.py**
Provides a function is_kind_of_class(obj, a_class) to check if an object is an instance of or inherited from a specified class.

**4-inherits_from.py**
Defines a function inherits_from(obj, a_class) to check if an object is an instance of a class that inherited from a specified class.

**5-base_geometry.py**
Introduces an empty class BaseGeometry representing base geometry.

**6-base_geometry.py**
Enhances the BaseGeometry class by adding a method area() that raises an exception indicating that the method is not implemented.

**7-base_geometry.py**
Further extends the BaseGeometry class by adding a method integer_validator to validate a value as an integer.

**8-rectangle.py**
Introduces a class Rectangle inheriting from BaseGeometry.
Defines attributes __width and __height to represent the width and height of the rectangle.

**9-rectangle.py**
Extends the Rectangle class by adding a method area() to calculate the area.

Implements a __ str __ method for a string representation of the rectangle.

**10-square.py**
Defines a class Square inheriting from Rectangle.

Initializes a square with a given size.

**11-square.py**
Further enhances the Square class by adding a __str__ method for a string representation.

## Usage

To utilize and test the functionalities, import the classes and functions from each module. Create instances to explore the features and understand the relationships between the classes.

## Example usage

from 0-lookup import lookup

from 1-my_list import MyList

 ... (import other modules)

 Create instances and explore functionalities
 
obj = MyList([1, 2, 3])

obj.print_sorted()

Explore other modules and classes as needed

## Tests

The Tests folder contains test scripts for specific modules. Execute these scripts to validate the functionality of the implemented classes and methods.

 Example test execution
 
python3 Tests/1-my_list.txt

python3 Tests/7-base_geometry.txt

... (execute other tests as needed)

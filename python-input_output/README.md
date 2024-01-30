# Python - Input/Output

This repository focuses on input and output operations in Python, specifically dealing with reading from and writing to files. The provided modules cover various aspects of file handling, including reading, writing, appending, and working with JSON representation.

## Modules

**0-read_file.py**
Defines a function read_file(filename) to read and print the content of a text file to stdout.

**1-write_file.py**
Provides a function write_file(filename, text) to write a string to a text file (UTF-8) and return the number of characters written.

**2-append_write.py**
Introduces a function append_write(filename, text) that appends a string to the end of a text file (UTF-8) and returns the number of characters added.

**3-to_json_string.py**
Defines a function to_json_string(my_obj) that returns the JSON representation of an object (string).

**4-from_json_string.py**
Implements a function from_json_string(my_str) that returns a Python object represented by a JSON string.

**5-save_to_json_file.py**
Provides a function save_to_json_file(my_obj, filename) to write an object to a text file using JSON representation.

**6-load_from_json_file.py**
Introduces a function load_from_json_file(filename) that creates an object from a JSON file.

**7-add_item.py**
A script that adds all command-line arguments to a Python list and saves them to a file in JSON format.

**8-class_to_json.py**
Defines a function class_to_json(obj) that returns the dictionary description with a simple data structure for JSON serialization of an object.

**9-student.py**
Defines a Student class representing a student.
Includes methods to_json for retrieving a dictionary representation and reload_from_json for replacing all attributes from a dictionary.

**10-student.py**
Extends the Student class by adding an optional attrs parameter to the to_json method.

**11-student.py**
Further enhances the Student class by adding a reload_from_json method.

**12-pascal_triangle.py**
Defines a function pascal_triangle(n) that generates Pascal's triangle up to the nth row.

## Usage

To use these modules, import the functions and classes into your Python script. Create instances and execute methods based on your specific file handling and data representation needs.

**Example usage**

from 0-read_file import read_file

from 1-write_file import write_file

 ... (import other modules)
 

 Use functions and classes as needed
 
read_file("example.txt")

write_file("output.txt", "Hello, World!")

 ... (use other functions and classes)

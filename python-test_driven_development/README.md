# Python - Test-driven development
Welcome to the Python Test-driven Development (TDD) repository! This collection of modules showcases the implementation of various functions, each rigorously tested using the TDD methodology.TDD involves writing tests for desired functionalities before implementing the actual code. Below, you'll find details about each module, its associated function, and corresponding unit tests.

## Modules and Functions

**0-add_integer.py**  
  - add_integer(a, b=98)
    - The add_integer function adds two numbers and returns the result as an integer. It validates input types and handles special cases, such as division by zero and overflow errors.

**2-matrix_divided.py**
  - matrix_divided(matrix, div)
    - The matrix_divided function divides all elements of a matrix by a given divisor. It ensures the matrix is well-formed, the divisor is a number, and handles various edge cases.

**3-say_my_name.py**
  - say_my_name(first_name, last_name="")
    - The say_my_name function prints "My name is <first name> <last name>". It checks if the input names are strings.

**4-print_square.py**
  - print_square(size)
    - The print_square function prints a square of '#' characters. It validates the size input and handles errors accordingly.

**5-text_indentation.py**
  - text_indentation(text)
    - The text_indentation function prints a text with two new lines after each of these characters: ., ? and :. It validates the input text and adds new lines as required.

**6-max_integer.py**
  - max_integer(list=[])
    - The max_integer function finds and returns the maximum integer in a list of integers. If the list is empty, the function returns None. It includes various test cases to ensure accurate functionality.
## Unit Tests

Each module is accompanied by a set of unit tests located in the <strong>tests</strong> folder. These tests thoroughly validate the correctness and functionality of the implemented functions. You can run the tests for a specific module using the following command:

## How to Run Tests
To run the tests for a specific module, execute the corresponding testscript from the terminal. For example:

**python3 -m unittest tests.<module_name>_test**

**python3 -m unittest tests.6-max_integer_test**

This command will execute the tests for the 6-max_integer.py module

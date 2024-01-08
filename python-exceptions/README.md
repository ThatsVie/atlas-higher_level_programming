# Python - Exceptions

This repository contains Python scripts demonstrating the use of exception handling in various scenarios. Each script focuses on a specific aspect of exception handling and is designed to showcase how to handle errors gracefully.

## List of Scripts

1. **0-safe_print_list.py**
   - Function: `safe_print_list(my_list=[], x=0):`
   - Description: Safely prints the elements of a list up to a specified number. Handles cases where the specified number is greater than the length of the list.

2. **1-safe_print_integer.py**
   - Function: `safe_print_integer(value):`
   - Description: Safely prints an integer using the `"{:d}".format()` method. Handles cases where the value is not an integer.

3. **2-safe_print_list_integers.py**
   - Function: `safe_print_list_integers(my_list=[], x=0):`
   - Description: Safely prints integers from a list up to a specified number. Skips elements that are not integers.

4. **3-safe_print_division.py**
   - Function: `safe_print_division(a, b):`
   - Description: Safely performs division and prints the result. Handles cases of division by zero and prints the result, whether it's the actual result or `None`.

5. **4-list_division.py**
   - Function: `list_division(my_list_1, my_list_2, list_length):`
   - Description: Performs element-wise division of two lists and handles various exceptions, including division by zero, wrong type, and index out of range.

6. **5-raise_exception.py**
   - Function: `raise_exception():`
   - Description: Raises a `TypeError` with a custom message.

7. **6-raise_exception_msg.py**
   - Function: `raise_exception_msg(message=""):`
   - Description: Raises a `NameError` with a custom message.

## How to Use

Each script is standalone and can be executed individually. Simply run each script using Python

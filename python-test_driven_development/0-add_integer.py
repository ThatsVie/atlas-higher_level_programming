#!/usr/bin/python3
"""
This module contains add_integer function
"""


def add_integer(a, b=98):
    """
    Adds two numbers and returns the result as an integer.

    Parameters:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Raises:
        TypeError: If either a or b is not an integer or float.

    Return:
        int: The sum of a and b as an integer.
    """
    # Check if a is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")

    # Check if b is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    # Cast a and b to integers
    a = int(a)
    b = int(b)

    # Return the sum of a and b as an integer
    return a + b

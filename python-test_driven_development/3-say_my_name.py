#!/usr/bin/python3
"""
This module contains say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>

    Parameters:
        first_name (str): The first name.
        last_name (str): The last name.

    Raises:
        TypeError: If first_name or last_name is not a string.

    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the full name
    print("My name is {} {}".format(first_name, last_name))

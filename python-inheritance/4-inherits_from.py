#!/usr/bin/python3
"""4-inherits_from.py module"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited 
    (directly or indirectly) from the specified class; otherwise False.

    Parameters:
    - obj: Any object.
    - a_class: The specified class to check against.
    """
    return issubclass(type(obj), a_class)

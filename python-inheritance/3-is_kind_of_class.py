#!/usr/bin/python3
"""3-is_kind_of_class.py module"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, specified class. Otherwise False.

    Parameters:
    - obj: Any object.
    - a_class: The specified class to check against.
    """
    return isinstance(obj, a_class)

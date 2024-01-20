#!/usr/bin/python3
"""2-is_same_class.py module"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class.
    Otherwise returns False.

    Parameters:
    - obj: Any object.
    - a_class: The specified class to check against.
    """
    return type(obj) is a_class

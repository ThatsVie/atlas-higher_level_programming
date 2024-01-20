#!/usr/bin/python3

"""0-lookup.py Module"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
    - obj: Any object for which you want to retrieve attributes and methods.
    """
    return dir(obj)

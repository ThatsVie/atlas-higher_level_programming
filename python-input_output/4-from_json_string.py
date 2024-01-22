#!/usr/bin/python3
"""Function that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
    my_str (str): The JSON string.
    """
    return json.loads(my_str)

#!/usr/bin/python3
"""1-my_list.py module"""


class MyList(list):
    """class MyList that inherits from the built-in list class."""

    def print_sorted(self):
        """Public instance method that prints the list in ascending order."""
        print(sorted(self))

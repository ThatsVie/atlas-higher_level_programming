#!/usr/bin/python3

"""
This module defines a Square class
"""


class Square:
    """
    Class to represent a square

    Attributes:
        __size (int): Private attribute representing the size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new square instance

        Parameters:
            size (int): The size of the square.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


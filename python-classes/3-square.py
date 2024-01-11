#!/usr/bin/python3
"""This module defines a class named Square"""

class Square:
    """This class defines a square."""

    def __init__(self, size=0):
        """
        Initializes a new square instance.

        Parameters:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: the area of the square
        """
        return self.__size ** 2

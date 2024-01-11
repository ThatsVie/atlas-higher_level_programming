#!/usr/bin/python3

"""
This module defines a Square class
"""


class Square:
    """
    This class represents a square

    Attributes:
        __size (int): Private attribute representing size of square


    Note:
        The size attribute (__size) is marked as private with
        double underscore.
    """

    def __init__(self, size):
        """
        Initializes a new square with specified size.


        Parameters:
            size (int): size of the square
        """

        self.__size = size

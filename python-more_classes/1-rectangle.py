#!/usr/bin/python3
"""1-rectangle.py module"""


class Rectangle:
    """
    Class representing a rectangle.
    """
    
    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle instance.

        Parameters:
            width (int, optional): The width of the rectangle. Default is 0.
            height (int, optional): The height of the rectangle. Default is 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method to retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

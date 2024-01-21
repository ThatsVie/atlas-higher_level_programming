#!/usr/bin/python3
"""8-rectangle.py module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class, inherits from BaseGeometry.

    Attributes:
    __width (int): Private attribute representing the width of the rectangle.
    __height (int): Private attribute representing the height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with given width and height.

        Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

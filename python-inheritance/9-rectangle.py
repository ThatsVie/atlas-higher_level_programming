#!/usr/bin/python3
"""9-rectangle.py module - Class Rectangle that inherits from BaseGeometry"""
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

    def area(self):
        """Returns area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation of Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

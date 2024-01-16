#!/usr/bin/python3
"""6-rectangle.py Module"""


class Rectangle:
    """
    Class representing a rectangle.

    Attributes:
    __width (int): Private attribute representing the width of the rectangle.
    __height (int): Private attribute representing the height of the rectangle.
    number_of_instances (int): Public attribute representing num of instances.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle instance.

        Parameters:
            width (int): The width of the rectangle. Default 0.
            height (int): The height of the rectangle. Default 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Returns a string representation of the rectangle for recreation."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints message when an instance of Rectangle is deleted.
        Decrements the number_of_instances class attribute.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

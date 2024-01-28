#!/usr/bin/python3
"""Module defines Rectangle class, inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.

    Attributes:
    id (int): Public instance attribute representing the object's ID.
    __width (int): Private instance attribute for width.
    __height (int): Private instance attribute for height.
    __x (int): Private instance attribute for x.
    __y (int): Private instance attribute for y.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Parameters:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): x-coordinate of the rectangle (default is 0).
        y (int): y-coordinate of the rectangle (default is 0).
        id (int): If provided, assigns the specified ID. If None,increments
        __nb_objects and assigns the new value to the instance's ID.

        Note:
        If id is provided, it is assumed to be an integer, and no type
        checking is performed.
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the #"""
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """Return the string representation of the Rectangle."""
        return (
                f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}"
        )

#!/usr/bin/python3
"""Module defines Square class, inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Attributes:
    id (int): Public instance attribute representing the object's ID.
    size (int): Private instance attribute for size.
    x (int): Private instance attribute for x.
    y (int): Private instance attribute for y.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square class.

        Parameters:
        size (int): Size of the square.
        x (int): x-coordinate of the square (default is 0).
        y (int): y-coordinate of the square (default is 0).
        id (int): If provided, assigns the specified ID. If None,increments
        __nb_objects and assigns the new value to the instance's ID.

        Note:
        If id is provided, it is assumed to be an integer
        and no type checking is performed.
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the Square."""
        return ("[Square] ({}) {}/{} - {}".format(id, x, y, width))

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
    def update(self, *args, **kwargs):
        """Update Square attributes using positional and keyword arguments.

        Args:
        *args: No-keyword arguments representing new attribute values.
        1st argument should be the id attribute.
        2nd argument should be the size attribute.
        3rd argument should be the x attribute.
        4th argument should be the y attribute.
        **kwargs: Keyword arguments representing new attribute values.
        Each key in the dictionary represents an attribute to the instance.

        Note:
        **kwargs must be skipped if *args exists and is not empty.
        """
        if args:
            # Handle positional arguments
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            # Handle keyword arguments if *args is empty
            for key, value in kwargs.items():
                setattr(self, key, value)

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
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

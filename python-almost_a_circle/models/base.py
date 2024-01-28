#!/usr/bin/python3
"""Module defines model base class"""


class Base:
    """
    Base class for managing IDs in this project.

    Attrributes:
    - __nb_objects (int): Private class attribute to keep track of the
    number of objects.
    - id (int): Public instance attribute representing the object's ID.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base Class

        Parameters:
        - id (int): If provided, assigns the specified ID. If None, increments
        __nb_objects and assigns the new value to the instance's ID.

        Note:
        - If id is provided, it is assumed to be an integer, and no type
        checking is performed.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

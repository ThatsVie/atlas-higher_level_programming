#!/usr/bin/python3
"""Module defines model base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as file:
            if list_objs is None:
                # Save an empty list if list_objs is None
                file.write("[]")
            else:
                # Convert instances to dictionaries and save as JSON
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string."""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        # Apply real values using update method
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()

        list_dicts = json.loads(json_string)
        instances = [cls.create(**d) for d in list_dicts]
        return instances

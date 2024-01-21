#!/usr/bin/python3
"""11-square.py module - class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square, rectangle with equal sides."""

    def __init__(self, size):
        """Initialize a square using the size parameter."""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

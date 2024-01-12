#!/usr/bin/python3

"""Defines a class named Square."""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): Private attribute representing the size of the square.
        __position (tuple): Private attribute representing position of square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square instance.

        Parameters:
            size (int): The size of the square. Default 0.
            position (tuple): The position of the square. Default (0, 0).

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0 or
            position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Parameters:
            value (int): The size of the square.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position of the square.

        Parameters:
            value (tuple): The position of the square.

        Raises:
            TypeError: If the provided position is not a tuple of 2 positive
            integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character # to stdout.

        If size is equal to 0, print an empty line.
        """
        # Check if the size of the square is 0.
        if self.__size == 0:
            # If the size is 0, print an empty line and return.
            print("")
            return

        # Print newlines before the square to position it vertically.
        for _ in range(self.__position[1]):
            print("")
        # Print each row of square with appropriate indentation and characters.
        for _ in range(self.__size):
            # Indent the row based on the horizontal position.
            print(" " * self.__position[0], end="")
            # Print the characters '#' to represent the square.
            print("#" * self.__size)

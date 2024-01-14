#!/usr/bin/python3
"""
This module contains matrix_divided function
"""


def matrix_divided(matrix, div):
     """
     Divide all elements of a matrix by a given divisor.

     Parameters:
        matrix (list): A list of lists containing integers or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If the matrix is not a matrix of integers/floats
        or rows have different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.

    Returns:
        list: A new matrix representing the result of the division.
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return result_matrix

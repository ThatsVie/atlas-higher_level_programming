#!/usr/bin/python3
"""Pascal's Triangle Function"""


def pascal_triangle(n):
    """Pascal's triangle up to the nth row.

    Args:
    n (int): The number of rows in Pascal's triangle.

    Returns:
    list of lists: A list of lists of integers representing Pascal's triangle.
    """

    # Check for non-positive input
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate each subsequent row
    for i in range(1, n):
        row = [1]  # First element in each row is always 1
        for j in range(1, i):
            # Calculate middle elements based on the previous row
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Last element in each row is always 1
        triangle.append(row)

    return triangle

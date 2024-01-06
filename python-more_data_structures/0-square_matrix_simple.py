#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result_matrix = []
    # Iterate over rows of the matrix
    for row in matrix:
        # Create a new row for the result matrix
        result_row = []
        # Iterate over elements in the row and square each value
        for element in row:
            result_row.append(element ** 2)
        # Append the squared row to the result matrix
        result_matrix.append(result_row)
    return result_matrix


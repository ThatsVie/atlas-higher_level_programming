#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Use str.join() to concatenate formatted integers with a space
        print(" ".join("{:d}".format(elem) for elem in row))

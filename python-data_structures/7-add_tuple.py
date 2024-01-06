#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Use tuple slicing to ensure only the first 2 elements are considered
     a = tuple_a[:2] + (0, 0)
     b = tuple_b[:2] + (0, 0)
     # Return a tuple with the sum of corresponding elements
     return (a[0] + b[0], a[1] + b[1])

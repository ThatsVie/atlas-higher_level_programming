#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_integers = set()
    # Iterate over elements in the input list
    for element in my_list:
        # Add each unique integer to the set
        unique_integers.add(element)

    # Sum all unique integers in the set
    result = sum(unique_integers)
    return result

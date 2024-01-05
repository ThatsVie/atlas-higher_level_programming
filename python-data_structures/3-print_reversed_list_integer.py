#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
# Check if the input list is None
    if my_list is None:
    # Return None if the list is None
    return None
# Iterate through the list in reverse order
for i in range(len(my_list), 0, -1):
    # Print each integer using the str.format() method
    print("{:d}".format(my_list[i - 1]))

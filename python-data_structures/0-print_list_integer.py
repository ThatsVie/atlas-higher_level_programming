#!/usr/bin/python3
def print_list_integer(my_list=[]):
    # Iterate through each element (number) in the list
    for number in my_list:
        # Print each integer using the str.format() method
        print("{:d}".format(number))

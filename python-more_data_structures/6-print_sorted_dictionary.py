#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Iterate over the sorted keys and print key-value pairs
    for key in sorted(a_dictionary):
        value = a_dictionary[key]
        print("{}: {}".format(key, value))

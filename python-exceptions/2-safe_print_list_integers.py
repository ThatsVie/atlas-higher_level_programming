#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # Initialize a counter for number of integers printed
    printed_integers = 0
    # Iterate over the range from 0 to x-1
    for i in range(x):
        try:
            # Attempt to print the current element as an integer
            print("{:d}".format(my_list[i]), end="")
            # Increment the counter for successfully printed integers
            printed_integers += 1
        except (ValueError, TypeError):
            # Continue to next iteration if current element isnt an integer
            continue
    # Print a new line to separate the printed elements
    print()
    # Return the count of integers successfully printed
    return printed_integers        

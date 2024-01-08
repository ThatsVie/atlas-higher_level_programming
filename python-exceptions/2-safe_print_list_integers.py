#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0

    try:
        for i in range(x):
            # Check if current element is an integer
            if type(my_list[i]) == int:
                # Print the integer value
                print("{:d}".format(my_list[i]), end="")
                printed_integers += 1
        # Print a new line after all integers
        print()
    except (IndexError, ValueError):
        # Handle cases where x is greater than the length of my_list
        # or the value is not an integer
        pass
    return printed_integers
        

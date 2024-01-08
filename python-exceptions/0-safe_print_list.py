#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    # Variable to track the number of elements actually printed
    printed_elements = 0

    try:
        # Iterate through list up to specified number of elements (x)
        for i in range(x):
            # Print the current element without a new line
            print(my_list[i], end="")
            printed_elements += 1
    except IndexError:
        # Handle the case where x is greater than the length of my_list
        pass
    finally:
        # Print a new line to separate the printed elements
        print()
    # Return the actual count of printed elements
    return printed_elements

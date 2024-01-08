#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Use "{:d}".format() to print the integer value
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # Handle the case where the value is not an integer
        return False

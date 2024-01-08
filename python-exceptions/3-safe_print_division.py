#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        # Attempt the division operation
        division_result = a / b
    except ZeroDivisionError:
        # Handle division by zero by setting result to None
        division_result = None
    finally:
        # Print the result, whether it's the actual result or None
        print("Inside result: {}".format(division_result))
    # Return the result (which may be the actual result or None)
    return division_result

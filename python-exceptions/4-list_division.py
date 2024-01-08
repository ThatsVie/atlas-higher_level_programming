#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    # Create an empty list to store the division results
    division_results = []

    # Iterate over the specified length or until the shorter list is exhausted
    for i in range(list_length):
        try:
            # Try to perform element-wise division
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            # Handle division by zero
            print("division by 0")
            result = 0
        except TypeError:
            # Handle cases where elements are not integers or floats
            print("wrong type")
            result = 0
        except IndexError:
            # Handle index out of range
            print("out of range")
            result = 0
        finally:
            # Append the current result to the division_results list
            division_results.append(result)

    # Return the list containing the division results
    return division_results

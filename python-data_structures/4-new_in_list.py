#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        # Return a copy of the original list if idx is negative or out of range
        return my_list.copy()
    # Create a new list with the elements of the original list
    new_list = my_list.copy()
    # Replace the element at the specified index in the new list
    new_list[idx] = element
    # Return the new list with the replacement
    return new_list

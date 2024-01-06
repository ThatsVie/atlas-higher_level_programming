#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        # Return the same list if idx is negative or out of range
        return my_list
    # Use slicing to create a new list without the item at the specified index
    new_list = my_list[:idx] + my_list[idx+1:]
    return new_list

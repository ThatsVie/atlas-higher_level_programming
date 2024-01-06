#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if idx is non-negative and within the range of the list
    if idx >= 0 and idx < len(my_list):
        # Use del to remove the item at the specified index
        del my_list[idx]

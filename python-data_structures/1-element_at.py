#!/usr/bin/python3
def element_at(my_list, idx):
    # Check if the index is negative or greater/equal to the list length)
    if idx < 0 or idx >= len(my_list):
        # Return None if the index is out of range
        return None
    # Return the element at the specified index
    return my_list[idx]

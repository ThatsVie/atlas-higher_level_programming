#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    modified_list = []
    # Iterate over elements in the original list
    for element in my_list:
        # Replace element if it matches search value, if not keep original
        modified_element = replace if element == search else element
        # Add current element,modified or original,to list of modified elems
        modified_list.append(modified_element)
    return modified_list

#!/usr/bin/python3

def no_c(my_string):
    # Check if the input string is None
    if my_string is None:
        # Return None if the input string is None
        return None
    # Initialize an empty string to store the result
    new_string = ""
    # Iterate through each character in the input string
    for char in my_string:
        # Check if the lowercase version of the character is not 'c'
        if char.lower() != "c":
            # Append the character to the result string
            new_string += char
    # Return the new string without characters 'c' and 'C'
    return new_string

#!/usr/bin/python3

def uppercase(str):
    for char in str:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the lowercase letter to uppercase using ASCII values
            upper_char = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(upper_char), end="")
        else:
            # Print characters other than lowercase letters unchanged
            print("{}".format(char), end="")

        # Print a new line after processing the string
        print()

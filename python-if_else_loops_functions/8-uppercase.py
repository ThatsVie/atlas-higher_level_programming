#!/usr/bin/python3

def uppercase(input_str):
    for char in input_str:
        # Check if the character is a lowercase letter
        converted_char = (
                chr(ord(char) - (ord('a') - ord('A')))
                if ('a' <= char <= 'z')
                else char
        )
        result += "{}".format(converted_char)
    # Print the resulting uppercase string followed by a new line
    print("")

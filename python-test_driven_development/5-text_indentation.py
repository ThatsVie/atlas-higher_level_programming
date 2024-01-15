#!/usr/bin/python3
"""
This module contains text_indentation function
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Parameters:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty line buffer
    line_buffer = []

    # Iterate through each character in the text
    for char in text:
        # If character is one of specified punctuation marks,
        # print buffered line and reset buffer
        if char in ('.', '?', ':'):
            print("".join(line_buffer))
            line_buffer = []
        # Otherwise, add the character to the buffer
        else:
            line_buffer.append(char)

    # Print the last line (even if it doesn't end with ., ? or :)
    print("".join(line_buffer))

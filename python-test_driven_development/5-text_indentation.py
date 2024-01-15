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

    # Add 2 new lines after each specified character
    for char in '.:?':
        text = text.replace(char, char + '\n\n')

    # Print the modified text with stripped lines
    print(*(ln.strip() for ln in (text + '\n').splitlines()), sep='\n', end='')

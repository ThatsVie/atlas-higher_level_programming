#!/usr/bin/python3
"""function that appends a string at end of a text file"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file (UTF8) and
    returns the number of characters added.

    Args:
    filename (str): The name of the file.
    text (str): The text to append to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)

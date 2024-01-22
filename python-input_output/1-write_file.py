#!/usr/bin/python3
"""1-write_file.py module - Write a string to a text file (UTF-8) and return
the number of characters written."""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8),returns number of characters written

    Args:
    filename (str): The name of the file.
    text (str): The text to write to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)

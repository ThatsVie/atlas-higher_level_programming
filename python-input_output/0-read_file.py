#!/usr/bin/python3
"""0-read_file.py module - function reads a text file and prints to stdout"""


def read_file(filename=""):
    """Read and print the content of a text file."""
    with open(filename, encoding="utf-8") as file:
        print(file.read())

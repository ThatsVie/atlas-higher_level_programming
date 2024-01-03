#!/usr/bin/python3

def uppercase(str):
    result = ""
    for char in str:
        result += "{}".format(chr(ord(char) & ~32))
    print(result)

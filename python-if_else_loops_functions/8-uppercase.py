#!/usr/bin/python3

def uppercase(input_str):
    for char in input_str:
        print("{}".format(char.upper() if char.islower() else char), end="")
    print("")

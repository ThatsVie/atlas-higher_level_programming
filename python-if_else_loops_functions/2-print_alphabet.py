#!/usr/bin/python3
# Loop through ASCII values for lowercase letters (97 to 122),
# print each character using the format method, and prevent newlines.

for i in range(ord('a'), ord('z') + 1):
    print("{:s}".format(chr(i)), end="")

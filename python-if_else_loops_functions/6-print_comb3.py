#!/usr/bin/python3

# Iterate over the tens place from 0 to 8
for i in range(0, 9):
    # Iterate over the ones place from i + 1 to 9
    for j in range(i + 1, 10):
        # Check if it is the last combination
        if i == 8 and j == 9:
            # Print the combination without a trailing comma and space
            print("{:d}{:d}".format(i, j))
        else:
            # Print the combination followed by a comma and space
            print("{:d}{:d}".format(i, j), end=", ")

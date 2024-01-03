#!/usr/bin/python3
for tens_place in range(10):
    for ones_place in range(tens_place + 1, 10):
        print("{:d}{:d}".format(tens_place, ones_place), end=(", " if ones_place < 9 else "\n"))

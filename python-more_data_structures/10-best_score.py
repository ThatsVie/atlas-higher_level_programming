#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        # Return key with the maximum integer value using max() function
        return max(a_dictionary, key=a_dictionary.get)
    else:
        # Return None if the dictionary is empty
        return None

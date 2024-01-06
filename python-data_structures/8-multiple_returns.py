#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:  # Check if the string is empty
        return (0, None)
    # Return a tuple with the length and the first character of the string
    return (len(sentence), sentence[0])

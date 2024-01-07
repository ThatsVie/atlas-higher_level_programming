#!/usr/bin/python3
def roman_to_int(roman_string):
    # Check if the input is an empty string
    if not roman_string:
        return 0
    # Dictionary to map Roman numerals to integers
    roman_numerals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # Initialize the result
    result = 0
    # Initialize the previous value
    previous_value = 0

    # Iterate through the reversed string of Roman symbols
    for symbol in reversed(roman_string):
        # Retrieve value for current Roman symbol, default to 0 if not found
        current_value = roman_numerals.get(symbol, 0)

        # Update the result based on Roman numeral rules
        if current_value < previous_value:
            result -= current_value
        else:
            result += current_value
        # Update the previous value for the next iteration
        previous_value = current_value
    return result

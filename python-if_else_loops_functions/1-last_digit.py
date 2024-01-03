#!/usr/bin/python3
import random

# Generate a random signed number between -10000 and 10000
number = random.randint(-10000, 10000)

# Determine the last digit and adjust its sign based on the original number
if number < 0:
    num = -(abs(number) % 10)
else:
    num = abs(number) % 10

# Create a formatted string indicating the last digit of the original number
output = f"Last digit of {number} is {num}"

# Add additional information based on the value of the last digit
if num > 5:
    output += " and is greater than 5"
elif num == 0:
    output += " and is 0"
else:
    output += " and is less than 6 and not 0"

print(output)

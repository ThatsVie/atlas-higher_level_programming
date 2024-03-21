#!/usr/bin/node

// Get the list of arguments excluding the first two (which are the script name and interpreter)
const userInput = process.argv.slice(2);

// If there are no arguments or only one argument, print 0 and exit
if (userInput.length <= 1) {
    console.log(0);
    process.exit(0);
}

// Convert all arguments to integers
const numbers = userInput.map(Number);

// Find the maximum number
const maxNumber = Math.max(...numbers);

// Filter out the maximum number from the list
const lowerNumbers = numbers.filter(num => num < maxNumber);

// Find the second maximum number from the filtered list
const secondMax = Math.max(...lowerNumbers);

// Print the second largest integer
console.log(secondMax);

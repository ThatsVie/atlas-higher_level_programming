#!/usr/bin/node

// Define the add function with the given prototype
function add (a, b) {
  return a + b; // Perform addition and return the result
}

// Get the first and second integers from the arguments passed to the script
const num1 = parseInt(process.argv[2]); // Parse the first argument to an integer
const num2 = parseInt(process.argv[3]); // Parse the second argument to an integer

// Check if both arguments are valid integers
if (num1 && num2) {
  // If both arguments are valid integers, call the add function with the two integers as arguments
  // and print the result
  console.log(add(num1, num2));
} else {
  // If either argument is not a valid integer, print 'NaN' (Not a Number)
  console.log('NaN');
}

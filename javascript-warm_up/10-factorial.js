#!/usr/bin/node

// Define the factorial function using recursion
function factorial(n) {
  // Base case: factorial of 0 or 1 is 1
  if (n === 0 || n === 1) {
    return 1;
  }
  
  // Recursive case: factorial of n is n multiplied by factorial of (n - 1)
  return n * factorial(n - 1);
}

// Get the integer argument from the command line
const number = parseInt(process.argv[2]);

// Check if the argument is a valid integer
if (!isNaN(number)) {
  // If it's a valid integer, compute the factorial and print the result
  console.log(factorial(number));
} else {
  // If it's not a valid integer, print the factorial of NaN, which is 1
  console.log(1);
}

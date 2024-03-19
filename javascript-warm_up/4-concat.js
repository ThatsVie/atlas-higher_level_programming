#!/usr/bin/node

// Get the first and second arguments passed to the script using process.argv
const arg1 = process.argv[2]; // Retrieve the first argument
const arg2 = process.argv[3]; // Retrieve the second argument

// Concatenate the arguments together with the string " is "
// and print the result in the specified format
console.log(arg1 + ' is ' + arg2);

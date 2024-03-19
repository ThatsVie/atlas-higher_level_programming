#!/usr/bin/node

// Get the number of arguments passed to the script using process.argv
const numArgs = process.argv.length;

// Check the number of arguments and print a message accordingly
if (numArgs === 2) { 
  // If only the script name is passed (no arguments), print 'No argument'
  console.log('No argument');
} else if (numArgs === 3) {
  // If one argument is passed (including the script name itself),
  // print 'Argument found'
  console.log('Argument found');
} else {
  // If more than one argument is passed, print 'Arguments found'
  console.log('Arguments found');
}

#!/usr/bin/node

// Check if the first argument passed to the script exists
if (process.argv[2]) {
  // If the first argument exists, print it
  console.log(process.argv[2]);
} else {
  // If no arguments are passed, print "No argument"
  console.log('No argument');
}

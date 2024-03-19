#!/usr/bin/node

// Check if the first argument passed to the script can be converted
// to an integer using parseInt
if (parseInt(process.argv[2])) {
  // If the argument can be converted to an integer,print
  // "My number: <integer value>"
  console.log(`My number: ${process.argv[2]}`);
} else {
  // If the argument cannot be converted to an integer, print "Not a number"
  console.log('Not a number');
}

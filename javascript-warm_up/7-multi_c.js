#!/usr/bin/node

// Check if the first argument passed to the script can be
// converted to an integer
if (parseInt(process.argv[2])) {
  // If the argument can be converted to an integer, proceed
  // Parse the argument to an integer and store it in the 'number' variable
  const number = parseInt(process.argv[2]);

  // Loop 'number' times and print "C is fun" each time
  for (let n = 0; n < number; n++) {
    console.log('C is fun');
  }
} else {
  // If the argument cannot be converted to an integer,
  // print "Missing number of occurrences"
  console.log('Missing number of occurrences');
}

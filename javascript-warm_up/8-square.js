#!/usr/bin/node

// Check if the first argument passed to the script can be converted to an integer
if (parseInt(process.argv[2])) {
  // If the argument can be converted to an integer, proceed
  // Parse the argument to an integer and store it in the 'number' variable
  const number = parseInt(process.argv[2]);

  // Loop 'number' times to build each row of the square
  for (let num = 0; num < number; num++) {
    let row = ''; // Initialize an empty string to store the characters of the row

    // Loop 'number' times to add 'X' characters to the row
    for (let n = 0; n < number; n++) {
      row += 'X'; // Append 'X' to the row
    }

    // Print the row
    console.log(row);
  }
} else {
  // If the argument cannot be converted to an integer, print "Missing size"
  console.log('Missing size');
}

#!/usr/bin/node

// This line specifies the path to the Node.js interpreter,
// allowing the script to be executed directly from the command line.

exports.esrever = function (list) {
  // Define a function named esrever to export.

  // Initialize an empty array to store the reversed elements.
  const reversedList = [];

  // Iterate over the original list in reverse order.
  for (let i = list.length - 1; i >= 0; i--) {
    // Push each element of the original list into the
    // reversedList array in reverse order.
    reversedList.push(list[i]);
  }

  // Return the reversed list.
  return reversedList;
};

#!/usr/bin/node

// This line specifies the path to the Node.js interpreter,
// allowing the script to be executed directly from the command line.

exports.nbOccurences = function (list, searchElement) {
  // Define a function named nbOccurences to export.

  // Initialize a counter to count the occurrences of the searchElement.
  let counter = 0;

  // Iterate over each element in the list.
  list.forEach(elem => {
    // Check if the current element is equal to the searchElement.
    if (elem === searchElement) {
      // If they are equal, increment the counter.
      counter += 1;
    }
  });

  // Return the total count of occurrences.
  return counter;
};

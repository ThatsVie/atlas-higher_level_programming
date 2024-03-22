#!/usr/bin/node

// This line specifies the path to the Node.js interpreter,
// allowing the script to be executed directly from the command line.

exports.logMe = function (item) {
  // Define a function named logMe to export.

  // If the count property of the logMe function is undefined,
  // initialize it to 0 to keep track of the number of arguments printed.
  if (exports.logMe.count === undefined) {
    exports.logMe.count = 0;
  }

  // Print the number of arguments already printed and the new argument value.
  console.log(exports.logMe.count + ': ' + item);

  // Increment the count for the next call.
  exports.logMe.count++;
};

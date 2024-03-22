#!/usr/bin/node

// This line specifies the path to the Node.js interpreter,
// allowing the script to be executed directly from the command line.

exports.converter = function (base) {
  // Define a function named converter to export.

  function convertToBase (number) {
    // Define a recursive function named convertToBase which converts
    // a number to the specified base.

    if (number < base) {
      // If the number is less than the base,
      // convert it directly to the base and return it.
      return number.toString(base).toUpperCase();
    } else {
      // If the number is greater than or equal to the base,
      // recursively divide the number by the base
      // and concatenate the remainder converted to the base.
      return convertToBase(Math.floor(number / base)) +
        (number % base).toString(base).toUpperCase();
    }
  }

  return convertToBase;
};

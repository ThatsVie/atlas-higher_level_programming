#!/usr/bin/node

// This line specifies the path to the Node.js interpreter,
// allowing the script to be executed directly from the command line.

const BaseSquare = require('./5-square');
// Import the BaseSquare class from the './5-square' module.

class Square extends BaseSquare {
  // Define a class named Square that inherits from the BaseSquare class.

  charPrint (c) {
    // Define an instance method called charPrint for the Square class.
    // This method prints the square using the character c.

    if (c === undefined) {
      // Check if the character c is undefined.

      c = 'X';
      // If c is undefined, set it to the default character 'X'.
    }

    // Iterate over each row of the square and print the character c
    // repeated width times.
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
// Export the Square class to make it available for use in other modules.

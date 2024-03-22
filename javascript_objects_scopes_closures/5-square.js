#!/usr/bin/node

// This line specifies the path to the Node.js interpreter,
// allowing the script to be executed directly from the command line.

const Rectangle = require('./4-rectangle');
// Import the Rectangle class from the './4-rectangle' module.

class Square extends Rectangle {
  // Define a class named Square that extends the Rectangle class.

  constructor (size) {
    // Constructor function called when a new instance of Square is created.
    // It takes one argument: size.

    super(size, size);
    // Call the constructor of the parent class (Rectangle)
    // with the same size for width and height.
    // This initializes the width and height attributes of the Square instance.
  }
}

// Export the Square class to make it available for use in other modules.
module.exports = Square;

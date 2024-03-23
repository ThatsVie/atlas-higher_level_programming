#!/usr/bin/node

// Importing the Rectangle class from the './4-rectangle' module.
const Rectangle = require('./4-rectangle');

// Defining the Square class that extends the Rectangle class.
class Square extends Rectangle {
  constructor (size) {
    // Calling the constructor of the parent class (Rectangle) using super().
    // Passing the size argument to initialize both width and height attributes of the square.
    super(size, size);

    // Validating that the size is a positive number.
    if (size <= 0 || isNaN(size)) {
      // If the size is not a positive number or is NaN, throw an error.
      throw new Error('Size must be a positive number.');
    }
  }
}

// Exporting the Square class to make it available for use in other modules.
module.exports = Square;

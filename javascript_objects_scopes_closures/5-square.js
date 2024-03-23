#!/usr/bin/node

// Import the Rectangle class from the './4-rectangle.js' module.
const Rectangle = require('./4-rectangle.js');

// Define the Square class that extends the Rectangle class.
class Square extends Rectangle {
  // Define the constructor function for the Square class.
  constructor (size) {
    // Call the constructor of the parent class (Rectangle) using super().
    // Pass the size argument to initialize both width and height attributes of the square.
    super(size, size);

    // Ensure size is a positive number
    if (size <= 0) {
      // Log 'undefined undefined' to stdout if size is not positive
      console.log('undefined undefined');
    }
  }
}

// Export the Square class to make it available for use in other modules.
module.exports = Square;

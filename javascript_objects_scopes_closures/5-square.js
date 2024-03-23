#!/usr/bin/node

// Exporting a class named Square that extends the Rectangle class
// imported from the './4-rectangle.js' module.
module.exports = class Square extends require('./4-rectangle.js') {
  // Define the constructor function for the Square class.
  constructor(size) {
    if (size <= 0) {
      // If size is less than or equal to 0, log 'undefined undefined' to the stdout and return.
      console.log('undefined undefined');
      return;
    }
    
    // Call the constructor of the parent class (Rectangle) using super().
    // Pass the size argument to initialize both width and height attributes of the square.
    super(size, size);
  }
};

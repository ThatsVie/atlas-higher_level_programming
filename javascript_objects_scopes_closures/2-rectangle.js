#!/usr/bin/node

// This line specifies the path to the Node.js interpreter,
// allowing the script to be executed directly from the command line.

class Rectangle {
  // Define a class named Rectangle.

  constructor (w, h) {
    // Constructor function called when a new instance of Rectangle is created.
    // It takes two parameters: w (width) and h (height).

    if (w > 0 && h > 0) {
      // Check if both width and height are positive numbers.

      this.width = w;
      // If both width and height are positive, set the width property of
      // the new instance to the value of the w parameter.

      this.height = h;
      // If both width and height are positive, set the height property of
      // the new instance to the value of the h parameter.
    }
  }
}

// Export the Rectangle class to make it available for use in other modules.
module.exports = Rectangle;

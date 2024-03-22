#!/usr/bin/node

// This line specifies the path to the Node.js interpreter,
// allowing the script to be executed directly from the command line.

class Rectangle {
  constructor (w, h) {
    // Constructor function called when a new instance of Rectangle is created.
    // It takes two arguments: w (width) and h (height).

    if (w > 0 && h > 0) {
      // Check if both width and height are positive numbers.
      // If so, initialize the width and height attributes with the given values.

      this.width = w;
      this.height = h;
    } else {
      // If either width or height is not a positive integer or equal to 0,
      // create an empty rectangle with width and height set to 0.

      this.width = 0;
      this.height = 0;
    }
  }

  print () {
    // Define a method named print for the Rectangle class.
    // This method prints the rectangle using the character 'X'.

    if (this.width === 0 || this.height === 0) {
      // If either width or height is 0, the rectangle is empty,
      // so don't print anything.
      return;
    }

    // Iterate over each row of the rectangle and print 'X' characters.
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    // Define a method named rotate for the Rectangle class.
    // This method exchanges the width and height of the rectangle.

    [this.width, this.height] = [this.height, this.width];
    // Use destructuring assignment to swap the values of width and height.
  }

  double () {
    // Define a method named double for the Rectangle class.
    // This method multiplies the width and height of the rectangle by 2.

    this.width *= 2;
    this.height *= 2;
    // Multiply width and height by 2 to double the size of the rectangle.
  }
}

// Export the Rectangle class to make it available for use in other modules.
module.exports = Rectangle;

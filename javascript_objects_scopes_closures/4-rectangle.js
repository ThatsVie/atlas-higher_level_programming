#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    // Constructor function called when a new instance of Rectangle is created.
    // It takes two arguments: w (width) and h (height).
    // If either width or height is not positive, return an empty object.

    if (w <= 0 || h <= 0) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    // Define a method named print for the Rectangle class.
    // This method prints the rectangle using the character 'X'.

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

module.exports = Rectangle;

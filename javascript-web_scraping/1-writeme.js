#!/usr/bin/node

// Write a script that writes a string to a file.
// The first argument is the file path
// The second argument is the string to write
// The content of the file must be written in utf-8
// If an error occurred during while writing, print the error object

// Import the 'fs' module for file system operations
const fs = require('fs');

// Define an asynchronous function to write a string to a file
async function writeStringToFile (filename, string) {
  // Write the provided string to the specified file asynchronously
  fs.writeFile(filename, string, 'utf-8', (error) => {
    // Check if an error occurred during file writing
    if (error) {
      console.error(error);
    }
  });
}

// Call the writeStringToFile function with the filename and string provided as command line arguments
writeStringToFile(process.argv[2], process.argv[3]);

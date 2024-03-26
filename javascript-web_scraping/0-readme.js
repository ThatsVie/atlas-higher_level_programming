#!/usr/bin/node
// Write a script that reads and prints the content of a file.
// The first argument is the file path
// The content of the file must be read in utf-8
// If an error occurred during the reading, print the error object

// Import the 'fs' module for file system operations
const fs = require('fs');

// Define an asynchronous function to read and print the content of a file
async function readAndPrintFileContent (filename) {
  // Read the content of the file asynchronously
  fs.readFile(filename, 'utf-8', (error, data) => {
    // Check if an error occurred during file reading
    if (error) {
      console.error(error);
      return;
    }
    // Print the content of the file to the console
    console.log(data.toString());
  });
}

// Call the readAndPrintFileContent function with the file path provided as a command line argument
readAndPrintFileContent(process.argv[2]);

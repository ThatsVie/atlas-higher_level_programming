#!/usr/bin/node

// Import the 'fs' module for file system operations
const fs = require('fs');

// Store command line arguments in a variable for readability
const commandLineArgs = process.argv;

// Check if a file path argument is provided
if (commandLineArgs.length < 3) {
  console.error('Error: Please provide a file path as an argument.');
  process.exit(1);
}

// Extract the file path from the command line arguments
const filePath = commandLineArgs[2];

// Read the content of the file asynchronously
fs.readFile(filePath, 'utf-8', (error, fileContent) => {
  // Check if an error occurred during file reading
  if (error) {
    console.error('Error reading file:', error);
    return;
  }

  // Print the content of the file to the console
  console.log('File content:');
  console.log(fileContent);
});

#!/usr/bin/node

// Write a script that gets the contents of a webpage and stores it in a file.
// The first argument is the URL to request
// The second argument the file path to store the body response
// The file must be UTF-8 encoded
// You must use the module request

// Importing required modules
const request = require('request');
const fs = require('fs');

// Define a function to make a GET request to the specified URL and store the response in a file
async function requestAndStore (url, filePath) {
  // Make a GET request to the specified URL
  request.get(url, (error, response, body) => {
    // Check if an error occurred during the request
    if (error) console.log(error);
    // If resource not found (status code 404), print the status code
    else if (response.statusCode === 404) console.log(`code: ${response.statusCode}`);
    else {
      // If the request is successful, write the body response to the file
      fs.writeFile(filePath, (body), 'utf-8', (error) => {
        if (error) {
          // If an error occurs while writing to the file, print the error
          console.error(error);
        }
      });
    }
  });
}

// Call the function with the URL and file path provided as command-line arguments
requestAndStore(process.argv[2], process.argv[3]);

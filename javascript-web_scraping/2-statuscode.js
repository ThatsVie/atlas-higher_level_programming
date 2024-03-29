#!/usr/bin/node

// Write a script that display the status code of a GET request.
// The first argument is the URL to request (GET)
// The status code must be printed like this: code: <status code>
// You must use the module request

// Import the 'request' module for making HTTP requests
const request = require('request');

// Extract the URL from command line arguments
const url = process.argv[2];

// Make a GET request to the specified URL
request(url, (error, response) => {
  // Check if an error occurred during the request
  if (error) {
    // Log the error to the console
    console.error(error);
  } else {
    // If no error, print the status code of the response
    console.log(`code: ${response.statusCode}`);
  }
});

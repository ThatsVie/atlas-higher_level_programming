#!/usr/bin/node

// Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
// The first argument is the movie ID
// You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
// You must use the module request

// Import the 'request' module for making HTTP requests
const request = require('request');

// Define the base URL for the Star Wars API
const baseURL = 'https://swapi-api.hbtn.io/api/films/';

// Extract the movie ID from command line arguments
const movieId = process.argv[2];

// Construct the URL for the specific movie
const movieURL = `${baseURL}${movieId}`;

// Make a GET request to the specified URL
request.get(movieURL, (error, response, body) => {
  // Check if an error occurred during the request
  if (error) {
    console.log(error);
    return;
  }

  // Check if the request was successful (status code 200)
  if (response.statusCode === 200) {
    // Parse the JSON response body
    const movieData = JSON.parse(body);

    // Print the title of the movie
    console.log(movieData.title);
  } else {
    // Log an error message if the request failed
    console.error('Request failed with status:', response.statusCode);
  }
});

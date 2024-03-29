#!/usr/bin/node

// Write a script that prints the number of movies where the character “Wedge Antilles” is present.

// The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
// Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
// You must use the module request

// Import the 'request' module for making HTTP requests
const request = require('request');

// Define a function to count the number of movies where the character "Wedge Antilles" is present
async function countMoviesWithWedge (url) {
  // Make a GET request to the specified URL
  request.get(url, (error, response, body) => {
    // Check if an error occurred during the request
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode === 404) {
      // If resource not found (status code 404), print the status code
      console.log(`code: ${response.statusCode}`);
    } else if (body) {
      // If response body exists, parse it as JSON
      const results = JSON.parse(body).results;

      // Initialize a variable to count the number of movies with Wedge Antilles
      let count = 0;

      // Iterate over each movie
      for (const film of results) {
        // Iterate over each character in the movie
        for (const character of film.characters) {
          // Check if the character ID matches Wedge Antilles (ID 18)
          // /: Serves as the delimiter for the regular expression.
          // \: Is an escape character that allows us to match the forward slash / literally.
          // 18: Represents the character ID for "Wedge Antilles".
          // /: Matches another forward slash character.
          // g: Is a global flag that specifies the regular expression should be applied globally,
          // meaning it should find all occurrences within the string.
          if (character.match(/.\/18\//g)) {
            // If found, increment the count
            count += 1;
          }
        }
      }

      // Print the count of movies with Wedge Antilles
      console.log(count);
    }
  });
}

// Call the function with the API URL provided as command line argument
countMoviesWithWedge(process.argv[2]);

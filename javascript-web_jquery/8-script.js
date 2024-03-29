// Write a JavaScript script that fetches and lists the title for all movies
// by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
// All movie titles must be list in the HTML tag UL#list_movies
// You can’t use document.querySelector to select the HTML tag
// You must use the JQuery API


// Execute the code when the document is fully loaded
$(function () {
  // Make an AJAX GET request to fetch movie data from the specified URL
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      // Iterate through each movie information in the response
      for (const info of data.results) {
        // Append a new <li> element with the movie title to the list
        $('#list_movies').append(`<li>${info.title}</li>`);
      }
    },
    error: function () {
      // Display an error message if the request fails
      $('#list_movies').text('Error: Name not found!');
    }
  });
});

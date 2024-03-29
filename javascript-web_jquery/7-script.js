// Write a JavaScript script that fetches the character name from this
// URL: https://swapi-api.hbtn.io/api/people/5/?format=json
// The name must be displayed in the HTML tag DIV#character
// You can’t use document.querySelector to select the HTML tag
// You must use the JQuery API

// Wait for the document to be fully loaded
$(document).ready(function () {
  // Make a GET request to the specified URL and handle the response
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    // Update the text content of the element with ID 'character'
    // with the character name obtained from the response data
    $('#character').text(data.name);
  });
});

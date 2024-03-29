// Write a JavaScript script that fetches from 
// https://hellosalut.stefanbohacek.dev/?lang=fr
// and displays the value of hello from that fetch in the HTML tag DIV#hello.

// The translation of “hello” must be displayed in the HTML tag DIV#hello
// You can’t use document.querySelector to select the HTML tag
// You must use the JQuery API
// Your script must work when it is imported from the <head> tag


// Execute the code when the document is fully loaded
$(function () {
  // Make an AJAX GET request to fetch the translation from the specified URL
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    // Success callback function when the request is successful
    success: function (data) {
      // Set the text content of the DIV#hello element with the translation of "hello"
      $('#hello').text(data.hello);
    },
    // Error callback function when the request fails
    error: function () {
      // Display an error message in the DIV#hello element
      $('#hello').text('Error: Translation not found!');
    }
  });
});

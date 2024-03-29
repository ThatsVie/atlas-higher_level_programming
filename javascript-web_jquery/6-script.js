// Write a JavaScript script that updates the text of the <header> element to
// New Header!!! when the user clicks on DIV#update_header
// You can’t use document.querySelector to select the HTML tag
// You must use the JQuery API


// Add a click event listener to the DIV#update_header element
$('DIV#update_header').click(function () {
  // Update the text content of the <header> element to "New Header!!!"
  $('header').text('New Header!!!');
});

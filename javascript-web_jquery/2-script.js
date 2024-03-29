// Write a JavaScript script that updates the text color of the
// <header> element to red (#FF0000) when user clicks on tag DIV#red_header:
// You can’t use document.querySelector to select the HTML tag
// You must use the JQuery API

// Add a click event listener to the DIV#red_header element
$('DIV#red_header').click(function () {
  // When the DIV#red_header element is clicked, update the text color of
  // the <header> element to red (#FF0000)
  $('header').css('color', '#FF0000');
});

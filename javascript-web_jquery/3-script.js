// Write a JavaScript script that adds the class red to the
// <header> element when the user clicks on the tag DIV#red_header
// You can’t use document.querySelector to select the HTML tag
// You must use the JQuery API

// Wait for the document to be fully loaded
$(document).ready(function(){
    // Add a click event listener to the DIV#red_header element
    $('DIV#red_header').click(function(){
        // Add the class "red" to the <header> element
        $('header').addClass('red');
    });
});

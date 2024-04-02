# Javascript Web Jquery
This repository contains JavaScript scripts developed using the JQuery library for various web development tasks. Each script performs a specific function, ranging from DOM manipulation to fetching data from external APIs and updating HTML content dynamically.

## Learning Objectives

<details>
<summary>Why JQuery makes front-end programming so easy: </summary>
<ul>
  <li>

JQuery simplifies front-end programming by providing a concise and intuitive syntax for common tasks like  (Document Object Model) manipulation, event handling, and AJAX requests. Its abstraction layer hides browser inconsistencies, allowing developers to write code that works across different browsers with ease, thus reducing development time and effort.

</ul> </li> </details>

<details>
<summary>How to select HTML elements in JavaScript:</summary>

<ul>
  <li>
    
In JavaScript, you can select HTML elements using methods like getElementById, getElementsByClassName, getElementsByTagName, querySelector, and querySelectorAll. These methods allow you to target specific elements in the DOM based on their ID, class, tag name, or CSS selectors.

</ul> </li> </details>

<details>
<summary>How to select HTML elements with JQuery:</summary>

<ul>
  <li>

In JQuery, you can select HTML elements using selectors similar to CSS selectors. For example, $('selector') selects elements based on CSS selector syntax. JQuery also provides additional methods for more complex selection criteria and chaining for combining selectors.

</ul> </li> </details>

<details>
<summary>Differences between ID, class, and tag name selectors: </summary>
  
<ul>

<li>
  
  ID selectors (#) target a specific element based on its unique ID attribute.</li>

<li>
  
  Class selectors (.) target elements based on their class attribute, which can be shared among multiple elements.</li>

<li>
  
  Tag name selectors target elements based on their HTML tag name.
  
</ul> </li> </details>

<details>
<summary>How to modify an HTML element style:</summary>
<ul>
  <li>

You can modify an HTML element's style using JavaScript by accessing its style property and setting specific CSS properties like element.style.property = value.

</ul> </li> </details>

<details>
<summary>How to get and update an HTML element's content: </summary>
<ul>
  <li>

To get and update an HTML element's content, you can use JavaScript or JQuery. JavaScript provides methods like document.getElementById() or document.querySelector() to select elements, while JQuery simplifies this process with selectors like $('selector'). Once selected, you can update the element's content using methods like .text() or .html() in JQuery, or by directly modifying the textContent or innerHTML properties in JavaScript.

</ul> </li> </details>

<details>
<summary>How to modify the DOM:</summary>
<ul>
  <li>

To modify the DOM (Document Object Model), you can use JavaScript or JQuery to add, remove, or change HTML elements and their attributes dynamically. This involves selecting elements using methods like document.getElementById() or document.querySelector() in JavaScript, or JQuery selectors like $('selector'), and then manipulating them using methods like .append(), .remove(), .addClass(), .removeClass(), etc. JavaScript provides direct access to DOM elements and properties, while JQuery simplifies DOM manipulation with its concise syntax and methods.

</ul> </li> </details>

<details>
<summary>How to make a GET request with JQuery Ajax:</summary>
<ul>
  <li>


To make a GET request with JQuery Ajax, you can use the $ .ajax() function or shorthand methods like $ .get(). You specify the URL to request data from and handle the response using callback functions.

</ul> </li> </details>

<details>
<summary>How to make a POST request with JQuery Ajax:</summary>
<ul>
  <li>

To make a POST request with JQuery Ajax, you use the $ .ajax() function or shorthand methods like $ .post(). You specify the URL to send data to, along with the data to be sent in the request body, and handle the response using callback functions.

</ul> </li> </details>

<details>
<summary>How to listen/bind to DOM events:</summary>
<ul>
  <li>

You can listen to DOM events using JavaScript by selecting elements and attaching event listeners to them using methods like addEventListener. Events can include clicks, keypresses, mouse movements, and more.
</ul> </li> </details>

<details>
<summary>How to listen/bind to user events:</summary>
<ul>
  <li>
    
Listening to user events involves capturing interactions initiated by users, such as clicks, mouse movements, keyboard inputs, etc. In JavaScript, you can bind event listeners to elements using methods like addEventListener or JQuery methods like on() to respond to user actions effectively.

</ul> </li> </details>

## Task Summary

<details>
<summary>0-main.html and 0-script.js</summary>
<ul>
  <li>

0-main.html is an HTML file that serves as the main entry point for the web page.

It contains the structure of the web page, including the header and footer elements.

Inside the body tag, it includes a script tag that references the JavaScript file 0-script.js using the src attribute.

The purpose of 0-main.html is to define the layout and structure of the web page and to include external resources like JavaScript files.</li>


<li> 
  
0-script.js is a JavaScript file containing code that manipulates the HTML elements of 0-main.html.

It selects the header element using document.querySelector and updates its text color to red (#FF0000) by modifying its style.color property.

The code in 0-script.js achieves the task specified in the instructions by directly accessing and modifying the DOM elements.

The purpose of 0-script.js is to add dynamic behavior to the web page by responding to user actions or modifying the content of HTML elements. </li>


<li>
  
0-main.html includes 0-script.js using a script tag, effectively linking the JavaScript code to the HTML document.

When the browser loads 0-main.html, it also loads and executes the JavaScript code in 0-script.js.

In this specific task, 0-script.js updates the text color of the header element defined in 0-main.html.

Both files work together to create the desired functionality on the web page, demonstrating the interaction between HTML and JavaScript in a web development context.

</ul> </li> </details>

<details>
<summary>1-main.html and 1-script.js</summary>
<ul>
  <li>
    
1-main.html is an HTML file that defines the structure of a web page. It includes a header element and a footer element, along with a reference to an external JavaScript file (1-script.js) using the script tag. The HTML file also imports the JQuery library using a CDN link in the head section. </li>

<li> 
  
1-script.js is a JavaScript file containing code that uses the JQuery library to manipulate the HTML elements defined in 1-main.html. It selects the header element using $ ('header'), a JQuery selector, and changes its text color to red (#FF0000) using the .css() method provided by JQuery. </li>

<li>
  
1-main.html serves as the HTML structure of the web page, while 1-script.js contains the JavaScript code that interacts with the HTML elements defined in 1-main.html. When the HTML file is loaded in a web browser, the browser also executes the JavaScript code from 1-script.js, allowing the manipulation of HTML elements as specified in the script.

</ul> </li> </details>

<details>
<summary>2-main.html and 2-script.js</summary>
<ul>
  <li>

2-main.html is an HTML file that defines the structure of a web page. It includes a header element, a div element with the id red_header, and a footer element. It imports the JQuery library using a CDN link in the head section and includes a reference to an external JavaScript file (2-script.js) using the script tag.</li>

<li> 
  
2-script.js is a JavaScript file containing code that uses the JQuery library to add a click event listener to the div element with the id red_header. When this div element is clicked, the script changes the text color of the header element to red (#FF0000) using the .css() method provided by JQuery. </li>

<li> 
  
2-main.html defines the structure of the web page, and 2-script.js contains the JavaScript code that interacts with the HTML elements defined in 2-main.html, performing the specified action when the div element with the id red_header is clicked.

</ul> </li> </details>

<details>
<summary>3-main.html and 3-script.js</summary>
<ul>
  <li>
    
3-main.html is a HTML file that defines the structure of a web page. It includes the following elements:

A title tag specifying the title of the webpage as "Holberton School". 

A script tag importing the JQuery library from a CDN (Content Delivery Network).

A style tag defining a CSS style with the class .red that sets the text color to red (#FF0000).

The body section contains:

A header element with the text "First HTML page".

A div element with the id red_header and the text "Red header".

A footer element with the text "Holberton School - 2017".

Finally, there's a script tag importing the JavaScript file 3-script.js. </li>

<li>
  
3-script.js is a  JavaScript file containing the script responsible for adding functionality to the webpage. 

It waits for the document to be fully loaded using $(document).ready().

It then attaches a click event listener to the div element with the id red_header.

When the div element is clicked, it adds the class "red" to the header element using JQuery's .addClass() method. </li>

<li>
  
3-script.js provides the functionality for the HTML page defined in 3-main.html. It adds interactivity to the webpage by responding to user clicks on the "Red header" div element and modifying the appearance of the header element. The HTML file includes the necessary JavaScript file and JQuery library to enable this functionality. 

</ul> </li> </details>

<details>
<summary>4-main.html and 4-script.js</summary>
<ul>
  <li>
    
4-main.html is a HTML file that defines the structure of a webpage. It includes a header element with the class "green", a div element with the id "toggle_header", and a footer element. It imports the jQuery library and a JavaScript file (4-script.js). The header's color is initially set to green, and when the "Toggle header" div is clicked, it triggers an action defined in 4-script.js. </li>

<li>
  
4-script.js is a JavaScript file containing the script to toggle the class of the header element between "red" and "green" when the user clicks on the "Toggle header" div. It uses jQuery to select the elements and add event listeners. When the "Toggle header" div is clicked, it toggles the class of the header element between "red" and "green" using the .toggleClass() method. </li>

<li>
  
4-main.html provides the structure and elements for the webpage, while 4-script.js provides the functionality to toggle the class of the header element in response to user interaction. 4-script.js is linked to 4-main.html using the script tag, allowing the browser to execute the JavaScript code when the HTML file is loaded.

</ul> </li> </details>

  <details>
<summary>5-main.html and 5-script.js</summary>
<ul>
  <li>
    
5-main.html is an HTML file that defines the structure of a web page.
It includes a header tag with the text "First HTML page", a div tag with the id "add_item", and a ul tag with the class "my_list". Additionally, it includes a script tag to import the JQuery library and another script tag to link the JavaScript file (5-script.js).
  
The purpose of this file is to provide the content and structure for the web page. </li>

<li>
  
5-script.js is a JavaScript file that contains the script responsible for adding a new li element to the list when the user clicks on the "Add item" button.
It uses JQuery to add a click event listener to the div element with the id "add_item". When this element is clicked, a new li element with the text "Item" is appended to the ul element with the class "my_list".
  
The script interacts with the HTML elements defined in 5-main.html using JQuery selectors and methods.

The purpose of this file is to provide the interactivity and behavior for the web page. </li>

<li>
  
5-main.html serves as the markup for the web page, defining its structure and content.
5-script.js provides the functionality to the web page by adding interactivity through JavaScript.
Together, these files work in tandem to create a web page where users can click on a button to dynamically add new list items. 

</ul> </li> </details>

<details>
<summary>6-main.html and 6-script.js</summary>
<ul>
  <li>
    
6-main.html is an HTML file that defines the structure of a webpage. It contains a header element with the text "First HTML page", a div element with the id "update_header" which says "Update the header", and a footer with the text "Holberton School - 2017". It includes a reference to the JQuery library and a script tag linking to 6-script.js. The purpose of this HTML file is to provide the content and structure for the webpage. </li>

<li>
  
6-script.js is a JavaScript file containing code that manipulates the DOM using the JQuery library. It adds a click event listener to the div element with the id "update_header". When this div is clicked, it updates the text content of the header element to "New Header!!!" using JQuery. The script utilizes the JQuery API for DOM manipulation. Its purpose is to provide interactivity to the webpage by responding to user actions.</li>

<li>
  
6-main.html provides the structure and content of the webpage, while 6-script.js enhances the webpage's functionality by adding interactivity. The JavaScript file is linked to the HTML file via a script tag, allowing it to access and manipulate the HTML elements defined in the HTML file.6-script.js is responsible for responding to user clicks on the "Update the header" div element and updating the text content of the header accordingly.

</ul> </li> </details>


<details>
<summary>7-main.html and 7-script.js</summary>
<ul>
  <li>
    
7-main.html is an HTML file that sets up the structure of a web page. It includes a header, a div element with the id "character", and a footer. It includes a script tag that links to the JavaScript file 7-script.js, allowing it to execute within the HTML document.</li>

<li>
  
7-script.js is a JavaScript file that contains the logic for fetching character data from a specific API endpoint (https://swapi-api.hbtn.io/api/people/5/?format=json) using JQuery's AJAX method $ .get(). Once the data is retrieved, it updates the content of the div id="character" element with the character's name extracted from the API response.</li>

<li>
  
7-main.html serves as the HTML structure of the web page, while 7-script.js contains the dynamic behavior of fetching and displaying the character's name. When the HTML file is loaded in a web browser, the JavaScript file is executed, and the character's name is fetched and displayed in the designated div element, as specified in the HTML file.

</ul> </li> </details>

<details>
<summary>8-main.html and 8-script.js</summary>
<ul>
  <li>
    
8-main.html is an HTML file that sets up the structure of the web page. It includes a header, an empty unordered list (ul), and a footer. The header indicates that the page is about Star Wars movies. It also includes a script tag that imports the JQuery library and another script tag that links to the JavaScript file 8-script.js.</li>

<li>
  
8-script.js is a JavaScript file that contains the logic to fetch data about Star Wars movies from a specific URL using the JQuery AJAX method. Upon successfully retrieving the data, it iterates through the list of movies and appends the titles as list items (li) to the unordered list (ul). If the request fails, it displays an error message in the list. This script must be executed after the HTML document is fully loaded, so it waits for the document to be ready before making the AJAX request.</li>


<li>
  
The HTML file (8-main.html) provides the structure and layout for the web page.
The JavaScript file (8-script.js) is responsible for fetching data about Star Wars movies and updating the HTML content dynamically.
The HTML file includes the JavaScript file using a script tag, allowing the JavaScript code to interact with and manipulate the HTML elements defined in the HTML file.

</ul> </li> </details>

<details>
<summary>9-main.html and 9-script.js</summary>
<ul>
  <li>
    
9-main.html is an HTML file that serves as the structure for a web page. It includes a header, a div with the ID hello where the translation of "hello" will be displayed, and a footer section. It also imports JQuery library and a JavaScript file named 9-script.js using script tags. This HTML file is responsible for displaying content to the user. </li>

<li>
  
9-script.js is a JavaScript file that contains the logic for fetching a translation of "hello" from a specified URL and updating the content of the div element with the ID hello accordingly. It uses the JQuery API to make an AJAX GET request to the URL https://hellosalut.stefanbohacek.dev/?lang=fr. If the request is successful, it updates the text content of the div element with the translation obtained from the response data. If the request fails, it displays an error message in the div element. </li>

<li>
  
9-main.html provides the structure and layout for the web page.
  
9-script.js provides the functionality for fetching the translation and updating the content dynamically.

9-main.html imports 9-script.js to utilize its functionality, allowing the web page to fetch and display the translation of "hello" to the user.

</ul> </li> </details>

## Usage/ Task Descriptions with Visuals

Clone this repository

```bash
git clone https://github.com/ThatsVie/atlas-higher_level_programming.git
```

Navigate to javascript-web_jquery directory

```bash
cd javascript-web_jquery
```

<details>
<summary>
Step-by-step instructions for opening and testing your HTML files using VS Code with the Live Server extension: </summary>


These instructions guide you through starting the local development server, opening the HTML files in the browser for testing, and accessing the browser's developer tools to monitor JavaScript-related activities.

<ul>

<li>
  
Open Visual Studio Code (VS Code). </li>
  
<li>
  
In the upper-left corner of VS Code, click on "File" in the menu.</li>
  
<li>
  
Select "Open Folder" from the dropdown menu and navigate to the directory where your HTML files are located (specifically, the javascript-web_jquery folder). </li>
  
<li>
  
Once the folder is open in VS Code, navigate to the bottom right corner and click on "Go Live". This action will start a local development server on port 5500.</li>
  
<li>
  
VS Code will prompt you to open the browser. Click on the provided link to open your HTML files in the browser. You'll see a list of all your .html and .js files.</li>
  
<li>

From there, you can click on the .html files to view them in the browser. You can also inspect the elements, check the console for JavaScript-related logs or errors by right-clicking on the page and selecting "Inspect" or pressing Ctrl+Shift+I to open the browser's developer tools.</li>
  
<li>
  
Interact with your HTML files in the browser to test their functionality, such as clicking on elements or observing any changes made by your JavaScript code.</li>


![live server extension](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/d5adcdc4-f2a0-4b4e-87ac-335729146383)

![vscode go live](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/b9b7a4c9-0209-45c4-acd1-7f207585e86a)

![vscode open in browser](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/82aeac50-3b22-46bf-9d20-d1e25e527b7a)

![files in browser](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/e39e07f3-f965-4346-9ed5-48ee3a7beeaf)

</ul> </li> </details>
<details>
<summary>0-main.html and 0-script.js </summary>
<ul> 
0-main.html provides the structure of the web page, and 0-script.js adds interactivity by manipulating the content of the HTML elements defined in 0-main.html. They are linked together through the script tag, allowing the JavaScript code to interact with the HTML document.

The task requires writing a JavaScript script to update the text color of the  header element to red (#FF0000). The script should use document.querySelector to select the HTML tag and should not utilize the JQuery API.

0-scripts.js selects the header element using document.querySelector('header') and assigns it to the header constant. Then, it changes the text color of the header element to red (#FF0000) by setting the style.color property of the header constant.


![viewing 0-main html in browser and inspect open](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/db03bf12-0c75-4542-b530-c2e6b3a9e3fe)

</ul>  </details>
<details>
<summary> 1-main.html and 1-script.js </summary>
<ul>
1-main.html provides the structure of the web page, and 1-script.js adds interactivity by manipulating the content of the HTML elements defined in 1-main.html. They are linked together through the script tag, allowing the JavaScript code to interact with the HTML document.

This task requires writing a JavaScript script that changes the text color of the header element to red (#FF0000). However, unlike the previous task, this time, the JQuery API must be used to select the HTML tag, and the use of document.querySelector is prohibited. The script will be tested with the provided HTML file.

1-script.js utilizes the JQuery API to select the header element using $('header'). Then, it modifies the text color of the <header> element to red (#FF0000) by using the .css() method provided by JQuery.

![viewing 1-main html in browser and using inspect](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/59428922-95e8-4141-b056-22e50cafc15e)
</ul>  </details>

<details>
<summary> 2-main.html and 2-script.js  </summary>
<ul>

2-main.html defines the structure of the web page, and 2-script.js contains the JavaScript code that interacts with the HTML elements defined in 2-main.html, performing the specified action when the div element with the id red_header is clicked.

The task requires writing a JavaScript script that updates the text color of the header element to red (#FF0000) when the user clicks on the div element with the id red_header. The script must use the JQuery API for DOM manipulation and cannot use document.querySelector.

2-script.js attaches a click event listener to the div element with the id red_header using JQuery's selector ($('DIV#red_header')). When the div element is clicked, the code changes the text color of the header element to red (#FF0000) by applying the CSS property using JQuery's .css() method ($('header').css('color', '#FF0000')).

**Before clicking on Red header:**

![before pressing red header](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/1a910d68-cc4f-4942-b46d-10fa48cea511)

**After clicking on Red header:**

![after pressing red header](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/0105f3b3-613e-4529-a6f5-0ac71c7c642c)

</ul>  </details>

<details>
<summary> 3-main.html and 3-script.js </summary>
<ul>

The task requires writing a JavaScript script that adds the class "red" to the header element when the user clicks on the div element with the id red_header. The script should use the JQuery API for DOM manipulation and cannot use document.querySelector.

3-script.js waits for the document to be fully loaded using $(document).ready() function. Then, it attaches a click event listener to the div element with the id red_header using JQuery's selector ($('DIV#red_header')). When the div element is clicked, the code adds the class "red" to the header element using JQuery's .addClass() method ($('header').addClass('red')).

**Before clicking on Red header:**

![3-main html before clicking red header](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/8bb65451-502f-4281-a618-dd844b312454)


**After clicking on Red header:**

![3-main html after clicking red header](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/17c5febd-e989-42db-9bcc-185a61f6995e)

</ul>  </details>

<details>
<summary> 4-main.html and 4-script.js  </summary>
<ul>
  
The task requires writing a JavaScript script that toggles the class of the header element between "red" and "green" when the user clicks on the div element with the id toggle_header. The header element must always have one class, either "red" or "green", but never both at the same time and never empty.

4-script.js accomplishes the task using JQuery. It adds a click event listener to the div element with the id toggle_header. When clicked, it toggles the class of the header element between "red" and "green" using JQuery's .toggleClass() method. This ensures that the header element always has one class, switching between "red" and "green" on each click.

**Before clicking on Toggle header**

![4-main html before toggle](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/61dfe360-5ea4-4780-9b5f-b3bdd5b1c5f8)

**After clicking on Toggle header**

![4-main html after toggle](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/11fe0b8c-3afc-4267-8794-5fe878a29f28)

**Clicking on Toggle header again to show interaction**

![4-main html toggle again](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/766b510b-0382-43ad-992f-0dfed852d593)

</ul>  </details>

<details>
<summary> 5-main.html and 5-script.js  </summary>
<ul>
  
5-main.html serves as the markup for the web page, defining its structure and content.

5-script.js provides the functionality to the web page by adding interactivity through JavaScript.
  
The task requires writing a JavaScript script that adds a new li element containing the text "Item" to a list (UL.my_list) when the user clicks on the div tag with the id "add_item". The script must use the JQuery API and cannot use document.querySelector().

5-script.js adds a click event listener to the div element with the id "add_item". When the user clicks on this element, the script appends a new li element with the text "Item" to the ul element with the class "my_list". It achieves this by using JQuery's .click() method to listen for clicks on the specified element and .append() method to add the new li element to the list.

**Before clicking Add item**

![5-main html before clicking add item](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/3972013c-32db-42d0-89f2-04eca1b2a0bc)

**After clicking Add item**

![5-main html after clicking add item once](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/315c7dca-8275-491d-855b-c821242affab)

**After clicking Add item a few times**

![5-main html after clicking add item a few times](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/ee2ce9f8-893a-4989-90e2-e3e4a820aa7f)

</ul>  </details>

<details>
<summary> 6-main.html and 6-script.js  </summary>
<ul>
  
The task is to write a JavaScript script that updates the text content of the header element to "New Header!!!" when the user clicks on the div element with the id "update_header". The script should use the JQuery API for DOM manipulation.

6-script.js adds a click event listener to the div element with the id "update_header". When this div element is clicked, the text content of the header element is updated to "New Header!!!" using JQuery.

**Before clicking Update the header**

![6-main html before clicking Update the header](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/e81ac7ac-6029-4628-bbd4-b2b2dcb315b4)


**After clicking Update the header**

![6-main html after clicking Update the header](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/247cf342-03d7-45cc-8baa-babdbe0e6ebc)

</ul>  </details>

<details>
<summary> 7-main.html and 7-script.js  </summary>
<ul>

The task requires writing a JavaScript script that fetches character data from a specific URL (https://swapi-api.hbtn.io/api/people/5/?format=json) and displays the character's name in the HTML tag div id="character". The script should utilize the JQuery API for DOM manipulation.

7-script.js uses JQuery to wait for the document to be fully loaded ($(document).ready()). Then, it makes a GET request to the provided URL using $.get(). Upon receiving the response, it updates the text content of the div id="character" element with the character's name extracted from the response data.

![7-main html](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/988841dd-5bdd-4cf2-aadb-b8de13c02bcd)

</ul>  </details>

<details>
<summary> 8-main.html and 8-script.js  </summary>
<ul>

The task involves writing a JavaScript script that fetches movie data from a specific URL (https://swapi-api.hbtn.io/api/films/?format=json) and lists the titles of all the movies in an unordered list (ul). The script must use the JQuery API to make the AJAX request and manipulate the DOM to display the movie titles.

8-script.js starts by waiting for the document to be fully loaded ($(function () { ... })).

It then makes an AJAX GET request to the specified URL using $.ajax().

Upon successful retrieval of data, it iterates through each movie object in the response (data.results) using a for loop.

For each movie, it appends a new li element containing the movie title to the unordered list (#list_movies) using JQuery's .append() method.

If the AJAX request fails, an error message is displayed in the list.

![8-main html](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/0eb83c14-2bdc-42d9-9e76-024715bea684)

</ul>  </details>

<details>
<summary> 9-main.html and 9-script.js  </summary>
<ul>

This task involves writing a JavaScript script that fetches a translation of "hello" in French from a specific URL and displays it in an HTML div element with the ID hello. The script must use the JQuery API and be imported from the head tag of an HTML document.

9-script.js starts by waiting for the document to be fully loaded using $(function () {...}).

It then makes an AJAX GET request to the specified URL (https://hellosalut.stefanbohacek.dev/?lang=fr).

If the request is successful, the script updates the text content of the div element with the ID hello with the translation of "hello" obtained from the response data.

If the request fails, it displays an error message in the div element.

![9-main html](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/242ee27b-d30c-48b0-8281-7230cab4b908)

</ul>  </details>

With love,

Vie Paula - [Github](https://github.com/ThatsVie)

![OIP](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/611aaca7-adbd-4c3a-8ff5-100969eee9f0)

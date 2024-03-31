# Javascript Web Jquery

## Learning Objectives

**Why JQuery makes front-end programming so easy:**

JQuery simplifies front-end programming by providing a concise and intuitive syntax for common tasks like  (Document Object Model) manipulation, event handling, and AJAX requests. Its abstraction layer hides browser inconsistencies, allowing developers to write code that works across different browsers with ease, thus reducing development time and effort.

**How to select HTML elements in JavaScript:**

In JavaScript, you can select HTML elements using methods like getElementById, getElementsByClassName, getElementsByTagName, querySelector, and querySelectorAll. These methods allow you to target specific elements in the DOM based on their ID, class, tag name, or CSS selectors.

**How to select HTML elements with JQuery:**

In JQuery, you can select HTML elements using selectors similar to CSS selectors. For example, $('selector') selects elements based on CSS selector syntax. JQuery also provides additional methods for more complex selection criteria and chaining for combining selectors.

**Differences between ID, class, and tag name selectors:**

ID selectors (#) target a specific element based on its unique ID attribute.

Class selectors (.) target elements based on their class attribute, which can be shared among multiple elements.

Tag name selectors target elements based on their HTML tag name.

**How to modify an HTML element style:**

You can modify an HTML element's style using JavaScript by accessing its style property and setting specific CSS properties like element.style.property = value.

**How to get and update an HTML element's content:**

To get an HTML element's content, you can access its innerHTML property. To update the content, you can assign new values to innerHTML or use methods like textContent, innerText, or innerHTML to set the content.

**How to modify the DOM:**

You can modify the DOM using JavaScript by creating, removing, or manipulating elements and their attributes, properties, and content. Methods like createElement, appendChild, removeChild, setAttribute, and removeAttribute are commonly used for DOM manipulation.

**How to make a GET request with JQuery Ajax:**

To make a GET request with JQuery Ajax, you can use the $.ajax() function or shorthand methods like $.get(). You specify the URL to request data from and handle the response using callback functions.

**How to make a POST request with JQuery Ajax:**

To make a POST request with JQuery Ajax, you use the $.ajax() function or shorthand methods like $.post(). You specify the URL to send data to, along with the data to be sent in the request body, and handle the response using callback functions.

**How to listen/bind to DOM events:**

You can listen to DOM events using JavaScript by selecting elements and attaching event listeners to them using methods like addEventListener. Events can include clicks, keypresses, mouse movements, and more.

**How to listen/bind to user events:**

Listening to user events involves capturing interactions initiated by users, such as clicks, mouse movements, keyboard inputs, etc. In JavaScript, you can bind event listeners to elements using methods like addEventListener or JQuery methods like on() to respond to user actions effectively.

## Task Overview

**0-main.html:**

0-main.html is an HTML file that serves as the main entry point for the web page.

It contains the structure of the web page, including the header and footer elements.

Inside the body tag, it includes a script tag that references the JavaScript file 0-script.js using the src attribute.

The purpose of 0-main.html is to define the layout and structure of the web page and to include external resources like JavaScript files.

**0-script.js:**

0-script.js is a JavaScript file containing code that manipulates the HTML elements of 0-main.html.

It selects the header element using document.querySelector and updates its text color to red (#FF0000) by modifying its style.color property.

The code in 0-script.js achieves the task specified in the instructions by directly accessing and modifying the DOM elements.

The purpose of 0-script.js is to add dynamic behavior to the web page by responding to user actions or modifying the content of HTML elements.

**Relationship:**

0-main.html and 0-script.js are related in the sense that 0-main.html includes 0-script.js using a script tag, effectively linking the JavaScript code to the HTML document.

When the browser loads 0-main.html, it also loads and executes the JavaScript code in 0-script.js.

In this specific task, 0-script.js updates the text color of the <header> element defined in 0-main.html.

Both files work together to create the desired functionality on the web page, demonstrating the interaction between HTML and JavaScript in a web development context.


## Usage

Clone this repository

```bash
git clone https://github.com/ThatsVie/atlas-higher_level_programming.git
```

Navigate to javascript-web_jquery directory

```bash
cd javascript-web_jquery
```

###  Step-by-step instructions for opening and testing your HTML files using VS Code with the Live Server extension:

1. Open Visual Studio Code (VS Code).
2. In the upper-left corner of VS Code, click on "File" in the menu.
3. Select "Open Folder" from the dropdown menu and navigate to the directory where your HTML files are located (specifically, the javascript-web_jquery folder).
4. Once the folder is open in VS Code, navigate to the bottom right corner and click on "Go Live". This action will start a local development server on port 5500.
5. VS Code will prompt you to open the browser. Click on the provided link to open your HTML files in the browser. You'll see a list of all your .html and .js files.
6. From there, you can click on the .html files to view them in the browser. You can also inspect the elements, check the console for JavaScript-related logs or errors by right-clicking on the page and selecting "Inspect" or pressing Ctrl+Shift+I to open the browser's developer tools.
7 .Interact with your HTML files in the browser to test their functionality, such as clicking on elements or observing any changes made by your JavaScript code.

These instructions guide you through starting the local development server, opening the HTML files in the browser for testing, and accessing the browser's developer tools to monitor JavaScript-related activities.

![vscode go live](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/b9b7a4c9-0209-45c4-acd1-7f207585e86a)

![vscode open in browser](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/82aeac50-3b22-46bf-9d20-d1e25e527b7a)

![files in browser](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/e39e07f3-f965-4346-9ed5-48ee3a7beeaf)


### 0-main.html and 0-script.js

0-main.html provides the structure of the web page, and 0-script.js adds interactivity by manipulating the content of the HTML elements defined in 0-main.html. They are linked together through the script tag, allowing the JavaScript code to interact with the HTML document.

The task requires writing a JavaScript script to update the text color of the  header element to red (#FF0000). The script should use document.querySelector to select the HTML tag and should not utilize the JQuery API.

0-scripts.js selects the header element using document.querySelector('header') and assigns it to the header constant. Then, it changes the text color of the header element to red (#FF0000) by setting the style.color property of the header constant.

With love,

Vie Paula - [Github](https://github.com/ThatsVie)

![OIP](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/611aaca7-adbd-4c3a-8ff5-100969eee9f0)



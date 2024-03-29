# Javascript Web Scraping
This repository contains a set of Node.js scripts for web scraping tasks. Each script is designed to perform a specific action related to web scraping and data retrieval.

## Learning Objectives

**Why JavaScript programming is amazing:**

JavaScript is amazing due to its versatility, allowing developers to create interactive and dynamic web applications. Its asynchronous nature enables non-blocking I/O operations, enhancing performance. JavaScript's wide adoption, extensive community support, and constant evolution through frameworks and libraries make it a powerful language for both frontend and backend development.

**How to manipulate JSON data:**

JSON (JavaScript Object Notation) is a lightweight data interchange format commonly used for transmitting data between a server and a web application. In JavaScript, JSON data can be manipulated using built-in methods such as JSON.parse() to convert JSON strings to JavaScript objects, and JSON.stringify() to convert JavaScript objects to JSON strings. Once parsed, JavaScript objects can be accessed and modified using standard object manipulation techniques.

**How to use request and fetch API:**

Request Module: The request module simplifies making HTTP requests in Node.js. It allows developers to send HTTP requests to servers and handle responses easily. With request, developers can perform tasks like fetching data from APIs, downloading files, and more.

Fetch API: In web browsers, the Fetch API provides a modern alternative to XMLHttpRequest for making network requests. It offers a more powerful and flexible interface for fetching resources asynchronously from the server. The Fetch API uses Promises, making it easier to handle asynchronous operations and chain requests.

**How to read and write a file using fs module:**
The fs (file system) module in Node.js provides functions for interacting with the file system. To read from a file, developers can use the fs.readFile() method, specifying the file path and encoding (optional) to receive the file's content asynchronously. To write to a file, the fs.writeFile() method is used, specifying the file path, data to be written, and encoding (optional). These methods allow developers to perform file I/O operations, such as reading configuration files, logging data, or storing application data.

**Additionally:**

Asynchronous programming is a programming paradigm that allows multiple tasks to be executed concurrently without blocking the execution of other tasks. In an asynchronous programming model, tasks are initiated and executed independently, and their results are handled asynchronously when they become available.

In the context of JavaScript, asynchronous programming is commonly used for tasks that involve I/O operations, such as reading from files, making network requests, or waiting for user input. Rather than waiting for these tasks to complete before moving on to the next instruction, asynchronous operations are initiated, and the program continues executing other tasks. When an asynchronous task completes, a callback function is invoked to handle the result.

Asynchronous programming in JavaScript is facilitated by features such as callbacks, Promises, and async/await syntax. These mechanisms allow developers to write non-blocking code that efficiently handles I/O-bound operations, improving the overall responsiveness and performance of applications.

## Tasks Overview
**0-readme.js**
This script reads and prints the content of a file.

**1-writeme.js**
This script writes a string to a file.

**2-statuscode.js**
This script displays the status code of a GET request to a specified URL.

**3-starwars_title.js**
This script prints the title of a Star Wars movie based on the episode number.

**4-starwars_count.js**
This script prints the number of movies where the character “Wedge Antilles” is present.

**5-request_store.js**
This script gets the contents of a webpage and stores it in a file.

**6-completed_tasks.js**
This script computes the number of tasks completed by user ID from a specified API URL.

## Setup
To get started with the project, ensure you have Node.js installed on your system. [ Visit this site for details about which version may be appropriate for you ](https://github.com/nodejs/Release)


Additionally, install semistandard globally using npm:

```bash
sudo npm install semistandard --global
```
Semistandard is a JavaScript coding style guide and linting tool that enforces consistent coding conventions, including the use of semicolons at the end of statements. It helps maintain clean, readable, and error-free code by ensuring adherence to standardized coding practices.

Run semistandard on your JavaScript files to check for adherence to the coding style guide.

You can use ``` semistandard --fix``` to automatically fix some of the linting errors

Before running the scripts, make sure you have installed the request module. You can install it globally using npm:

```bash
$ sudo npm install request --global
```

After installing the module, export the NODE_PATH to point to the global node_modules directory:
```bash
$ export NODE_PATH=/usr/lib/node_modules
```

**Note:** The request module has been deprecated since February 2020. However, it’s a simple and powerful module for practicing web scraping in JavaScript.

## Usage
Clone this repository

```bash
git clone https://github.com/ThatsVie/atlas-higher_level_programming.git
```

Navigate to javascript_objects_scopes_closures directory

```bash
cd javascript-web_scraping
```
### 0-readme.js

0-readme.js is a Node.js script designed to read and print the content of a file specified as a command line argument.

Input this command in your terminal:
```bash
./0-readme.js puggies
```

This command runs the script 0-readme.js with the command line argument puggies. The script attempts to read the content of the file named puggies. In this case, it successfully reads the file and prints its content:

Puggies are the best! I love them so much. My life is richer with them in it!

Input this command in your terminal: 
```bash
./0-readme.js nonexistent
```

This command runs the script 0-readme.js with the command line argument nonexistent. The script attempts to read the content of the file named nonexistent, which does not exist. As a result, it encounters an error (ENOENT: no such file or directory) and logs the error details:

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/65f3b588-c547-49a9-9f8c-b8a88a43a02d)


The script 0-readme.js is responsible for reading the content of a file specified as a command line argument and printing it to the console. If the file exists, its content is printed. If the file does not exist or there is an error during reading, an appropriate error message is displayed.

### 1-writeme.js

1-writeme.js is a Node.js script designed to write a string to a file. 

Input this command in your terminal:
```bash
./1-writeme.js my_file.txt "Pugs bring me joy"
```

This command executes the script 1-writeme.js with two command line arguments:

my_file.txt is the filename where the string "Pugs bring me joy" will be written.
"Pugs bring me joy" is the string content that will be written to the file specified by the first argument.

Input this command in your terminal:
```bash
cat my_file.txt ; echo ""
```

This command is used to display the contents of the file my_file.txt. 

cat my_file.txt: This command reads the contents of the file my_file.txt and prints it to the terminal.
;: This is a command separator, allowing multiple commands to be executed sequentially on one line.
echo "": This command simply prints a newline character to the terminal, providing a clean separation between the output of cat and the command prompt.

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/b137ee44-5e88-4c1f-abd2-3a8031d8080f)


The output of cat my_file.txt displays the content of the file my_file.txt, which is "Pugs bring me joy". The echo "" command is used here to add an empty line after the content of the file for better readability.

### 2-statuscode.js

2-statuscode.js is a Node.js script designed to make a GET request to a specified URL and display the status code of the response.

Input this command in your terminal: 
```bash
./2-statuscode.js https://homewardboundpugs.com/
```

This command runs the script 2-statuscode.js with the URL https://homewardboundpugs.com/ as an argument.

The script makes a GET request to the specified URL using the request module.

The server responds with a status code of 200, which means "OK". This indicates that the request was successful, and the resource exists on the server.

The script prints code: 200 to the console, indicating that the status code returned by the server is 200.

Input this command in your terminal:
```bash
./2-statuscode.js https://homewardboundpugs.com/nope
```
This command runs the script 2-statuscode.js with the URL https://homewardboundpugs.com/nope as an argument.

The script makes a GET request to the specified URL using the request module.

The server responds with a status code of 404, which means "Not Found". This indicates that the requested resource could not be found on the server.

The script prints code: 404 to the console, indicating that the status code returned by the server is 404.

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/36b4a941-3d59-4b63-b81d-96a11943f982)

The commands are testing the script with different URLs to see how it behaves when making GET requests to different endpoints. The script retrieves the status codes returned by the server and prints them to the console, allowing you to verify whether the requests were successful and the resources exist on the server.

### 3-starwars_title.js

3-starwars_title.js is a Node.js script designed to print the title of a Star Wars movie where the episode number matches a given integer. It uses [This Star Wars API](https://swapi-api.hbtn.io/).

Input this command in your terminal:
```bash
./3-starwars_title.js 1
```

This command runs the script 3-starwars_title.js with the movie ID 1 as an argument.

The script makes a request to the Star Wars API to retrieve information about the movie with episode number 1.

The Star Wars movie with episode number 1 is "A New Hope".

The script prints A New Hope to the console.

Input this command in your terminal: 
```bash
./3-starwars_title.js 5
```

This command runs the script 3-starwars_title.js with the movie ID 5 as an argument.

The script makes a request to the Star Wars API to retrieve information about the movie with episode number 5.

The Star Wars movie with episode number 5 is "Attack of the Clones".

The script prints Attack of the Clones to the console.

Input this command in your terminal:
```bash
./3-starwars_title.js Pugs
```

This command runs the script 3-starwars_title.js with the argument Pugs, which is an invalid movie ID.

The script attempts to make a request to the Star Wars API with the invalid movie ID.

Since Pugs is not a valid movie ID, the request fails, and the server responds with a status code of 404 (Not Found).

The script handles this error by printing the error message Request failed with status: 404 to the console.

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/83ca9888-49f1-4027-b738-b078cf532bd0)

These commands allow you to retrieve and print the title of a specific Star Wars movie by providing its episode number (movie ID) as a command line argument. If the provided movie ID is invalid, the script handles the error appropriately and prints an error message.

### 4-starwars_count.js

4-starwars_count.js is a Node.js script designed to print the number of movies where the character "Wedge Antilles" is present.

Input this command in your terminal:
```bash
./4-starwars_count.js https://swapi-api.hbtn.io/api/films
```

The command ./4-starwars_count.js https://swapi-api.hbtn.io/api/films is running the script 4-starwars_count.js with the URL https://swapi-api.hbtn.io/api/films as a command-line argument.

The output 3 indicates that the script has counted the number of movies where the character "Wedge Antilles" is present, and in this case, it has found that there are three such movies.

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/ad5cdbbf-1be9-4f11-a2ce-42427fbe9525)

### 5-request_store.js

5-request_store.js is a Node.js script designed to get the contents of a webpage and stores it in a file.

Input this commands in your terminal:
```bash
./5-request_store.js http://loripsum.net/api loripsum
```

This command executes the script 5-request_store.js, passing the Loripsum API URL (http://loripsum.net/api) as the first argument and the file path (loripsum) as the second argument.

The script sends a request to the Loripsum API to fetch content and stores the response in a file named loripsum.

Input this command in your terminal:
```bash
cat loripsum
```

This command prints the contents of the loripsum file to the terminal. The output shows the lorem ipsum text obtained from the Loripsum API and stored in the loripsum file.


![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/adb2cb0a-9af0-4748-848b-64cd2f555346)

### 6-completed_tasks.js

6-completed_tasks.js is a Node.js script designed to compute the number of tasks completed by user id.

Input this command in your terminal:
```bash
./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
```

The command is executing a Node.js script 6-completed_tasks.js, and it's passing the URL https://jsonplaceholder.typicode.com/todos as a command-line argument to the script.

Upon execution, the script retrieves data from the specified API URL, which is a list of todos. It then processes the todos to count the number of completed tasks for each user and prints the results to the console.

The output displayed is a JSON object where each key represents a user ID, and the corresponding value represents the number of completed tasks by that user.


![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/d10d1e83-5bc1-4d0a-83bb-9990ca3fe824)


With love,

Vie Paula - [Github](https://github.com/ThatsVie)


![download](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/1e367673-5158-4dd7-8af4-7fdaf6b85df5)

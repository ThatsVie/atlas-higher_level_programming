# Javascript Warm Up
This project is designed to help you become familiar with JavaScript programming concepts through a series of hands-on tasks. By completing these tasks, you'll gain practical experience and understanding of essential JavaScript concepts.

## Learning Objectives

**Why JavaScript programming is amazing:**

JavaScript is amazing because of its versatility, powering dynamic web applications, server-side development, and even mobile applications.

**How to run a JavaScript script:**

To run a JavaScript script, you can use the Node.js runtime environment by executing the script file with the node command in the terminal.

**How to create variables and constants:**

In JavaScript, you can create variables using let or const keywords, with let allowing reassignment and const creating immutable variables.

**Differences between var, const, and let:**

var is function-scoped, let is block-scoped, and const creates variables that cannot be reassigned after initialization.

**Data types available in JavaScript:**

JavaScript supports various data types, including strings, numbers, booleans, arrays, objects, functions, and symbols.

**How to use if, if...else statements:**

Conditional statements such as if and if...else allow you to execute code conditionally based on boolean expressions. (Boolean expressions are expressions that evaluate to either true or false.)

**How to use comments:**

Comments in JavaScript can be single-line (//) or multi-line (/* */) and are used to add notes or explanations within the code.

**How to assign values to variables:**

You can assign values to variables using the assignment operator (=), allowing you to store and manipulate data within your programs.

**How to use while and for loops:** 

Loops like while and for allow you to execute a block of code repeatedly until a condition is met or for a specified number of iterations.

**How to use break and continue statements:**

break is used to exit a loop prematurely, while continue skips the rest of the loop iteration and continues to the next one.

**What is a function and how to use functions:**

Functions in JavaScript are blocks of reusable code that can be called with parameters and may return a value.

**What does a function that does not use any return statement return:**

A function that does not use a return statement implicitly returns undefined.

**Scope of variables:**

Variables in JavaScript have either global or local scope, with local variables defined within functions and block-scoped variables introduced by let and const.

**Arithmetic operators and how to use them:**

JavaScript supports various arithmetic operators such as addition (+), subtraction (-), multiplication (*), division (/), and modulus (%).

**How to manipulate dictionary:** 

In JavaScript, dictionaries are referred to as objects and can be manipulated using dot notation or bracket notation to access or modify their properties.

**How to import a file:**

In Node.js, you can import a file/module using the require function, specifying the path to the file/module you want to import.

## Setup
To get started with the project, ensure you have Node.js installed on your system. [Visit the website](https://nodejs.org/en)


Additionally, install semistandard globally using npm:
```bash
sudo npm install semistandard --global
```

## Tasks Overview

**0-javascript_is_amazing.js:** 
Print "JavaScript is amazing" using a constant variable.

**1-multi_languages.js:** 
Print three lines using an array of strings and a loop.

**2-arguments.js:**
Print a message based on the number of arguments passed to the script.

**3-value_argument.js:**
Print the first argument passed to the script.

**4-concat.js:** 
Print two arguments passed to the script in a specific format.

**5-to_integer.js:** 
Print an integer argument converted to a specific format.

**6-multi_languages_loop.js:** 
Print three lines using a loop.

**7-multi_c.js:** 
Print "C is fun" a certain number of times.

**8-square.js:** 
Print a square using a loop.

**9-add.js:** 
Print the addition of two integers.

**10-factorial.js:** 
Compute and print the factorial of an integer.

**11-second_biggest.js:** 
Search for the second biggest integer in the list of arguments.

**12-object.js:** 
Update a script to replace a specific value within an object.

**13-add.js:** 
Write a function that returns the addition of two integers, visible from outside.

## Usage
Clone this repository
```bash
git clone https://github.com/ThatsVie/atlas-higher_level_programming.git
```

Navigate to javascript-warm_up directory
```bash
cd javascript-warm_up
```
**0-javascript_is_amazing.js:**

Input this command in your terminal:

```bash
./0-javascript_is_amazing.js
```

The command ./0-javascript_is_amazing.js is executing a JavaScript file named 0-javascript_is_amazing.js using the Node.js runtime environment. The ./ before the filename indicates that the file is located in the current directory. When you run this command in your terminal, Node.js executes the JavaScript code in the specified file. As a result, it prints the string "JavaScript is amazing" to the terminal.

Input this command in your terminal:

```bash
semistandard ./0-javascript_is_amazing.js
```

The command semistandard ./0-javascript_is_amazing.js is using the semistandard tool to check the JavaScript file 0-javascript_is_amazing.js for coding style and standards compliance. semistandard is a linter that enforces the semicolon standard for JavaScript code. It ensures that the code follows a specific set of rules, such as indentation, spacing, and semicolon usage. If there are any violations, semistandard will report them in the terminal along with the corresponding line numbers.
Since no issues are found in the code, semistandard exits without producing any output, indicating that the code meets the style standards enforced by semistandard.

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/a1348838-19eb-45c6-a978-307b29901560)

**1-multi_languages.js**

Input this command in your terminal:

```bash
./1-multi_languages.js
```

The command ./1-multi_languages.js is executing a JavaScript file named 1-multi_languages.js using the Node.js runtime environment. When you run this command in your terminal, Node.js executes the JavaScript code contained in the file.

The JavaScript code inside 1-multi_languages.js contains three console.log() statements, each printing a different string to the terminal. Therefore, executing the script results in printing the following lines to the terminal:

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/e558e3aa-b5f8-4d03-9592-d3d655925220)

**2-arguments.js**

These commands are executing the JavaScript file named 2-arguments.js using the Node.js runtime environment. When you run each of these commands in your terminal, Node.js executes the JavaScript code contained in the file.

Input this commands in your terminal:
```bash
./2-arguments.js
```

Prints "No argument" to the terminal.
When no additional arguments are provided after the script name, the JavaScript code inside 2-arguments.js detects this and prints "No argument" to the terminal.

Input this command in your terminal:

```bash
./2-arguments.js Puggie
```

Prints "Argument found" to the terminal.
When one argument ("Puggie") is provided after the script name, the JavaScript code inside 2-arguments.js detects this and prints "Argument found" to the terminal.

Input this command in your terminal"

```bash
./2-arguments.js Puggie Wuggie
```

Prints "Arguments found" to the terminal.
When multiple arguments ("Puggie" and "Wuggie) are provided after the script name, the JavaScript code inside 2-arguments.js detects this and prints "Arguments found" to the terminal.

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/47ae6236-5bdb-46e4-a567-410a74a33e99)

**3-value_argument.js**

These commands are executing a JavaScript file named 3-value_argument.js using the Node.js runtime environment. When you run each of these commands in your terminal, Node.js executes the JavaScript code contained in the file.

Input this command in your terminal:

```bash
./3-value_argument.js
```
Prints "No argument" to the terminal.
When no additional arguments are provided after the script name, the JavaScript code inside 3-value_argument.js detects this and prints "No argument" to the terminal.

Input this command in your terminal:
```bash
./3-value_argument.js Puggie
```

Prints "Puggie" to the terminal.
When one argument ("Puggie") is provided after the script name, the JavaScript code inside 3-value_argument.js detects this and prints the provided argument ("Puggie") to the terminal. The script simply prints the first argument passed to it.

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/41baf691-17fe-4601-a588-d84608efaf44)

**4-concat.js**

These commands are executing a JavaScript file named 4-concat.js using the Node.js runtime environment. When you run each of these commands in your terminal, Node.js executes the JavaScript code contained in the file.

Input this command in your terminal:
```bash
./4-concat.js Pug Cool
```
Prints "Pug is Cool" to the terminal.
When two arguments ("Pug" and "Cool") are provided after the script name, the JavaScript code inside 4-concat.js detects this and concatenates the two arguments with the string " is " in between, then prints the result ("Pug is Cool") to the terminal.

Input this commandin your terminal:
```bash
./4-concat.js Pug
```

Prints "Pug is undefined" to the terminal.
When one argument ("Pug") is provided after the script name, the JavaScript code inside 4-concat.js detects this and attempts to concatenate it with an undefined second argument. Since the second argument is not provided, it is undefined, resulting in the output "Pug is undefined".

Input this command in your terminal:

```bash
./4-concat.js
```

Prints "undefined is undefined" to the terminal.
When no arguments are provided after the script name, the JavaScript code inside 4-concat.js detects this and attempts to concatenate two undefined arguments, resulting in the output "undefined is undefined".

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/0990e759-e30a-452a-8f73-ff107daa8de5)












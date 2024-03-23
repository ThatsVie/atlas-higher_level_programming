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

**5-to_integer.js**

These commands are executing a JavaScript file named 5-to_integer.js using the Node.js runtime environment. When you run each of these commands in your terminal, Node.js executes the JavaScript code contained in the file.

Input this command in your terminal:

```bash
./5-to_integer.js
```

Prints "Not a number" to the terminal.
When no arguments are provided after the script name, the JavaScript code inside 5-to_integer.js detects this and prints "Not a number" to the terminal.

Input this command in your terminal:
```bash
./5-to_integer.js 89
```

Prints "My number: 89" to the terminal.
When the argument "89" (without quotes) is provided after the script name, the JavaScript code inside 5-to_integer.js detects this and interprets it as a valid integer. It then prints "My number: 89" to the terminal.

Input this command in your terminal:
```bash
./5-to_integer.js "89"
```

Prints "My number: 89" to the terminal.
When the argument "89" (with quotes) is provided after the script name, the JavaScript code inside 5-to_integer.js detects this and interprets it as a valid integer. It then prints "My number: 89" to the terminal.

Input this command in your terminal:

```bash
./5-to_integer.js 89.89
```

Prints "My number: 89.89" to the terminal.
The output 'My number: 89.89' is produced because the JavaScript code inside 5-to_integer.js uses the parseInt() function to attempt to convert the string '89.89' to an integer. However, parseInt() only parses the integer portion of the string and ignores any non-numeric characters after that. As a result, it converts '89.89' to the integer 89. Since the conversion is successful, the script prints 'My number: 89.89' to the terminal."

Input this command in your terminal:
```bash
./5-to_integer.js Pugs
```

Prints "Not a number" to the terminal.
When the argument "Pugs" (without quotes) is provided after the script name, the JavaScript code inside 5-to_integer.js detects this and recognizes that it cannot be converted to an integer. Therefore, it prints "Not a number" to the terminal.

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/13793e91-1b1a-4d41-a9d2-d04f74b142dc)

**6-multi_languages_loop.js**

Input this command in your terminal:
```bash
./6-multi_languages_loop.js
```

The command ./6-multi_languages_loop.js is executing a JavaScript script named 6-multi_languages_loop.js. This script contains logic to print three lines of text ("C is fun", "Python is cool", and "JavaScript is amazing") using a loop. When you run this command in your terminal, the script is executed, and the output of the script, which includes the three lines of text, is displayed in the terminal.

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/abb7671a-aef0-46e1-8346-083728bbf6c0)

**7-multi_c.js**

Input this command in your terminal:

```bash
./7-multi_c.js 2
```

This command executes the JavaScript script named 7-multi_c.js with the argument 2. Inside the script, it loops two times and prints "C is fun" each time.

Input this command in your terminal:

```bash
./7-multi_c.js 5
```

This command executes the JavaScript script named 7-multi_c.js with the argument 5. Inside the script, it loops five times and prints "C is fun" each time.

Input this command in your terminal:

```bash
./7-multi_c.js
```

This command executes the JavaScript script named 7-multi_c.js without any arguments. Inside the script, there is a check to see if any arguments are provided. Since no arguments are provided, it prints "Missing number of occurrences".

Input this command in your terminal:
```bash
./7-multi_c.js -3
```

This command executes the JavaScript script named 7-multi_c.js with the argument -3. Inside the script, there is a check to see if the argument is a positive integer. Since -3 is not a positive integer, the script does nothing.

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/5cad04d8-17f3-42e3-9e22-1f86a1704631)

**8-square.js**

Input this command in your terminal:

```bash
./8-square.js
```

This command executes the JavaScript script named 8-square.js without providing any arguments. Inside the script, there is a check to see if any argument is provided. Since no argument is provided, it prints "Missing size".

Input this command in your terminal:

```bash
./8-square.js Pug
```

This command executes the JavaScript script named 8-square.js with the argument Pug. Inside the script, there is a check to see if the argument is a positive integer. Since Pug is not a positive integer, but a majestic breed of dog, it prints "Missing size".

Input this command in your terminal

```bash
./8-square.js 2
```

This command executes the JavaScript script named 8-square.js with the argument 2. Inside the script, it creates a 2x2 square made of 'X' characters and prints it to the console.

Input this command in your terminal:

```bash
./8-square.js 6
```

This command executes the JavaScript script named 8-square.js with the argument 6. Inside the script, it creates a 6x6 square made of 'X' characters and prints it to the console.

Input this command in your terminal:

```bash
./8-square.js -3
```

This command executes the JavaScript script named 8-square.js with the argument -3. Inside the script, there is a check to see if the argument is a positive integer. Since -3 is not a positive integer, the script does nothing.

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/49044db0-3b41-424b-835c-40c322d53b0a)

**9-add.js**

Input this command in your terminal:

```bash
./9-add.js 1 7
```

This command executes the JavaScript script named 9-add.js with two arguments: 1 and 7. Inside the script, the add function takes these two arguments and returns their sum, which is 8. The script then prints 8 to the console.

Input this command in your terminal:

```bash
./9-add.js 13 89
```

Similar to the first command, this command executes the 9-add.js script with two arguments: 13 and 89. The add function adds these two arguments together and returns their sum, which is 102. The script then prints 102 to the console.

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/5fff4789-5ffc-46d8-a859-652b772a7de0)

**10-factorial.js**

Input this command in your terminal:
```bash
./10-factorial.js
```

This command executes the JavaScript script named 10-factorial.js without any arguments. Inside the script, since no argument is provided, it computes the factorial of NaN, which is 1, and prints 1 to the console.

Input this command in your terminal:
```bash
./10-factorial.js 3
```

Here, the script is executed with the argument 3. Inside the script, it computes the factorial of 3, which is 3! = 3 * 2 * 1 = 6, and prints 6 to the console.

Input this command in your terminal:

```bash
./10-factorial.js 89
```

In this command, the script is executed with the argument 89. Inside the script, it computes the factorial of 89, which results in a very large number (1.6507955160908452e+136) due to the size of the factorial, and prints it to the console.

Input this command in your terminal:

```bash
./10-factorial.js 333
```

Similarly, the script is executed with the argument 333. Inside the script, it computes the factorial of 333, which exceeds the maximum value that can be represented in JavaScript (1.7976931348623157e+308). Therefore, it returns Infinity and prints it to the console.

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/33812835-80c9-4013-8122-fdb1da737710)

**11-second_biggest.js**

Input this command in your terminal:
```bash
./11-second_biggest.js
```

This command executes the JavaScript script named 11-second_biggest.js without any arguments. Inside the script, since no arguments are provided, it prints 0 to the console, indicating that no second biggest integer exists.

Input this command in the terminal:
```bash
./11-second_biggest.js 1
```

Here, the script is executed with the argument 1. Inside the script, it checks for the second biggest integer in the list of arguments. However, as only one argument is provided, there are no other integers to compare it to. Therefore, it prints 0 to the console.

Input this command in your terminal:

```bash
./11-second_biggest.js 4 2 5 3 0 -3
```

In this command, the script is executed with multiple arguments: 4 2 5 3 0 -3. Inside the script, it identifies the second biggest integer from the list (4 being the largest and 3 being the second largest) and prints 4 to the console.

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/449c6129-6dbf-4803-a211-e49ac8899551)

**12-object.js**

Input this command in your terminal:

```bash
./12-object.js
```

This command executes the JavaScript script named 12-object.js. 
The script defines an object myObject with type and value properties initially set to object and 12, respectively. It then updates the value property of myObject to 89 and prints both the initial and updated objects to the console.

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/0437ff9d-1080-45e8-b1c4-4f4269170d56)

**13-add.js**

Input this command in your terminal:
```bash
./13-main.js
```

The script 13-main.js is executing the function add from the 13-add.js module. The add function takes two arguments, 3 and 5, and returns their sum, which is 8. The result 8 is then printed to the console using console.log().

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/1c10b258-b381-4d2c-8211-bc0589cc7f74)

With love,
Vie Paula - [Github](https://github.com/ThatsVie)

![download](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/dab7a278-e769-49a0-9530-c84221806220)


# Javascript Objects Scopes Closures

## Learning Objectives

**Why JavaScript programming is amazing:**

JavaScript is an amazing programming language because of its versatility. It allows developers to build interactive and dynamic web applications, manipulate HTML and CSS, handle asynchronous events, and much more.

**How to create an object in JavaScript:**

In JavaScript, objects are key components used to store and organize data. You can create an object using object literal notation, constructor functions, or the class syntax introduced in ES6.

(ES6, or ECMAScript 2015, is the sixth edition of the ECMAScript standard, which is the specification that JavaScript is based on. ES6 introduced many new features and enhancements to the JavaScript language, including arrow functions, classes, template literals, let and const keywords for variable declaration, and much more. It significantly improved the syntax and functionality of JavaScript, making it more powerful and expressive for developers.)

**What this means:**

The this keyword refers to the current execution context in JavaScript. Its value depends on how a function is called and can dynamically change. It's commonly used within object methods to access and manipulate object properties.

**What undefined means:**

In JavaScript, undefined is a primitive value that represents the absence of a value. It's returned when accessing a variable that has not been initialized, or when a function does not explicitly return a value.

**Why variable type and scope is important:**

Understanding variable types (such as strings, numbers, booleans, objects, etc.) and scope (global scope, function scope, block scope) is crucial for writing maintainable JavaScript code. Proper variable type and scope management help prevent bugs and optimize code performance.

**What is a closure:**

A closure is a JavaScript feature that allows functions to retain access to variables from their parent scope even after the parent function has finished executing. Closures are commonly used to create private variables, implement data encapsulation, and manage asynchronous operations.

**What is a prototype:**

Prototypes are a core concept in JavaScript's object-oriented programming model. Every JavaScript object has a prototype, which is used to provide inheritance and shared behavior among objects. By modifying the prototype chain, you can extend and customize object functionality.

**How to inherit an object from another:**

Inheritance in JavaScript can be achieved through prototype chaining or using the class syntax introduced in ES6. By setting an object's prototype to another object, you can inherit properties and methods from the parent object, enabling code reuse and abstraction.


## Tasks Overview

### 0-rectangle.js:

This file contains an empty class `Rectangle` defined using the class notation. It serves as the starting point for creating a `Rectangle` class with properties and methods.

### 0-main.js:

This file is a script that demonstrates the usage of the `Rectangle` class defined in `0-rectangle.js`. It imports the `Rectangle` class, creates an instance of `Rectangle` named `r1`, and prints out the instance and its constructor.

### 1-rectangle.js:

This script defines a class Rectangle with a constructor that initializes width and height attributes based on the parameters passed to it.

### 1-main.js:

This script serves as a demonstration of the Rectangle class defined in 1-rectangle.js. It imports the Rectangle class using require('./1-rectangle'), creates multiple instances of Rectangle with different sets of parameters, and then logs the instances and their properties to the console.

### 2-rectangle.js:

This script defiines a class Rectangle using the class notation. The class has a constructor that initializes the width and height attributes if both parameters provided are positive integers. If w or h is not a positive integer or equal to 0, it returns an empty object.

### 2-main.js:

This script demonstrates the usage of the Rectangle class defined in 2-rectangle.js. It imports the Rectangle class, creates multiple instances of Rectangle with different sets of parameters, and then logs the instances and their properties to the console.

### 3-rectangle.js:

This script defines a class named Rectangle using the class notation in JavaScript. The constructor takes two arguments, w for width and h for height. If both w and h are positive numbers, the instance attributes width and height are initialized with these values. The class also includes a method print() which prints a rectangle made of 'X' characters based on the width and height.

### 3-main.js: 

This script demonstrates the usage of the Rectangle class defined in 3-rectangle.js. It imports the Rectangle class, creates two instances (r1 and r2) with different width and height values, and calls the print() method on each instance to print rectangles made of 'X' characters.

### 4-rectangle.js

This script contains a class named Rectangle that defines a rectangle. It has a constructor that takes two arguments, w for width and h for height, initializes the width and height properties of the rectangle, and returns an empty object if either w or h is not a positive integer. It also defines three methods: print(), rotate(), and double(). The print() method prints the rectangle using the character 'X', the rotate() method exchanges the width and height of the rectangle, and the double() method multiplies the width and height of the rectangle by 2.

### 4-main.js

This script demonstrates the usage of the Rectangle class defined in 4-rectangle.js. It imports the Rectangle class, creates an instance of Rectangle named r1 with width 2 and height 3, and prints it using the print() method. Then, it doubles the size of the rectangle using the double() method and prints it again. Finally, it rotates the rectangle using the rotate() method and prints it once more.

###




## Setup
To get started with the project, ensure you have Node.js installed on your system. [ Visit this site for details about which version may be appropriate for you ](https://github.com/nodejs/Release)


Additionally, install semistandard globally using npm:

```bash
sudo npm install semistandard --global
```
## Usage
Clone this repository

```bash
git clone https://github.com/ThatsVie/atlas-higher_level_programming.git
```

Navigate to javascript_objects_scopes_closures directory

```bash
cd javascript_objects_scopes_closures
```
### 0-rectangle.js & 0-main.js

Input this command in your terminal:

```bash
./0-main.js
```

When you run ./0-main.js, the script 0-main.js is executed. Inside this script, it imports the Rectangle class from 0-rectangle.js using require('./0-rectangle'). Then, it creates an instance of the Rectangle class named r1 using new Rectangle(). Finally, it logs r1 and its constructor to the console. In this case, r1 is an empty instance of the Rectangle class, and its constructor is the Rectangle class itself. Therefore, you see Rectangle {} and [class Rectangle] printed in the terminal.

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/d44fad95-1be8-432f-8d16-b9569927abbf)

### 1-rectangle.js & 1-main.js

Input this command in your terminal:

```bash
./1-main.js
```

In the output, ./1-main.js creates instances of the Rectangle class with different sets of parameters, such as (2, 3), (2, -3), and (2). For the first instance, the width is set to 2 and the height is set to 3. For the second instance, the width is 2, but the height is -3. For the third instance, only the width is provided, resulting in the height being undefined. Each instance and its properties are then logged to the console.

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/77b726e9-8890-4d88-a8a2-4a4c9357d27d)

### 2-rectangle.js & 2-main.js

Input this command in your terminal:

```bash
./2-main.js
```

The output shows an instance of Rectangle with width 2 and height 3 is created (r1).
Another instance is created with invalid parameters (negative height), resulting in an empty object (r2).
Two more instances with invalid parameters (one with one parameter and the other with a height of 0) also result in empty objects (r3 and r4).

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/d1480ae7-a6ca-44ce-a488-ddc25e40e877)

### 3-rectangle.js & 3-main.js

Input this command in the terminal:

```bash
./3-main.js
```

This output indicates that the print() method of the Rectangle class successfully printed two rectangles. The first rectangle has a width of 2 and a height of 3, so it prints two rows of 'X' characters, each row containing two 'X' characters.
The second rectangle has a width of 10 and a height of 5, so it prints five rows of 'X' characters, each row containing ten 'X' characters.

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/59fab7df-140e-4197-bd2f-aa5ee2cb0ea9)

### 4-rectangle.js & 4-main.js

Input this command in your terminal:

``bash
./4-main.js
```

The command ./4-main.js is executing the JavaScript file named 4-main.js using the Node.js interpreter. This script contains code that imports the Rectangle class from another file (4-rectangle.js), creates instances of the Rectangle class, and performs various operations such as printing, doubling, and rotating rectangles. When executed, this command runs the script and outputs the results of these operations to the console.

Normal: The initial rectangle has a width of 2 and a height of 3, so it prints three rows of 'X' characters, each row containing two 'X' characters.

Double: After doubling the size of the rectangle, its width becomes 4 and height becomes 6. Therefore, it prints six rows of 'X' characters, each row containing four 'X' characters.

Rotate: After rotating the rectangle, its width becomes 6 and height becomes 4. Hence, it prints four rows of 'X' characters, each row containing six 'X' characters.

![image](https://github.com/ThatsVie/atlas-higher_level_programming/assets/143755961/c3ab1923-a37d-45e2-8785-54038604e520)



















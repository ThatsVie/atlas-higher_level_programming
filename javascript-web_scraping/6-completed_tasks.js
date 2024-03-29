#!/usr/bin/node

// Write a script that computes the number of tasks completed by user id.
// The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
// Only print users with completed task
// You must use the module request

// Importing required module
const request = require('request');

// Extracting command line argument for API URL
const apiUrl = process.argv[2];

// Making a GET request to the specified API URL
request(apiUrl, (error, response, body) => {
  // Check if an error occurred during the request
  if (error) {
    console.log(error);
  } else {
    // If the request is successful, parse the response body as JSON
    const todos = JSON.parse(body);

    // Initialize an object to store completed tasks count for each user
    const completedTasksByUser = {};

    // Iterate over each todo
    for (const todo of todos) {
      // Check if the task is completed (completed: true)
      if (todo.completed) {
        // Increment the completed tasks count for the user
        if (completedTasksByUser[todo.userId] === undefined) {
          completedTasksByUser[todo.userId] = 1;
        } else {
          completedTasksByUser[todo.userId]++;
        }
      }
    }

    // Print the completed tasks count for each user
    console.log(completedTasksByUser);
  }
});

# Javascript Web Scraping
## Usage
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


In summary, the script 0-readme.js is responsible for reading the content of a file specified as a command line argument and printing it to the console. If the file exists, its content is printed. If the file does not exist or there is an error during reading, an appropriate error message is displayed.

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

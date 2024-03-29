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

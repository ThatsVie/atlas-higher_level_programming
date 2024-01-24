#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    #check if any of the parameters is an empty string
    if not filename or not search_string or not new_string:
        return

    #open the file in read mode
    with open(filename, 'r') as file:
        # read all the lines from the file
        lines = file.readlines()

        #open the file in write mode to overwrite contents
        with open(filename, 'w') as file:
            #iterate through the lines
            for line in lines:
                #write the original line
                file.write(line)

                #check if the search string is  present in line
                if search_string in line:
                    #append the new_string after the line containing the search string
                    file.write(new_string + '\n')
                

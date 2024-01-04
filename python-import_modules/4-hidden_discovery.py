#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    # Get the list of names in the hidden_4 module
    names_list = dir(hidden_4)

    # Iterate over each name in the list
    for name in names_list:
        # Check if the name does not start with double underscores
        if name[:2] != "__":
            # Print the name
            print(name)

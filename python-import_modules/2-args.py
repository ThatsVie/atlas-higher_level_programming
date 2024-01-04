#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # Number of command-line arguments excluding the script name
    num_args = len(sys.argv) - 1

    # Display the appropriate message based on the number of arguments
    if num_args == 1:
        print("Number of argument: 1:")
    elif num_args > 1:
        print("Number of arguments: {}:".format(num_args))
    else:
        print("Number of arguments: .")

    # Display each argument along with its position
    for i, arg in enumerate(sys.argv[1:], start=1):
         print("{}: {}".format(i, arg))

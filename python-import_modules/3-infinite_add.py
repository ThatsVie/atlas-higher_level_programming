#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # Calculate the number of command-line arguments
    arg_len = len(sys.argv) - 1

    # Display the appropriate message based on the number of arguments
    if arg_len == 1:
        print("1 argument:")
    elif arg_len > 1:
        print(f"{arg_len} arguments:")
    else:
        print("0 arguments.")

    # Display each argument along with its position
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")

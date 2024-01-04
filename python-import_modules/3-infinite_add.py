#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # Extract command-line arguments excluding the script name
    arguments = sys.argv[1:]

    # Sum all arguments (casted to integers)
    result = sum(int(arg) for arg in arguments)

    # Print the result
    print(result)

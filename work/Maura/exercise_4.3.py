# Write a program that redirects the standard output to a file whose path is passed as the first argument.
# Test this by having the program write several strings to the standard output.
    # Also, redirect the standard error output to the file.
# Verify the operation by including several statements that print to both streams. Is there a difference if the redirections are performed in a different order?

import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <output_file>")
        sys.exit(1)
    
    # get output file path
    output_file_path = sys.argv[1]

    # open the file in append mode to save prev writes
    with open(output_file_path, 'a') as output_file:
        # Redirect stdout and stderr to the file
        sys.stdout = output_file
        sys.stderr = output_file

        # Example output
        print("This is a standard output message.")
        print("This is another standard output message.")

        # Simulate an error message by printing to stderr
        print("This is a standard error message.", file=sys.stderr)
        print("This is another error message.", file=sys.stderr)

if __name__ == "__main__":
    main()

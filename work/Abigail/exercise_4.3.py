import sys

def redirect_output(file_path):
    # Redirect standard output
    sys.stdout = open(file_path, 'w')
    # Redirect standard error
    sys.stderr = sys.stdout

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python program.py <output_file>")
        sys.exit(1)
    
    output_file = sys.argv[1]
    
    # Redirect output
    redirect_output(output_file)

    # Test statements
    print("This is a test message written to standard output.")
    print("This is another test message written to standard output.")
    print("This is a test error message written to standard error.", file=sys.stderr)
    print("This is another test error message written to standard error.", file=sys.stderr)
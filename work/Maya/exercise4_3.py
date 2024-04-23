import sys

def redirect(file_path):
    with open(file_path, 'w') as f:
        sys.stdout = f
        sys.stderr = f

        print("Standard output test")

        print("Standard error test", file=sys.stderr)

        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to provide a file path")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        redirect(file_path)
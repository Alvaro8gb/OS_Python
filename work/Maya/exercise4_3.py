import sys

def redirect(file_path):
    try:
        with open(file_path, "w") as f:
            sys.stdout = f
            print("Hello, World!")
            print("Redirected from standard output")
    except Exception as e:
        print(e)
    finally:
        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to provide a file path")
    else:
        file_path = sys.argv[1]
        redirect(file_path)
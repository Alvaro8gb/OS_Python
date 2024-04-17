import os
import sys

def display_permission(file_path):
    if not os.path.exists(file_path):
        print(f"{file_path} does not exist")
        return
    permission = os.stat(file_path).st_mode
    print(f"permission of {file_path} is {permission}")
    print(f"Write permission: {'Yes' if permission & 0o200 else 'No'}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    elif len(sys.argv) == 1:
        file_path = input("Enter the file path: ")
    else:
        print("Invalid number of arguments")
        sys.exit(1)
    display_permission(sys.argv[1])
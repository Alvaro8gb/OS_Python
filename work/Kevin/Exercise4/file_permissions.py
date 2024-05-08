import os
import sys

def check_permissions(file_path):
    try:
        # Get file permissions
        permissions = os.stat(file_path).st_mode

        # Check if the user can write to the file. I understand this line
        # because I took computer organization and x86 assembly. I did use
        # chatgpt to help me come up with it though.
        user_can_write = bool(permissions & 0o200)

        # Print file permissions
        print("File permissions:", oct(permissions))

        # Print if the user can write to the file
        if user_can_write:
            print("You can write to this file.")
        else:
            print("You cannot write to this file.")
    except FileNotFoundError:
        print("File not found:", file_path)
    except PermissionError:
        print("Permission denied to access file:", file_path)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_permissions.py <path/to/file>")
        sys.exit(1)

    file_path = sys.argv[1]
    check_permissions(file_path)

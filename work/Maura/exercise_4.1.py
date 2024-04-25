# Format: python file_permissions.py path/to/file
# Display the file's permissions
# Indicate if the user who run it, can write to it

import os
import sys

def check_file_permissions(file_path):
    # check if file exists
    if not os.path.exists(file_path):
        return f"Error: The file '{file_path}' does not exist."
    # get file's permissions
    permissions = os.stat(file_path).st_mode
    readable = os.access(file_path, os.R_OK)
    writable = os.access(file_path, os.W_OK)
    executable = os.access(file_path, os.X_OK)
    perms = []
    perms.append('r' if readable else '-')
    perms.append('w' if writable else '-')
    perms.append('x' if executable else '-')
    permission_string = ''.join(perms)
    can_write = "Yes" if writable else "No"
    
    return f"Permissions: {permission_string}\nCan the user write to the file? {can_write}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        file_path = input("Please enter a file path: ")
    elif len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        print("Only enter one file path.")
        sys.exit(1)
    result = check_file_permissions(file_path)
    print(result)

import os

def display_permissions(file_path):

    '''
        ‼ os.stat() displays the stats at the file path (e.g. file mode, i-node, user id, etc.) ‼
        ‼ st_mode holds the file permissions at that specific file path ‼
    '''
    permission_bits = os.stat(file_path).st_mode 
    permission_octal = oct(permission_bits)[-3:] # convert the permission bits into octal form

    print("permissions for", file_path, ":", permission_octal)

    print(f"user can write to file: {os.access(file_path, os.W_OK)}")

file_path = input("provide a file path: ")
if os.path.exists(file_path):
    display_permissions(file_path)
else:
    print(f"The file path '{file_path}' does not exist or is invalid.")

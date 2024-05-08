#change this code around a bit to make less complex

import os
import sys

def check_file_permissions(file_path):
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            print("File not found.")
            return
        
        # Check if file is a regular file
        if not os.path.isfile(file_path):
            print("Not a regular file.")
            return
        
        # Check write permission
        if os.access(file_path, os.W_OK):
            print("You have write permission to the file.")
        else:
            print("You do not have write permission to the file.")
        
        # Get file permissions
        permissions = {
            'user': {
                'read': os.access(file_path, os.R_OK),
                'write': os.access(file_path, os.W_OK),
                'execute': os.access(file_path, os.X_OK)
            },
            'group': {
                'read': os.access(file_path, os.R_OK, effective_ids=True),
                'write': os.access(file_path, os.W_OK, effective_ids=True),
                'execute': os.access(file_path, os.X_OK, effective_ids=True)
            },
            'others': {
                'read': os.access(file_path, os.R_OK, effective_ids=False),
                'write': os.access(file_path, os.W_OK, effective_ids=False),
                'execute': os.access(file_path, os.X_OK, effective_ids=False)
            }
        }
        
        print("File Permissions:")
        print("User - Read: {}, Write: {}, Execute: {}".format(permissions['user']['read'], permissions['user']['write'], permissions['user']['execute']))
        print("Group - Read: {}, Write: {}, Execute: {}".format(permissions['group']['read'], permissions['group']['write'], permissions['group']['execute']))
        print("Others - Read: {}, Write: {}, Execute: {}".format(permissions['others']['read'], permissions['others']['write'], permissions['others']['execute']))
    
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input("Enter the file path: ")

    check_file_permissions(file_path)

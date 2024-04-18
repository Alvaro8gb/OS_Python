import os

# Define the path to the file (make sure the file exists)
file_path = 'data/hola.txt'

# Define the desired new permissions
# Example: '00755' grants read/write/execute to the owner,
# and read/execute to group and others
permissions = 0o755

os.chmod(file_path, permissions)
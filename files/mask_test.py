import os
from stat import S_IRUSR, S_IRGRP, S_IROTH

# Octal value for umask
# octal value 00777 is

# 511 in decimal
mask = 0o111 # octal

# Set the current umask value
# and get the previous

mask_old = os.umask(mask)

print("Current umask:", oct(mask))

print("Previous umask:", oct(mask_old))


# File path
filename = "data/permisions"

# Flags for opening the file
flags = os.O_WRONLY | os.O_CREAT

# File permissions (octal mode)
mode = 0o666

# Open the file using os.open
fd = os.open(filename, flags, mode)


file_stat = os.stat(filename)

# Print permission details in human-readable format
print(f"Permissions for '{filename}':")
mode = file_stat.st_mode
print(f"- User: {(mode & S_IRUSR) and 'read' or '---'}")
print(f"- Group: {(mode & S_IRGRP) and 'read' or '---'}")
print(f"- Others: {(mode & S_IROTH) and 'read' or '---'}")

os.close(fd)
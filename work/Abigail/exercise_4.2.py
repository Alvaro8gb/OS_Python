import os
import subprocess

sym_og_file = 'symbolic_og_file.txt'
sym_og_dir = 'symbolic_og_dir'

new_sym_file = 'sym_new_file.txt'
new_sym_dir = 'sym_new_dir'

# Create symbolic link to a regular file
os.symlink(sym_og_file, new_sym_file)

# Create symbolic link to a directory
os.symlink(sym_og_dir, new_sym_dir)

# Verify symbolic links using ls command
subprocess.run(['ls', '-l', new_sym_file])
subprocess.run(['ls', '-l', new_sym_dir])

# Verify inodes using ls -i command
subprocess.run(['ls', '-i', new_sym_file])
subprocess.run(['ls', '-i', new_sym_dir])

#creating hard link files and directories 
hard_og_file = 'hardlnk_og_file.txt'
hard_og_dir = 'hardlnk_og_dir'

new_hard_file = 'hardlnk_new_file.txt'
new_hard_dir = 'hardlnk_new_dir'

######
#NEED TO HANDLE PERMISSIONS HANDLING 
#####

# Create hard links
os.link(hard_og_file, new_hard_file)
os.link(hard_og_dir, new_hard_dir)

# Verify hard links using ls command
subprocess.run(['ls', '-l', new_hard_file])
subprocess.run(['ls', '-l', new_hard_dir])

# Get inode of the files and link count attribute using stat
print("Stat for hard link file:")
print(os.stat(new_hard_file))
print("Stat for hard link directory:")
print(os.stat(new_hard_dir))

# Simulate deleting hard link and observe the changes
os.remove(new_hard_file)
subprocess.run(['ls', '-l', hard_og_file])

# Simulate deleting symbolic link and observe the changes
os.remove(new_sym_file)
subprocess.run(['ls', '-l', new_sym_file])

# Simulate deleting original file and observe the changes
os.remove(hard_og_file)
subprocess.run(['ls', '-l', new_hard_dir])


#What happens when one of the hard links is deleted? What happens if one of the symbolic links is deleted? And if the original file is deleted?
#If a hard link is deleted the specific link to the file is the only thing deleted not the original final. The content in the file is the same as long as there are other hard links or the original file exists.
# When a symbolic link is deleted it removes the link but does not change the original file, directory, or the symbolic links.
#When the original file is deleted all hard links are inaccessible, however, symbolic links still point to where the original file existed.
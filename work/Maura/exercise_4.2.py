# Create with python a rigid and a symbolic 'In(1)': -
# With the '-s' option, a symbolic link is created.
# Create a symbolic link to a regular file and another to a directory. Verify the result with 'Is -l' and 'Is-i'.
# Determine the i-node of each file.
# Repeat the previous section with hard links.
# Determine the i-nodes of the files and the properties with 'stat' (observe the link count attribute).
# What happens when one of the hard links is deleted? What happens if one of the symbolic links is deleted? And if the original file is deleted?
# To create the symbolic link, you can use commands or python.

import os

# symbolic links

# path of og file and directory
original_sym_file = '4.2_sym_og.py'
original_sym_dir = '4.2_sym_og'

# path for new links
link_to_sym_file = '4.2_sym_new.py'
link_to_sym_dir = '4.2_sym_new'

os.symlink(original_sym_file, link_to_sym_file)

os.symlink(original_sym_dir, link_to_sym_dir)

og_symfile_stats = os.stat(original_sym_file)
og_symfile_inode = og_symfile_stats.st_ino
print("original file for symbolic link inode: ", og_symfile_inode)

og_symdir_stats = os.stat(original_sym_dir)
og_symdir_inode = og_symdir_stats.st_ino
print("new file for symbolic link inode: ", og_symdir_inode)

new_symfile_stats = os.stat(link_to_sym_file)
new_symfile_inode = new_symfile_stats.st_ino
print("original directory for symbolic link inode: ", new_symfile_inode)

new_symdir_stats = os.stat(link_to_sym_dir)
new_symdir_inode = new_symdir_stats.st_ino
print ("new directory for symbolic link inode: ", new_symdir_inode)

# ls -l 4.2_sym_new.py
# ls -l 4.2_sym_new



# hard links

# path of og file and directory
original_hard_file = '4.2_hard_og.py'

# path for new links
link_to_hard_file = '4.2_hard_new.py'

# Create hard link to a file
os.link(original_hard_file, link_to_hard_file)

og_hardfile_stats = os.stat(original_hard_file)
og_hardfile_inode = og_hardfile_stats.st_ino
print("original file for hard link inode: ", og_hardfile_inode)

new_hardfile_stats = os.stat(link_to_hard_file)
new_hardfile_inode = new_hardfile_stats.st_ino
print ("new file for hard link inode: ", new_hardfile_inode)

# stat 4.2_hard_og.py
# stat 4.2_hard_new.py

# when a hard link is deleted the newly created file or directory can still be accessed 
# by ther links, but the file can deleted if the last hard link is deleted

# when a symbolic link is deleted the newly created file or directory is not affected at 
# all, the link is lost but the file doesn't change

# when the original file is deleted a symbolic link will still exist but connects to a 
# non-existant location, while new file connected with a hard link will still be abe to be 
# accessed by other hard linked until the last hard link is deleted

import os

directory_og = "4_2orig"
file_name_og = "4_2orig.txt"
file_hard_link = "4_2orig_hardlink.txt"

symbolic_link_file = "symbolic_link_file"
symbolic_link_dir = "symbolic_link_directory"
hard_link_file = "hard_link_file"

os.symlink(file_name_og, symbolic_link_file)
os.symlink(directory_og, symbolic_link_dir)

os.link(file_hard_link, hard_link_file)

def display(path):
    info = os.stat(path)
    inode = info.st_ino
    link_count = info.st_nlink
    print(f'{path}: inode = {inode}, link count = {link_count}')

print('Symbolic links:')
display(symbolic_link_file)
display(symbolic_link_dir)

print('\nHard link:')
display(hard_link_file)
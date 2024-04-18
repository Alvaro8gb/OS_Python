import os

def create_symbolic_link(target, link_name):
    os.symlink(target, link_name)

def create_hard_link(target, link_name):
    os.link(target, link_name)

def get_inode(file_path):
    return os.stat(file_path).st_ino

def main():
    target_file = "target_file.txt"
    target_dir = "target_directory"
    
    if not os.path.exists(target_file):
        open(target_file, 'w').close()
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    
    create_symbolic_link(target_file, "symbolic_link_to_file")
    create_symbolic_link(target_dir, "symbolic_link_to_directory")
    
    create_hard_link(target_file, "hard_link_to_file")
    
    print("Inodes:")
    print("Symbolic link to file:", get_inode("symbolic_link_to_file"))
    print("Symbolic link to directory:", get_inode("symbolic_link_to_directory"))
    print("Hard link to file:", get_inode("hard_link_to_file"))
    print("Target file:", get_inode(target_file))
    print("Target directory:", get_inode(target_dir))

if __name__ == "__main__":
    main()

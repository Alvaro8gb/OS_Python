import os

def create_symlink(src, dst):
    try:
        os.symlink(src, dst)
        print(f"Symbolic link created")
    except OSError as e:
        print(f"Failed to create symbolic link: {e}")



def create_hardlink(src, dst):
    try:
        os.link(src, dst)
        print(f"Hard link created")
    except OSError as e:
        print(f"Failed to create hard link: {e}")



def main():
    # Source directory and file
    source_dir = "/home/csuser/Desktop/OS_Python/work/Kevin/Test Dir"
    source_file = "/home/csuser/Desktop/OS_Python/work/Kevin/Test Dir/test_file.txt"

    # Destination directory and file for symbolic links
    sym_dir_link = "/home/csuser/Desktop/OS_Python/work/Kevin/Link Dir/sym_link_dir.txt"
    sym_file_link = "/home/csuser/Desktop/OS_Python/work/Kevin/Link Dir/sym_link_file.txt"

    # Destination directory and file for hard links
    hard_dir_link = "/home/csuser/Desktop/OS_Python/work/Kevin/Link Dir/hard_link_dir.txt"
    hard_file_link = "/home/csuser/Desktop/OS_Python/work/Kevin/Link Dir/hard_link_file.txt"


    # # Create symbolic links
    # create_symlink(source_dir, sym_dir_link)
    # create_symlink(source_file, sym_file_link)

    # # Create hard links
    # create_hardlink(source_dir, hard_dir_link)
    # create_hardlink(source_file, hard_file_link)

    print(os.stat(source_dir))
    print(os.stat(source_file))


if __name__ == "__main__":
    main()


'''
ANSWERS:
    st_nlink = 2 for the Test Dir and st_nlink = 3 for the test_file.txt
    The hard link to the directory was never created as it would break the file system.

    If the symlink is deleted, the file and hard-link persists
    If the hard link is deleted, the file and sym-links persist
    If the file is deleted, the hard-link persists and functions, but the sym-links break.
    The exception to this is if you meant the file is deleted by deleting both the hard-links
    and original file

PERMISSIONS:
    -rw-rw-r-- 2 csuser csuser  0 May  8 08:22 hard_link_file.txt
    lrwxrwxrwx 1 csuser csuser 50 May  8 08:27 sym_link_dir.txt -> '/home/csuser/Desktop/OS_Python/work/Kevin/Test Dir'
    lrwxrwxrwx 1 csuser csuser 64 May  8 08:27 sym_link_file.txt -> '/home/csuser/Desktop/OS_Python/work/Kevin/Test Dir/test_file.txt'

I-NODES:
    918878 hard_link_file.txt  
    925103 sym_link_dir.txt  
    925104 sym_link_file.txt
'''
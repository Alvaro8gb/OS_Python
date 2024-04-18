import os

def create_symbolic_link(source, target):
    os.symlink(source, target)

if __name__ == "__main__":
    regular_file_source = "4.2test"
    directory_source = "example.txt"
    
    regular_file_link = "regular_file_link"
    directory_link = "directory_link"
    
    create_symbolic_link(regular_file_source, regular_file_link)
    create_symbolic_link(directory_source, directory_link)

    regular_file_info = os.lstat(regular_file_link)
    directory_info = os.lstat(directory_link)
    
    print("Regular File Link:")
    print("i-node:", regular_file_info.st_ino)
    print("Mode:", oct(regular_file_info.st_mode))
    print("Link Count:", regular_file_info.st_nlink)
    print("\nDirectory Link:")
    print("i-node:", directory_info.st_ino)
    print("Mode:", oct(directory_info.st_mode))
    print("Link Count:", directory_info.st_nlink)
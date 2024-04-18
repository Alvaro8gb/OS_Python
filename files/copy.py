import os
import sys

def copy_file(source, destination):
    src_fd = os.open(source, os.O_RDONLY)

    dest_fd = os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o666)

    while True:
        data = os.read(src_fd, 1024)  # Read in 1024 byte blocks
        if not data:  # If there is no data, end of file
            break
        os.write(dest_fd, data)  # Write the data to the target file

    os.close(src_fd)
    os.close(dest_fd)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py source_file destination_file")
        print("e.g: The file hola.txt has been copied to hola2 successfully.")
    else:
        source_filename = sys.argv[1]
        destination_filename = sys.argv[2]
        copy_file(source_filename, destination_filename)
        print(f"The file {source_filename} has been copied to {destination_filename} successfully.")

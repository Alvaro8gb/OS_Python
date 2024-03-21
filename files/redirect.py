import os

def main():
    fd = os.open("data/out.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o666)

    print("File descriptor", fd)

    os.close(1)  # Close STDOUT
    fd_d = os.dup(fd)   # Duplicate file descriptor to STDOUT
    os.close(fd)

    print("File descriptor", fd_d)
    print("Executing ..")

    os.close(fd_d)
   

if __name__ == "__main__":
    main()
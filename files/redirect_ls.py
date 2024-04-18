import os

def main():
    fd = os.open("data/out_2.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o666) 
    pid = os.fork()

    if pid == 0:
        try:
            os.dup2(fd, 1)  # Redirect standard output to the file
            os.execvp("ls", ["ls"])
        except OSError as e:
            print(f"Execvp error: {e}")
            exit(1)
    else:
        os.wait()

    os.close(fd)

    return 0


if __name__ == "__main__":
    main()

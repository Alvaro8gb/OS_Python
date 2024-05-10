
import os
import sys
import subprocess


def main():

    # Error Handling
    if len(sys.argv) < 5:
        print("Usage: python", sys.argv[0], "cmd1 arg1 cmd2 arg2")
        return 1

    # Get commands and arguments from input
    cmd1, arg1, cmd2, arg2 = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Create a pipe to communicate between the parent and child process
    fd_r, fd_w = os.pipe()

    # Fork a child process
    pid = os.fork()

    # Parent Process
    if pid > 0:
        os.close(fd_r)  # Close the read end of the pipe, not used by parent
        os.dup2(fd_w, sys.stdout.fileno())  # Redirect stdout to the write end of the pipe
        subprocess.run([cmd1, arg1])  # Execute the first command
        os.close(fd_w)  # Close the write end of the pipe after the command is executed

    # Child Process
    elif pid == 0:
        os.close(fd_w)  # Close the write end of the pipe, not used by child
        os.dup2(fd_r, sys.stdin.fileno())  # Redirect stdin from the read end of the pipe
        subprocess.run([cmd2, arg2])  # Execute the second command
        os.close(fd_r)  # Close the read end of the pipe after the command is executed

    # Error
    else:
        print("Fork failed!")
        return 1


if __name__ == '__main__':
    main()

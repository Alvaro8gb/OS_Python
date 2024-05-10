
import os
import sys


def main(command):

    # Fork a child process
    pid = os.fork()

    # Parent Process
    if pid > 0:
        print(f"Parent process (PID {os.getpid()}) with child process (PID {pid}).")
        os.waitpid(pid, 0)
    # Child Process
    elif pid == 0:
        print(f"Child process (PID {os.getpid()}).")
        # Create and run a bash command if provided
        if command is not None:
            print(f"Executing command: {command}.")
            os.execvp(command[0], command)
        else:
            print("No command provided in argument.")
    # Error
    else:
        print("Fork failed!")


if __name__ == '__main__':
    cmd = None
    if len(sys.argv) > 1:
        cmd = sys.argv[1:]
    main(cmd)

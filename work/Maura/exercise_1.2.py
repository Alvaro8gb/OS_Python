import os 
import sys
from os import wait

def bash_command(command):

    pid = os.fork()

    if pid < 0:
        print("Error forking")
        exit(1)

    if pid > 0:
        print("parent process")
        os.wait()

    elif pid == 0:
        print("child process")
        os.execvp(command[0], command)
    
    else:
        print("failed")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("not enough arguments, failed")
        sys.exit(1)
    command = sys.argv[1:]
    bash_command(command)
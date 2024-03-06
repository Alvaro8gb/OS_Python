import os
import sys

def daemon_process(command):
    pid = os.fork()

    if pid < 0:
        print("error in forking")
        sys.exit(1)

    if pid == 0:
        child = os.getpid()
        print(f"Child process: {child}")
        os.setsid()
        os.chdir('/tmp') 
        os.execvp(command[0], command)

    if pid > 0:
        parent = os.getpid()
        print(f"Parent process: {parent}")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Not enough arguments")
    command = sys.argv[1:]
    daemon_process(command)
import os
import sys
from os import wait

def bash_terminal(command):
    try:
        pid = os.fork()

        if pid > 0:
            # parent process
            print(f"parent process with PID: {os.getpid()}, my child's PID is: {pid}")
            os.wait()
        elif pid == 0:
            # child process
            print(f"child process with PID: {os.getpid()} my parent's PID is: {os.getppid()}")
            os.execvp(command[0], command)
        else:
            print("fork failed")
    except OSError as e:
        print(f"fork failed: {e}")
        os._exit(1)
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 exersize1_2.py <command>")
        sys.exit(1)
    command = sys.argv[1:]
    bash_terminal(command)
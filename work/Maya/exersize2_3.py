# Create a daemon process. Daemon processes are started working when the system will be bootstrapped and terminate only when the system is shutdown. ( dont have parents)
# It does not have a controlling terminal. It always runs in the background.

import os
import sys

def create_daemon(command):
    pid = os.fork()

    if pid < 0:
        print("Fork failed")
        sys.exit(-1)        
    elif pid > 0:
        print(f"Parent process: {os.getpid()}")
        sys.exit(0)
    
    print(f"Child process: {os.getpid()}")
    os.setsid()
    os.chdir('/tmp')
    os.execvp(command[0], command)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <command> [<arg1> <arg2> ...]")
        sys.exit(1)

    command = sys.argv[1:]
    create_daemon(command)
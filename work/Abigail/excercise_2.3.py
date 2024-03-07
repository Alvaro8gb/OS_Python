import os
import sys

def daemon_process(command):
    pid = os.fork()

    if pid < 0:
        print("Error in fork")
        exit()

    # If pid is not 0, this is the parent process
    if pid > 0:
        exit()

    # Child process
    # Create a new sessionn and change directory
    print("starting Child process")
    os.setsid()
    os.chdir('/tmp')

    # Execute the program
    os.execv(command[0], command)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Not enough arguments found")
    command = sys.argv[1:]
    daemon_process(command)
        

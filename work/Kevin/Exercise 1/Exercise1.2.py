import os
import sys

def execute_command(command):
    pid = os.fork()

    if pid == 0:
        os.execl('/bin/bash', 'bash', '-c', command)
    if pid > 0:
        os.wait()
    else:
        print("fork failed")
    
if __name__ == "__main__":
    # Check if there is an argument
    if len(sys.argv) != 2:
        print("Usage: python3 program.py \"command\"")
        sys.exit(1) # I think positive means error idk tho

    bash_command = sys.argv[1]
    execute_command(bash_command)

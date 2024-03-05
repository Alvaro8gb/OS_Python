import os
import subprocess
import sys

#this need to be looked over!
def main():
    if len(sys.argv) < 2:
        print("Usage: python bash_terminal.py <command>")
        sys.exit(1)

    command = sys.argv[1]
    
    # Fork the process
    pid = os.fork()
    if pid < 0:
        print("Fork failed")
        sys.exit(1)
    elif pid == 0:  # Child process
        # Execute the command using exec
        subprocess.run(command)
        sys.exit(0)
    else:  # Parent process
        status = os.waitpid(pid, 0)
        print("Child process", pid, "exited with status", status)

if __name__ == "__main__":
    main()
    
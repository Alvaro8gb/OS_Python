import os
import signal
import sys
import subprocess
import time

def handler(signum, frame):
    # Signal handler function to handle SIGALRM
    print("Time limit exceeded. Killing child process...")
    os.kill(child_pid, signal.SIGTERM)

def main():
    if len(sys.argv) < 3:
        print("Rewrite to have the form segs commmand [arg] ")
        sys.exit(1)

    try:
        segs = int(sys.argv[1])
    except ValueError:
        print("Invalid number of seconds")
        sys.exit(1)

    command = sys.argv[2:]
    
    # Set up signal handler for SIGALRM
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(segs)

    try:
        # Create child process
        child_pid = os.fork()
        if child_pid == 0:  # Child process
            os.execvp(command[0], command)
        else:  # Parent process
            # Wait for child to finish
            child_pid, status = os.waitpid(child_pid, 0)
            # Cancel the alarm
            signal.alarm(0)

    except KeyboardInterrupt:
        # Handle Ctrl-C
        print("Ctrl-C pressed. Killing child process...")
        os.kill(child_pid, signal.SIGTERM)
        sys.exit(1)
    except Exception as e:
        print("An error occurred: ")
        sys.exit(1)

if __name__ == "__main__":
    main()

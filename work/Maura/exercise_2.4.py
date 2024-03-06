# Code in Python for Unix the program "timer" whose invocation is:
# `timer segs command [args...]`

# capable of limiting the maximum execution time of the command indicated as an argument:

#   - The indicated command (mandate) will be executed in a child process with the 
# arguments (args...) indicated in the invocation.

#   - If the user presses Ctrl-C the indicated command (mandate) should die, but 
# the parent process (temporizar) should not.

#   - If the child process does not finish before the time (seconds) indicated, 
# the parent should warn it by sending the proper signal.

#   - If it has not finished (the child process) one second later, the parent should kill it.

#   - In any of these cases, the parent process must decode the termination status of 
# the child process, display said status on the standard output, and terminate correctly.

import os 
import sys
import signal
from os import wait
from os import fork
import time

def over_timer():

    if pid == 0:
        os.kill(pid, signal.SIGTERM) # warning the child
        time.sleep(1)
        os.kill(pid, signal.SIGKILL) # kills the child


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Not enough arguments")

    seconds = int(sys.argv[1])
    command = sys.argv[2]
    args = sys.argv[2:]

    signal.signal(signal.SIGINT, over_timer) # ctrl c 
    signal.alarm(seconds) 

    pid = os.fork()

    if pid < 0:
        print("Error forking")
        exit(1)

    if pid == 0:
        print("Child process")
        os.execvp(command, args)

    if pid > 0:
        print("Parent process")
        while True:
            try:
                # Wait for any child process to change state
                wpid, status = os.waitpid(pid, 0)
                if os.WIFEXITED(status):
                    print(f"Child process exited with status {os.WEXITSTATUS(status)}")
                elif os.WIFSIGNALED(status):
                    print(f"Child process terminated by signal {os.WTERMSIG(status)}") 
                break
            except ChildProcessError:
                # No child processes
                break

        signal.alarm(0) # cancels the alarm


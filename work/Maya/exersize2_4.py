#Code in Python for Unix the program "timer" whose invocation is: timer segs command [args...]

#capable of limiting the maximum execution time of the command indicated as an argument:

#The indicated command (mandate) will be executed in a child process with the arguments (args...) indicated in the invocation.
#If the user presses Ctrl-C the indicated command (mandate) should die, but the parent process (temporizar) should not.
#If the child process does not finish before the time (seconds) indicated, the parent should warn it by sending the proper signal.
#If it has not finished (the child process) one second later, the parent should kill it.

import os
import sys
import subprocess
import signal
import time


def timeout(signum, frame):
    # signal handler for SIGALRM
    print("Child process timed out")
    sys.exit(1)

def timer(secs, command_with_args):
    # set up signal handler for SIGALRM
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(secs)
    
    # executes the command in the child process
    try:
        child_pid = os.fork()
        if child_pid == 0:
            # child process
            subprocess.run(command_with_args)
            os._exit(0)
        else:
            # parent process
            _, status = os.waitpid(child_pid, 0)
            if os.WIFSIGNALED(status):
                print("Child process terminated by signal:", os.WTERMSIG(status))
    except OSError as e:
        print("Execution failed:", e)
        sys.exit(1)
    finally:
        # Cancel the alarm
        signal.alarm(0)
                
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <seconds> <command> [<arg1> <arg2> ...]")
        sys.exit(1)
    secs = int(sys.argv[1])
    command_with_args = sys.argv[2:]

    timer(secs, command_with_args)

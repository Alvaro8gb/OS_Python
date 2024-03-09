# The objective of this exercise is to develop a process through the use of Python’s os and signal modules that simulates kill -9 <pid> command

import os
import signal
import sys

def simulate_kill_9(pid):
    try:
        os.kill(pid, signal.SIGKILL)
        print(f"Process with PID {pid} killed")
    except OSError as e:
        print(f"Process with PID {pid} killed")
        sys.exit(1)

if __name__ == "__main__":
    pid_delete = int(input("What is the PID of the process you want to kill: "))
    simulate_kill_9(pid_delete)
    sys.exit(0)
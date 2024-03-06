# The objective of this exercise is to develop a process through the use of Python’s os and signal modules that simulates kill -9 <pid> command

import os
import signal
import sys

def start_process():
    try:
        pid = os.fork()
        if pid < 0:
            print("Fork failed")
            os.exit(-1)
        elif pid > 0:
            print(f"Parent process: {os.getpid()}")
            return pid
        else:
            os._exit(0)
    except OSError as e:
        print(f"Fork failed: {e}")
        os._exit(1)

def simulate_kill_9(pid):
    try:
        os.kill(pid, signal.SIGKILL)
        print(f"Process with PID {pid} killed")
    except OSError as e:
        print(f"Process with PID {pid} killed")
        sys.exit(1)

def list_child_process(child_pid):
    print(f"Child process PID: {child_pid}")

if __name__ == "__main__":
    child_pid = start_process()
    list_child_process(child_pid)

    try:
        pid = int(input("What is the PID of the process you want to kill: "))
        if pid != child_pid and pid != os.getpid():
            print("Invalid PID.")
        else:
            simulate_kill_9(pid)
    except ValueError:
        print("Invalid PID.")
        sys.exit(1)

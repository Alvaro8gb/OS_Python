import os
import signal
import time
import sys

def handle_input():
    while True:
        try:
            val = input("Enter the process ID: ")
            pid = os.getpid()
            if val == str(pid): # killing process
                os.kill(pid, signal.SIGTERM)
                print("Successfully killed process")
                sys.exit(0)
        except EOFError:
            pass  # Ignore EOFError and keep waiting for input


time.sleep(1)  # Introduce a delay in parent process
handle_input()

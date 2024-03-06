import os
import time

pid = os.fork()
if pid < 0:
    print("Error forking")
    exit(1)
if pid > 0:
    print("Parent process, PID:", os.getpid(), ", Child PID:", pid)
elif pid == 0:
    print("Child process, PID:", os.getpid())
    # Execute the command
    time.sleep(2)
    print("Hello")
import os
import signal
import time

def handle_input(pid):
    while True:
        try:
            val = input("Enter the process ID: ")
            if val == str(pid): # killing process
                os.kill(pid, signal.SIGTERM)
                print("Process with pid:", val, "killed successfully")
                exit()
            else:
                print("Invalid value entered ")
        except EOFError:
            pass  # Ignore EOFError and keep waiting for input

# Fork the process
pid = os.fork()

if pid < 0:
    print("Error in fork")
elif pid == 0: # Child process
    parent_pid = os.getppid()
    handle_input(parent_pid)
else: # Parent process
    print("Parent pid:", os.getppid())
    child_pid = pid
    print("Child pid:", child_pid)
    time.sleep(2)  # Introduce a delay in parent process
    handle_input(child_pid)


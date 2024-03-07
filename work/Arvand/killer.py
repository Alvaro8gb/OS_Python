import os
import signal

# Fork a child process
pid = os.fork()

# pid greater than 0 indicates the parent process
if pid > 0:
    print(f"parent process with PID: {os.getpid()}, my child's PID is: {pid}")
# pid equal to 0 indicates the child process
elif pid == 0:
    try:
        print(f"Sending SIGTERM signal to process {os.getpid()}")
        os.kill(pid, signal.SIGTERM)
    except OSError:
        print(f"Failed to send SIGTERM signal to process {pid}")
else:
    # An error occurred​
    print("Fork failed.")
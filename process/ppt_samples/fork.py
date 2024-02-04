import os

# Fork a child process
pid = os.fork()

# pid greater than 0 indicates the parent process
if pid > 0:
    print(f"parent process with PID: {os.getpid()}, my child's PID is: {pid}")
# pid equal to 0 indicates the child process
elif pid == 0:
    print(f"child process with PID: {os.getpid()} my parent's PID: {os.getppid()}")
else:
    # An error occurred​
    print("Fork failed.")

print("This line is executed by both processes")
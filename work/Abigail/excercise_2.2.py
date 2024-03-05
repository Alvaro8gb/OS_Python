import os
import signal
import time

pid = os.fork()
parent_pid = os.getppid()
print("parent ", os.getppid() )

if pid < 0:
    print("Error in fork")
elif pid == 0: # child process
    # Ensure child process waits for user input
    while True:
        try:
            val = input("Enter the process ID: ")
            break  # Break the loop if input is received successfully
        except EOFError:
            pass  # Ignore EOFError and keep waiting for input
    print("Parent pid should be ", parent_pid)
    print ("Child pid should be ", pid)
    if val == str(parent_pid): # killing parent process
        os.kill(os.getppid(), signal.SIGTERM)
        print("Process with pid:", val, "killed successfully")
        exit()
    elif val == str(os.getpid()): # killing child process
        os.kill(os.getpid(), signal.SIGTERM)
        print("Process with pid:", val, "killed successfully")
        exit()
    else:
        print("Parent process ", os.getppid())
        print("Invalid value entered ")
        exit()
else: # parent process
    print("Parent pid:", os.getppid()) # gets parent process id 
    print("Child pid:", os.getpid()) # gets child process id 
    os.wait()
    time.sleep(2)  # Introduce a delay in parent process

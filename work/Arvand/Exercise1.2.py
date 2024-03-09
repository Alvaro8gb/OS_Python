import sys
import os

# fork a child process
pid = os.fork()

if pid > 0: 
    os.wait() # the parent process waits for the child to complete

if pid == 0:
    os.execvp(sys.argv[1], sys.argv[1:])
elif pid <= 0:
    # an error occurred​
    print("Fork failed.")
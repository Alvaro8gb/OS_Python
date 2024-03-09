import time
import os

# fork a child process
pid = os.fork()

if pid > 0:
    os.wait() # the parent process waits for the child to complete

# child process
if pid == 0:
    time.sleep(2)
    print('Hello World')

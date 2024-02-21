import time
import os

# Fork a child process
pid = os.fork()

# child process
if pid == 0:
    time.sleep(3)
    print('Hello World')
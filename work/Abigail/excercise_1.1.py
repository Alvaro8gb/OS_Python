import time
import os

pid = os.fork()

if pid < 0:
    print("Error in fork")
elif pid == 0: #child process
    print("Hello")
    exit()
else: # parent process taking place 
    print("Parent process taking place")
    time.sleep(2)


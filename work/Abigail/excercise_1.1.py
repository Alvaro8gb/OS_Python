import time
import os
from os import fork

pid = fork()

if pid < 0:
    print("Error in fork")
elif pid == 0: #child process
    time.sleep(2)
    print("Hello")
else: # parent process taking place 
    print("Parent process taking place")

